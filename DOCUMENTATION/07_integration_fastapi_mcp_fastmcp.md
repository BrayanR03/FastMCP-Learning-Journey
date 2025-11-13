## MÓDULO 07: Integracion FastMCP en FastAPI 📊🔙🔚

### 1. Concepto general de FastMCP

FastMCP es un framework construido sobre el SDK oficial de **Model Context Protocol (MCP)**, desarrollado por Anthropic.
Su propósito es permitir la creación de **servidores MCP** capaces de exponer herramientas, recursos o datos para que **clientes MCP** (como Claude u otros agentes compatibles) puedan interactuar con ellos.

Lo más interesante de FastMCP es que puede funcionar de forma **independiente** o **integrarse dentro de aplicaciones FastAPI**, lo cual permite combinar el poder del protocolo MCP con la flexibilidad, seguridad y estructura modular de FastAPI.

### 2. ¿Por qué FastAPI es ideal para integrar FastMCP?

FastAPI es uno de los frameworks más potentes y modernos en el ecosistema Python, el cuál permite construir APIs escalables, seguras y con tipado completo de datos.
Su naturaleza asíncrona lo hace perfectamente compatible con el modelo ASGI (Asynchronous Server Gateway Interface), que es la base sobre la cual se ejecuta FastMCP.

Por debajo, FastAPI utiliza Starlette como su motor ASGI, esto significa que, aunque la infraestructura técnica provenga de Starlette, todo el ecosistema de FastAPI (rutas, middlewares, dependencias, autenticación, documentación automática, etc.) puede convivir perfectamente con FastMCP.
Por otro lado, Starlette se caracteriza por ser:

* Extremadamente ligero y rápido.

* Base sobre la cual se construye FastAPI.

* Ideal para manejar rutas personalizadas (custom routes) y servidores HTTP asíncronos.

> 🧭 Si quieres aprender a crear una API desde cero en FastAPI antes de integrar FastMCP, revisa mi serie [Creando una API desde cero con FastAPI](https://bryanneciosup626.wixsite.com/brayandataanalitics/post/creando-una-api-desde-cero-con-fastapi), que está próxima a culminar.

###  3. Nested Mounts (Montajes Anidados)

Los nested mounts son una característica avanzada de FastMCP que permiten montar varios servidores MCP dentro de un mismo framework (FastAPI).

* Cada servidor MCP puede tener:

* Sus propios recursos (resources).

* Sus propias tools (herramientas).

* Sus propios prompts o configuraciones.
```python
from fastapi import FastAPI
from fastmcp import FastMCP

app = FastAPI()

server_a = FastMCP(name="server_a")
server_b = FastMCP(name="server_b")


app_a = server_a.http_app(transport="sse",path="/mcp/a")
app_b = server_b.http_app(transport="sse",path="/mcp/b")

app.mount(path="/mcp-server-a/",app=app_a)
app.mount(path="/mcp-server-b",app=app_b)
```
Esto permite:

* Exponer múltiples servidores bajo distintas rutas.

* Escalar sistemas con diferentes propósitos (por ejemplo, uno para documentos internos y otro para datos financieros).

* Crear arquitecturas modulares y fácilmente mantenibles.

Para más detalle verificar el video: [Explicacion Integracion FastAPI](https://www.youtube.com/watch?v=0VUwQ-GTaao) y el archivo: [07_integration_fastapi_mcp_fastmcp.py](https://github.com/BrayanR03/FastMCP-Learning-Journey/blob/main/CODE/07_integration_fastapi_mcp_fastmcp.py)

### 4. Servidores autenticados

FastMCP puede integrarse con sistemas de autenticación (tokens, OAuth2, headers, etc.) al montarse sobre FastAPI.
Esto garantiza que solo clientes autorizados puedan acceder a los recursos MCP expuestos.

Ejemplo de autenticación simple con token:

```python
from fastapi import FastAPI, Header, HTTPException
from fastmcp import FastMCP

app = FastAPI()
server_secure = FastMCP(name="secure_server")

@app.middleware("http")
async def verify_token(request, call_next):
    token = request.headers.get("Authorization")
    if token != "Bearer mi_token_seguro":
        raise HTTPException(status_code=401, detail="Token inválido")
    return await call_next(request)

app.mount("/secure_mcp", server_secure.http_app(path="/path_fastmcp",transport="sse"))

# Utilizamos el transporte "sse" para que FastMCP actúe como un módulo ASGI pasivo, delegando el transporte HTTP al servidor principal.

```
Esto garantiza que solo las solicitudes con el header adecuado puedan acceder al servidor MCP.

### 5. Integración práctica y escalabilidad

Gracias a su compatibilidad con FastAPI, FastMCP puede:

* Integrarse en sistemas empresariales complejos, donde distintos módulos MCP exponen partes de información o servicios internos.

* Mantener la seguridad interna de los recursos sin necesidad de publicarlos en Internet.

* Escalar horizontalmente (añadiendo más servidores MCP según las necesidades).

* Servir simultáneamente a clientes internos (por API) y externos (por MCP clients).

### En conclusión

| Concepto          | Descripción                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| **Starlette**     | Framework ASGI ligero que sirve como base de FastAPI y motor de ejecución de FastMCP.                  |
| **FastMCP**       | Framework que implementa el protocolo MCP para crear servidores que exponen recursos, tools y prompts. |
| **Custom Routes** | Rutas personalizadas para extender las capacidades de un servidor FastMCP.                             |
| **Nested Mounts** | Técnica que permite montar varios servidores MCP dentro de un mismo framework.                         |
| **Autenticación** | Mecanismos (token, OAuth, middleware) para proteger el acceso a los servidores MCP.                    |
| **Integración**   | FastMCP puede montarse dentro de Starlette o FastAPI, combinando capacidades web y de IA.              |

