# MODEL CONTEXT PROTOCOL
## MÓDULO 1 — MCP Conceptos y Setup
---

### 🧩 ¿Qué es MCP?

MCP (Model Context Protocol) es un protocolo abierto que define cómo los Modelos de Lenguaje (LLMs) pueden comunicarse con servicios externos (como APIs, bases de datos o sistemas internos) de forma estructurada, segura y reproducible.

Antes de MCP, los LLMs estaban limitados a respuestas textuales o integraciones propietarias (plugins, APIs privadas). MCP rompe ese paradigma al ofrecer una manera estandarizada de:

* Exponer herramientas (tools) y recursos (resources) a los LLMs.

* Asegurar la privacidad y el control total de los datos por parte de las empresas.

* Permitir que tanto organizaciones privadas como usuarios individuales conecten sus modelos con servidores MCP públicos o privados.

En esencia, MCP permite extender las capacidades de los modelos de forma modular, controlada y segura.

---

### 🧱 Componentes de MCP

| Componente              | Descripción                                                             | Ejemplo                                              |
| ----------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------- |
| **Client (MCP Client)** | El cliente que envía solicitudes al servidor (ej. Claude, Copilot)      | Claude invoca una herramienta `tool:generate_report` |
| **Server (MCP Server)** | Servicio que define y expone herramientas o recursos al cliente         | Tu servidor FastMCP local o en la nube               |
| **Tool**                | Acción ejecutable con parámetros definidos                              | `analyze_sales(file="ventas.csv")`                   |
| **Resource**            | Información accesible por el cliente (archivos, documentos, plantillas) | `/resources/manual_ventas.pdf`                       |
| **Manifest (mcp.json)** | Archivo que describe qué ofrece el servidor (tools, resources, prompts) | `mcp_data_profiler/mcp.json`                         |

---

### 🔒 Seguridad y paradigma MCP

Antes, las empresas evitaban exponer sus datos a los modelos por miedo a filtraciones o dependencia de integraciones inseguras.
Con MCP, la empresa controla el servidor y los datos. El modelo solo accede a lo que se le expone explícitamente mediante el protocolo.

Esto permite:

* Desarrollar servidores privados para uso interno.

* Publicar MCP servers públicos seguros para la comunidad.

* Conectar LLMs a sistemas empresariales sin comprometer la información.

MCP redefine la relación entre los LLMs y los datos empresariales:
ya no es el modelo quien “ve” los datos, sino el servidor quien decide qué mostrarle y cómo.

---

### ⚡ ¿Qué es FastMCP?

FastMCP es un framework en Python inspirado en FastAPI, diseñado para crear y ejecutar servidores MCP fácilmente.
Proporciona una sintaxis moderna y minimalista, basada en decoradores, para exponer tools, resources y prompts.

🚀 Ventajas clave

* Define tools y resources con decoradores simples.

* Soporta modos de ejecución (STDIO, HTTP, SSE).

* Permite crear servidores compuestos o proxys.

* Se integra perfectamente con FastAPI, si se desea exponer endpoints web.

* Es seguro, modular y escalable, ideal para entornos productivos.

En resumen:

- FastMCP es para MCP lo que FastAPI fue para REST.

---

### 🧩 Conceptos clave para recordar

* MCP: Protocolo para conectar LLMs con sistemas externos.

* FastMCP: Framework Python para construir servidores MCP fácilmente.

* Tools: Funciones o acciones ejecutables por el cliente.

* Resources: Datos o archivos accesibles por el cliente.

* Manifest (mcp.json): Describe las capacidades del servidor MCP.

* Transportes: Mecanismos de comunicación entre cliente y servidor (STDIO, HTTP, SSE).

---

### 🔍 Modos de ejecución

| Modo      | Descripción                                      | Uso típico                                 |
| --------- | ------------------------------------------------ | ------------------------------------------ |
| **STDIO** | Comunicación local entre el modelo y el servidor | Desarrollo local / integración con Claude  |
| **HTTP**  | Comunicación vía API REST                        | Despliegue en la nube o servidores remotos |
| **SSE**   | Transmisión de eventos (heredado)                | Compatibilidad con versiones antiguas      |

---

📄 Documentación de FastMCP: [FastMCP-Documentation](https://gofastmcp.com/getting-started/welcome) 
