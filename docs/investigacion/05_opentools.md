# 🛠️ Herramientas Open Source para el Proyecto

Este documento presenta un resumen de herramientas de código abierto seleccionadas para automatizar flujos de trabajo y procesar documentos científicos. Para cada herramienta, se evaluará su aplicabilidad en el sistema propuesto, considerando sus ventajas, desventajas y casos de uso específicos. Además, se analizará su compatibilidad con Docker, disponibilidad de APIs y capacidad de integración en flujos de automatización. El objetivo es proporcionar una base sólida para la implementación de un sistema eficiente y escalable.

## Tabla de herramientas

| Herramienta     | Rol principal                 | Aplicabilidad en el sistema                     |
|-----------------|-------------------------------|------------------------------------------------|
| n8n             | Automatización                | Orquestación de flujos de trabajo              |
| GROBID          | Extracción de metadatos       | Procesamiento de PDFs científicos              |
| Qdrant          | Almacenamiento vectorial      | Sistema RAG y búsqueda semántica               |
| VosViewer       | Análisis bibliométrico        | Visualización de redes de colaboración         |
| Ollama          | Modelos de lenguaje           | Generación y procesamiento de texto            |


## 🧠 **1. [n8n](./06_n8n.md)**
- **Función:** Automatización de flujos de trabajo (workflow automation).
- **Aplicabilidad:** Ideal para orquestar procesos como descarga de documentos, extracción de metadatos, IA, carga en base vectorial, notificaciones, etc.
- **Ventajas:** Interfaz visual, altamente extensible, soporte para HTTP, Webhooks, Google Drive, Python y más.
- **Desventajas:** Curva de aprendizaje inicial, puede requerir recursos significativos para workflows complejos.
- **Docker:** ✅ Compatible con Docker, imagen oficial disponible.
- **APIs:** ✅ API REST disponible para integración programática.

---

## 📄 **2. [GROBID](./07_grobid.md)**
- **Función:** Extracción estructurada de información de documentos científicos en PDF.
- **Aplicabilidad:** Extrae título, autores, referencias, secciones, keywords y más en formato XML.
- **Ventajas:** Alta precisión en papers académicos, fácil de dockerizar e integrar con Python o n8n.
- **Desventajas:** Rendimiento variable según la calidad del PDF, requiere configuración específica para diferentes formatos de documentos.
- **Docker:** ✅ Compatible con Docker, imagen oficial disponible.
- **APIs:** ✅ API REST disponible para procesamiento de documentos.

---

## 🔍 **3. VosViewer**
- **Función:** Análisis bibliométrico y visualización de mapas de ciencia.
- **Aplicabilidad:** concurrencia de autores.
- **Ventajas:** interfaz gráfica simple.
- **Desventajas:** Limitado en personalización, requiere datos preprocesados en formatos específicos.
- **Docker:** ❌ No compatible con Docker, aplicación de escritorio. (trataremos de hacer una adaptación para que sea compatible)
- **APIs:** ❌ No dispone de API oficial.

---

## 🗃️ **4. Qdrant**
- **Función:** Base de datos vectorial.
- **Aplicabilidad:** Almacena los embeddings generados desde los textos científicos para el sistema RAG.
- **Ventajas:** Rápido, soporte para metadata.
- **Desventajas:** Consumo de memoria significativo con grandes volúmenes de datos, requiere optimización para producción.
- **Docker:** ✅ Compatible con Docker, imagen oficial disponible.
- **APIs:** ✅ API REST y gRPC disponibles para operaciones vectoriales.

---

## 📄 **5. Ollama**
- **Función:** Modelos de lenguaje.
- **Aplicabilidad:** Generación y procesamiento de texto.
- **Ventajas:** Fácil de usar, soporte para múltiples modelos de lenguaje, ejecución local sin necesidad de conexión a internet.
- **Desventajas:** Limitado por recursos locales, modelos pueden ser menos potentes que versiones en la nube, requiere gestión de memoria cuidadosa.
- **Docker:** ✅ Compatible con Docker, imagen oficial disponible.
- **APIs:** ✅ API REST disponible para interacción con modelos.



## 🔗 **Referencias Oficiales**

**n8n** : [Sitio oficial](https://n8n.io/) | [GitHub](https://github.com/n8n-io)

**GROBID** : [Sitio oficial](https://grobid.readthedocs.io/) | [GitHub](https://github.com/kermitt2/grobid)

**VosViewer** : [Sitio oficial](https://www.vosviewer.com/) | [GitHub (versión open source utilizada)](https://github.com/neesjanvaneck/VOSviewer-Online)

**Qdrant** : [Sitio oficial](https://qdrant.tech/) | [GitHub](https://github.com/qdrant/qdrant)

**Ollama** : [Sitio oficial](https://ollama.com/) | [GitHub](https://github.com/ollama)

