# MÓDULO 12: DESPLIEGUE DE UN SERVIDOR MCP DE FASTMCP EN LA NUBE

## 📋 Descripción General

En este capítulo aprenderemos a **desplegar un servidor MCP de FastMCP en la nube** utilizando el servicio cloud AWS EC2.

El servidor MCP utilizado es el desarrollado previamente, y utilizaremos una arquitectura de despliegue profesional ideal para disponibilizar herramientas de IA de forma segura y escalable.

📁 **[Repositorio Servidor MCP - FastMCP](https://github.com/BrayanR03/Capitulo_11_FastMCP_ArquitecturaMCP)**

---

## 🌍 Introducción al Despliegue en la Nube de Servidores MCP

Antes de iniciar, es importante entender que el despliegue de un servidor MCP (Model Context Protocol) tiene particularidades respecto a una API REST tradicional. Mientras que una API REST suele responder a peticiones HTTP estandar, un servidor MCP puede funcionar sobre stdio (local) o SSE (Server-Sent Events) para conexiones remotas.

En esta guía configuraremos nuestro servidor MCP para funcionar en modo **HTTP**, permitiendo que clientes remotos (como Claude Desktop u otros agentes) se conecten a nuestras herramientas alojadas en AWS.

---

## 🏗️ Arquitectura: Servidor MCP en AWS EC2

Esta es la arquitectura recomendada para entornos profesionales que requieren persistencia y disponibilidad.

### 📌 Componentes

- **Servidor MCP**: Desplegado en una instancia AWS EC2 (máquina virtual en la nube)
- **Modo de Transporte**: HTTP (Hypert Text Transfer Protocol)

### 🐳 Herramientas Utilizadas

Utilizaremos la containerización para garantizar que el entorno de ejecución de Python y las dependencias de FastMCP sean idénticas a las de desarrollo:

- **Dockerfile**: Para construir la imagen del servidor MCP.
- **Docker**: Para ejecutar el contenedor en la instancia EC2.

---

## 🚀 FASE 2: DESPLIEGUE EN AWS EC2

### Introducción

En esta fase desplegaremos nuestro servidor MCP en una instancia de Amazon EC2. Usaremos Docker para aislar las dependencias y facilitar la ejecución del servidor.

### Prerrequisitos

- Cuenta activa en AWS
- Servidor MCP desarrollado con FastMCP y configurado para escuchar peticiones externas (bind 0.0.0.0)
- Dockerfile preparado en el repositorio

### PASO A) Acceder a AWS e iniciar sesión

Lo primero será ingresar al portal de AWS:
👉 https://aws.amazon.com/es/


▶️ Recomendación importante:
* Registra una **tarjeta de crédito o débito** para evitar problemas de verificación.
* Activa el **MFA (autenticación multifactor)** por seguridad.

---

### PASO B) Buscar el servicio Amazon EC2

Dentro de la consola de AWS, utiliza la barra de búsqueda (la lupa) e ingresa:
**“EC2”**

Selecciona el servicio y luego haz clic en:
👉 **Lanzar instancia**

Ver imagen referencial: [Buscar EC2 en AWS](https://github.com/BrayanR03/FastMCP-Learning-Journey/tree/main/ASSETS/Buscar_EC2.mp4)

---

### PASO C) Configurar la instancia EC2

En este paso configuraremos todos los parámetros necesarios para crear la máquina virtual.

#### i. Nombre y etiquetas

En Nombre, ingresa el identificador de la instancia:
* ➡️ **mcp-server-deployment**

#### ii. Selección del sistema operativo (AMI)

En el apartado **Imágenes de aplicaciones y sistemas operativos (AMI)**, selecciona:
* **➡️ Ubuntu Server**
(recomendado por compatibilidad y facilidad de uso con Docker)

#### iii. Crear un par de claves (Key Pair)

Como no tenemos un par de claves creado, seleccionaremos:
**👉 Crear un nuevo par de claves**

Luego completamos el formulario:
* **Nombre del par de claves:** *➡️ claves-mcp-server*
* **Tipo de par de claves:** *➡️ RSA*
* **Formato del archivo de clave privada:** *➡️ .pem*

Finalmente, presiona: **✔️ Crear par de claves**

#### iv. Configuración de red

Mantendremos todas las opciones predeterminadas de la VPC y activaremos:

☑️ **Permitir tráfico HTTP desde Internet**

☑️ **Permitir tráfico HTTPS desde Internet**

☑️ **Permitir tráfico SSH desde cualquier lugar (0.0.0.0/0)** (Para conectarnos y configurar)

#### v. Crear la instancia

Seleccionamos: **👉 Lanzar instancia**

Esperamos a que el estado cambie a: 🟢 **3/3 comprobaciones superadas** (o estado "Running").

---

### PASO D) Conexión a la instancia EC2

1. En el panel de EC2, selecciona la instancia previamente creada.
2. Haz clic en el botón **Conectar**.
3. Utilizaremos la opción **EC2 Instance Connect** (en el navegador).
4. Hacemos clic en **Connect**.

Se abrirá una terminal web. Deberías ver una interfaz similar a esta:
➡️ [INSERTE IMAGEN TERMINAL EC2]

---

### PASO E) Instalar dependencias para el entorno de despliegue

Actualizaremos el sistema e instalaremos Docker y Git.

#### 1. Actualizar paquetes del sistema
```bash
sudo apt update && sudo apt upgrade -y
```
#### 2. Instalar dependencias necesarias para Docker
```bash
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
Agregar el repositorio oficial de Docker:
```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```
Actualizar nuevamente:
```bash
sudo apt update && sudo apt upgrade -y
```
---

#### 3. Instalar Docker y componentes necesarios
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 4. Comprobar estado del servicio Docker
```bash 
sudo systemctl status docker
```

#### 5. Levantar Docker al iniciar la instancia
```bash
sudo systemctl start docker
```

#### 6. Verificar instalación
```bash
docker --version
```
---

#### 7. Instalar Git
```bash
sudo apt-get install git
```
#### 8. Verificar versión
```bash
git --version
```
#### 9. Clonar el repositorio
```bash
git clone https://github.com/BrayanR03/Capitulo_11_FastMCP_ArquitecturaMCP.git
```

#### 10. Verificar que el repositorio se descargó
```bash
ls -l
```

Deberás ver la carpeta:
📁 Capitulo_11_FastMCP_ArquitecturaMCP

---

### PASO F) Crear el archivo .env en la instancia

En buenas prácticas, nunca se debe subir el archivo `.env` a GitHub, porque contiene credenciales y datos sensibles del proyecto.

Sin embargo, necesitaremos ese archivo para poder ejecutar nuestra API correctamente, por ello, crearemos manualmente el archivo `.env` dentro de EC2 y les brindaré el contenido de ese archivo.

#### 1. Entrar a la carpeta del proyecto
```bash
cd Capitulo_11_FastMCP_ArquitecturaMCP
```
#### 2. Crear el archivo .env
```bash
nano .env
```

Se abrirá la pantalla del editor Nano, como se muestra en la imagen:
👉 [Archivo env Ubuntu](https://github.com/BrayanR03/FastMCP-Learning-Journey/tree/main/ASSETS/Archivo_ENV_Ubuntu.png)

#### 3. Agregar las variables de entorno

Copia y pega dentro del archivo:
```bash
## DETALLES SERVIDOR MCP - FASTMCP LEARNING JOURNEY

APP_NAME = "SERVIDOR MCP - FASTMCP LEARNING JOURNEY"
APP_ENV = "production"
API_PORT = 8000

## DETALLES API CLIENTES DESPLEGADA
API_CLIENTES_URL = "http://18.219.190.87/"
API_CLIENTES_URL_SPECIFICATION = "http://18.219.190.87/openapi.json"

## DETALLES API POKEMON DESPLEGADA
API_POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"
```

#### 4. Guardar y salir del archivo Nano

En teclado Windows:

1. **CTRL + O** → guardar

2. **ENTER** → confirmar

3. **CTRL + X** → salir

---

### PASO G) Creamos imagen, ejecutamos contenedor Docker y desplegamos la API
Creamos la imagen a partir del **Dockerfile**:
```bash
sudo docker build -t fastmcp_image_ec2 .
```
Levantamos el contenedor de la API:
```bash
sudo docker run -d --name project_server_mcp -p 80:8000 fastmcp_image_ec2
```

Espera unos minutos mientras Docker descarga imágenes y levanta la API.

Una vez terminado, tu API estará desplegada en AWS.
Puedes verificarlo con tu navegador usando:

http://<ip_publica_de_EC2>:80


Imagen de referencia:
👉 [Servidor MCP Desplegado](https://github.com/BrayanR03/FastMCP-Learning-Journey/tree/main/ASSETS/ServidorMCP_Despliegue.png)

### PASO H). Configuración para Clientes MCP

Vamos a definir la configuración del servidor MCP para los clientes MCP. Esta configuración
aplicará en cualquier cliente MCP (Claude Desktop, GitHub Copilot, entre otros).

#### Configuración Básica

En el archivo de configuración correspondiente a tu cliente MCP (por ejemplo, `config.json` 
para Claude Desktop o settings de VS Code para GitHub Copilot), agrega:
```json
"fastmcp-server": {
  "command": "npx",
  "args": [
    "-y",
    "mcp-remote",
    "http://<ip_publica_de_EC2>/mcp",
    "--allow-http"
  ]
}
```

**Nota importante:** Reemplaza `<ip_publica_de_EC2>` con la IP pública de tu instancia EC2.

#### Explicación del Flag `--allow-http`

El flag `--allow-http` es **obligatorio** cuando te conectas a servidores MCP mediante HTTP 
(no HTTPS) que no están en localhost. Por razones de seguridad, `mcp-remote` solo permite 
conexiones HTTP sin cifrar en las siguientes situaciones:

- **Sin flag:** Solo `localhost` o `127.0.0.1` (desarrollo local)
- **Con `--allow-http`:** Cualquier IP pública o dominio mediante HTTP

**¿Por qué existe esta restricción?**

Los servidores MCP en producción deberían usar HTTPS para:
- Cifrar la comunicación entre cliente y servidor
- Proteger credenciales y datos sensibles en tránsito
- Evitar ataques man-in-the-middle

Sin embargo, para entornos de desarrollo, pruebas o despliegues internos donde HTTPS no 
es crítico, el flag `--allow-http` permite conexiones HTTP sin cifrar.

Y listo, nuestro servidor MCP esta desplegado correctamente.