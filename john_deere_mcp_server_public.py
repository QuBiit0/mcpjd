"""
Servidor MCP Público para John Deere (solo documentación y ejemplos)
-------------------------------------------------------------------
- Expone herramientas de ejemplo y documentación.
- No requiere credenciales privadas ni acceso a APIs reales.
- Ideal para despliegue en gitmcp.io y pruebas públicas.
"""

from mcp.server.fastmcp import FastMCP
from typing import Dict

mcp = FastMCP("John Deere MCP Server Público (solo ejemplos)")

@mcp.tool()
def ejemplo_documentacion() -> Dict:
    """Devuelve un ejemplo de respuesta de documentación pública."""
    return {
        "mensaje": "Este es un ejemplo de herramienta pública. Para acceso real, ejecuta el servidor localmente con tus credenciales." 
    }

@mcp.tool()
def listar_endpoints_publicos() -> Dict:
    """Lista los endpoints y herramientas disponibles en el servidor público."""
    return {
        "endpoints": [
            "ejemplo_documentacion",
            "listar_endpoints_publicos"
        ],
        "nota": "Para acceso completo a las APIs privadas de John Deere, ejecuta el servidor localmente."
    }

if __name__ == "__main__":
    mcp.run() 