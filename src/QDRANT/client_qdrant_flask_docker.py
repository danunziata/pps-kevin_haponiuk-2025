from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, SearchRequest
import requests
import json
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Configuración desde variables de entorno
OLLAMA_URL = "http://ollama-k:11434"
QDRANT_URL = "http://qdrant-k:6333"
collection_name = "TEST_DOROTEA"

def get_embedding(text):
    print(f"\n[DEBUG] Enviando texto a Ollama: {text}")
    try:
        response = requests.post(f'{OLLAMA_URL}/api/embeddings',
                               json={
                                   "model": "nomic-embed-text",
                                   "prompt": text
                               },
                               timeout=10)
        print(f"[DEBUG] Respuesta de Ollama: {response.status_code}")
        if response.status_code != 200:
            print(f"[ERROR] Error en la respuesta: {response.text}")
            return None
        embedding = response.json()['embedding']
        print(f"[DEBUG] Longitud del embedding: {len(embedding)}")
        return embedding
    except requests.exceptions.Timeout:
        print("[ERROR] Timeout al conectar con Ollama. ¿Está Ollama corriendo?")
        return None
    except requests.exceptions.ConnectionError:
        print("[ERROR] No se pudo conectar con Ollama. ¿Está Ollama corriendo?")
        return None
    except Exception as e:
        print(f"[ERROR] Error inesperado: {str(e)}")
        return None

def search_qdrant(query):
    print("\n[DEBUG] Iniciando proceso con query:", query)
    query_embedding = get_embedding(query)

    if query_embedding is None:
        return {"error": "No se pudo obtener el embedding"}, 500

    print("\n[DEBUG] Conectando a Qdrant...")
    try:
        client = QdrantClient(url=QDRANT_URL)
        print("[DEBUG] Conexión a Qdrant exitosa")
    except Exception as e:
        return {"error": f"No se pudo conectar a Qdrant: {str(e)}"}, 500

    print(f"\n[DEBUG] Realizando búsqueda en colección '{collection_name}'...")
    try:
        results = client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=20,
            with_payload=True
        )
        print(f"[DEBUG] Número de resultados encontrados: {len(results)}")
    except Exception as e:
        return {"error": f"Error en la búsqueda: {str(e)}"}, 500

    output = []
    for r in results:
        output.append({
            "score": r.score,
            "content": r.payload.get("content", ""),
            "metadata": r.payload.get("metadata", {})
        })

    return {"results": output}, 200

@app.route('/search', methods=['POST'])
def search():
    print("\n[DEBUG] Recibiendo petición POST")
    print(f"[DEBUG] Headers: {request.headers}")
    print(f"[DEBUG] Raw data: {request.get_data()}")
    
    try:
        data = request.get_json(force=True)
        print(f"[DEBUG] JSON data: {data}")
        
        if not data or 'query' not in data:
            print("[ERROR] No se encontró el campo 'query' en el JSON")
            return jsonify({"error": "Se requiere el campo 'query' en el JSON"}), 400
        
        results, status_code = search_qdrant(data['query'])
        return jsonify(results), status_code
    except Exception as e:
        print(f"[ERROR] Error procesando la petición: {str(e)}")
        return jsonify({"error": f"Error procesando la petición: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 