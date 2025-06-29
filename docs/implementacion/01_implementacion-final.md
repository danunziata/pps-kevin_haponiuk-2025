Actualizar el sistema
  
  ```sh
  sudo apt update
  sudo apt upgrade
  ```

Instalar Python

  ```sh
  sudo apt install python
  ```

Instalar Git

  ```sh
  sudo apt install git
  git --version ## (para verificar)
  ```

Instalar Docker

  ```sh
  sudo apt install docker.io
  sudo systemctl enable docker
  sudo systemctl start docker
  docker --version ## (para verificar)
  ```

Instalar Docker-Compose

  ```sh
  sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  docker-compose --version
  ```

Clonar el repositorio

  ```sh
  git clone git@github.com:danunziata/pps-kevin_haponiuk-2025.git
  cd pps-kevin_haponiuk-2025/src/self-hosted-ai-starter-kit
  ```

Ejecutar el docker-compose.yml

Moverse a self-hosted-ai-starter-kit


  Para caso de uso con CPU
  ```sh
  docker compose --profile cpu up
  ```

  Para caso de uso con GPU NVIDIA
  ```sh
  docker compose --profile gpu-nvidia up
  ```

Instalar las librerias necesarias

  ```sh
  python3 -m venv venv #Crea un nuevo entorno virtual donde se guardan todas las librerias a utilizar
  source venv/bin/activate
  pip install -r requirements.txt
  ```


Cosas que faltan definir bien aun:

1. [Credenciales de Google](../../pruebas/01_install-n8n/#credenciales-de-google).
2. Seleccionar la carpeta de google drive de donde se descargarán los pdfs.
3. Escribir una Qdrant Collection a utilizar.
4. La collection que se va a utilizar se la debe escribir manualmente en el cliente python "client_qdrant_flask_docker.py"
5. Falta explicar el test_grobid.py
6. Explicación del cliente grobid de python. (las cosas que se pueden definir ahí)



### 🌐 Listado de Puertos Utilizados



| Servicio | Puerto |
|----------|--------|
| **N8N** | `5678` |
| **Ollama** | `11434` |
| **PgAdmin** | `5050` |
| **Qdrant** | `6333` |
| **Qdrant Search** | `5000` |
| **PostgreSQL** | `5432` |
| **OpenWebUI** | `3001` |
| **Grobid** | `8070` |

