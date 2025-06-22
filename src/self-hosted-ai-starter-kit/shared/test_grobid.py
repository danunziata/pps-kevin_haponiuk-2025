import http.client

host = "grobid"
port = 8070

try:
    conn = http.client.HTTPConnection(host, port, timeout=5)
    conn.request("GET", "/api/isalive")
    response = conn.getresponse()
    print("Status:", response.status)
    print("Respuesta:", response.read().decode())
    conn.close()
except Exception as e:
    print("Error al conectar con GROBID:", e)