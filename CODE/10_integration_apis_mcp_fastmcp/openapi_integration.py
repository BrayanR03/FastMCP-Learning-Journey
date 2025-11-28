import httpx
from fastmcp import FastMCP
from pathlib import Path
# import yaml ## Librería para la lectura de la especificación de la API 

## Creo un cliente HTTP para la API
openapi_cliente = httpx.AsyncClient(base_url="https://petstore3.swagger.io/api/v3")


## Cargar la especificación de la OpenAPI ( DESDE LA URL JSON)
openapi_especificacion = httpx.get("https://petstore3.swagger.io/api/v3/openapi.json").json()


# Cargar la especificación de la OpenAPI ( DESDE SU .YAML)
# current_file = Path(__file__)
# project_root = current_file.parents[0]
# file_yaml = project_root / "openapi.yaml"

# with open(file_yaml,"r",encoding="utf-8") as file:
#     openapi_especificacion = yaml.safe_load(file)



# Crear el servidor MCP Server

mcp_server = FastMCP.from_openapi(
    openapi_spec=openapi_especificacion,
    client=openapi_cliente,
    name="PetStore-MCP"
)

if __name__ == "__main__":
    mcp_server.run(transport="http",host="127.0.0.1",port=8000)




