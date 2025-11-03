# 🧩 MI PRIMER SERVIDOR MCP BÁSICO

En este módulo crearemos **nuestro primer servidor MCP** utilizando **FastMCP**, entendiendo su estructura, las herramientas (tools) y los modos de transporte.
Además. centraremos la serie en todo lo referente a servidores MCP en FastMCP.
---

## 📘 Conceptos previos

Antes de crear nuestro primer servidor, debemos comprender los siguientes conceptos:

* **FastMCP** → Librería que combina la simplicidad de **FastAPI** con el nuevo **Model Context Protocol (MCP)**, permitiendo construir servidores MCP escalables y rápidos.
* **Servidor MCP (MCP Server)** → Conjunto de herramientas (tools) expuestas local o remotamente que amplían las capacidades de un LLM.
* **Herramienta (Tool)** → Función o acción concreta que el LLM puede ejecutar a través del servidor MCP.

---

## ⚙️ PASO A. Importar las librerías necesarias

```python
from fastmcp import FastMCP
```

FastMCP es la base para trabajar con servidores MCP dentro de entornos Python/FastAPI.

---

## ⚙️ PASO B. Establecer un contexto MCP Server

```python
mcp_server = FastMCP(name="hello-fastmcp")
```

El parámetro `name` define el nombre interno de tu servidor MCP (sin tildes ni caracteres especiales).
Este nombre se usará para identificar al servidor desde el cliente MCP.

---

## ⚙️ PASO C. Crear una herramienta (Tool)

Gracias al decorador `@mcp_server.tool`, podemos registrar una herramienta dentro del servidor MCP.

```python
@mcp_server.tool(
    name="sumar_numeros",  # nombre de la herramienta (válido MCP)
    description="Suma dos números y devuelve el resultado."
)
async def sumar(a: int, b: int) -> float:
    """Función asincrónica que realiza una suma."""
    return a + b
```

📌 **Notas importantes:**

* El nombre de la tool **no puede tener tildes, espacios ni caracteres especiales**.
  Solo se permiten: `a-z`, `A-Z`, `0-9`, `_` y `-`.
* `description` puede incluir texto libre (con tildes, emojis, etc.).
* Los parámetros (`a`, `b`) son tipados para que el LLM sepa qué argumentos enviar.
* Las funciones pueden ser `async` o normales.

---

## ⚙️ PASO D. Levantar el servidor MCP

FastMCP soporta tres modos de transporte:

| Transporte | Descripción                                        | URL o comunicación          |
| ---------- | -------------------------------------------------- | --------------------------- |
| `http`     | Recomendado para pruebas locales y despliegue web. | `http://127.0.0.1:3000/mcp` |
| `sse`      | Server-Sent Events (modo heredado).                | `http://127.0.0.1:3000/sse` |
| `stdio`    | Comunicación directa entre procesos (sin red).     | No genera URL               |

Ejemplo:

```python
if __name__ == "__main__":
    mcp_server.run(transport="http", host="127.0.0.1", port=3000)
    # mcp_server.run(transport="sse", host="127.0.0.1", port=3000)
    # mcp_server.run()  # modo stdio (por defecto)
```

Para desarrollo local se recomienda usar **`transport="http"`**, debido que permite visualizar y probar el servidor fácilmente.
Además, para ejecutar el archivo principal utilizaremos el gestor de paquetes uv, con los siguientes comandos:

```bash
uv init ## Inicializar proyecto
uv add fastmcp ## Agregar la librería FastMCP
uv run main.py ## Inicializar proyecto
```

**uv** es un gestor moderno para proyectos en Python que facilita la creación y administración del entorno de trabajo.
Al ejecutar **`uv init`**, se genera automáticamente una estructura básica de proyecto que incluye archivos como **`.gitignore`**, **`.python-version`**, **`main.py`**, **`pyproject.toml`** y un **`README.md`**. Esto permite iniciar rápidamente el desarrollo con buenas prácticas y una configuración inicial compatible con Git (la cual puedes ajustar antes de realizar tus commits o pushes).

A diferencia de otros enfoques donde configuramos manualmente un *virtual environment*, **uv** lo crea automáticamente la primera vez que instalas una librería.
Por ejemplo, al ejecutar **`uv add fastmcp`**, se instala la dependencia y se genera el entorno virtual correspondiente.
Una vez hecho esto, basta con cerrar y abrir una nueva terminal: uv activará automáticamente el entorno virtual, permitiéndote ejecutar tu proyecto desde main.py sin pasos adicionales.

---

## 🧠 ¿Qué ocurre internamente?

Cuando un LLM (como Claude) ejecuta una instrucción natural:

> “Suma 4 y 5 usando el servidor MCP.”

1. El cliente MCP identifica la tool `sumar_numeros`.
2. Traduce la instrucción a una **llamada JSON-RPC** y la envía a `http://127.0.0.1:3000/mcp`.
3. FastMCP ejecuta la función `sumar(4, 5)` en tu servidor.
4. Retorna el resultado `9` al cliente.
5. El LLM interpreta la respuesta y te muestra el resultado natural.

---

## ⚙️ Configuración del cliente MCP (Claude)

Para que Claude se comunique con tu servidor, se debe agregar en el archivo de configuración del cliente (por ejemplo, `.claude_config.json`):

```json
"mcp-hello-fastmcp-local": {
  "command": "npx",
  "args": [
    "-y",
    "mcp-remote",
    "http://127.0.0.1:3000/mcp"
  ]
}
```

📍 Si usas SSE, cambia la ruta final a `/sse`.

Verificar 📽️ [Configuracion_ServidorMCP_ClaudeDesktop.mp4](https://www.youtube.com/watch?v=2A7m_7B7-c4)

Para mas detalle del servidor MCP Básico revisar: [02_primer_servidor_mcp.py](https://github.com/BrayanR03/FastMCP-Learning-Journey/blob/main/CODE/02_primer_servidor_mcp.py)
---

## 🧩 Conclusión:

✅ Comprendimos qué es un servidor MCP y qué papel juega FastMCP.
✅ Creamos una primera herramienta (`sumar_numeros`) y la registramos.
✅ Aprendimos a levantar el servidor con distintos modos de transporte.
✅ Configuramos un cliente MCP (Claude) para conectarse a nuestro servidor.

Con esto, ya tenemos las bases para construir **servidores MCP funcionales y probables de ampliar** con tools más complejas y dinámicas.

---

📘 **Siguiente capítulo:**
*Tools avanzadas, parámetros y registro dinámico de herramientas.*
