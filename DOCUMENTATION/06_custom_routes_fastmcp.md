## MÓDULO 06: 📘 Custom Routes en FastMCP (Model Context Protocol)
🧩 ¿Qué son las Custom Routes?

Las custom routes en un servidor FastMCP permiten definir endpoints HTTP personalizados, adicionales al endpoint principal `/mcp/`, para ofrecer información o servicios complementarios al propio servidor MCP.

En otras palabras, te permiten exponer rutas HTTP normales (GET, POST, etc.) dentro del mismo servidor donde corre tu protocolo MCP.

---

### ⚙️ ¿Para qué sirven?

Las rutas personalizadas son útiles para:

* 🔍 Mostrar información acerca del servidor MCP (ej. autor, versión, descripción, fecha de despliegue).

* 🧠 Servir documentación o una página “About Me” con detalles del servidor.

* ⚙️ Exponer métricas del sistema o health checks (para monitoreo o supervisión).

* 📋 Mostrar listados de tools, resources o prompts útiles para el cliente o usuarios internos.

* 🌐 Integrar el servidor MCP con otros sistemas HTTP internos o externos.

---

### 🏢 Contexto de uso

* Si tu servidor MCP se expone públicamente (Internet), las rutas personalizadas pueden servir como una mini documentación interactiva o punto de referencia para quienes consumen tus herramientas o prompts.

* Si tu servidor MCP se usa internamente (en una empresa, red local o laboratorio), basta con una ruta sencilla como /about o /status para mostrar información básica del sistema o del equipo responsable.

---

### 🚦 Transporte requerido

⚠️ Las custom routes sólo funcionan cuando el transporte de tu servidor MCP es HTTP. No están disponibles para transportes como stdio o unix-socket.

Ejemplo:
```python
if __name__=="__main__":
    mcp_server.run(transport="http", host="127.0.0.1", port=3000)
```

---

### 🧱 Ejemplo básico:
```python
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
```
Resultado accesible en:
➡️ http://127.0.0.1:3000/aboutme

Para más detalle verificar el video: [Explicacion Custom Routes](https://youtu.be/25C9mjzafrw) y el archivo: [06_custom_routes_fastmcp.py](https://github.com/BrayanR03/FastMCP-Learning-Journey/blob/main/CODE/06_custom_routes_fastmcp.py)

---

### 🧭 Buenas prácticas

. Evita exponer información sensible (usuarios, rutas locales, credenciales).

. Usa métodos HTTP coherentes (GET para información, POST para acciones).

. Mantén las rutas simples y organizadas: /about, /status, /metrics, etc.

. Documenta dentro de la ruta el propósito del servidor MCP y sus componentes.

. No sobrecargues las rutas con funciones que ya están cubiertas por tools o resources.

---

### 💡 Conclusión

Las custom routes son una herramienta complementaria dentro de FastMCP:

* No sustituyen a las tools, resources ni prompts.

* Se usan para informar, documentar y monitorear tu servidor MCP.

* Son especialmente útiles en entornos públicos o distribuidos, donde otros necesitan entender o verificar rápidamente el estado y propósito de tu servidor MCP.

En entornos internos o locales, basta con una ruta /about o /status para mantener un registro claro de tu instancia MCP.
