# Ejemplo de Integración MCP en n8n

Esta sección describe el proceso para instalar y utilizar los nodos MCP (Model Context Protocol) en n8n, utilizando como ejemplo la conexión con el servicio Brave Search.

## 1. Instalación de los nodos MCP

Para instalar los nodos MCP desarrollados por la comunidad, se deben seguir los siguientes pasos:

1. Acceder a **Ajustes** en n8n.
2. Seleccionar **Community Nodes**.
3. Buscar "n8n-nodes-mcp" y hacer clic en **Install**.

<p align="center">
  <img src="/images/mcp_install-nodes.png" width="60%">
  <br>
  <em>Figura 1: Instalación del nodo MCP en n8n</em>
</p>

Una vez instalado, el nodo MCP estará disponible para ser agregado a los flujos de trabajo.

<p align="center">
  <img src="/images/mcp_install-nodes-2.png" width="50%">
  <br>
  <em>Figura 2: Nodo MCP disponible en n8n</em>
</p>

> **Nota:** Si el nodo no aparece, se recomienda refrescar la página.

## 2. Configuración de credenciales MCP

Para conectar el nodo MCP con un servicio, es necesario agregar las credenciales correspondientes. La lista de servicios compatibles se encuentra disponible en:

[https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

En este ejemplo, se utilizará **Brave Search**. Para ello, se debe localizar el servicio en la lista:

[https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)

La información obtenida debe ser ingresada en el bloque de configuración del cliente MCP:

<p align="center">
  <img src="/images/mcp_brave-npx.png" width="100%">
  <br>
  <em>Figura 3: Configuración del cliente MCP con credenciales de Brave</em>
</p>

Posteriormente, estos datos deben ser cargados en las credenciales del nodo MCP Client en n8n, como se puede observar, necesitamos agregar la API KEY también:

<p align="center">
  <img src="/images/mcp_brave-npx-n8n.png" width="80%">
  <br>
  <em>Figura 4: Ingreso de credenciales en n8n para MCP Client</em>
</p>

la cual puede obtenerse registrándose en:

[https://api-dashboard.search.brave.com/app/keys](https://api-dashboard.search.brave.com/app/keys)

<p align="center">
  <img src="/images/mcp_brave.png" width="100%">
  <br>
  <em>Figura 5: Panel de Brave Search para obtener la API Key</em>
</p>

## 3. Pruebas de conexión y uso de herramientas

Para verificar las herramientas disponibles, se puede realizar una consulta desde el nodo MCP:

<p align="center">
  <img src="/images/mcp_brave-npx-n8n-availabletools.png" width="80%">
  <br>
  <em>Figura 6: Consulta de herramientas disponibles en MCP</em>
</p>

De igual manera, es posible probar la herramienta de búsqueda de Brave de forma individual:

<p align="center">
  <img src="/images/mcp_brave-npx-n8n-executetools.png" width="80%">
  <br>
  <em>Figura 7: Ejecución de la herramienta de búsqueda de Brave</em>
</p>

---

### Referencias
- [Video tutorial: Integración MCP en n8n (YouTube)](https://www.youtube.com/watch?v=MZ1YECHTZb0)