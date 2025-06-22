## Prueba en local

Invoke-RestMethod -Uri "http://localhost:5000/search" -Method Post -ContentType "application/json" -Body '{"query":"que sabes acerca de Kubernetes?"}'

## Comentario

No soporta caracteres especiales como "¿", "ñ", "á", "é", "í", "ó", "ú" (problemas de codificación UTF-8)