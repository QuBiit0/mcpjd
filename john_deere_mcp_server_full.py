"""
Servidor MCP para John Deere API (conexión real, SOLO GET)
---------------------------------------------------------
- Expone TODOS los endpoints GET de la documentación de John Deere como herramientas MCP.
- Solo lectura de información (no incluye POST/PUT/DELETE).
- Listo para conectar con cualquier LLM compatible con MCP.
- Lee las credenciales desde el archivo .env.

Uso:
1. Instala dependencias:
   pip install -r requirements.txt
2. Asegúrate de tener el archivo .env correctamente configurado.
3. Ejecuta el servidor:
   python john_deere_mcp_server_full.py
4. Conecta tu LLM o cliente MCP a este servidor.
"""

import os
import requests
import time
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp import Context
from typing import Optional

# Cargar variables de entorno
load_dotenv()

CLIENT_ID = os.getenv("JOHN_DEERE_CLIENT_ID")
CLIENT_SECRET = os.getenv("JOHN_DEERE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("JOHN_DEERE_REDIRECT_URI")
SCOPES = os.getenv("JOHN_DEERE_SCOPES", "ag1 ag2 ag3 eq1 eq2 org1 org2 files offline_access")
REFRESH_TOKEN = os.getenv("JOHN_DEERE_REFRESH_TOKEN")
API_BASE = "https://api.deere.com/platform"
TOKEN_URL = "https://signin.deere.com/oauth2/aus78tnlaysMraFhC1t7/v1/token"

API_BASES = {
    "prod": "https://api.deere.com/platform",
    "sandbox": "https://sandboxapi.deere.com/platform"
}

if not all([CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, REFRESH_TOKEN]):
    raise Exception("Faltan variables de entorno requeridas en el archivo .env")

# ------------------ Cliente John Deere API ------------------
class JohnDeereAPIClient:
    def __init__(self, env="prod"):
        self.env = env
        self.api_base = API_BASES.get(env, API_BASES["prod"])
        self.access_token = None
        self.token_expiry = 0
        self.refresh_token = REFRESH_TOKEN
        self.session = requests.Session()
        self._refresh_access_token()

    def _refresh_access_token(self):
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
        }
        resp = self.session.post(TOKEN_URL, data=data)
        if resp.status_code != 200:
            raise Exception(f"Error al refrescar el token: {resp.text}")
        tokens = resp.json()
        self.access_token = tokens["access_token"]
        self.token_expiry = int(time.time()) + tokens.get("expires_in", 3600) - 60
        if "refresh_token" in tokens:
            self.refresh_token = tokens["refresh_token"]

    def _ensure_token(self):
        if not self.access_token or time.time() > self.token_expiry:
            self._refresh_access_token()

    def _headers(self):
        self._ensure_token()
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/vnd.deere.axiom.v3+json"
        }

    def get(self, endpoint, params=None):
        url = f"{self.api_base}{endpoint}"
        resp = self.session.get(url, headers=self._headers(), params=params)
        if resp.status_code == 401:
            self._refresh_access_token()
            resp = self.session.get(url, headers=self._headers(), params=params)
        resp.raise_for_status()
        return resp.json()

# ------------------ Servidor MCP ------------------
mcp = FastMCP("John Deere MCP Server (API real, SOLO GET)")
api = JohnDeereAPIClient()

# -------- Herramientas MCP para TODOS los GET --------
# --- Equipos y Maquinaria ---
@mcp.tool()
def get_machines(org_id: str, env: str = "prod") -> dict:
    """Listar todas las máquinas de una organización en el entorno especificado."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines")

@mcp.tool()
def get_machine_details(org_id: str, machine_id: str, env: str = "prod") -> dict:
    """Obtener detalles de una máquina."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}")

@mcp.tool()
def get_machine_telemetry(org_id: str, machine_id: str, startTime: Optional[str] = None, endTime: Optional[str] = None, metrics: Optional[str] = None, env: str = "prod") -> dict:
    """Obtener telemetría de una máquina."""
    params = {}
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if metrics: params["metrics"] = metrics
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}/telemetry", params=params)

@mcp.tool()
def get_machinery_catalog(org_id: str, category: Optional[str] = None, model: Optional[str] = None, env: str = "prod") -> dict:
    """Listar maquinaria disponible en el catálogo."""
    params = {}
    if category: params["category"] = category
    if model: params["model"] = model
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machinery-catalog", params=params)

@mcp.tool()
def get_machinery_catalog_details(org_id: str, machinery_id: str, env: str = "prod") -> dict:
    """Obtener detalles de maquinaria del catálogo."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machinery-catalog/{machinery_id}")

@mcp.tool()
def get_fleet_status(org_id: str, env: str = "prod") -> dict:
    """Obtener estado de la flota."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/fleet")

# --- Operaciones ---
@mcp.tool()
def get_operations(org_id: str, startDate: Optional[str] = None, endDate: Optional[str] = None, operationType: Optional[str] = None, env: str = "prod") -> dict:
    """Listar operaciones de una organización."""
    params = {}
    if startDate: params["startDate"] = startDate
    if endDate: params["endDate"] = endDate
    if operationType: params["operationType"] = operationType
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/operations", params=params)

@mcp.tool()
def get_operation_details(org_id: str, operation_id: str, env: str = "prod") -> dict:
    """Obtener detalles de una operación."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/operations/{operation_id}")

# --- Campos ---
@mcp.tool()
def get_fields(org_id: str, env: str = "prod") -> dict:
    """Listar campos de una organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/fields")

@mcp.tool()
def get_field_details(org_id: str, field_id: str, env: str = "prod") -> dict:
    """Obtener detalles de un campo."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/fields/{field_id}")

# --- Archivos ---
@mcp.tool()
def get_files(org_id: str, env: str = "prod") -> dict:
    """Listar archivos de una organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/files")

@mcp.tool()
def get_file_details(org_id: str, file_id: str, env: str = "prod") -> dict:
    """Obtener detalles de un archivo."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/files/{file_id}")

# --- Prescripciones y Mapas de Rendimiento ---
@mcp.tool()
def get_prescriptions(org_id: str, fieldId: Optional[str] = None, startDate: Optional[str] = None, endDate: Optional[str] = None, env: str = "prod") -> dict:
    """Listar prescripciones."""
    params = {}
    if fieldId: params["fieldId"] = fieldId
    if startDate: params["startDate"] = startDate
    if endDate: params["endDate"] = endDate
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/prescriptions", params=params)

@mcp.tool()
def get_yield_maps(org_id: str, fieldId: Optional[str] = None, year: Optional[int] = None, env: str = "prod") -> dict:
    """Listar mapas de rendimiento."""
    params = {}
    if fieldId: params["fieldId"] = fieldId
    if year: params["year"] = year
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/yield-maps", params=params)

# --- Guiado y Autoguiado ---
@mcp.tool()
def get_guidance_systems(org_id: str, machineId: Optional[str] = None, env: str = "prod") -> dict:
    """Listar sistemas de guiado."""
    params = {}
    if machineId: params["machineId"] = machineId
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/guidance-systems", params=params)

# --- Flota y Asignaciones ---
@mcp.tool()
def get_fleet_assignments(org_id: str, env: str = "prod") -> dict:
    """Obtener asignaciones de flota."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/fleet/assignments")

# --- Órdenes de Trabajo ---
@mcp.tool()
def get_work_orders(org_id: str, status: Optional[str] = None, startDate: Optional[str] = None, endDate: Optional[str] = None, env: str = "prod") -> dict:
    """Listar órdenes de trabajo."""
    params = {}
    if status: params["status"] = status
    if startDate: params["startDate"] = startDate
    if endDate: params["endDate"] = endDate
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/work-orders", params=params)

@mcp.tool()
def get_work_order_details(org_id: str, work_order_id: str, env: str = "prod") -> dict:
    """Obtener detalles de una orden de trabajo."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/work-orders/{work_order_id}")

# --- Programación de Recursos ---
@mcp.tool()
def get_resource_schedule(org_id: str, resourceType: Optional[str] = None, startDate: Optional[str] = None, endDate: Optional[str] = None, env: str = "prod") -> dict:
    """Obtener programación de recursos."""
    params = {}
    if resourceType: params["resourceType"] = resourceType
    if startDate: params["startDate"] = startDate
    if endDate: params["endDate"] = endDate
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/resource-scheduling", params=params)

# --- Análisis ---
@mcp.tool()
def get_performance_analytics(org_id: str, fieldId: str, year: int, env: str = "prod") -> dict:
    """Obtener análisis de rendimiento."""
    params = {"fieldId": fieldId, "year": year}
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/analytics/performance", params=params)

@mcp.tool()
def get_efficiency_analytics(org_id: str, machineId: str, startDate: str, endDate: str, env: str = "prod") -> dict:
    """Obtener análisis de eficiencia."""
    params = {"machineId": machineId, "startDate": startDate, "endDate": endDate}
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/analytics/efficiency", params=params)

# --- Dealer Solutions, Service, Sales, Parts, Marketing, Financial, Supply Chain, Insights, User, Setup, Work Results, Otros ---
# (Agrega aquí todos los endpoints GET adicionales según la documentación, siguiendo el mismo patrón)
# Por ejemplo:
@mcp.tool()
def get_organizations(env: str = "prod") -> dict:
    """Listar organizaciones disponibles."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations")

@mcp.tool()
def get_organization_details(org_id: str, env: str = "prod") -> dict:
    """Obtener detalles de una organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}")

@mcp.tool()
def get_users(org_id: str, env: str = "prod") -> dict:
    """Listar usuarios de una organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/users")

@mcp.tool()
def get_user_details(org_id: str, user_id: str, env: str = "prod") -> dict:
    """Obtener detalles de usuario."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/users/{user_id}")

# --- Dealer Solutions: Service ---
@mcp.tool()
def get_work_order_disregard_reasons(org_id: str, locale: str = "es-AR", env: str = "prod") -> dict:
    """Listar motivos de cancelación de órdenes de trabajo."""
    params = {"locale": locale}
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/work-orders/disregard-reasons", params=params)

@mcp.tool()
def get_expert_services_jobs(org_id: str, env: str = "prod") -> dict:
    """Listar trabajos y checklists de Expert Services."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/expert-services/jobs")

@mcp.tool()
def get_service_agreements(org_id: str, env: str = "prod") -> dict:
    """Listar acuerdos de servicio y facturación diferida."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/service-admin/agreements")

# --- Dealer Solutions: Sales ---
@mcp.tool()
def get_quotes(org_id: str, env: str = "prod") -> dict:
    """Listar cotizaciones."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/quotes")

@mcp.tool()
def get_quote_details(org_id: str, quote_id: str, env: str = "prod") -> dict:
    """Obtener detalles de una cotización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/quotes/{quote_id}")

@mcp.tool()
def get_po_data(org_id: str, quote_id: str = None, env: str = "prod") -> dict:
    """Obtener datos de órdenes de compra (PO Data)."""
    params = {"quote_id": quote_id} if quote_id else None
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/po-data", params=params)

@mcp.tool()
def get_transaction_pricing(org_id: str, env: str = "prod") -> dict:
    """Comparar precios de transacciones."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/transaction-pricing")

# --- Dealer Solutions: Parts ---
@mcp.tool()
def get_dealer_syndication(org_id: str, env: str = "prod") -> dict:
    """Listar integración de partes (Dealer Syndication)."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/parts/syndication")

@mcp.tool()
def get_supplier_part_quotes(org_id: str, env: str = "prod") -> dict:
    """Listar cotizaciones de partes (Supplier Part Quoting)."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/parts/quotes")

# --- Dealer Solutions: Marketing Reporting ---
@mcp.tool()
def get_market_share(org_id: str, env: str = "prod") -> dict:
    """Obtener datos de market share por tienda y condado."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/market-share")

@mcp.tool()
def get_dealer_data_hub(org_id: str, env: str = "prod") -> dict:
    """Obtener datos de Dealer Data Hub."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/dealer-data-hub")

# --- Dealer Solutions: Financial ---
@mcp.tool()
def get_merchant_accounts(org_id: str, env: str = "prod") -> dict:
    """Listar cuentas de cliente merchant."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/merchant/accounts")

@mcp.tool()
def get_merchant_transactions(org_id: str, env: str = "prod") -> dict:
    """Listar transacciones merchant."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/merchant/transactions")

@mcp.tool()
def get_credit_applications(org_id: str, env: str = "prod") -> dict:
    """Listar aplicaciones de crédito online."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/credit-applications")

# --- Supply Chain ---
@mcp.tool()
def get_supplier_part_quotes_supply(org_id: str, env: str = "prod") -> dict:
    """Listar cotizaciones de partes de proveedor (Supply Chain)."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/supplier-part-quotes")

# --- Precision Tech: Application ---
@mcp.tool()
def get_connections(org_id: str, env: str = "prod") -> dict:
    """Listar conexiones de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/connections")

@mcp.tool()
def get_org_webhooks(org_id: str, env: str = "prod") -> dict:
    """Listar webhooks de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/webhooks")

# --- Precision Tech: Equipment ---
@mcp.tool()
def get_iso15143_3(org_id: str, machine_id: str, env: str = "prod") -> dict:
    """Obtener datos ISO 15143-3 (AEMP 2.0) de una máquina."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}/iso15143-3")

@mcp.tool()
def get_machine_alerts(org_id: str, machine_id: str, env: str = "prod") -> dict:
    """Obtener alertas de máquina."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}/alerts")

@mcp.tool()
def get_machine_device_state(org_id: str, machine_id: str, env: str = "prod") -> dict:
    """Obtener estado de dispositivo de máquina."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}/device-state")

@mcp.tool()
def get_machine_engine_hours(org_id: str, machine_id: str, env: str = "prod") -> dict:
    """Obtener horas de motor de máquina."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}/engine-hours")

@mcp.tool()
def get_machine_operation_hours(org_id: str, machine_id: str, env: str = "prod") -> dict:
    """Obtener horas de operación de máquina."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}/operation-hours")

@mcp.tool()
def get_machine_locations(org_id: str, machine_id: str, env: str = "prod") -> dict:
    """Obtener historial de ubicaciones de máquina."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}/locations")

@mcp.tool()
def get_machine_measurements(org_id: str, machine_id: str, env: str = "prod") -> dict:
    """Obtener mediciones de máquina."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/machines/{machine_id}/measurements")

# --- Precision Tech: Insights/Monitoring ---
@mcp.tool()
def get_assets(org_id: str, env: str = "prod") -> dict:
    """Listar assets de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/assets")

@mcp.tool()
def get_map_layers(org_id: str, env: str = "prod") -> dict:
    """Listar capas de mapas de terceros."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/map-layers")

@mcp.tool()
def get_notifications(org_id: str, env: str = "prod") -> dict:
    """Listar notificaciones de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/notifications")

# --- Precision Tech: Organization/User ---
@mcp.tool()
def get_partnerships(org_id: str, env: str = "prod") -> dict:
    """Listar partnerships de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/partnerships")

@mcp.tool()
def get_user_details_full(org_id: str, user_id: str, env: str = "prod") -> dict:
    """Obtener detalles de usuario (completo)."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/users/{user_id}")

# --- Precision Tech: Setup/Plan ---
@mcp.tool()
def get_boundaries(org_id: str, env: str = "prod") -> dict:
    """Listar boundaries de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/boundaries")

@mcp.tool()
def get_clients(org_id: str, env: str = "prod") -> dict:
    """Listar clientes de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/clients")

@mcp.tool()
def get_crop_types(org_id: str, env: str = "prod") -> dict:
    """Listar tipos de cultivos disponibles."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/crop-types")

@mcp.tool()
def get_farms(org_id: str, env: str = "prod") -> dict:
    """Listar fincas de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/farms")

@mcp.tool()
def get_flags(org_id: str, env: str = "prod") -> dict:
    """Listar flags de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/flags")

@mcp.tool()
def get_guidance_lines(org_id: str, env: str = "prod") -> dict:
    """Listar líneas de guiado."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/guidance-lines")

@mcp.tool()
def get_operators(org_id: str, env: str = "prod") -> dict:
    """Listar operadores de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/operators")

@mcp.tool()
def get_products(org_id: str, env: str = "prod") -> dict:
    """Listar productos de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/products")

@mcp.tool()
def get_work_plans(org_id: str, env: str = "prod") -> dict:
    """Listar planes de trabajo de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/work-plans")

# --- Precision Tech: Work Results ---
@mcp.tool()
def get_field_operations(org_id: str, env: str = "prod") -> dict:
    """Listar operaciones de campo."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/field-operations")

@mcp.tool()
def get_harvest_id_cotton(org_id: str, env: str = "prod") -> dict:
    """Listar módulos de algodón cosechados."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/harvest-id-cotton")

# --- Otros Recursos Especiales ---
@mcp.tool()
def get_customer_data_product(org_id: str, env: str = "prod") -> dict:
    """Obtener datos de producto de cliente."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/customer-data-product")

@mcp.tool()
def get_customer_linkage(org_id: str, env: str = "prod") -> dict:
    """Obtener vínculos de cliente."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/customer-linkage")

@mcp.tool()
def get_special_offers(org_id: str, locale: str = "es-AR", env: str = "prod") -> dict:
    """Listar ofertas especiales."""
    params = {"locale": locale}
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/special-offers", params=params)

# --- Precision Tech: Integración avanzada ---
@mcp.tool()
def get_org_integrations(org_id: str, env: str = "prod") -> dict:
    """Listar integraciones de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations")

@mcp.tool()
def get_org_integration_secrets(org_id: str, integration_id: str, env: str = "prod") -> dict:
    """Listar secretos de una integración de la organización."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets")

@mcp.tool()
def get_org_integration_secret(org_id: str, integration_id: str, secret_id: str, env: str = "prod") -> dict:
    """Obtener detalles de un secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}")

@mcp.tool()
def get_org_integration_secret_versions(org_id: str, integration_id: str, secret_id: str, env: str = "prod") -> dict:
    """Listar versiones de un secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions")

@mcp.tool()
def get_org_integration_secret_version(org_id: str, integration_id: str, secret_id: str, version_id: str, env: str = "prod") -> dict:
    """Obtener detalles de una versión de secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions/{version_id}")

@mcp.tool()
def get_org_integration_secret_version_access(org_id: str, integration_id: str, secret_id: str, version_id: str, env: str = "prod") -> dict:
    """Obtener accesos de una versión de secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions/{version_id}/access")

@mcp.tool()
def get_org_integration_secret_version_events(org_id: str, integration_id: str, secret_id: str, version_id: str, env: str = "prod") -> dict:
    """Listar eventos de una versión de secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions/{version_id}/events")

@mcp.tool()
def get_org_integration_secret_version_event(org_id: str, integration_id: str, secret_id: str, version_id: str, event_id: str, env: str = "prod") -> dict:
    """Obtener detalles de un evento de versión de secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions/{version_id}/events/{event_id}")

@mcp.tool()
def get_org_integration_secret_version_event_logs(org_id: str, integration_id: str, secret_id: str, version_id: str, event_id: str, env: str = "prod") -> dict:
    """Listar logs de un evento de versión de secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions/{version_id}/events/{event_id}/logs")

@mcp.tool()
def get_org_integration_secret_version_event_log(org_id: str, integration_id: str, secret_id: str, version_id: str, event_id: str, log_id: str, env: str = "prod") -> dict:
    """Obtener detalles de un log de evento de versión de secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions/{version_id}/events/{event_id}/logs/{log_id}")

@mcp.tool()
def get_org_integration_secret_version_event_log_entries(org_id: str, integration_id: str, secret_id: str, version_id: str, event_id: str, log_id: str, env: str = "prod") -> dict:
    """Listar entradas de un log de evento de versión de secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions/{version_id}/events/{event_id}/logs/{log_id}/entries")

@mcp.tool()
def get_org_integration_secret_version_event_log_entry(org_id: str, integration_id: str, secret_id: str, version_id: str, event_id: str, log_id: str, entry_id: str, env: str = "prod") -> dict:
    """Obtener detalles de una entrada de log de evento de versión de secreto de integración."""
    api = JohnDeereAPIClient(env=env)
    return api.get(f"/organizations/{org_id}/integrations/{integration_id}/secrets/{secret_id}/versions/{version_id}/events/{event_id}/logs/{log_id}/entries/{entry_id}")

# --- Fin de endpoints de integración avanzada ---

if __name__ == "__main__":
    mcp.run() 