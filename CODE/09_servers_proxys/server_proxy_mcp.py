from fastmcp import FastMCP
from fastmcp.server.proxy import ProxyClient
from pathlib import Path

## Creación del Proxy Server

## Opción 1: Siempre que contemos con el archivo del servidor MCP y se encuentre en transporte STDIO
# MCP_SERVER_PATH = Path(__file__).parent / "mcp_server_local.py"

# proxy_server = FastMCP.as_proxy(
#     ProxyClient(MCP_SERVER_PATH),
#     name="ProxyMCP",
# )
# """
# 💡 EJECUTAMOS DIRECTAMENTE ESTE ARCHIVO (server_proxy_mcp.py):
#     uv run server_proxy_mcp.py
# """

## ====================================================================================

## Opción 2: Siempre que el servidor MCP se encuentre desplegado y en modo de transporte SSE

MCP_SERVER_REMOTE = "http://127.0.0.1:3000/sse" ## Modo de transporte SSE


proxy_server = FastMCP.as_proxy(
    ProxyClient(MCP_SERVER_REMOTE),
    name="ProxyMCP",
)

# """
#     💡 PREVIAMENTE DEBEMOS TENER EL SERVIDOR MCP LOCAL LEVANTADO o DESPLEGADO.
# """

if __name__=="__main__":
    proxy_server.run(transport="http",host="127.0.0.1",port=8000)
    

