from fastmcp import FastMCP


server_local = FastMCP(name="ServidorMCP-SSE")

@server_local.tool(
    name="add_numbers_total",
    description="Calcula la suma de 2 números y retorna su resultado",
    tags={"tool"}
)
async def add_numbers(a: int,b: int)->float:
    return a + b

if __name__=="__main__":
    # server_local.run() ## Modo de transporte STDIO
    server_local.run(transport="sse",host="127.0.0.1",port=3000) ## Modo de transporte SSE (Ejemplo de MCP Remoto)
    
