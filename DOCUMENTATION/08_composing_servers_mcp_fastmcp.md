## MÓDULO 08: Composing Servers en FastMCP
La composición de servidores (composing servers) es la capacidad de un servidor FastMCP principal de incluir dentro de sí múltiples servidores FastMCP secundarios (subservidores).

Dicho de otra manera:

> “Un servidor MCP puede actuar como orquestador de otros servidores MCP”.

Esto te permite agrupar varias funcionalidades independientes —cada una en su propio servidor MCP— y montarlas dentro de un servidor principal, que se expone externamente como una sola unidad coherente.

---

## ⚙️ ¿Por qué es útil?

Esta característica existe para dividir responsabilidades y escalar sistemas MCP complejos sin perder organización.

Por ejemplo:
| Servidor MCP   | Función                  | Descripción                                                               |
| -------------- | ------------------------ | ------------------------------------------------------------------------- |
| `mcp_datasets` | Gestión de datasets      | Expone tools y resources para leer, limpiar o cargar datasets.            |
| `mcp_auth`     | Autenticación y permisos | Maneja credenciales, tokens o control de acceso.                          |
| `mcp_files`    | Sistema de archivos      | Expone tools para leer, escribir y listar archivos.                       |
| `mcp_main`     | Servidor principal       | Integra a todos los anteriores y los expone como un ecosistema unificado. |

---

## 🧠 Concepto clave: Encadenamiento de Servidores MCP

Cada servidor MCP (subordinado o principal):

* Tiene sus propios tools, resources, prompts y custom routes.

* Puede ejecutarse por sí solo o integrarse en otro servidor.

* Cuando se integra, sus componentes se fusionan dentro del servidor principal, lo que significa que el servidor principal podrá invocar herramientas y recursos definidos en los subordinados.

---

## ⚙️ Método mount()

El método central de la composición es:
```python
FastMCP.mount(server=other_server,prefix="other_server")
```

| Parámetro      | Tipo      | Descripción                                             |
| -------------- | --------- | ------------------------------------------------------- |
| `server` | `FastMCP` | Nombre del otro servidor FastMCP que se va a incluir. |
| `prefix` | `FastMCP` | Prefijo del otro servidor FastMCP que se va a incluir. |

---

Qué hace internamente

* Fusiona los tools, resources, prompts y rutas personalizadas del servidor incluido.

* Mantiene su espacio de nombres (namespace) para evitar colisiones de nombres.

* Puede montar múltiples servidores a la vez (cada uno con su propio contexto).

Para más detalle verificar el video: [Explicacion Composing Servers](https://www.youtube.com/watch?v=Gr7ANpbG8Mo) y el archivo: [08_composing_servers_mcp_fastmcp.py](https://github.com/BrayanR03/FastMCP-Learning-Journey/blob/main/CODE/08_composing_servers_mcp_fastmcp.py)


---

## 🧠 Beneficios clave
| Beneficio             | Descripción                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Modularidad total** | Cada servidor MCP se puede desarrollar, probar y desplegar por separado.                                    |
| **Reutilización**     | Puedes importar servidores MCP ya existentes sin duplicar código.                                           |
| **Escalabilidad**     | Estructura jerárquica que crece junto a tus necesidades.                                                    |
| **Mantenibilidad**    | Separar lógica de negocio (datasets, auth, archivos, etc.) en servidores aislados mejora la mantenibilidad. |
| **Seguridad**         | Puedes controlar qué servidores tienen acceso al principal o a qué recursos.                                |

---

## 🔒 Consideraciones de despliegue

* Solo el servidor principal necesita exponerse (por HTTP, por ejemplo).

* Los subservidores no requieren ejecución individual, debido que su contexto es absorbido.

* En entornos productivos (Docker o Kubernetes), el main server es el que se lanza como proceso principal (uvicorn main_server:app --host 0.0.0.0 --port 8000).

---

## 📘 En resumen
| Concepto        | Descripción                                                                 |
| --------------- | --------------------------------------------------------------------------- |
| **Composición** | Combinar múltiples servidores FastMCP en uno solo.                          |
| **mount()**   | Método para incluir servidores subordinados.                                |
| **Jerarquía**   | Permite crear niveles MCP (main → sub → sub-sub).                           |
| **Ventajas**    | Modularidad, escalabilidad, seguridad y reutilización.                      |
| **Uso típico**  | Integrar varios servidores especializados bajo un solo punto de acceso MCP. |
