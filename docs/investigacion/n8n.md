# Introducción a n8n

**n8n** es una herramienta de automatización de flujos de trabajo (*workflow automation*) basada en nodos, de código abierto y altamente personalizable. Permite conectar diferentes servicios, APIs y procesos de manera visual e intuitiva, ideal para integrar tareas complejas sin necesidad de escribir mucho código.

<p align="center">
  <img src="/images/n8n-interface.png" width="100%">
  <br>
  <em>Figura 1: Ejemplo Interfaz gráfica de n8n</em>
</p>


## Características principales

- ⚙️ **Basado en nodos**: cada paso del flujo es un nodo que realiza una tarea (leer un archivo, hacer una petición HTTP, analizar texto, etc.).
- 🔁 **Automatización condicional**: permite bifurcar flujos según condiciones lógicas, errores, o datos.
- 🌐 **Integración con cientos de servicios**: Google Drive, APIs REST, bases de datos, herramientas de IA, entre otros.
- 🤖 **Extensible con código**: se pueden usar códigos JavaScript o Python personalizados.
- 💾 **Self-hosted o en la nube**: puede desplegarse localmente, en servidores propios, o usar su versión cloud.


## ¿Cómo se usa?

### 1. Crear un nuevo flujo

Los flujos en n8n comienzan desde un nodo gatillo (trigger), como por ejemplo:

- Un archivo subido a Google Drive
- Una petición entrante por HTTP
- Un webhook desde una aplicación externa
- mediante otro workflow


### 2. Encadenar nodos

Luego del nodo de inicio, se encadenan nodos de procesamiento:

- Transformaciones con nodos como `Set`, `Function`, `Merge`
- Interacciones externas como `HTTP Request`, `Google Sheets`, `Email`
- Análisis de datos, consultas a bases, o comunicación con APIs de IA


## Aplicación en este proyecto

En el contexto del presente proyecto, **n8n** se utiliza como motor de orquestación para automatizar tareas como:

- 🔄 **Esperar la notificación de petición de procesamiento de papers**
- 📊 **Ejecución GROBID para análisis del paper**
- 📈 **Generación de resúmenes o procesamiento necesario**
- 📤 **Indexación de información en la base de datos vectorial (Qdrant)**
- 🧠 **Interacción con modelos de lenguaje (LLMs)**
- 📁 **Interacción con el usuario final**


## Ventajas de usar n8n en el proyecto

| Ventaja                        | Descripción |
|-------------------------------|-------------|
| **Ejecución Local** | Permite el control total sin necesidad de pagos mensuales a aplicaciones externas. |
| **Automatización sin código** | Reduce la necesidad de scripting manual. |
| **Reutilización de flujos**   | Se pueden guardar y clonar flujos. |
| **Integración rápida**        | Conexiones simples con múltiples servicios. |
| **Observabilidad**            | Logs visuales y control sobre cada nodo. |
| **Control de errores**        | Permite manejar errores de forma precisa. |


## Conclusión

n8n es una herramienta poderosa y versátil que facilita la integración de servicios y la creación de automatismos sin requerir gran experiencia en programación. En este proyecto, permite centralizar todas las tareas repetitivas relacionadas con el análisis, resumen e indexación de papers científicos, funcionando como columna vertebral de la arquitectura de RAG implementada.


## Referencia
Si estás más interesado conocer más sobre n8n.

- [Página principal](https://n8n.io/)
- [Documentación](https://docs.n8n.io/)