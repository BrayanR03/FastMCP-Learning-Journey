from fastmcp import FastMCP
import requests

mcp_server_main = FastMCP(name="FastMCP-Server-main")

mcp_server_one = FastMCP(name="FastMCP-One")

mcp_server_two = FastMCP(name="FastMCP-Two")

## FASTMCP-ONE

@mcp_server_one.tool(
    name="listar_informacion_pokemon",
    description="En base a un nombre de pokemon, retorna su informacion",
    tags={"tool"},
    enabled=True,
    meta={"author":"Brayan Neciosup"}
)
async def listar_informacion_pokemon(name: str)->dict:
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        if response.status_code!=200:
            return {"message":"Ingresa correctamente el nombre del pokemon"}
        return response.json()
    except:
        return {"message":"Error del llamado de la API"}
    
## FASTMCP-TWO

@mcp_server_two.tool(
    name="add_numbers",
    description="""Calcular la suma de 2 numeros y
    devolver su resultado."""
)
async def add_numbers(a: int,b: int)->float:
    return a + b


mcp_server_main.mount(server=mcp_server_one,prefix="server one") ## ⬅️ prefijo sin "/"
mcp_server_main.mount(server=mcp_server_two,prefix="server two") ## ⬅️ prefijo sin "/"


if __name__ == "__main__":
    mcp_server_main.run(host="127.0.0.1", port=8000,transport="http",log_level="debug")