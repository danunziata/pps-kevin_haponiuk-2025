# Introducción / Problemática

n8n dispone de un nodo llamado `Extract from File` que permite múltiples opciones, entre ellas, **"extract from PDF"**. Inicialmente, el flujo del sistema consistía en descargar cada paper y luego procesarlo con este nodo. Si bien este método es relativamente rápido para extraer texto plano desde un PDF, el **output no es preciso ni estructurado**.

Esto genera una gran desventaja cuando se busca trabajar los datos de forma organizada por cada paper, especialmente al intentar identificar secciones específicas como introducción, metodología, resultados, etc. —como se estudió en `/investigacion/revision_biblio/`. Por lo tanto, se vuelve confuso y poco confiable para alimentar una base de datos vectorial, que luego será utilizada en el sistema RAG para responder preguntas basadas en el contenido de los papers.

Ante esta necesidad, se exploraron soluciones más robustas y específicas para la lectura y estructuración de artículos científicos en PDF. De esta búsqueda surge **GROBID**, una herramienta open-source, dockerizada y ampliamente adoptada en contextos académicos y científicos, que permite una extracción **estructurada y enriquecida** de los documentos.

<p align="center">
  <img src="/images/grobid-rag.png" width="100%">
  <br>
  <em>Figura 1: "Ilustración de dónde entraría GROBID en nuestro esquema"</em>
</p>

---

# ¿Qué es GROBID?

**GROBID** (GeneRation Of BIbliographic Data) es una herramienta de código abierto basada en machine learning que permite extraer y estructurar información desde documentos científicos en PDF. Está entrenado específicamente en el **dominio académico**, por lo que reconoce con alta precisión elementos como:

- Títulos
- Autores
- Afiliaciones
- Secciones del paper
- Citas bibliográficas
- Referencias cruzadas
- Figuras y ecuaciones

Su modelo se basa en técnicas de **procesamiento de lenguaje natural (NLP)** y **CRF (Conditional Random Fields)** para el etiquetado de textos, lo cual lo convierte en una alternativa ideal para estructurar artículos científicos de forma automática.

---

## Nuestro uso

En nuestro proyecto, **utilizamos GROBID para transformar documentos PDF en archivos XML con estructura semántica**. Esto permite luego procesar los papers por secciones específicas, enriquecer los resúmenes automáticos y alimentar la base de datos vectorial para responder preguntas con mayor precisión.

<p align="center">
  <img src="/images/grobid-pdf_xml.png" width="50%">
  <br>
  <em>Figura 2: "Conversión de PDF a XML estructurado mediante GROBID"</em>
</p>

---

# Instalación

GROBID puede instalarse de varias formas:

# AGREGAR MANUALMENTE

Esta última opción es la más práctica, ya que permite levantar rápidamente el servicio sin preocuparse por dependencias.

---
Falta agregar las opciones que tiene GROBID y especificar que la que uso se llama processFulltextDocument

---

## Estructura del entorno de trabajo

En nuestro flujo, definimos una estructura simple con tres elementos clave:

- 📁 input_papers # Carpeta que contiene los archivos PDF a procesar 
- 📁 output_papers # Carpeta donde se guardarán los archivos XML generados por GROBID 
- 📄 config.json # Archivo de configuración del cliente GROBID 
- 📄 cliente_grobid.py # Script Python para ejecutar la conversión masiva



---

## `📄 config.json`

Archivo necesario para establecer la configuración del cliente. En nuestro caso, no requiere modificación:


``````bash
    "grobid_server": "http://localhost:8070",
    "batch_size": 100,
    "sleep_time": 5,
    "timeout": 60,
    "coordinates": [ "persName", "figure", "ref", "biblStruct", "formula", "s", "note", "title" ]
``````


## `📄 cliente_grobid.py`

Este script ejecuta el cliente GROBID para transformar todos los archivos .pdf en la carpeta input_papers y guardar los .xml resultantes en output_papers.

from grobid_client.grobid_client import GrobidClient

``````bash
if __name__ == "__main__":
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", "input_papers", output="output_papers/", consolidate_citations=False, tei_coordinates=False, force=True)
``````


## Referencia

FALTA AGREGAR ACÁ