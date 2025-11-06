from fastmcp import FastMCP
import random
from datetime import datetime
import getpass
import psutil
import platform
mcp_server = FastMCP(name="servidor-mcp-resources")


@mcp_server.tool(
    name="multiplicar_numeros",
    description="Calcularas la multiplicación de los números y retornarás en resultado"
)
async def multiplicar(a: int,b: int)->float:
    """ Función que permite multiplicar números  """
    return a * b

# #### ===================================================================================
## --- RECURSO QUE SE EXPONE INTERNAMENTE (ESTADO DEL SISTEMA)[EJEMPLO 1]
@mcp_server.resource(
    uri="resource://estado_sistema",
    title="Recurso - Estado del Sistema",
    name="estado_sistema",
    description="Devuelve el estado actual del servidor MCP",
    mime_type="application/json"
)
async def estado_sistema() -> dict:
    return {
        "status": "activo",
        "uptime": f"{random.randint(1, 500)} minutos",
        "timestamp": datetime.now().isoformat()
    }


# #### ===================================================================================
## --- RECURSO QUE SE EXPONE INTERNAMENTE (ESTADO DE LA MÁQUINA LOCAL)[EJEMPLO 2]

# Definimos el recurso interno
@mcp_server.resource(
    uri="resource://system_status",
    name="system_status",
    title="Recurso - Estado de mi Laptop",
    description="Muestra información básica del sistema local (hora, usuario, CPU, memoria, disco)",
    mime_type="application/json"
)
def obtener_estado_sistema() -> dict:
    # Hora y fecha actuales
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Usuario actual
    usuario = getpass.getuser()

    # Información del sistema operativo
    sistema = platform.system()
    version = platform.version()

    # Uso de CPU y memoria
    uso_cpu = psutil.cpu_percent(interval=0.5)
    memoria = psutil.virtual_memory()
    uso_memoria = memoria.percent

    # Espacio en disco
    disco = psutil.disk_usage('/')
    espacio_total_gb = round(disco.total / (1024 ** 3), 2)
    espacio_usado_gb = round(disco.used / (1024 ** 3), 2)
    espacio_libre_gb = round(disco.free / (1024 ** 3), 2)

    return {
        "hora_actual": hora_actual,
        "usuario": usuario,
        "sistema": f"{sistema} {version}",
        "uso_cpu_%": uso_cpu,
        "uso_memoria_%": uso_memoria,
        "disco_total_GB": espacio_total_gb,
        "disco_usado_GB": espacio_usado_gb,
        "disco_libre_GB": espacio_libre_gb
    }

## 💡 Importante: Los recursos son utilizados por el cliente MCP como contexto agregado al prompt que ingresemos.
##                Es decir, se agrega como un adjunto para ser utilizado.

## ✅ Post donde encontré como usar los recursos: https://medium.com/@laurentkubaski/mcp-resources-explained-and-how-they-differ-from-mcp-tools-096f9d15f767

if __name__=="__main__":
    mcp_server.run(transport="http",port=8000,host="127.0.0.1",log_level="debug")
