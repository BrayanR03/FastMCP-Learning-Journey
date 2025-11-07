from fastmcp import FastMCP


mcp_server = FastMCP(name="servidor-mcp-prompts")

@mcp_server.prompt(
    name="saludo_formal_usuario",
    description="Devuelve una respuesta con los parámetros indicados.",
    tags={"prompt"},
    enabled=True,
    meta={"author":"Brayan"}
)
def prompt_saludo(name: str):
    """ Prompt para generar un saludo personalizado"""
    return f"""
    Genera un mensaje de saludo para el usuario llamado {name}.
    Si el usuario se llama 'Brayan', usa un estilo formal, de lo contrario
    usa un estilo callejero
    """
@mcp_server.tool(
    name="saludo_formal",
    description="Devuelve un saludo formal al usuario",
    tags={"tool"},
    meta={"author":"Brayan"}
)
async def saludo_formal(name: str)->str:
    """ Tool que devuelve un saludo formal"""
    return f"Estimado {name}, es un gusto tenerlo en este espacio."

@mcp_server.tool(
    name="saludo_callejero",
    description="Devuelve un saludo callejero",
    tags={"tool"},
    meta={"author":"Brayan"}
)
def saludo_callejero(name: str)->str:
    """ Tool que devuelve un saludo callejero"""
    return f"""
    Hola {name}, que hay?, en que andas??
    """

## 💡 Foro MCP Prompts: https://medium.com/@laurentkubaski/mcp-prompts-explained-including-how-to-actually-use-them-9db13d69d7e2

if __name__=="__main__":
    mcp_server.run(transport="http",port=8000,host="127.0.0.1")