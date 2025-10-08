"""
title: N8N Pipeline
author: owndev (adapted by Kevin Haponiuk)
version: 2.1.0
description: A pipeline for interacting with N8N workflows directly from OpenWebUI.
features:
- Integrates with N8N for seamless communication.
- Supports dynamic message handling.
- Enables real-time interaction with N8N workflows.
- Provides configurable status emissions.
- Cloudflare Access support for secure communication.
- Encryption-safe for API keys.
"""

from typing import Optional, Callable, Awaitable, Any, Dict
from pydantic import BaseModel, Field, GetCoreSchemaHandler
from cryptography.fernet import Fernet, InvalidToken
import aiohttp
import os
import base64
import hashlib
import logging
import time
from open_webui.env import AIOHTTP_CLIENT_TIMEOUT, SRC_LOG_LEVELS
from pydantic_core import core_schema


# ======================
# 🔐 Encrypted String Type
# ======================
class EncryptedStr(str):
    """A string type that automatically handles encryption/decryption."""

    @classmethod
    def _get_encryption_key(cls) -> Optional[bytes]:
        secret = os.getenv("WEBUI_SECRET_KEY")
        if not secret:
            return None
        hashed_key = hashlib.sha256(secret.encode()).digest()
        return base64.urlsafe_b64encode(hashed_key)

    @classmethod
    def encrypt(cls, value: str) -> str:
        if not value or value.startswith("encrypted:"):
            return value
        key = cls._get_encryption_key()
        if not key:
            return value
        f = Fernet(key)
        encrypted = f.encrypt(value.encode())
        return f"encrypted:{encrypted.decode()}"

    @classmethod
    def decrypt(cls, value: str) -> str:
        if not value or not value.startswith("encrypted:"):
            return value
        key = cls._get_encryption_key()
        if not key:
            return value[len("encrypted:") :]
        try:
            encrypted_part = value[len("encrypted:") :]
            f = Fernet(key)
            decrypted = f.decrypt(encrypted_part.encode())
            return decrypted.decode()
        except (InvalidToken, Exception):
            return value

    # Pydantic integration
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: Any, _handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.union_schema(
            [
                core_schema.is_instance_schema(cls),
                core_schema.chain_schema(
                    [
                        core_schema.str_schema(),
                        core_schema.no_info_plain_validator_function(
                            lambda value: cls(cls.encrypt(value) if value else value)
                        ),
                    ]
                ),
            ],
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda instance: str(instance)
            ),
        )

    def get_decrypted(self) -> str:
        return self.decrypt(self)


# ======================
# 🧠 Main Pipe Definition
# ======================
class Pipe:
    class Valves(BaseModel):
        N8N_URL: str = Field(
            default="https://<your-endpoint>/webhook/<your-workflow>",
            description="URL for the N8N webhook endpoint",
        )
        N8N_BEARER_TOKEN: Optional[EncryptedStr] = Field(
            default=None, description="Bearer token for N8N authentication"
        )
        INPUT_FIELD: str = Field(
            default="chatInput", description="Input field name in N8N payload"
        )
        RESPONSE_FIELD: str = Field(
            default="output", description="Response field name in N8N payload"
        )
        EMIT_INTERVAL: float = Field(
            default=2.0, description="Interval in seconds between status updates"
        )
        ENABLE_STATUS_INDICATOR: bool = Field(
            default=True, description="Enable status messages during workflow"
        )
        CF_ACCESS_CLIENT_ID: Optional[EncryptedStr] = Field(
            default=None, description="Cloudflare Access client ID (optional)"
        )
        CF_ACCESS_CLIENT_SECRET: Optional[EncryptedStr] = Field(
            default=None, description="Cloudflare Access client secret (optional)"
        )

    def __init__(self):
        self.name = "N8N Agent"
        self.valves = self.Valves()
        self.last_emit_time = 0
        self.log = logging.getLogger("n8n_pipeline")
        self.log.setLevel(SRC_LOG_LEVELS.get("OPENAI", logging.INFO))

    # ======================
    # ⚙️ Helper Methods
    # ======================
    async def emit_status(
        self,
        __event_emitter__: Callable[[dict], Awaitable[None]],
        level: str,
        message: str,
        done: bool,
    ):
        current_time = time.time()
        if (
            __event_emitter__
            and self.valves.ENABLE_STATUS_INDICATOR
            and (
                current_time - self.last_emit_time >= self.valves.EMIT_INTERVAL or done
            )
        ):
            await __event_emitter__(
                {
                    "type": "status",
                    "data": {
                        "status": "complete" if done else "in_progress",
                        "level": level,
                        "description": message,
                        "done": done,
                    },
                }
            )
            self.last_emit_time = current_time

    def extract_event_info(self, event_emitter):
        if not event_emitter or not event_emitter.__closure__:
            return None, None
        for cell in event_emitter.__closure__:
            if isinstance(request_info := cell.cell_contents, dict):
                chat_id = request_info.get("chat_id")
                message_id = request_info.get("message_id")
                return chat_id, message_id
        return None, None

    def _safe_decrypt(self, value):
        """Safely decrypt even if not EncryptedStr."""
        if hasattr(value, "get_decrypted"):
            return value.get_decrypted()
        return value or ""

    def get_headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}

        bearer_token = self._safe_decrypt(self.valves.N8N_BEARER_TOKEN)
        if bearer_token:
            headers["Authorization"] = f"Bearer {bearer_token}"

        cf_id = self._safe_decrypt(self.valves.CF_ACCESS_CLIENT_ID)
        if cf_id:
            headers["CF-Access-Client-Id"] = cf_id

        cf_secret = self._safe_decrypt(self.valves.CF_ACCESS_CLIENT_SECRET)
        if cf_secret:
            headers["CF-Access-Client-Secret"] = cf_secret

        return headers

    async def cleanup_session(self, session: Optional[aiohttp.ClientSession]) -> None:
        if session:
            await session.close()

    # ======================
    # 🚀 Main Execution Logic
    # ======================
    async def pipe(
        self,
        body: dict,
        __user__: Optional[dict] = None,
        __event_emitter__: Callable[[dict], Awaitable[None]] = None,
        __event_call__: Callable[[dict], Awaitable[dict]] = None,
    ) -> Optional[dict]:
        await self.emit_status(__event_emitter__, "info", f"Calling {self.name} ...", False)

        session = None
        n8n_response = None
        messages = body.get("messages", [])

        if not messages:
            error_msg = "No messages found in the request body"
            self.log.warning(error_msg)
            await self.emit_status(__event_emitter__, "error", error_msg, True)
            return {"error": error_msg}

        question = messages[-1]["content"]
        if "Prompt: " in question:
            question = question.split("Prompt: ")[-1]

        try:
            chat_id, message_id = self.extract_event_info(__event_emitter__)
            self.log.info(f"Starting N8N workflow request for chat ID: {chat_id}")

            payload = {
                "systemPrompt": f"{messages[0]['content'].split('Prompt: ')[-1]}",
                "user_id": __user__.get("id") if __user__ else None,
                "user_email": __user__.get("email") if __user__ else None,
                "user_name": __user__.get("name") if __user__ else None,
                "user_role": __user__.get("role") if __user__ else None,
                "chat_id": chat_id,
                "message_id": message_id,
                self.valves.INPUT_FIELD: question,
            }

            headers = self.get_headers()

            session = aiohttp.ClientSession(
                trust_env=True,
                timeout=aiohttp.ClientTimeout(total=AIOHTTP_CLIENT_TIMEOUT),
            )

            async with session.post(self.valves.N8N_URL, json=payload, headers=headers) as response:
                if response.status == 200:
                    response_data = await response.json()
                    n8n_response = response_data.get(self.valves.RESPONSE_FIELD, "")
                else:
                    text = await response.text()
                    raise Exception(f"N8N returned {response.status}: {text}")

            body["messages"].append({"role": "assistant", "content": n8n_response})

        except Exception as e:
            error_msg = f"Error during sequence execution: {str(e)}"
            self.log.exception(error_msg)
            await self.emit_status(__event_emitter__, "error", error_msg, True)
            return {"error": str(e)}
        finally:
            await self.cleanup_session(session)

        await self.emit_status(__event_emitter__, "info", "Complete", True)
        return n8n_response
