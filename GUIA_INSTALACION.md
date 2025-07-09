# Guía Detallada de Instalación y Uso del Servidor MCP para John Deere

## Índice
1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Preparación del Entorno](#preparación-del-entorno)
3. [Instalación del Servidor](#instalación-del-servidor)
4. [Configuración](#configuración)
5. [Uso del Servidor](#uso-del-servidor)
6. [Ejemplos Prácticos](#ejemplos-prácticos)
7. [Solución de Problemas](#solución-de-problemas)

## Requisitos del Sistema

### Requisitos Mínimos
- Sistema operativo: Windows 10/11, macOS 10.15+, o Linux
- Python 3.8 o superior
- 4GB de RAM mínimo
- 1GB de espacio en disco
- Conexión a Internet estable

### Requisitos de Software
- Git
- pip (gestor de paquetes de Python)
- Un editor de código (VS Code recomendado)
- Credenciales de John Deere API

## Preparación del Entorno

### 1. Instalar Python
1. Descargar Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marcar la opción "Add Python to PATH"
3. Verificar la instalación:
```bash
python --version
pip --version
```

### 2. Instalar Git
1. Descargar Git desde [git-scm.com](https://git-scm.com/downloads)
2. Instalar con opciones por defecto
3. Verificar la instalación:
```bash
git --version
```

### 3. Configurar VS Code (Opcional pero recomendado)
1. Descargar VS Code desde [code.visualstudio.com](https://code.visualstudio.com/)
2. Instalar las extensiones recomendadas:
   - Python
   - Python Extension Pack
   - GitLens

## Instalación del Servidor

### 1. Clonar el Repositorio
```bash
# Crear directorio para el proyecto
mkdir john-deere-mcp
cd john-deere-mcp

# Clonar el repositorio
git clone <repository-url> .
```

### 2. Crear Entorno Virtual
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

## Configuración

### 1. Configurar Credenciales
1. Crear archivo `.env` en el directorio raíz:
```bash
# En Windows:
echo JOHN_DEERE_CLIENT_ID=tu_client_id > .env
echo JOHN_DEERE_CLIENT_SECRET=tu_client_secret >> .env

# En macOS/Linux:
echo "JOHN_DEERE_CLIENT_ID=tu_client_id" > .env
echo "JOHN_DEERE_CLIENT_SECRET=tu_client_secret" >> .env
```

2. Reemplazar `tu_client_id` y `tu_client_secret` con tus credenciales de John Deere

### 2. Verificar Configuración
```bash
# Verificar que las variables de entorno están configuradas
python -c "import os; print('JOHN_DEERE_CLIENT_ID' in os.environ)"
```

## Uso del Servidor

### 1. Iniciar el Servidor
```bash
# Asegurarse de que el entorno virtual está activado
python john_deere_mcp_server_full.py
```

### 2. Verificar que el Servidor está Funcionando
1. Abrir un navegador web
2. Visitar `http://localhost:8000/docs`
3. Deberías ver la documentación de la API

### 3. Probar la Conexión
```python
# Crear archivo test_connection.py
import requests

response = requests.get('http://localhost:8000/health')
print(response.json())
```

## Ejemplos Prácticos

### 1. Consultar Estado de Maquinaria
```python
import requests

# Configurar headers
headers = {
    'Authorization': 'Bearer tu_token',
    'Content-Type': 'application/json'
}

# Realizar consulta
response = requests.get(
    'http://localhost:8000/machinery/8R410',
    headers=headers
)

print(response.json())
```

### 2. Crear Orden de Trabajo
```python
import requests

# Datos de la orden
data = {
    "field_id": "field123",
    "operation_type": "PLANTING",
    "start_date": "2024-03-20T08:00:00Z",
    "end_date": "2024-03-20T17:00:00Z"
}

# Crear orden
response = requests.post(
    'http://localhost:8000/work-orders',
    headers=headers,
    json=data
)

print(response.json())
```

### 3. Configurar Autoguiado
```python
import requests

# Parámetros de configuración
params = {
    "mode": "AUTO",
    "accuracy": "HIGH",
    "boundaryOffset": 0.5
}

# Configurar sistema
response = requests.put(
    'http://localhost:8000/guidance-systems/system123',
    headers=headers,
    json=params
)

print(response.json())
```

### 1. Consultar conexiones de Precision Tech
```python
import requests

response = requests.get('http://localhost:8000/connections', headers=headers)
print(response.json())
```

### 2. Consultar webhooks de la organización
```python
import requests

response = requests.get('http://localhost:8000/org-webhooks', headers=headers)
print(response.json())
```

### 3. Obtener datos ISO 15143-3 de una máquina
```python
import requests

response = requests.get('http://localhost:8000/iso15143-3?org_id=org123&machine_id=machine123', headers=headers)
print(response.json())
```

## Conexión con LLMs

### 1. Configuración del Cliente LLM

#### 1.1 Conexión con ChatGPT/Claude
```python
# config_llm.py
from mcp.client import MCPClient
import openai  # o anthropic para Claude

# Configurar credenciales
openai.api_key = "tu_api_key"  # o anthropic.api_key para Claude

# Crear cliente MCP
mcp_client = MCPClient(
    server_url="http://localhost:8000",
    llm_provider="openai",  # o "anthropic" para Claude
    model="gpt-4"  # o "claude-3-opus" para Claude
)

# Ejemplo de uso
async def consultar_maquinaria():
    response = await mcp_client.process_query(
        "¿Cuál es el estado actual del tractor 8R410?"
    )
    return response
```

#### 1.2 Conexión con Ollama (LLM Local)
```python
# config_ollama.py
from mcp.client import MCPClient
import requests

# Configurar cliente Ollama
OLLAMA_BASE_URL = "http://localhost:11434"

# Crear cliente MCP
mcp_client = MCPClient(
    server_url="http://localhost:8000",
    llm_provider="ollama",
    model="llama2"  # o cualquier otro modelo instalado
)

# Verificar modelo disponible
def verificar_modelo():
    response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
    return response.json()
```

#### 1.3 Conexión con LLMStudio
```python
# config_llmstudio.py
from mcp.client import MCPClient
import requests

# Configurar cliente LLMStudio
LLMSTUDIO_URL = "http://localhost:8001"

# Crear cliente MCP
mcp_client = MCPClient(
    server_url="http://localhost:8000",
    llm_provider="llmstudio",
    model="tu_modelo_personalizado"
)
```

### 2. Ejemplos de Integración

#### 2.1 Ejemplo con ChatGPT
```python
# ejemplo_chatgpt.py
import asyncio
from config_llm import mcp_client

async def main():
    # Consulta sobre maquinaria
    maquinaria = await mcp_client.process_query(
        "¿Cuál es el estado de la flota de tractores?"
    )
    print("Estado de maquinaria:", maquinaria)

    # Crear orden de trabajo
    orden = await mcp_client.process_query(
        "Necesito crear una orden de trabajo para siembra en el campo A123"
    )
    print("Orden creada:", orden)

    # Configurar autoguiado
    autoguiado = await mcp_client.process_query(
        "Configura el autoguiado del tractor 8R410 para máxima precisión"
    )
    print("Configuración de autoguiado:", autoguiado)

if __name__ == "__main__":
    asyncio.run(main())
```

#### 2.2 Ejemplo con Ollama
```python
# ejemplo_ollama.py
import asyncio
from config_ollama import mcp_client

async def main():
    # Consulta sobre rendimiento
    rendimiento = await mcp_client.process_query(
        "Analiza el rendimiento del campo B456 del último año"
    )
    print("Análisis de rendimiento:", rendimiento)

    # Planificar operación
    planificacion = await mcp_client.process_query(
        "Planifica la operación de siembra para la próxima semana"
    )
    print("Planificación:", planificacion)

if __name__ == "__main__":
    asyncio.run(main())
```

### 3. Configuración Avanzada

#### 3.1 Personalización de Prompts
```python
# prompts_personalizados.py
from mcp.client import MCPClient, PromptTemplate

# Crear templates personalizados
maquinaria_template = PromptTemplate(
    template="Analiza el estado de la maquinaria {maquinaria_id} y proporciona recomendaciones",
    input_variables=["maquinaria_id"]
)

operacion_template = PromptTemplate(
    template="Planifica la operación {tipo_operacion} para el campo {campo_id}",
    input_variables=["tipo_operacion", "campo_id"]
)

# Configurar cliente con templates
mcp_client = MCPClient(
    server_url="http://localhost:8000",
    llm_provider="openai",
    model="gpt-4",
    prompt_templates={
        "maquinaria": maquinaria_template,
        "operacion": operacion_template
    }
)
```

#### 3.2 Manejo de Contexto
```python
# manejo_contexto.py
from mcp.client import MCPClient, ContextManager

# Crear gestor de contexto
context_manager = ContextManager(
    max_tokens=4000,
    temperature=0.7,
    top_p=0.9
)

# Configurar cliente con gestor de contexto
mcp_client = MCPClient(
    server_url="http://localhost:8000",
    llm_provider="openai",
    model="gpt-4",
    context_manager=context_manager
)

# Ejemplo de uso con contexto
async def consulta_con_contexto():
    # Agregar contexto
    context_manager.add_context("campo_id", "A123")
    context_manager.add_context("operacion_actual", "siembra")
    
    # Realizar consulta
    response = await mcp_client.process_query(
        "¿Cuál es el estado óptimo para la operación actual?"
    )
    return response
```

### 4. Solución de Problemas Comunes

#### 4.1 Problemas de Conexión
```python
# solucion_problemas.py
from mcp.client import MCPClient
import asyncio
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)

async def verificar_conexion():
    try:
        mcp_client = MCPClient(
            server_url="http://localhost:8000",
            llm_provider="openai",
            model="gpt-4"
        )
        
        # Verificar conexión con MCP
        await mcp_client.health_check()
        
        # Verificar conexión con LLM
        await mcp_client.llm_health_check()
        
        return "Conexión exitosa"
    except Exception as e:
        logging.error(f"Error de conexión: {str(e)}")
        return f"Error: {str(e)}"
```

#### 4.2 Manejo de Errores
```python
# manejo_errores.py
from mcp.client import MCPClient, MCPError
import asyncio

async def consulta_segura():
    try:
        mcp_client = MCPClient(
            server_url="http://localhost:8000",
            llm_provider="openai",
            model="gpt-4"
        )
        
        response = await mcp_client.process_query(
            "Consulta compleja que podría fallar"
        )
        return response
    except MCPError as e:
        if e.code == "AUTH_ERROR":
            return "Error de autenticación"
        elif e.code == "RATE_LIMIT":
            return "Límite de consultas excedido"
        else:
            return f"Error desconocido: {str(e)}"
```

### 5. Monitoreo y Logging

#### 5.1 Configuración de Logging
```python
# config_logging.py
import logging
from mcp.client import MCPClient

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('mcp_client.log'),
        logging.StreamHandler()
    ]
)

# Crear cliente con logging
mcp_client = MCPClient(
    server_url="http://localhost:8000",
    llm_provider="openai",
    model="gpt-4",
    enable_logging=True
)
```

#### 5.2 Monitoreo de Rendimiento
```python
# monitoreo.py
from mcp.client import MCPClient
import time
import asyncio

async def monitorear_rendimiento():
    mcp_client = MCPClient(
        server_url="http://localhost:8000",
        llm_provider="openai",
        model="gpt-4"
    )
    
    start_time = time.time()
    response = await mcp_client.process_query("Consulta de prueba")
    end_time = time.time()
    
    print(f"Tiempo de respuesta: {end_time - start_time} segundos")
    print(f"Tokens utilizados: {response.usage.total_tokens}")
    return response
```

## Solución de Problemas

### 1. Errores Comunes

#### Error de Autenticación
```bash
# Verificar credenciales
echo $JOHN_DEERE_CLIENT_ID
echo $JOHN_DEERE_CLIENT_SECRET
```

#### Error de Puerto en Uso
```bash
# Encontrar proceso usando el puerto 8000
# En Windows:
netstat -ano | findstr :8000
# En macOS/Linux:
lsof -i :8000
```

#### Error de Dependencias
```bash
# Reinstalar dependencias
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### 2. Logs y Depuración
1. Verificar logs del servidor:
```bash
# En Windows:
type john_deere_mcp_server.log
# En macOS/Linux:
cat john_deere_mcp_server.log
```

2. Activar modo debug:
```bash
export LOG_LEVEL=DEBUG
python john_deere_mcp_server.py
```

### 3. Contacto y Soporte
- Crear un issue en el repositorio
- Contactar al equipo de soporte
- Consultar la documentación oficial de John Deere

## Mantenimiento

### 1. Actualizaciones
```bash
# Actualizar dependencias
pip install --upgrade -r requirements.txt

# Actualizar código
git pull origin main
```

### 2. Backup
```bash
# Crear backup de la configuración
cp .env .env.backup
```

### 3. Monitoreo
- Revisar logs regularmente
- Monitorear uso de recursos
- Verificar estado de la API

---

*Esta guía fue actualizada por última vez el 20 de marzo de 2024* 

## Instalación y Uso Simplificado

Ejecuta simplemente:
```bash
python main.py
```

Esto realizará automáticamente:
- Verificación de versión de Python
- Creación y activación del entorno virtual (si es necesario)
- Instalación de dependencias
- Solicitud de credenciales y configuración automática del archivo .env (si es necesario)
- Flujo de autenticación OAuth2 para obtener el refresh token (si es necesario)
- Lanzamiento del servidor MCP

El servidor MCP quedará corriendo y listo para recibir consultas desde LLMs compatibles (Claude, ChatGPT, etc.).

---

### ¿Por qué ocurre el error?
El error ocurre porque `FastMCP` no es una aplicación ASGI compatible directamente con Uvicorn.  
**FastMCP debe exponer internamente una instancia ASGI (como FastAPI) para que Uvicorn pueda ejecutarla.**

---

## Solución práctica

### 1. **Verifica si FastMCP expone una app ASGI**
Busca en la documentación o en el código de `FastMCP` si tiene una propiedad como `asgi_app`, `app`, o un método para obtener la aplicación ASGI.

Por ejemplo:
```python
app = mcp.app  # o mcp.asgi_app
```
Luego, en el arranque:
```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("john_deere_mcp_server_full:app", host="0.0.0.0", port=8000, reload=False)
```

### 2. **Si no existe esa propiedad**
- Es posible que debas crear una instancia de FastAPI y registrar las herramientas de FastMCP sobre ella.
- O bien, el propio `FastMCP` tiene un método para lanzar el servidor (por ejemplo, `mcp.run()`), y debes ejecutarlo directamente, **sin usar Uvicorn**.

### 3. **¿Qué hacer ahora?**
- Si tienes acceso al código de `FastMCP`, dime si ves algo como `self.app = FastAPI()` o `def asgi_app(self): ...`.
- Si la documentación de `FastMCP` dice que debes usar `mcp.run()`, simplemente ejecuta:
  ```bash
  python john_deere_mcp_server_full.py
  ```
  y no uses Uvicorn directamente.

---

## Resumen

- **No uses Uvicorn directamente** si FastMCP ya lanza el servidor.
- Si necesitas exponer la app para Uvicorn, busca la propiedad `app` o `asgi_app` en FastMCP.
- El objetivo es que el servidor quede corriendo y el LLM pueda consultarlo vía HTTP.

---

¿Quieres que revise el código de `FastMCP` en tu proyecto para encontrar la forma correcta de exponer la app y dejar el servidor corriendo? ¿O prefieres que adapte el arranque para que solo uses `mcp.run()` y el LLM pueda consultarlo?  
¡Dímelo y lo hago automáticamente! 

---

## ¿Cómo conectar Claude Desktop (o cualquier LLM compatible) a tu MCP?

### 1. **Asegúrate de que el servidor MCP esté corriendo**
Ya lo tienes:  
```bash
python main.py
```
El servidor queda escuchando en `http://localhost:8000` (o la IP/puerto que configures).

---

### 2. **Configura tu cliente LLM para apuntar al MCP**

#### **Con un cliente MCP en Python (ejemplo para Claude/OpenAI):**
```python
from mcp.client import MCPClient

mcp_client = MCPClient(
    server_url="http://localhost:8000",  # O la IP de tu servidor si es remoto
    llm_provider="anthropic",            # "anthropic" para Claude, "openai" para ChatGPT, etc.
    model="claude-3-opus"                # O el modelo que prefieras
)

# Ejemplo de consulta
async def consulta():
    respuesta = await mcp_client.process_query("¿Cuál es el estado de la maquinaria?")
    print(respuesta)
```

---

### 3. **Para Claude Desktop (o cualquier LLM con integración MCP):**

- **Busca en la configuración de Claude Desktop** (o el LLM que uses) la opción para agregar un “servidor MCP” o “plugin externo”.
- **Agrega la URL de tu MCP:**  
  - Si es en la misma máquina: `http://localhost:8000`
  - Si es en otra máquina: `http://IP_DEL_SERVIDOR:8000`
- **Guarda y prueba una consulta** en lenguaje natural, por ejemplo:  
  - “¿Cuál es el estado de la maquinaria?”
  - “Listar operaciones recientes”

---

### 4. **Notas importantes**
- Si usas Claude Desktop en otra máquina, asegúrate de que el puerto 8000 esté abierto en el firewall.
- Si tu LLM requiere autenticación adicional, revisa la documentación de tu cliente MCP.
- Puedes consultar y modificar los endpoints y herramientas MCP en `john_deere_mcp_server_full.py`.

---

## Resumen de pasos para Claude Desktop

1. Ejecuta el MCP:  
   ```bash
   python main.py
   ```
2. En Claude Desktop, configura el plugin o integración MCP apuntando a `http://localhost:8000`.
3. Realiza consultas desde Claude Desktop y el MCP responderá usando los endpoints de John Deere.

---

¿Quieres un ejemplo de flujo de integración paso a paso para Claude Desktop, o necesitas ayuda con la configuración específica de algún cliente? 

---

### ¿Qué hace esta configuración?
- Indica a Claude (o el cliente MCP) que, cuando necesite usar el servidor MCP de John Deere, debe ejecutar:
  ```bash
  python C:/Users/QuBit/Desktop/projects/john_deere_mcp_server_full.py
  ```
- Esto lanzará el servidor MCP en tu máquina, listo para recibir consultas desde Claude.

---

## Recomendaciones adicionales

1. **Asegúrate de que las variables de entorno y el archivo `.env` estén configurados** en la misma carpeta donde está el script.
2. **El entorno virtual debe estar activado** o el Python usado debe tener todas las dependencias instaladas.
3. Si tienes problemas de permisos, puedes probar con rutas relativas o asegurarte de que el usuario tenga acceso a esa carpeta.
4. Si el servidor ya está corriendo, Claude puede conectarse directamente a `http://localhost:8000` sin relanzar el proceso.

---

## ¿Cómo probar la integración?
- Lanza Claude Desktop.
- Realiza una consulta que requiera el uso del servidor MCP (por ejemplo, “¿Cuál es el estado de la maquinaria?”).
- El cliente debería lanzar el script, conectar y mostrar la respuesta.

---

¿Quieres una guía paso a paso para probar la integración desde Claude Desktop, o necesitas ayuda para depurar si algo no responde? 