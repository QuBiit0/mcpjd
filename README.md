# Servidor MCP para John Deere API

Este servidor MCP (Model Context Protocol) permite la integración de cualquier LLM con las APIs de John Deere, facilitando la interacción en lenguaje natural con los servicios de John Deere.

## Requisitos Previos

- Python 3.8 o superior
- Credenciales de John Deere API (Client ID y Client Secret)
- Acceso a las APIs de John Deere

## Instalación y Uso Rápido

1. Ejecuta el siguiente comando:
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

## Endpoints Destacados de Precision Tech

- `

## Seguridad y buenas prácticas

- **Nunca subas el archivo `.env` ni credenciales reales al repositorio.**
- El archivo `.env` está en el `.gitignore` y solo debe existir localmente.
- Todos los ejemplos usan variables ficticias, nunca valores reales.
- Al ejecutar `python main.py` por primera vez, se solicitarán las credenciales de forma segura y se guardarán solo en tu máquina.

## Ejemplo de integración con LLMs (ChatGPT, Claude, Ollama)

Puedes conectar cualquier LLM compatible con MCP usando un cliente MCP. Ejemplo con Python:

```python
from mcp.client import MCPClient

# Crear cliente MCP para ChatGPT o Claude
mcp_client = MCPClient(
    server_url="http://localhost:8000",  # Dirección de tu servidor MCP
    llm_provider="openai",  # o "anthropic" para Claude, "ollama" para Ollama
    model="gpt-4"  # o el modelo que prefieras
)

# Ejemplo de consulta
async def consulta():
    respuesta = await mcp_client.process_query("¿Cuál es el estado de la maquinaria?")
    print(respuesta)
```

## Integración con n8n

Puedes integrar el MCP con n8n usando el nodo HTTP Request para enviar consultas MCP al servidor y procesar las respuestas.

### Ejemplo de flujo básico en n8n:
1. **Nodo HTTP Request**
   - Método: POST o GET (según la herramienta MCP que expongas)
   - URL: `http://localhost:8000/tu-endpoint-mcp` (ajusta según tu configuración)
   - Headers: Si es necesario, agrega autenticación o tokens.
   - Body: JSON con los parámetros requeridos por la herramienta MCP.

2. **Nodo de procesamiento**
   - Procesa la respuesta del MCP y continúa el flujo según tu lógica de negocio.

### Ejemplo de configuración del nodo HTTP Request:
- **Método:** POST
- **URL:** `http://localhost:8000/process_query`
- **Body Parameters:**
  - `query`: "¿Cuál es el estado de la maquinaria?"

### Notas:
- Puedes encadenar varios nodos para automatizar consultas y acciones con LLMs y MCP.
- Consulta la documentación de n8n para detalles sobre nodos HTTP y manejo de respuestas JSON.