# 🧩 MÓDULO 3: Tools en MCP (Model Context Protocol)

## 1️⃣ ¿Qué es una Tool en MCP?

En el ecosistema de Model Context Protocol (MCP), una Tool es una función o acción especializada que un MCP Server expone hacia un cliente MCP (como Claude, GitHub Copilot o cualquier otro LLM compatible) con el objetivo de extender las capacidades nativas del modelo de lenguaje.

Las Tools actúan como puntos de entrada funcionales que permiten al LLM ejecutar operaciones que, de forma directa, no podría realizar por sí mismo, como:

* Consultar una base de datos local o remota.

* Consumir APIs externas.

* Manipular archivos o datos del sistema.

* Ejecutar transformaciones, cálculos o tareas de negocio específicas.

En síntesis, las Tools son la interfaz de comunicación funcional entre el LLM y el entorno del servidor MCP, haciendo posible la ejecución de acciones reales en respuesta a instrucciones en lenguaje natural del usuario.

## 2️⃣ Relación entre el LLM, el Cliente MCP y las Tools

Cuando un usuario formula una solicitud en lenguaje natural (por ejemplo: “Calcula el promedio de ventas del último mes”), el cliente MCP analiza la instrucción, infiriendo qué Tool disponible en el servidor MCP es la más adecuada para resolverla.

Esta inferencia se basa principalmente en:

* El name y la description de cada Tool (que le dan contexto semántico).

* Los tags, que agrupan herramientas similares por dominio funcional.

* Los schemas de entrada y salida (Input Schema y Output Schema), que indican qué parámetros espera y qué datos produce la Tool.

Así, el LLM traduce la intención del usuario en una llamada estructurada hacia la Tool correspondiente, construyendo una petición (generalmente en formato JSON) que se envía al MCP Server mediante el canal de transporte (HTTP, SSE o STDIO).

---

## 3️⃣ Definición de una Tool

En FastMCP, las Tools se definen mediante un decorador sobre una función asíncrona:
```python
@mcp_server.tool(
    name="sumar_dos_numeros",
    description="Suma dos números y retorna el resultado",
    tags={"aritmetica"},
    meta={"author": "Brayan R.", "version": "1.0.0"}
)
async def sumar(a: int, b: int) -> float:
    return a + b
```
Cada Tool queda registrada en el servidor MCP, y automáticamente se genera:

* Un Input Schema, derivado de los parámetros de entrada (a, b).

* Un Output Schema, basado en el tipo de retorno (float).

Esto le permite al cliente MCP conocer exactamente qué espera la Tool y qué devuelve, garantizando compatibilidad e interoperabilidad.

---

## 4️⃣ Parámetros Clave de una Tool

| Parámetro                            | Descripción                                                                         | Importancia                                                                |
| ------------------------------------ | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **name**                             | Identificador único de la Tool. No debe contener espacios ni caracteres especiales. | Permite al LLM reconocer la Tool.                                          |
| **description**                      | Explicación breve y clara del propósito de la Tool.                                 | Sirve como contexto semántico para el LLM al inferir qué herramienta usar. |
| **tags**                             | Conjunto de etiquetas o categorías funcionales.                                     | Agrupa Tools relacionadas, facilitando filtrado o priorización.            |
| **meta**                             | Diccionario de metadatos: autor, versión, dependencias, etc.                        | Permite versionado y trazabilidad del desarrollo de Tools.                 |
| **input_schema** / **output_schema** | Estructuras JSON generadas automáticamente a partir de los type hints.              | Determinan la comunicación entre el LLM y la Tool.                         |

---

## 5️⃣ Input Schema y Output Schema

El Input Schema se genera automáticamente a partir de los parámetros de la función y sus anotaciones de tipo.
Por ejemplo:

```python
async def multiplicar(a: int, b: int) -> int:
```
genera un esquema de entrada equivalente a:
```json
{
  "type": "object",
  "properties": {
    "a": {"type": "integer"},
    "b": {"type": "integer"}
  },
  "required": ["a", "b"]
}
```
El Output Schema se genera a partir del tipo de retorno (-> int), permitiendo al cliente MCP saber qué estructura esperar como respuesta.

Además, FastMCP permite enriquecer los campos con validaciones descriptivas, utilizando Annotated y Field:
```python
async def dividir(
    a: Annotated[int, Field(description="Dividendo, mayor que cero")],
    b: Annotated[int, Field(description="Divisor, no puede ser cero")]
) -> float:
```
Esto refuerza la comunicación entre el servidor y el cliente, mejorando la robustez de las Tools y el feedback hacia el usuario.

---

## 6️⃣ Tags y Metadatos (Meta)

Los tags y meta son campos opcionales pero altamente recomendados:

* Tags: ayudan a clasificar Tools por dominio (por ejemplo: {"aritmetica"}, {"database"}, {"api"}), lo que facilita la organización y la inferencia contextual por parte del cliente MCP.

* Meta: puede incluir información como:

    * version: control de versiones.

    * author: responsable o creador de la Tool.

    * dependencies: librerías o recursos externos requeridos.

Estos campos son muy útiles en entornos colaborativos o de despliegue, donde múltiples Tools evolucionan con el tiempo.

---

## 7️⃣ Tools Derivadas o Extensibles

En MCP, también se pueden crear Tools derivadas, que extienden o especializan la funcionalidad de una Tool base.
Esto se asemeja conceptualmente a la herencia o sobrecarga de funciones en programación orientada a objetos.

Ejemplo:
```python
@mcp_server.tool()
async def sumar(a: int, b: int) -> float:
    """Tool base: suma dos números."""
    return a + b

@mcp_server.tool()
async def sumar_redondeado(a: int, b: int) -> int:
    """Tool derivada: suma dos números y redondea el resultado."""
    resultado = await sumar(a, b)
    return round(resultado)
```
De esta manera, ambas Tools conviven en el mismo MCP Server, pero con propósitos distintos y reutilizando lógica base.

Para mas detalle revisar: 📽️[Ejecucion_ServidorMCP-Tool](https://youtu.be/O_45ipV94Mw) y el archivo [03_tools_mcp_fastmcp.py](https://github.com/BrayanR03/FastMCP-Learning-Journey/blob/main/CODE/03_tools_mcp_fastmcp.py)

---

## 8️⃣ Buenas Prácticas al Definir Tools

1. Usar nombres descriptivos y consistentes (sumar_dos_numeros, no sumar1).

2. Evitar caracteres especiales o acentos en name.

3. Describir claramente la intención de la Tool en description.

4. Agrupar Tools relacionadas con tags.

5. Versionar Tools con meta["version"].

6. Utilizar Annotated y Field para campos más claros y validados.

7. Evitar lógica compleja dentro de una Tool: mejor delegar a módulos internos.

8. Separar responsabilidades: mantener las Tools en archivos o módulos específicos dentro de la arquitectura MCP (por ejemplo, tools/database.py, tools/api.py, tools/utils.py).

## 9️⃣ Conclusión

Las Tools en MCP representan el núcleo funcional que conecta la inteligencia de los modelos de lenguaje con la acción concreta en el mundo real.
A través de FastMCP, su definición se vuelve limpia, tipada, validada y extensible, logrando una arquitectura modular que:

* Escala fácilmente con nuevas capacidades.

* Facilita el mantenimiento.

* Permite al LLM trabajar de manera más precisa, segura y contextual.

En esencia, las Tools son la extensión programable del razonamiento de un LLM, el puente entre el pensamiento y la acción.