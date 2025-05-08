# Arquitecturas para el agente IA


## Tipos de Arquitecturas

En primer lugar, se describirá la arquitectura empleada en el presente proyecto, brindando una explicación detallada de su funcionamiento. Luego, se mencionarán algunas arquitecturas generales relevantes en el contexto. Cabe destacar que este proyecto tiene un enfoque open source, por lo que, en caso de interés, es posible modificar su estructura o incorporar nuevas capacidades según las necesidades específicas de cada implementación.

---

### RAG (Retrieval Augmented Generation)

<p align="center">
  <img src="/images/arquitectura-augmentedLLM.webp" width="100%">
  <br>
  <em>Figura 1: Arquitectura Augmented LLM</em>
</p>


Este tipo de arquitectura tiene un modelo de lenguaje (LLM) que dispone de capacidades como recuperación de información "**retrieval**", uso de herramientas externas "**tools**" y gestión de memoria "**memory**". Estos modelos no solo cuentan con dichas funciones, sino que también son capaces de utilizarlas activamente: pueden generar sus propias consultas de búsqueda, seleccionar las herramientas más adecuadas y decidir qué información conservar a lo largo de una conversación.

Este es el modelo que vamos a usar como modelo para nuestro proyecto, a continuación se explica mejor cómo es el proceso del mismo.

<p align="center" id="figura2">
  <img src="/images/rag.webp" width="100%">
  <br>
  <em>Figura 2: Arquitectura RAG (Retrieval Augmented Generation)</em>
</p>


**¿Cómo funciona RAG?**

Podemos dividir el funcionamiento de RAG en dos grandes etapas:  
1. **Carga de la información a la base de datos vectorial**  
2. **Interacción del usuario con el agente**

##### Etapa 1: Carga de información

Comenzamos con una fuente de información, como un archivo PDF. El primer paso es aplicar un proceso llamado **chunking**, que consiste en dividir el contenido en fragmentos más pequeños (<a href="#figura2">etapa 1</a>). Esto permite un tratamiento más eficiente y preciso, especialmente durante las búsquedas semánticas, donde queremos que el sistema encuentre información en partes específicas del documento, y no en su totalidad.

Luego preparamos estos fragmentos (<a href="#figura2">etapa 2</a>). Existen dos estrategias comunes:

- **Fixed Token Splitter:** divide el contenido en fragmentos de longitud fija.
- **Recursive Token Splitter:** realiza divisiones más inteligentes y superpuestas para evitar que se pierda contexto cuando una pregunta coincide justo en los bordes entre fragmentos. Esta técnica permite mantener solapamiento entre fragmentos, como se ilustra en la siguiente imagen.

<p align="center">
  <img src="/images/fixed-recursive.png" width="40%">
  <br>
  <em>Figura 3: Fixed vs Recursive splitting</em>
</p>


Luego, Cada fragmento se convierte en un vector mediante un **modelo de embeddings** (<a href="#figura2">etapa 3</a>). Esto transforma el contenido textual en una representación matemática comprensible para el sistema.

Finalmente, los vectores generados se almacenan en una **base de datos vectorial** (<a href="#figura2">etapa 4</a>), que queda lista para ser consultada durante la etapa de recuperación de información.


##### Etapa 2: Consulta del usuario

Cuando el usuario realiza una consulta (<a href="#figura2">etapa 7</a>), esta también se convierte en un vector utilizando el mismo modelo de embeddings (<a href="#figura2">etapa 3</a>). Luego, se compara este vector con los almacenados en la base de datos para encontrar los más similares (esto es el **retrieval**).

Luego, El sistema recupera (<a href="#figura2">etapa 5</a>):

- El **contexto relevante** desde la base de datos (fragmentos similares).
- La **consulta del usuario** original.

Ambos elementos se integran en una plantilla de prompt, por ejemplo:

``` bash
"Sos un buscador especializado en Bibliografía" (esto sería el prompt) 
Responde esta "consulta" (lo que pregunta el usuario) 
basandote en el siguiente "contexto" (va a ser lo que te devuelva la base vectorial)
``` 

Además, en este paso se puede personalizar el comportamiento del agente, indicando que responda con un estilo determinado o como si fuera especialista en un área.

Finalmente, un modelo de lenguaje (LLM) preentrenado toma ese prompt completo (contexto + consulta) y genera la respuesta final para el usuario (<a href="#figura2">etapa 6</a>).  
Es importante destacar que el modelo ya está entrenado previamente, ya que realizar un entrenamiento desde cero suele ser costoso o técnicamente complejo. Por eso, es importante elegir un modelo que sea eficiente para el uso que le daremos.

---
### Prompt chaining
<p align="center">
  <img src="/images/prompt-chaining.webp" width="100%">
  <br>
  <em>Figura 4: Arquitectura Prompt chaining</em>
</p>

El encadenamiento de *prompts* descompone una tarea en una secuencia de pasos, donde cada llamada a un modelo de lenguaje procesa la salida de la anterior. Este flujo de trabajo es ideal para situaciones en las que la tarea puede dividirse de forma clara y sencilla en subtareas fijas. El objetivo principal es sacrificar algo de latencia a cambio de una mayor precisión, haciendo que cada llamada al modelo sea una tarea más simple.

---
### Routing
<p align="center">
  <img src="/images/routing.png" width="100%">
  <br>
  <em>Figura 5: Arquitectura Routing </em>
</p>

El enrutamiento clasifica una entrada y la dirige a una tarea de seguimiento especializada. Este enfoque permite una clara separación de responsabilidades y la creación de *prompts* más específicos y eficaces. Sin esta estructura, optimizar el rendimiento para un tipo de entrada podría perjudicar el desempeño en otros casos. El enrutamiento resulta especialmente útil en tareas complejas con categorías bien diferenciadas, donde cada una puede ser tratada de forma más eficiente por separado. La clasificación inicial puede realizarse mediante un modelo de lenguaje o utilizando métodos tradicionales de clasificación.

---
### Parallelization
<p align="center">
  <img src="/images/parallelization.webp" width="100%">
  <br>
  <em>Figura 6: Arquitectura Parallelization</em>
</p>

Los LLMs pueden abordar múltiples tareas de forma simultánea, y sus resultados pueden combinarse posteriormente mediante programación. Este enfoque, conocido como paralelización, se presenta en dos formas principales:

- **Seccionamiento**: consiste en dividir una tarea en subtareas independientes que se ejecutan en paralelo.  
- **Votación**: implica ejecutar la misma tarea varias veces para obtener resultados variados y seleccionar el más adecuado.

La paralelización es especialmente útil cuando las subtareas pueden procesarse simultáneamente para mejorar la velocidad, o cuando se requieren múltiples perspectivas para obtener respuestas más confiables. En tareas complejas con múltiples dimensiones, los LLMs suelen ofrecer mejores resultados cuando cada aspecto se gestiona por separado, permitiendo que cada parte reciba una atención más enfocada.

---
### Orchestrator-workers
<p align="center">
  <img src="/images/orchestrator-workers.webp" width="100%">
  <br>
  <em>Figura 7: Arquitectura Orchestrator-workers</em>
</p>

En el flujo de trabajo de orquestador y trabajadores, un LLM central actúa como orquestador: descompone dinámicamente las tareas, las asigna a LLMs especializados (trabajadores) y luego sintetiza sus respuestas. Aunque este enfoque puede parecer similar a la paralelización, su diferencia clave radica en la flexibilidad: las subtareas no están predefinidas, sino que son generadas en tiempo real por el orquestador según la naturaleza de la tarea.

---
### Evaluator-optimizer
<p align="center">
  <img src="/images/evaluator-optimizer.webp" width="100%">
  <br>
  <em>Figura 8: Arquitectura Evaluator-optimizer</em>
</p>

En el flujo de trabajo de evaluador-optimizador, una instancia de LLM genera una respuesta, mientras que otra evalúa su calidad y proporciona retroalimentación, formando un ciclo iterativo. Este enfoque resulta efectivo cuando se disponen de criterios de evaluación bien definidos y cuando la mejora progresiva aporta un valor tangible.

---

## Referencia
[Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
