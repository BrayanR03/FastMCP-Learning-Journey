# MÓDULO 9: PROXY SERVERS EN FASTMCP

En este capítulo profundizamos en un componente avanzado dentro del ecosistema de FastMCP: los Proxy Servers.
Este tipo de servidores cumple un papel crucial cuando necesitamos intermediar la comunicación entre un cliente MCP y un servidor MCP existente, especialmente en escenarios donde existen limitaciones de compatibilidad, transporte o seguridad.

---

## ⚙️ ¿Qué es un Proxy Server?

Un Proxy Server en FastMCP es un servidor intermediario que recibe las solicitudes de un cliente MCP y las redirige hacia un servidor MCP real.
Su función principal es gestionar el tráfico y adaptarlo, permitiendo que las comunicaciones se mantengan funcionales incluso si el cliente o el servidor utilizan diferentes tipos de transporte (por ejemplo, stdio, SSE, WebSocket, HTTP, etc.).

Podríamos definirlo como un puente inteligente que traduce y encamina las peticiones para que sistemas MCP, separados por versiones, entornos o restricciones tecnológicas, sigan siendo compatibles entre sí.

---

## 🧠 Motivación y propósito

La existencia de los Proxy Servers responde a una necesidad muy real:
mantener la interoperabilidad y disponibilidad de servidores MCP ya existentes sin necesidad de modificar su código original.

Imaginemos el siguiente caso:

    En el año 2025, una empresa desarrolló un servidor MCP que expone herramientas de base de datos PostgreSQL bajo transporte SSE.
    15 años después, los clientes MCP modernos ya no soportan SSE por razones de seguridad y actualización de protocolos.
    Sin embargo, ese servidor sigue siendo funcional y crítico para el negocio.
    En lugar de modificar su código —lo cual podría desestabilizarlo— se crea un Proxy Server FastMCP, que recibe las solicitudes del cliente moderno y las redirige al servidor MCP antiguo, realizando la conversión de transporte necesaria.

De esta manera, FastMCP Proxy Servers se convierten en una solución de compatibilidad y resiliencia a largo plazo.

---

🚀 Ventajas principales

1. Compatibilidad retroactiva:
Permiten conectar clientes modernos con servidores MCP antiguos o no modificables.

2. Seguridad controlada:
Se puede aislar el acceso directo a servidores críticos, utilizando el proxy como capa intermedia de seguridad.

3. Conversión de transportes:
Facilitan la comunicación entre distintos medios de transporte (stdio, http, sse, etc.) sin alterar los endpoints originales.

4. Escalabilidad modular:
Pueden implementarse múltiples proxies, cada uno redirigiendo tráfico a diferentes servidores MCP según la necesidad.

---

⚠️ Desventajas y consideraciones

Aunque extremadamente útiles, los Proxy Servers también presentan limitaciones que deben considerarse:

* Latencia adicional:
Al existir un paso intermedio (cliente → proxy → servidor), el tiempo de respuesta puede aumentar ligeramente.

* Complejidad de configuración:
La correcta definición de rutas, transportes y puertos puede requerir planificación, sobre todo en arquitecturas distribuidas.

* Dependencia del proxy:
Si el proxy falla, se interrumpe el flujo de comunicación, por lo que debe mantenerse alta disponibilidad.

---

## 🧩 Ejemplo conceptual

Supongamos el siguiente esquema de redirección:
```bash
Cliente MCP  →  Proxy Server (FastMCP)  →  Servidor MCP real
```
En el código, esto se podría visualizar de forma conceptual así:
```python
BACKEND_PATH = Path(__file__).parent / "backend_mcp_server.py"

proxy_server = FastMCP.as_proxy(
    ProxyClient(BACKEND_PATH),
    name="ProxyMCP",
)
if __name__=="__main__":
    proxy_server.run(transport="http",host="127.0.0.1",port=3000)
```
Aquí, el cliente MCP se conecta al proxy en el puerto 3000,
y este proxy redirige todas las solicitudes al servidor MCP real que está en el puerto 9000.
El cliente no necesita conocer la existencia del servidor original; todo ocurre de forma transparente.

Para más detalle verificar el video: [Explicacion Server Proxys](https://www.youtube.com/watch?v=JQKN2LJBqqg) y la carpeta: [09_servers_proxys](https://github.com/BrayanR03/FastMCP-Learning-Journey/blob/main/CODE/09_servers_proxys/)


---

## 🧭 Cuándo utilizar un Proxy Server

De acuerdo con las recomendaciones del propio framework, los Proxy Servers deben implementarse en los siguientes escenarios:

1. Cuando no se tiene acceso al código fuente del servidor MCP original.

2. Cuando no es seguro ni conveniente modificar dicho servidor.

3. Cuando se requiere compatibilidad entre diferentes protocolos o transportes.

4. Cuando se necesita aislar el tráfico o registrar peticiones antes de llegar al servidor real.

---

## 🧱 Arquitectura práctica

Un diseño posible dentro de un ecosistema MCP empresarial podría lucir así:
```css
            ┌───────────────────────┐
            │      Cliente MCP                                       │
            └──────────┬────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │   Proxy Server MCP    │
            │ (Conversión SSE→HTTP) │
            └──────────┬────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │   Servidor MCP real  │
            │ (Base de datos 2025) │
            └──────────────────────┘
```

Cada capa cumple su función, pero el Proxy Server es el que mantiene viva la conexión y asegura la interoperabilidad entre componentes que no fueron diseñados originalmente para hablar entre sí.

---

## 🧩 Conclusión

Los Proxy Servers en FastMCP representan una pieza avanzada de arquitectura MCP, pensada para mantener la sostenibilidad, seguridad y compatibilidad del ecosistema a largo plazo. Si bien añaden una pequeña capa de latencia, su valor real reside en preservar la funcionalidad y el acceso a servidores que, de otro modo, serían inaccesibles.

En resumen, un Proxy Server MCP:

    “No es el servidor, pero actúa como él.
    No ejecuta herramientas, pero las permite alcanzar.
    Es el puente silencioso que mantiene unidas las eras tecnológicas.”
