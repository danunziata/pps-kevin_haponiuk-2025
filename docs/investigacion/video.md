## ¿Por qué usar una arquitectura local?

Implementar una arquitectura local puede ser una estrategia conveniente según el contexto y los objetivos del proyecto. Estas son algunas de sus principales ventajas:

- Privacidad  
Permite mantener los datos dentro de un entorno seguro, sin necesidad de compartir información sensible en la nube. Esto es especialmente importante en contextos empresariales o académicos donde se maneja información crítica.

- Control  
Ofrece total autonomía sobre la infraestructura y el flujo de trabajo. Las decisiones técnicas no dependen de terceros ni de políticas externas.

- Costo  
Aunque la inversión inicial en hardware o configuración puede ser más alta, se eliminan los pagos recurrentes de servicios en la nube. Además, si el sistema de IA depende de una API externa (como ChatGPT), el costo será por uso lo que puede escalar rápidamente con el tiempo. También implica un riesgo operativo si esa API deja de funcionar o entra en mantenimiento.

- Escalabilidad personalizada  
Es posible adaptar la infraestructura a medida que crecen las necesidades del proyecto, sin depender de planes predeterminados o restricciones externas.

- Latencia  
La respuesta del sistema depende únicamente de tu red y hardware, sin pasar por servidores externos. Esto mejora la velocidad, estabilidad y confiabilidad.


---

### ¿Qué modelo local escojo?
Esta es una parte esencial del proyecto. esto va a depender de:

¿cuantos recursos tengo?
¿cuanta potencia necesito?


- Tamaño de modelo: modelos grandes ofrecen más precisión, pero consumen más recursos; modelos más pequeños son rápidos y ligeros.
- Dominio: existen modelos especializados para tareas específicas. por ejemplo: medicina. (en su fase de entrenamiento fueron preparados con una base más orientada a su uso.) Esto es importante porque no siempre un modelo más complejo va a ser mejor para resolver una tarea, con menos recursos un modelo especializado puede responder muchísimo mejor.
- Idioma: 
- Requerimientos computacionales: Modelos grandes necesitan GPUs más potentes.
- Velocidad vs precisión: modelos ligeros son rápidos para tiempo real; modelos grandes destacan en tareas complejas.
- tipo de tarea:

una manera de elegir es basandose 

[RANKING DE MODELOS EN LOCAL](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/)


Parámetros: Los parámetros en los modelos de inteligencia artificial son valores que el modelo ajusta automáticamente durante el proceso de entrenamiento. Estos determinan cómo el modelo procesa la información y toma decisiones. En redes neuronales, por ejemplo, los parámetros son los pesos y sesgos que se ajustan para minimizar el error entre las predicciones del modelo y los resultados reales. Cuantos más parámetros tiene un modelo, mayor es su capacidad para aprender patrones complejos, aunque también aumenta el riesgo de sobreajuste y la necesidad de más datos y potencia de cómputo.


## RAG

¿Qué es? ¿por qué debemos implementarlo?

<p align="center">
  <img src="/images/rag.webp" width="100%">
  <br>
  <em>Figura x: "descripción de la imagen"</em>
</p>