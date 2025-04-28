# GROBID

## Introducción / Problemática

n8n dispone de un nodo llamado `Extract from File` que permite múltiples opciones, entre ellas, **"extract from PDF"**. Inicialmente, el flujo del sistema consistía en descargar cada paper y luego procesarlo con este nodo. Si bien este método es relativamente rápido para extraer texto plano desde un PDF, el **output no es preciso ni estructurado**.

Esto genera una gran desventaja cuando se busca trabajar los datos de forma organizada por cada paper, especialmente al intentar identificar secciones específicas como introducción, metodología, resultados, etc. Por lo tanto, se vuelve confuso y poco confiable para alimentar una base de datos vectorial, que luego será utilizada en el sistema RAG para responder preguntas basadas en el contenido de los papers.

Ante esta necesidad, se exploraron soluciones más robustas y específicas para la lectura y estructuración de artículos científicos en PDF. De esta búsqueda surge [GROBID](https://github.com/kermitt2/grobid), una herramienta open-source, dockerizada y ampliamente adoptada en contextos académicos y científicos, que permite una extracción **estructurada y enriquecida** de los documentos.

<p align="center">
  <img src="/images/grobid-rag.png" width="100%">
  <br>
  <em>Figura 1: "Ilustración de dónde entraría GROBID en nuestro esquema"</em>
</p>

---

## ¿Qué es GROBID?

**GROBID** (GeneRation Of BIbliographic Data) es una herramienta de código abierto basada en machine learning que permite extraer y estructurar información desde documentos científicos a PDF. Está entrenado específicamente en el **dominio académico**, por lo que reconoce con alta precisión elementos como:

- Títulos
- Autores
- Afiliaciones
- Secciones del paper
- Citas bibliográficas
- Referencias cruzadas
- Figuras y ecuaciones

Su modelo se basa en técnicas de **procesamiento de lenguaje natural (NLP)** y **CRF (Conditional Random Fields)** para el etiquetado de textos, lo cual lo convierte en una alternativa ideal para estructurar artículos científicos de forma automática.

## Nuestro uso

En nuestro proyecto, **utilizamos GROBID para transformar documentos PDF en archivos XML**. Esto permite luego procesar los papers por secciones específicas, enriquecer los resúmenes automáticos y alimentar la base de datos vectorial para responder preguntas con mayor precisión.

<p align="center">
  <img src="/images/grobid-pdf_xml.png" width="50%">
  <br>
  <em>Figura 2: "Conversión de PDF a XML estructurado mediante GROBID"</em>
</p>

### Que es XML?

**XML (eXtensible Markup Language)** es un lenguaje de marcado diseñado para almacenar y transportar datos de forma estructurada, legible tanto para humanos como para máquinas.  

### Características clave:  
- **Etiquetas personalizables**: `<dato>contenido</dato>`.  
- **Autodescriptivo**: La estructura define el significado de los datos.  

**Ejemplo**:  
```xml
<libro>
   <titulo>El principito</titulo>
   <autor>Antoine de Saint-Exupéry</autor>
</libro>
```

---

## Instalación y ejecución de GROBID

La forma más recomendada de utilizar **GROBID** es a través de **Docker**, ejecutándolo como un servidor local.

Existen dos opciones de imágenes disponibles:

1. **Imagen completa**  
    
    Esta imagen ofrece la mejor precisión, ya que incluye todas las bibliotecas necesarias de Python, TensorFlow, soporte para GPU y todos los modelos de Deep Learning.  
    
    - Es ideal para quienes disponen de una buena computadora (preferentemente con GPU) y trabajan con una cantidad limitada de archivos PDF.
    - Requiere más recursos de hardware.
    - Para ejecutarla, se utiliza el siguiente comando:

      ```bash
      docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.1
      ```
     
2. **Imagen liviana**
   
   Esta versión prioriza el rendimiento en tiempo de ejecución, el menor uso de memoria y un tamaño de imagen más reducido.  
   
   - Es adecuada para sistemas con pocos recursos o para quienes necesitan procesar una gran cantidad de PDFs de forma rápida.
   - Sin embargo, **no incorpora los modelos más precisos**, por lo que la exactitud del procesamiento es inferior.

   Para ejecutarla, se utiliza el siguiente comando:

   ```bash
   docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.1
   ```


**Nota importante:**  
Durante las pruebas, se intentó utilizar la **imagen liviana** (`lfoppiano/grobid:0.8.1`), pero no funcionó correctamente para el flujo de trabajo requerido.  
Por este motivo, se optó por utilizar la **imagen completa** (`grobid/grobid:0.8.1`), que ofreció una mejor precisión y rendimiento en la extracción de datos de los documentos PDF.


Una vez que GROBID está en ejecución, se puede verificar su funcionamiento accediendo en un navegador web a:

[http://localhost:8070](http://localhost:8070)

Allí se encontrará la página de bienvenida del servidor, desde donde es posible utilizar los servicios de procesamiento de documentos de manera manual, pero lo que se hara para este proyecto automatizado es utilizarlo mediante clientes python como se explicara a continuacion.


## Estructura del entorno de trabajo

En nuestro flujo, definimos una estructura simple con tres elementos clave:

- 📁 input_papers # Carpeta que contiene los archivos PDF a procesar 
- 📁 output_papers # Carpeta donde se guardarán los archivos XML generados por GROBID 
- 📄 config.json # Archivo de configuración del cliente GROBID 
- 📄 cliente_grobid.py # Script Python para ejecutar la conversión masiva

### `📄 config.json`

Archivo necesario para establecer la configuración del cliente. En nuestro caso, no requiere modificación:


``````bash
    "grobid_server": "http://localhost:8070",
    "batch_size": 100,
    "sleep_time": 5,
    "timeout": 60,
    "coordinates": [ "persName", "figure", "ref", "biblStruct", "formula", "s", "note", "title" ]
``````


### `📄 cliente_grobid.py`

Este script ejecuta el cliente GROBID para transformar todos los archivos .pdf en la carpeta input_papers y guardar los .xml resultantes en output_papers.

from grobid_client.grobid_client import GrobidClient

``````bash
if __name__ == "__main__":
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", "input_papers", output="output_papers/", consolidate_citations=False, tei_coordinates=False, force=True)
``````

El script utiliza la biblioteca `grobid-client` para interactuar con el servidor GROBID. La función `process` se encarga de procesar los documentos PDF en la carpeta `input_papers`, generando archivos XML que se guardan en la carpeta `output_papers`. Los parámetros adicionales permiten ajustar el comportamiento del procesamiento, como la consolidación de citas y las coordenadas TEI.




## Referencia

- [GROBID GitHub](https://github.com/kermitt2/grobid)
- [GROBID Documentación](https://grobid.readthedocs.io/en/latest/)
- [GROBID Docker](https://hub.docker.com/r/grobid/grobid)