En esta sección se presentarán dos ejemplos prácticos de implementación de las arquitecturas **RAG** y **CRAG** que fueron explicadas en detalle en la sección de [Tipos de Arquitecturas](../investigacion/04_arquitectura.md). Estos ejemplos demostrarán cómo aplicar los conceptos teóricos en casos reales.

Para comenzar con los ejemplos, necesitamos importar el flujo de trabajo de ejemplo en n8n. El archivo `ejemplo_RAG_vs_CRAG.json` contiene la configuración completa de ambos ejemplos. Para importarlo:

1. En la interfaz de n8n, haz clic en el botón "Workflows" en el menú lateral
2. Haz clic en el botón "Import from File" en la esquina superior derecha
3. Navega hasta la carpeta `docs/implementacion/files` y selecciona el archivo `ejemplo_RAG_vs_CRAG.json`
4. Haz clic en "Import"

Una vez importado, deberás ver algo como lo siguiente:

<p align="center">
  <img src="/images/n8n_rag-crag.png" width="100%">
  <br>
  <em>Figura 1: Ejemplo de RAG y CRAG en n8n</em>
</p>

La implementación se divide en tres bloques principales:

1. **Bloque RAG (Amarillo)**: Implementa el flujo de trabajo del RAG tradicional
2. **Bloque CRAG (Rojo)**: Implementa el flujo de trabajo del CRAG
3. **Bloque de Consultas (Azul)**: Permite realizar consultas a la base de datos vectorial

### Configuración de las Colecciones
Cada bloque de base de datos vectorial debe configurarse con su colección correspondiente:

   - El bloque RAG se conecta a la colección `prueba_RAG`
   - El bloque CRAG se conecta a la colección `prueba_CRAG`
   - El bloque de consultas permite seleccionar la colección a consultar

### Flujo de Trabajo RAG
El flujo de trabajo del RAG sigue estos pasos:

  1. Descarga un archivo XML desde Google Drive (extraído previamente de un paper mediante GROBID)
  2. Procesa el archivo para extraer el texto contenido
  3. Carga el contenido en la base de datos vectorial con una configuración recursiva que permite que cada chunk contenga información de contexto de los chunks adyacentes

### Flujo de Trabajo CRAG
El flujo de trabajo del CRAG implementa una estrategia más sofisticada:

   1. Realiza la misma descarga y extracción inicial que el RAG
   2. Divide manualmente el contenido en chunks
   3. Procesa los chunks en grupos de 5 mediante un loop
   4. Para cada grupo, utiliza un modelo de lenguaje para generar contexto individual basado en el documento completo
   5. Carga los chunks enriquecidos en la base de datos vectorial
      - Nota: No se utiliza la configuración recursiva ya que la separación y enriquecimiento de chunks se realiza previamente


## Ejecución del flujo de trabajo
para la ejecución debemos agregar el bloque **when clicking 'test workflow'** y conectarlo con el bloque de google drive para testear el flujo de trabajo que queremos ejecutar, ya sea RAG o CRAG.

<p align="center">
  <img src="/images/n8n_rag-ejec.png" width="100%">
  <br>
  <em>Figura 2: Ejecución del flujo de trabajo RAG</em>
</p>

Una vez ejecutado el flujo de trabajo, se puede observar el proceso completo en acción:

Para verificar que los datos se han cargado correctamente, se puede acceder al panel de control de Qdrant a través de:

- [http://localhost:6333/dashboard#/collections](http://localhost:6333/dashboard#/collections)

Aquí se puede visualizar las colecciones creadas y verificar que los vectores se hayan almacenado correctamente.

<p align="center">
  <img src="/images/qdrant-collections.png" width="100%">
  <br>
  <em>Figura 3: Colecciones en Qdrant</em>
</p>

una vez llegado a este punto, está preparada la base de datos para que el agente pueda preguntar algo relacionado con el contenido que se cargó.

<p align="center">
  <img src="/images/n8n-rag-example.png" width="100%">
  <br>
  <em>Figura 4: Pregunta al agente</em>
</p>

