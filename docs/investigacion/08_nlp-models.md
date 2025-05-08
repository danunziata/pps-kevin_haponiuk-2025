# Modelos de NLP para Revisión Automatizada de Literatura

La integración de NLP (Procesamiento de Lenguaje Natural / Natural Language Processing) representa un cambio significativo, permitiendo automatizar tareas manuales y mejorar la precisión de los procesos. Estas tecnologías cierran la brecha entre lenguaje humano y máquina, permitiendo a los sistemas procesar y comprender lenguaje natural. Esta capacidad es fundamental para desarrollar herramientas inteligentes que asistan a los ingenieros en la gestión de requerimientos, facilitando el desarrollo de software más robusto y alineado con las necesidades de los usuarios.

## Técnicas de NLP para Revisión Automatizada de Literatura

Existen tres enfoques principales para el procesamiento de lenguaje natural:

1. **El método basado en frecuencia (Spacy)** es el más simple y ligero, ideal para tareas básicas con bajo consumo de recursos, aunque tiene limitaciones en la comprensión del contexto.

2. **Los modelos Transformer** representan un punto medio, ofreciendo mejor comprensión contextual y precisión semántica a costa de mayores recursos y necesidad de más datos de entrenamiento.

3. **Los modelos RAG con LLM** son la opción más avanzada, proporcionando el mejor rendimiento en análisis y generación de texto, pero requieren significativos recursos computacionales y una implementación más compleja.

### Comparativa de Rendimiento
| Técnica | Precisión | Velocidad | Recursos | Coherencia |
|---------|-----------|-----------|----------|------------|
| Frecuencia | Baja | Alta | Bajos | Media |
| Transformer | Media | Media | Medios | Alta |
| LLM | Alta | Baja | Altos | Muy Alta |

> **Nota**: Los LLMs han demostrado ser la mejor opción según métricas ROUGE-N, aunque requieren más recursos computacionales.


## Primero, ¿Por qué usar una arquitectura local?

Implementar una arquitectura local puede ser una estrategia conveniente según el contexto y los objetivos del proyecto. Estas son algunas de sus principales ventajas:

- **Privacidad**: Permite mantener los datos dentro de un entorno seguro, sin necesidad de compartir información sensible en la nube. Esto es especialmente importante en contextos empresariales o académicos donde se maneja información crítica.

- **Control**: Ofrece total autonomía sobre la infraestructura y el flujo de trabajo. Las decisiones técnicas no dependen de terceros ni de políticas externas.

- **Costo**: Aunque la inversión inicial en hardware o configuración puede ser más alta, se eliminan los pagos recurrentes de servicios en la nube. Además, si el sistema de IA depende de una API externa (como ChatGPT), el costo será por uso lo que puede escalar rápidamente con el tiempo. También implica un riesgo operativo si esa API deja de funcionar o entra en mantenimiento.

- **Escalabilidad personalizada**: Es posible adaptar la infraestructura a medida que crecen las necesidades del proyecto, sin depender de planes predeterminados o restricciones externas.

- **Latencia**: La respuesta del sistema depende únicamente de tu red y hardware, sin pasar por servidores externos. Esto mejora la velocidad, estabilidad y confiabilidad.


---

## Segundo, ¿Qué modelo local escojo?
Esta es una parte esencial del proyecto. esto va a depender de:

**- ¿Cuantos recursos tengo?**

**- ¿Cuanta potencia necesito?**

**- ¿Qué tipo de tarea voy a realizar?**

Algunos factores a tener en cuenta:

- Tamaño de modelo: modelos grandes ofrecen más precisión, pero consumen más recursos; modelos más pequeños son rápidos y ligeros.
- Dominio: existen modelos especializados para tareas específicas. por ejemplo: medicina. (en su fase de entrenamiento fueron preparados con una base más orientada a su uso.) Esto es importante porque no siempre un modelo más complejo va a ser mejor para resolver una tarea, con menos recursos un modelo especializado puede responder muchísimo mejor.
- Idioma: algunos modelos están entrenados en idiomas específicos.
- Velocidad vs precisión: modelos ligeros son rápidos para tiempo real; modelos grandes destacan en tareas complejas.


**Parámetros:** Los parámetros en los modelos de inteligencia artificial son valores que el modelo ajusta automáticamente durante el proceso de entrenamiento. Estos determinan cómo el modelo procesa la información y toma decisiones. En redes neuronales, por ejemplo, los parámetros son los pesos y sesgos que se ajustan para minimizar el error entre las predicciones del modelo y los resultados reales. Cuantos más parámetros tiene un modelo, mayor es su capacidad para aprender patrones complejos, aunque también aumenta el riesgo de sobreajuste y la necesidad de más datos y potencia de cómputo.

Lo que pasa con los modelos es que salen nuevos cada día, y es muy difícil mantenerse al día. Una manera de elegir es basandose en el leaderboard de modelos. En este caso, lo que haremos es usar el leaderboard de Hugging Face como referencia de los modelos que se podrian utilizar.

[RANKING DE MODELOS EN LOCAL](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/)

> **Aclaración:** Actualmente, no existe un leaderboard oficial y centralizado para modelos específicamente preparados para ejecutarse en Ollama, como sí lo hay en Hugging Face. El ranking enlazado corresponde a modelos evaluados y comparados por la comunidad de Hugging Face, pero no necesariamente refleja el rendimiento de esos modelos ejecutados en Ollama. Si bien Ollama soporta varios de estos modelos y permite correrlos localmente, la plataforma no mantiene un ranking propio ni métricas de comparación estandarizadas. Para comparar modelos en Ollama, se recomienda consultar el [catálogo oficial de modelos](https://ollama.com/library) o buscar benchmarks independientes realizados por la comunidad.


### Comparativa de modelos aplicables al caso (creo que esto es mejor responderlo luego)







## Referencias

- [A Systematic Literature Review on Natural Language Processing (NLP)](https://ieeexplore.ieee.org/document/10055568)
- [The State of the Art of Natural Language](https://direct.mit.edu/dint/article/5/3/707/115133/The-State-of-the-Art-of-Natural-Language)
- [Automated Literature Review Using NLP Techniques and LLM-Based Retrieval-Augmented Generation](https://arxiv.org/abs/2411.18583)
- [The Use of Natural Language Processing in Literature Reviews](https://insights.axtria.com/hubfs/thought-leadership-whitepapers/Axtria-Insights-White-Paper-The-Use-of-Natural-Language-Processing-in-Literature-Reviews.pdf)
