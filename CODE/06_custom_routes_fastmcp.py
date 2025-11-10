from fastmcp import FastMCP
from starlette.responses import JSONResponse

mcp_server = FastMCP(name="MCP-Custom-Routes")

@mcp_server.tool(
    name="add_numbers",
    description="""Calcular la suma de 2 números y
    devolver su resultado."""
)
async def add_numbers(a: int,b: int)->float:
    return a + b

@mcp_server.custom_route(
    path="/aboutme",
    methods=["GET"],
    name="about_me_server"
)
async def about_me(request)->JSONResponse:
    data= {
        "name_server":"MCP-Custom-Routes",
        "tools_server":{
            "tool_1":"add_numbers"
        },
        "author":"Brayan Neciosup"
    }
    return JSONResponse(data)
    
if __name__=="__main__":
    mcp_server.run(transport="http",host="127.0.0.1",port=8000)
