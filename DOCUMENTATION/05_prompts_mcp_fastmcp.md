## MÓDULO 05: 🧠 Prompts en MCP (Model Context Protocol)

### 📘 Introducción

Dentro del ecosistema MCP (Model Context Protocol), los Prompts representan el tercer componente esencial junto a los Recursos (Resources) y las Herramientas (Tools). Mientras los recursos exponen información y las herramientas permiten operar sobre ella, los Prompts actúan como plantillas inteligentes de contexto que guían al modelo (LLM) para ejecutar tareas específicas de forma más estructurada, rápida y reutilizable.

---

### ⚙️ ¿Qué son los Prompts?

Un Prompt en MCP, especialmente en el caso de FastMCP, es una plantilla predefinida que se guarda dentro del servidor MCP.
Cada prompt puede contener:

* Un texto base estructurado, que define el contexto o la instrucción principal.

* Parámetros personalizables, que el usuario puede completar según la tarea.

* Relaciones con herramientas o recursos, para que el modelo sepa qué usar y cómo usarlo.

En resumen, un prompt en MCP no solo define qué se le pide al modelo, sino cómo debe hacerlo y con qué recursos o herramientas debe trabajar.

---

### 💡 Ejemplo conceptual

Supongamos que el servidor MCP tiene un prompt llamado AnalizarDatos.

Este prompt podría tener una estructura base como:
```css
Analiza los siguientes datos usando las herramientas estadísticas disponibles.
Asegúrate de generar un resumen claro y un gráfico visual si es posible.

Datos:
{{dataset}}
```
Al llamarlo desde el cliente MCP, el usuario solo tendría que pasar el parámetro dataset, sin necesidad de escribir todo el texto cada vez. Ver el siguiente: [Demostración Prompts](https://youtu.be/DoZXPrgblyE) y [05_prompts_mcp_fastmcp.py](https://github.com/BrayanR03/FastMCP-Learning-Journey/blob/main/CODE/05_prompts_mcp_fastmcp.py)
)

---
### 🔁 Ventajas de los Prompts en MCP

1. Reutilización
Permiten definir instrucciones complejas una sola vez y utilizarlas repetidamente con distintos parámetros.

2. Estandarización
Garantizan que las tareas ejecutadas por el LLM sigan un formato, estilo o proceso coherente.

3. Contexto estructurado
El modelo recibe un contexto predefinido, mejorando la precisión y relevancia de las respuestas.

4. Integración fluida
Los prompts pueden estar vinculados a recursos (por ejemplo, un archivo CSV o una API) y a herramientas (por ejemplo, una función de análisis o visualización).

---

### 🔺 Relación entre los 3 Componentes Principales de MCP

| Componente               | Función Principal                                                                  | Ejemplo                                    |
| ------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------ |
| **Resources (Recursos)** | Exponen información o datos desde archivos, APIs, BD, etc.                         | `dataset.csv`, `API externa`, `JSON local` |
| **Tools (Herramientas)** | Permiten ejecutar acciones o transformaciones sobre los recursos.                  | `analyze_data()`, `generate_plot()`        |
| **Prompts**              | Definen el contexto y la lógica de cómo se deben usar los recursos y herramientas. | `AnalizarDatos`, `GenerarInforme`          |

En conjunto, los tres conforman un ecosistema integrado donde:

* Los Recursos alimentan de datos.

* Las Herramientas ejecutan acciones.

* Los Prompts guían al modelo y conectan ambos elementos.

### 🧩 Conclusión

Los Prompts en MCP representan la capa de inteligencia contextual dentro del protocolo.
Permiten definir instrucciones personalizadas, reutilizables y dirigidas, que facilitan el trabajo entre cliente y servidor MCP.

Gracias a ellos, el usuario no necesita escribir instrucciones largas ni detallar cada vez qué herramientas o recursos utilizar.
Simplemente invoca un prompt predefinido, introduce los parámetros necesarios, y el sistema se encarga del resto, garantizando precisión, coherencia y eficiencia en cada ejecución.
