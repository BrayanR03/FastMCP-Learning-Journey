from fastmcp import FastMCP ## ⬅️ Importamos librería FastMCP

## 💡 Establecemos el contexto del servidor MCP
mcp_server = FastMCP(
    name="FastMCP-Primer-Servidor", ## ⬅️ Nombre asignado a Servidor MCP
    version="1.0.0" ## ⬅️ Versión asignada a Servidor tMCP
)

## 💡 Tool básica de ejemplo (Indagaremos más adelante ...)
@mcp_server.tool(
    name="add_numbers", ## 💡 Nombre asignada a la tool
    description="Calcular la suma de 2 números y retornar su valor" ## 💡 Descripción asignada a la tool
)
async def add_numbers(a: int,b: int)->float: ## ⬅️ Función asíncrona asignada a la tool del Servidor MCP
    return a + b ## ⬅️ Lógica de la función

## ✅ Levantamiento de Servidor MCP
if __name__=="__main__":
    mcp_server.run(transport="http",host="127.0.0.1",port=3000) ## ⬅️ Modo de transporte http (Indagaremos más adelante ...)