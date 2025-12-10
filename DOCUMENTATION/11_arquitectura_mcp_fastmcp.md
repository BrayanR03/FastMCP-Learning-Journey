# MÓDULO 11: ARQUITECTURA EN FASTMCP

En este capítulo presentaré **mi propuesta de arquitectura para proyectos MCP (Model Context Protocol)** desarrollados con el framework **FastMCP**.
Aclaro que esta es la **Versión 1** de mi arquitectura, diseñada desde mi experiencia y necesidades actuales, y que seguirá evolucionando a medida que aborde proyectos más complejos y se vayan incorporando buenas prácticas adicionales.

## 12.1. Propósito de esta arquitectura

La mayoría de tutoriales, videos y repositorios sobre MCP en FastMCP muestran ejemplos funcionales, pero no una forma clara y escalable de:

* Separar responsabilidades.

* Organizar tools, resources, prompts y custom routes.

* Manejar credenciales y configuraciones.

* Integrar datasets, assets o dependencias internas.

* Preparar el proyecto para crecimiento real (composing servers, proxys, APIs externas, etc.).

Por ello decidí construir **mi propia arquitectura orientada a buenas prácticas**, fácil de mantener y preparada para futuras extensiones.

---

## 12.2. Alcance de esta arquitectura

Esta arquitectura se enfoca en:

✔️ Servidores MCP basados en FastMCP

Es decir, cómo crear, organizar y escalar un servidor MCP limpio.

❌ No cubre aún:

* Clientes MCP (Claude, ChatGPT, Copilot, etc.).

* Proxys, orquestadores o servidores MCP compuestos.

Estos sí podrán integrarse más adelante, pero no son parte del núcleo de un servidor MCP base.

---

## 12.3. Estructura general del proyecto

La estructura base del proyecto es:
```css
mcp-project/
│
└── app/
    ├── assets/
    ├── core/
    ├── server_mcp/
    │   ├── tools/
    │   ├── prompts/
    │   ├── resource/
    │   └── custom_routes/
    │   └── server.py
    │
    ├── main.py
    |── uv.lock
    ├── pyproject.toml         
    ├── Dockerfile
    ├── docker-compose.yml
    └── README.md
```
---

## 12.4. Descripción de cada carpeta
### 1) mcp-project/

Carpeta raíz donde vive toda la solución MCP.

### 2) app/

Esta es la carpeta principal del proyecto, equivalente a la “aplicación” en arquitecturas backend tradicionales.
Aquí vive todo lo necesario para iniciar y ejecutar el servidor MCP.

### 3) /app/assets/

Contiene datos o archivos utilizados internamente por el servidor MCP:

* Datasets de ejemplo

* Plantillas Excel/CSV

* Documentos de referencia

* Archivos procesados por tools o resources

Ejemplo:
```css
assets/
├── dataset_1996.xlsx
└── dataset_1997.xlsx
```

### 4) /app/core/ 

Aquí colocarás todo lo que NO pertenece directamente a MCP, pero que MCP necesita:

* Configuración del proyecto

* Variables de entorno

* Conexiones a bases de datos

* Inicializadores

* Clases compartidas

* Utilidades globales

Propuesta:
```css
core/
├── config.py
├── settings.py
├── security.py
└── __init__.py
```

### 5) /app/server_mcp/

Es el corazón del servidor MCP.
Dentro se organizan todos los componentes que MCP ofrece:
```css
server_mcp/
├── tools/
├── prompts/
├── custom_routes/
└── resource/
```
---

## 12.5. Componentes MCP dentro de server_mcp/
### A) /tools/

Contiene las herramientas (Tools) organizadas por contexto.
Ejemplo real de tu proyecto:
```css
tools/
├── base_datos_tools.py
└── data_analyst_tools.py
```
Cada archivo representa un dominio.
Esto respeta el principio: SRP (Single Responsibility Principle).

### B) /prompts/

Prompts estructurados por rol, área o comportamiento:
```css
prompts/
└── data_analyst_prompts.py
```
### C) /resource/

Aquí van recursos estáticos o dinámicos que MCP puede exponer:
```css
resource/
└── data_analyst_resource.py
```

### D) /custom_routes/

Rutas personalizadas que no encajan en Tools o Resources:
```css
custom_routes/
└── data_analyst_custom_routes.py
```

### E) server.py

Archivo que permite crear el contexto del servidor MCP 
principal y secundarios (según los requerimientos):
```css
app/
└── server.py
```
---

## 12.6. Archivo principal main.py

Aquí se inicializa el servidor MCP:

* se importan tools, resources, prompts

* se monta el servidor

* se registran componentes

* se arranca FastMCP

Y sirve como entrypoint oficial del proyecto.

---

## 12.7. Archivos raíz útiles

En la raíz de app/ puedes añadir:

* `README.md` → Documentación del proyecto

* `pyproject.toml` → Dependencias

* `Dockerfile` → Contenedor

* `docker-compose.yml` (opcional, útil en múltiples contenedores)

* `.env` → Variables de entorno (Configuración sensible)

Esto facilita despliegues en cloud.

---

## ✅ 12.8. Arquitectura Visual Final

Aquí tienes tu arquitectura final, visual, limpia y documentada:
```css
mcp-project/
│
└── app/
    │
    ├── assets/                    # Archivos utilizados por el servidor MCP
    │   ├── dataset_1996.xlsx
    │   └── dataset_1997.xlsx
    │
    ├── core/                      # Configuración, conexiones
    │   ├── config.py
    │   ├── settings.py
    │   ├── security.py
    │   └── __init__.py
    │
    ├── server_mcp/                # Núcleo del servidor MCP
    │   │
    │   ├── tools/                 # Tools por dominio (SRP)
    │   │   ├── base_datos_tools.py
    │   │   └── data_analyst_tools.py
    │   │
    │   ├── prompts/               # Prompts organizados por contexto
    │   │   └── data_analyst_prompts.py
    │   │
    │   ├── resource/              # Resources del servidor MCP
    │   │   └── data_analyst_resource.py
    │   │
    │   └── custom_routes/         # Rutas personalizadas
    │       └── data_analyst_custom_routes.py
    │
    ├── main.py                    # Entry point
    ├── Dockerfile                   # Configuración de imagen Docker
    ├── docker-compose.yml           # Orquestación de contenedores
    ├── main.py                      # Punto de entrada de la aplicación
    ├── pyproject.toml               # Dependencias del proyecto
    ├── .env # variables de entorno
    |── uv.lock                      # Archivo de bloqueo de dependencias
    └── README.md
```

---

## ✅ 12.9. Módulo adicionales en la arquitectura de FastMCP

Además del núcleo `server_mcp/`, existen componentes avanzados que pueden incorporarse de manera gradual. 
Estos módulos **NO TIENEN** que existir desde el inicio, pero sí deben tener un lugar claro en la arquitectura para cuando el proyecto crezca.

### a). Composing Servers (`/mcp_composing`):
Es un servidor MCP que orquesta otros servidores MCP, permitiendo combinar tools, resources, prompts y custom routes de varios servidores, delegando operaciones para crear flujos complejos entre servidores secundarios.

```css
app/
└── mcp_composing/
    ├── server_secundario_1.py
    └── server_secundario_2.py
```

### b). Integration Frameworks (`/integration_frameworks`):
Son módulos adicionales que actúan como capas adaptadoras entre MCP y otras tecnologías, tales como: FastAPI, Flask, LangChain, entre otros. 
```css
app/
└── integration_frameworks/
    ├── fastapi_adapter.py
    ├── langchain_adapter.py
    └── flask_operator.py
```
### c). Server Proxys (`/mcp_proxys`):
El proxy MCP se vuelve una pieza fundamental si quieres escalar profesionalmente arquitecturas en FastMCP para
poder enrutar el tráfico entre varios servidores MCP.
```css
app/
└── mcp_proxy/
    └── proxy_server.py
```

### d). Integración con APIs externas (`/services_apis`)
Permiten que APIs externas se conviertan en servidores
MCP segmentando sus endpoints en los componentes de un
servidor MCP: tools, resources, prompts, etc.
```css
app/
└── services_apis/
    ├── api_fastapi_mcp.py
    ├── api_node_mcp.py
    └── api_springboot_mcp.py
```
---

## ✍️ En resumen:
Este módulo define una arquitectura clara y ordenada para servidores MCP con FastMCP, donde establece una estructura modular que separa responsabilidades, facilita el mantenimiento y deja preparado el proyecto para crecer con herramientas, resources, prompts, rutas personalizadas y futuros componentes avanzados. En esencia, este módulo sienta las bases para construir servidores MCP escalables y bien organizados desde el inicio.

Además, el uso de `uv` como gestor de paquetes aporta una ventaja clave: genera automáticamente una base de archivos bien estructurada —como `uv.lock`, `pyproject.toml`, `.python-version`, `.gitignore`, `README.md` y `main.py`— que sirve como punto de partida limpio y ordenado para construir una arquitectura escalable. Gracias a esta base inicial, el proyecto puede crecer sin fricción, manteniendo coherencia, control de dependencias y buenas prácticas desde el primer comando.

Para revisar la plantilla sobre la arquitectura MCP en FastMCP pueden revisar el siguiente repositorio : 📁 [Arquitectura MCP](https://github.com/BrayanR03/Capitulo_11_FastMCP_ArquitecturaMCP).