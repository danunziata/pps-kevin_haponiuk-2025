from qdrant_client import QdrantClient
from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)

# ==============================
# CONFIGURACIÓN
# ==============================
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama-k:11434")
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant-k:6333")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "TEST_DOROTEA")

print(f"[INIT] OLLAMA_URL: {OLLAMA_URL}")
print(f"[INIT] QDRANT_URL: {QDRANT_URL}")
print(f"[INIT] COLLECTION_NAME: {COLLECTION_NAME}")


# ==============================
# FUNCIONES AUXILIARES
# ==============================
def get_embedding(text: str):
    """Genera un embedding usando el modelo de Ollama."""
    print(f"\n[DEBUG] Solicitando embedding a Ollama para texto: {text[:60]}...")
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/embeddings",
            json={"model": "nomic-embed-text", "prompt": text},
            timeout=15
        )

        if response.status_code != 200:
            print(f"[ERROR] Ollama devolvió {response.status_code}: {response.text}")
            return None

        embedding = response.json().get("embedding")
        if embedding is None:
            print("[ERROR] No se encontró campo 'embedding' en la respuesta.")
        else:
            print(f"[DEBUG] Embedding recibido (len={len(embedding)})")
        return embedding

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Falló la conexión con Ollama: {e}")
        return None


def search_qdrant(query: str):
    """Busca en la base Qdrant usando embeddings."""
    print(f"\n[DEBUG] Iniciando búsqueda para: {query}")

    query_embedding = get_embedding(query)
    if query_embedding is None:
        return {"error": "No se pudo generar embedding desde Ollama."}, 500

    try:
        client = QdrantClient(url=QDRANT_URL)
        print(f"[DEBUG] Conectado a Qdrant en {QDRANT_URL}")
    except Exception as e:
        return {"error": f"No se pudo conectar a Qdrant: {str(e)}"}, 500

    try:
        print(f"[DEBUG] Buscando en colección '{COLLECTION_NAME}'...")
        results = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=10,
            with_payload=True
        )
        print(f"[DEBUG] Resultados encontrados: {len(results)}")

    except Exception as e:
        return {"error": f"Error en la búsqueda: {str(e)}"}, 500

    output = [
        {
            "score": r.score,
            "content": r.payload.get("content", ""),
            "metadata": r.payload.get("metadata", {})
        }
        for r in results
    ]

    return {"results": output}, 200


# ==============================
# ENDPOINT FLASK
# ==============================
@app.route("/search", methods=["POST"])
def search():
    print("\n[DEBUG] Petición POST recibida en /search")

    try:
        data = request.get_json(force=True)
        query = data.get("query", "").strip()

        if not query:
            return jsonify({"error": "Campo 'query' vacío o no proporcionado"}), 400

        results, status_code = search_qdrant(query)
        return jsonify(results), status_code

    except Exception as e:
        print(f"[ERROR] Fallo al procesar la petición: {str(e)}")
        return jsonify({"error": f"Error procesando la petición: {str(e)}"}), 400


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    print("[INFO] Iniciando servidor Flask en puerto 5000...")
    app.run(host="0.0.0.0", port=5000)
