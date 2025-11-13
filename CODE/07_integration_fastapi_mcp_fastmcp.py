from fastapi import FastAPI
from fastapi import status
from fastmcp import FastMCP

## FASTAPI

app = FastAPI(title="API-FastAPI")

@app.get("/",status_code=status.HTTP_200_OK)
async def main():
    return {"message":"Hola desde FastAPI"}

## FASTMCP
mcp_server = FastMCP(name="Servidor-MCP")

@mcp_server.tool(
    name="add_number",
    description="Calcula la suma de dos números y retorna su resultado.",
    tags={"tools"},
    enabled=True
) 
async def add_numbers(a: int,b: int)->float:
    return a + b

## INTEGRACIÓN DE FASTMCP EN FASTAPI
mcp_app = mcp_server.http_app(transport="sse",path="/mcp")

app.mount(path="/mcp-server",app=mcp_app)


"""
💡 Como la principal herramienta es FastAPI, levantaremos
   mediante uvicorn (servidor para FastAPI). Además, verificar
   que nos encontremos en la carpeta adecuada.
   
   ✔️ Comandos: uvicorn 07_integration_fastapi_mcp_fastmcp:app --reload
   ✔️ Ruta de configuración de servidor MCP para claude_desktop_config.json:
       
       http://127.0.0.1:8000/mcp-server/mcp
"""