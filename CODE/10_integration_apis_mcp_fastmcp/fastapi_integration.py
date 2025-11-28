from fastmcp import FastMCP
from fastapi import FastAPI
from fastmcp.server.openapi import RouteMap,MCPType

app = FastAPI()

clientes = [
    {"name":"Brayan","age":"24"},
    {"name":"Rafael","age":"50"},
    {"name":"Pepito","age":"48"}
]

@app.get("/status")
async def status_api():
    return {"message":{
        "status":"ok"
    }}


@app.get("/clientes")
async def listar_clientes():
    return clientes
    

@app.delete("/cliente/{name}")
async def delete_cliente(name: str):
    for i,j in enumerate(clientes):
        if name==j["name"]:
            clientes.remove(i)
    
    return {"message":{
        "status":"ok"
    }}


mcp_server = FastMCP.from_fastapi(
    app=app,
    name="Servidor-MCP-from-FastAPI",
    route_maps=[ ## ⬅️ Permite filtrar que ENDPOINTS serán resources, prompts y tools (por defecto)
        ## Métodos GET como recursos
        RouteMap(
            methods=["GET"],pattern=r".*",mcp_type=MCPType.RESOURCE
        ),
        ## Los demás ENDPOINTS serán TOOLS.
    ])

@mcp_server.tool(
    name="add_numbers",
    description="Calcular la suma de 2 números y retornar el valor."
)
async def add_numbers(a: int,b: int)->float:
    return a + b



if __name__=="__main__":
    mcp_server.run(transport="http",host="127.0.0.1",port=8000)

