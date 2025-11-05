from fastmcp import FastMCP
from fastmcp.tools import Tool,tool
from typing import Annotated ## Permite realizar validaciones estrictas en los parámetros de las tools
from pydantic import Field ## Define campo/parámetro en la tool(control estricto sobre el parámetro)

#### DEFINICIÓN DEL MCP SERVER
mcp_server_tools = FastMCP(name="servidor-mcp-tools") ## Nombre del MCP Server sin tildes


## =====================================================================================================================

# ### TOOL BÁSICA

# @mcp_server_tools.tool(
#     name= "sumar_dos_numeros", ## Nombre sin espacios en blanco, sin caracteres(tíldes)
#     description= "Debes sumar dos numeros y retornar un resultado" ## Contexto claro para el cliente MCP(LLM)
    
# )
# async def sumar(a: int, b: int)->float:  ## Generamos el input_schema con los parámetros de la función. 
#                                          ## Además, el output_schema se genera con el objeto que retorne la función.
#     """ Tool que permite al LLM sumar 2 numeros """ ## DocString de documentación técnica.
#     return a + b ## Lógica

## =====================================================================================================================

# ### TOOL CON TAGS Y METADATOS

# @mcp_server_tools.tool(
#     name= "sumar_dos_numeros", ## Nombre sin espacios en blanco, sin caracteres(tíldes)
#     description= "Debes sumar dos numeros y retornar un resultado", ## Contexto claro para el cliente MCP(LLM)
#     tags= {"artimeticas"},
#     meta={"version":"1.0.0","author":"Brayan R."}
# )
# async def sumar(a: int, b: int)->float:  ## Generamos el input_schema con los parámetros de la función. 
#                                          ## Además, el output_schema se genera con el objeto que retorne la función.
#     """ Tool que permite al LLM sumar 2 numeros """ ## DocString de documentación técnica.
#     return a + b ## Lógica

## =====================================================================================================================


# ### TOOL DERIVADA DE OTRA TOOL

# # Tool base con decorador
# @mcp_server_tools.tool()
# async def sumar(a: int, b: int) -> float:
#     """Suma dos números y devuelve el resultado"""
#     return a + b

# # Tool derivada que reutiliza la lógica base
# @mcp_server_tools.tool()
# async def sumar_redondeado(a: int, b: int) -> int:
#     """Suma dos números, multiplica el resultado por 10 y lo redondea"""
#     resultado = await sumar(a, b)
#     return round(resultado * 10)

## =====================================================================================================================


#### TOOL COMPLETA BIEN ESPECIFICADA

@mcp_server_tools.tool(
    name="multiplicar_numeros",
    description="Calcula la multiplicacion de los numeros y retorna su valor",
    tags={"aritmeticas"},
    meta={"author":"Brayan R.","version":"1.0.0"}
)
async def multiplicar(
    a: Annotated[int,Field(description="Ingresar primer numero")],
    b: Annotated[int,Field(description="Ingresar segundo numero")]
)->int:
    """ Función que permite multiplicar ambos números """
    return a * b


## =====================================================================================================================

## Lanzamos el servidor
if __name__=="__main__":
    mcp_server_tools.run(transport="http",port=8000,host="127.0.0.1")
    
