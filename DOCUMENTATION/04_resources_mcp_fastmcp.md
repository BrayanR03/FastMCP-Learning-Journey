# 🧩 MÓDULO 4: Resources en MCP (Model Context Protocol)

## 📘 Introducción

En el ecosistema MCP (Model Context Protocol), los resources son uno de los pilares fundamentales junto a las tools.
Mientras las tools ejecutan acciones, los resources aportan contexto, datos o conocimiento al modelo, para que pueda razonar o responder de forma más precisa y controlada.

🧠 En pocas palabras:

* Tools → hacen cosas.
* Resources → contienen información

---

## ⚙️ Concepto Base

Un *resource* en MCP se define mediante un **decorador** (`fastmcp`):

```python
@mcp_server.resource(
    uri="resource://ejemplo",
    name="ejemplo",
    description="Un recurso de ejemplo",
    mime_type="application/json"
)
def recurso():
    return {"mensaje": "Hola desde un recurso MCP"}
```
Componentes clave:

* uri: identificador único global del recurso (namespace interno).

* title: Titulo que permite exponerse en el listado de recursos del servidor MCP

* name: nombre legible o descriptivo (para el cliente MCP).

* description: descripción breve del propósito del recurso. (para el cliente MCP)

* mime_type: tipo de dato que retorna (application/json, text/plain, etc.).


Para mas detalle revisar: 📽️[Ejecucion_ServidorMCP-Resource](https://www.youtube.com/watch?v=ha_ILvZFQ-8) y el archivo [04_resources_mcp_fastmcp.py](https://github.com/BrayanR03/FastMCP-Learning-Journey/blob/main/CODE/04_resources_mcp_fastmcp.py)


---

## ⚙️ Problemas iniciales que encontré

Durante la implementación de mi servidor MCP personalizado, noté que:

* El recurso se cargaba correctamente en el servidor (visible en logs y listado interno).

* Pero no era reconocido por el cliente MCP (solo aparecían las tools).

* Intentar consultarlo desde el cliente generaba errores del tipo “resource not found”.

## 💡 Causa encontrada

El problema no era de conexión ni permisos, sino de cómo el recurso estaba definido:

* Algunos recursos no tenían correctamente el URI, el nombre o el tipo MIME.

* En otros casos, se retornaban estructuras no compatibles con el protocolo (por ejemplo, un objeto Python sin serializar).

## ✅ Solución final

Definí correctamente cada recurso usando el decorador @mcp_server.resource, con todos sus metadatos obligatorios y un valor de retorno serializable (texto, JSON, etc.).
Esto permitió que:

* El cliente MCP reconociera automáticamente el recurso.

* Los prompts y contextos pudieran incluirlo.

* Se validara su uso igual que con cualquier tool

--- 

## 🧩 Tipología conceptual de Resources
Aunque el protocolo MCP no impone tipos formales, en la práctica se clasifican según su objetivo o rol dentro del sistema.

| Tipo funcional    | Propósito                                                   | Ejemplo práctico                  |
| ----------------- | ----------------------------------------------------------- | --------------------------------- |
| 🗂️ **Estático**  | Contener información fija (configuración, parámetros base)  | Config global del sistema         |
| 📊 **Dinámico**   | Proveer datos que cambian en tiempo real (estado, métricas) | Uso de CPU, memoria, logs activos |
| 🌐 **Externo**    | Conectar con APIs o servicios externos                      | Consulta de clima, API de precios |
| 📚 **Documental** | Cargar conocimiento o referencias locales                   | Manual técnico, dataset, CSV      |
| ⚙️ **Interno**    | Exponer metainformación del propio servidor MCP             | Listado de tools, introspección   |

La diferencia clave en un recursos estático y dinámico, es el uso de async en la función del recurso.

## 🧭 Conclusión

Los resources son la forma más estructurada y segura de proveer contexto, estado o conocimiento a un modelo dentro del ecosistema MCP.
A diferencia de las tools, no ejecutan acciones, sino que describen el entorno en el que el modelo opera.

Su diseño correcto:

* Mejora la comprensión del modelo.

* Facilita la modularidad del sistema.

* Permite interoperabilidad con múltiples clientes MCP.

    🚀 En resumen:

    * Diseñar bien los resources es diseñar bien el conocimiento que el modelo entenderá. Y su acceso en el cliente MCP es mediante el agregado
    de un recurso como tal agregado en el prompt al cliente MCP.