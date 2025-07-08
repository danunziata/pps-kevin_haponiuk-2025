<a name="readme-top"></a>

<!-- PROJECT LOGO -->

<div align="center">
  <a href="https://github.com/danunziata/pps-kevin_haponiuk-2025">
    <img src="docs/images/logo.png" alt="Logo" width="500" height="500">
  </a>
<h3 align="center">🧠 Desarrollo de un Agente de Inteligencia Artificial para la Investigación Científica</h3>

  <p align="center">
    PPS Haponiuk Kevin Joel
    <br />
    <a href="https://danunziata.github.io/pps-kevin_haponiuk-2025/"><strong>Mira la Documentación completa »</strong></a>
    <br />
    <br />
  </p>

</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#sobre-el-proyecto">Sobre el proyecto</a>
      <ul>
        <li><a href="#Componentes">Componentes</a></li>
      </ul>
    </li>
    <li>
      <a href="#para-comenzar">Para Comenzar</a>
      <ul>
        <li><a href="#explicación-del-workflow">Explicación del Workflow</a></li>
        <li><a href="#instalación">Instalación</a></li>
        <li><a href="#commits">Commits</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contribuir">Contribuir</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## Sobre el proyecto

En la **investigación**, uno de los mayores desafíos es la **búsqueda y clasificación de literatura científica**. Los investigadores pueden pasar **meses** revisando cientos de artículos antes de iniciar su propio estudio. Hoy en día, si se quiere utilizar **IA** para este proceso, las herramientas disponibles suelen basarse en información dispersa  y pueden generar respuestas imprecisas o no verificables, lo que limita su uso en el ámbito científico.  


<p align="center">
  <img src="docs/images/manpapers.jpg" alt="Product Name Screen Shot" width="60%">
</p>

Este proyecto propone un **agente de inteligencia artificial** diseñado para **asistir en la investigación científica** con un enfoque en **precisión y confiabilidad**. A diferencia de otros modelos, este sistema trabajará con un **conjunto acotado de documentos** (por ejemplo, **50 papers**), asegurando que las respuestas se basen exclusivamente en esas fuentes y no existe información "inventada".  

### Características principales:

- Consulta inteligente
- Sin invención de datos
- Optimización del tiempo
- Código abierto y adaptable

Este agente permitirá a los investigadores **acceder y organizar el conocimiento de manera más eficiente**, impulsando la integración de la **IA en la ciencia** de forma confiable. 

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

### Componentes

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=black)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/Docker--Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![Qdrant](https://img.shields.io/badge/Qdrant-6A1AFF?style=for-the-badge&logo=qdrant&logoColor=white)](https://qdrant.tech/)
[![GROBID](https://img.shields.io/badge/GROBID-008080?style=for-the-badge)](https://github.com/kermitt2/grobid)
[![n8n](https://img.shields.io/badge/n8n-FE6A16?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/)
[![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge)](https://ollama.com/)
[![OpenWebUI](https://img.shields.io/badge/OpenWebUI-1A1A1A?style=for-the-badge)](https://github.com/open-webui/open-webui)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)](https://grafana.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![PgAdmin](https://img.shields.io/badge/PgAdmin-FF6F00?style=for-the-badge&logo=pgadmin&logoColor=white)](https://www.pgadmin.org/)
[![cAdvisor](https://img.shields.io/badge/cAdvisor-0082C9?style=for-the-badge)](https://github.com/google/cadvisor)

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- GETTING STARTED -->

## Para Comenzar

Este repositorio tiene como objetivo proporcionarte la información necesaria para comenzar rápidamente a trabajar con el proyecto en cuestión. Ya seas un desarrollador experimentado o nuevo en el proyecto, esta guía te ayudará a empezar en poco tiempo.

<!-- EXPLICACION WORKFLOW -->
### Explicación del Workflow

La explicación completa del workflow se encuentra en [la siguiente sección](https://danunziata.github.io/pps-kevin_haponiuk-2025/implementacion/00_workflow-completo/)


<!-- INSTALACION -->
### Instalación

Dirigirse a la sección [Implementación](https://danunziata.github.io/pps-kevin_haponiuk-2025/implementacion/01_implementacion-final/) para ver los pasos de instalación.

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- ROADMAP -->

## Roadmap 

- [ ] investigar herramientas de código abierto y metodologías de investigación.  
- [ ] diseñar la arquitectura del agente de ia, incluyendo modelos de nlp y flujos de datos.
- [ ] desarrollar e integrar el agente con fuentes científicas relevantes. 
- [ ] entrenar y optimizar el modelo para mejorar la precisión de recomendaciones.
- [ ] evaluar el desempeño mediante métricas y pruebas de automatización.
- [ ] ajustar modelos y flujos de trabajo según los resultados obtenidos.
- [ ] diseñar una interfaz intuitiva para facilitar su uso.
- [ ] documentar el proceso de desarrollo, pruebas y resultados.

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- CONTRIBUTING -->

## Contribuir

### Workflow seleccionado "Git Flow"  

El workflow **Git Flow**, creado por Vincent Driessen en 2010, organiza el desarrollo del código en dos ramas principales:  

- **master**: Contiene el código en producción.  
- **develop**: Contiene el código en pre-producción.  

Además, utiliza ramas auxiliares para distintas etapas del desarrollo:  

- **feature***: Para nuevas funcionalidades (se crean desde `develop` y se fusionan en `develop`).  
- **hotfix***: Para corregir errores críticos en producción (se crean desde `master` y se fusionan en `master` y `develop`).  
- **release***: Para preparar nuevas versiones de producción (se crean desde `develop` y se fusionan en `master` y `develop`).  


### ¿Cómo puedo contribuir?
Nos emociona que estés interesado en contribuir a nuestro proyecto. Esta guía está diseñada para ayudarte a entender cómo puedes colaborar con  nosotros, ya sea corrigiendo errores, mejorando la documentación,  agregando nuevas características o cualquier otra forma de contribución  que desees realizar.

Para incorporar una función en la rama `main`, simplemente se crea un "PR" (Pull Request), que deberá ser aprobado por algún colaborador. Cualquier colaborador puede hacerlo, o bien, si no requiere revisión, puede ser aceptado por quien esté incluyendo la funcionalidad.

Es crucial que el nombre de las ramas creadas sea lo más descriptivo posible. Por ejemplo, si trabajamos en una nueva funcionalidad relacionada con la API, la rama se debe llamar como referencia a la funcionalidad en cuestión. En el caso de tratarse de la corrección de un error en el código de la API, la llamaremos `fix-api`.

Este proceso asegura un flujo de trabajo ordenado y facilita la colaboración entre los miembros del equipo.

Los pasos para contribuir en este proyecto como individuo son:

1. Forkear el repositorio (`git fork`)
2. Crear una nueva rama para la función (`git checkout -b feature/AmazingFeature`)
3. Publicar la rama en el repositorio remoto(`git push --set-upstream origin <nombre-de-la-nueva-rama>`)
4. Commit los cambios (`git commit -m 'Add some AmazingFeature'`)
5. Push a la rama (`git push origin feature/AmazingFeature`)
6. Abrir un Pull Request dirigido a la rama `develop`

### Commits

Los commits convencionales nos permiten mantener la organización al realizar los commits y facilitan la creación de `releases` de forma automatizada.

Se basan en el uso de palabras clave al inicio del mensaje de cada commit, de la siguiente manera:

- **feat(tema de la modificación): Breve explicación**: Para cambios significativos o nuevas características.
- **fix(tema de la modificación): Breve explicación**: Para correcciones pequeñas.
- **chore(tema de la modificación): Breve explicación**: Para cambios menores insignificantes para el usuario.
- **docs: Breve explicación**: Para cambios que se realizan a la documentación.

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- LICENSE -->

## Licencia

Este proyecto se distribuye bajo los términos de la  Licencia Pública General de GNU, versión 3.0 (GNU General Public  License, version 3.0). Consulta el archivo [LICENSE](https://github.com/danunziata/pps-kevin_haponiuk-2025/blob/main/LICENSE) para obtener detalles completos.

### Resumen de la Licencia

La Licencia Pública General de GNU, versión 3.0 (GNU GPL-3.0), es una licencia de código abierto que garantiza la libertad de uso, modificación y distribución del software bajo los términos estipulados en la licencia. Requiere que cualquier software derivado se distribuya bajo los mismos términos de la GPL-3.0. Consulta el archivo [LICENSE](https://github.com/danunziata/pps-kevin_haponiuk-2025/blob/main/LICENSE) para más información sobre los términos y condiciones.

### Aviso de Copyright

El aviso de copyright para este proyecto se encuentra detallado en el archivo [LICENSE](https://github.com/danunziata/pps-kevin_haponiuk-2025/blob/main/LICENSE).

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- CONTACT -->

## Contacto

Haponiuk Kevin Joel - kevinhapo@gmail.com

Link del Proyecto: [https://github.com/danunziata/pps-kevin_haponiuk-2025](https://github.com/danunziata/pps-kevin_haponiuk-2025)

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>


