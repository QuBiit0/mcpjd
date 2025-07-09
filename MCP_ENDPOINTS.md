# Documentación de Endpoints MCP para John Deere

---

## get_machines

**Descripción:**  
Lista todas las máquinas de una organización en el entorno especificado.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machines("org123", env="sandbox")
```

**Ejemplo de respuesta:**
```json
{
  "machines": [
    {
      "id": "machine123",
      "name": "Tractor 8R 410",
      "model": "8R 410",
      "serialNumber": "SN123456",
      "status": "ACTIVE"
    }
  ]
}
```

---

## get_machine_details

**Descripción:**  
Obtiene los detalles de una máquina específica en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine456"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machine_details("org123", "machine456", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "machine456",
  "name": "Tractor 8R 410",
  "model": "8R 410",
  "serialNumber": "SN123456",
  "status": "ACTIVE",
  "engineHours": 1234,
  "lastMaintenance": "2024-03-01",
  "capabilities": ["auto_guidance", "variable_rate"]
}
```

---

## get_machine_telemetry

**Descripción:**  
Obtiene los datos de telemetría de una máquina específica en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine456"
- `startTime` (str, opcional): Fecha/hora de inicio en formato ISO.  
  Ejemplo: "2024-01-01T00:00:00Z"
- `endTime` (str, opcional): Fecha/hora de fin en formato ISO.  
  Ejemplo: "2024-01-02T00:00:00Z"
- `metrics` (str, opcional): Métricas a consultar, separadas por coma.  
  Ejemplo: "ENGINE_SPEED,FUEL_LEVEL"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machine_telemetry("org123", "machine456", startTime="2024-01-01T00:00:00Z", endTime="2024-01-02T00:00:00Z", metrics="ENGINE_SPEED,FUEL_LEVEL", env="sandbox")
```

**Ejemplo de respuesta:**
```json
{
  "machine_id": "machine456",
  "telemetry": [
    {"timestamp": "2024-01-01T10:00:00Z", "ENGINE_SPEED": 1500, "FUEL_LEVEL": 80}
  ]
}
```

---

## get_fields

**Descripción:**  
Lista todos los campos de una organización en el entorno especificado.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_fields("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "fields": [
    {
      "id": "field123",
      "name": "Campo Norte",
      "area": 100.5,
      "boundary": {
        "type": "Polygon",
        "coordinates": [[[0,0], [0,1], [1,1], [1,0], [0,0]]]
      }
    }
  ]
}
```

---

## get_field_details

**Descripción:**  
Obtiene los detalles de un campo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `field_id` (str): ID del campo.  
  Ejemplo: "field123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_details("org123", "field123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "field123",
  "name": "Campo Norte",
  "area": 100.5,
  "boundary": {
    "type": "Polygon",
    "coordinates": [[[0,0], [0,1], [1,1], [1,0], [0,0]]]
  }
}
```

---

## get_operations

**Descripción:**  
Lista todas las operaciones de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `operationType` (str, opcional): Tipo de operación. Ejemplo: "PLANTING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_operations("org123", startDate="2024-03-01", endDate="2024-03-31", operationType="PLANTING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "operations": [
    {
      "id": "op123",
      "type": "PLANTING",
      "startTime": "2024-03-20T08:00:00Z",
      "endTime": "2024-03-20T17:00:00Z",
      "status": "COMPLETED"
    }
  ]
}
```

---

## get_operation_details

**Descripción:**  
Obtiene los detalles de una operación específica de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `operation_id` (str): ID de la operación.  
  Ejemplo: "op123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_operation_details("org123", "op123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "op123",
  "type": "PLANTING",
  "startTime": "2024-03-20T08:00:00Z",
  "endTime": "2024-03-20T17:00:00Z",
  "status": "COMPLETED",
  "assignedMachines": ["machine123"]
}
```

---

## get_resource_schedule

**Descripción:**  
Obtiene la programación de recursos (máquinas, operadores) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `resourceType` (str, opcional): Tipo de recurso. Ejemplo: "MACHINE"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-20"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-21"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_resource_schedule("org123", resourceType="MACHINE", startDate="2024-03-20", endDate="2024-03-21", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "schedule": [
    {"resourceId": "machine123", "assignedTo": "op456", "date": "2024-03-20"}
  ]
}
```

---

## get_performance_analytics

**Descripción:**  
Obtiene analíticas de rendimiento de una organización o máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de análisis. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_performance_analytics("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "analytics": {
    "fieldId": "field123",
    "year": 2024,
    "yield": 13.2,
    "work_hours": 80
  }
}
```

---

## get_efficiency_analytics

**Descripción:**  
Obtiene analíticas de eficiencia de una organización o máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_efficiency_analytics("org123", machineId="machine123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "analytics": {
    "machine_id": "machine123",
    "efficiency": 92.5
  }
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_fleet_status

**Descripción:**  
Obtiene el estado de la flota de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_fleet_status("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "fleet": [
    {"id": "machine123", "status": "ACTIVE"},
    {"id": "machine456", "status": "INACTIVE"}
  ]
}
```

---

## get_fleet_assignments

**Descripción:**  
Obtiene las asignaciones de la flota de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_fleet_assignments("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "assignments": [
    {"machineId": "machine123", "operationId": "op123", "startTime": "2024-03-20T08:00:00Z"}
  ]
}
```

---

## get_machine_alerts

**Descripción:**  
Obtiene las alertas de una máquina específica.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machine_alerts("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "alerts": [
    {"timestamp": "2024-03-20T10:00:00Z", "code": "DTC123", "description": "Alerta de motor"}
  ]
}
```

---

## get_machine_device_state

**Descripción:**  
Obtiene el estado del dispositivo telemático de una máquina específica.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machine_device_state("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "deviceState": {
    "status": "ONLINE",
    "lastSeen": "2024-03-20T10:00:00Z"
  }
}
```

---

## get_machine_engine_hours

**Descripción:**  
Obtiene las horas de motor de una máquina específica.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machine_engine_hours("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "engineHours": 1234
}
```

---

## get_machine_operation_hours

**Descripción:**  
Obtiene las horas de operación de una máquina específica.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machine_operation_hours("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "operationHours": 567
}
```

---

## get_machine_locations

**Descripción:**  
Obtiene el historial de ubicaciones de una máquina específica.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machine_locations("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "locations": [
    {"timestamp": "2024-03-20T10:00:00Z", "lat": -34.6037, "lon": -58.3816}
  ]
}
```

---

## get_machine_measurements

**Descripción:**  
Obtiene las mediciones de una máquina específica.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machine_measurements("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "measurements": [
    {"timestamp": "2024-03-20T10:00:00Z", "metric": "OIL_PRESSURE", "value": 30}
  ]
}
```

---

## get_iso15143_3

**Descripción:**  
Obtiene los datos ISO 15143-3 (AEMP 2.0) de una máquina específica.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_iso15143_3("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "iso15143_3": {
    "engineHours": 1234,
    "fuelLevel": 80,
    "location": {"lat": -34.6037, "lon": -58.3816}
  }
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "score": 95}
  ]
}
```

---

## get_customer_linkage

**Descripción:**  
Obtiene los vínculos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_linkage("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "linkages": [
    {"id": "link1", "dbsCustomer": "dbs1", "jdCustomer": "jd1"}
  ]
}
```

---

## get_special_offers

**Descripción:**  
Lista las ofertas especiales disponibles para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_special_offers("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "offers": [
    {"id": "offer1", "name": "Descuento Primavera", "sku": "SPRING2024"}
  ]
}
```

---

## get_machinery_catalog

**Descripción:**  
Lista la maquinaria disponible en el catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `category` (str, opcional): Categoría de maquinaria. Ejemplo: "TRACTOR"
- `model` (str, opcional): Modelo específico. Ejemplo: "8R 410"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog("org123", category="TRACTOR", model="8R 410", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "catalog": [
    {"id": "cat1", "category": "TRACTOR", "model": "8R 410", "specs": {"power": 410, "weight": 15000}},
    {"id": "cat2", "category": "HARVESTER", "model": "S780", "specs": {"power": 473, "weight": 20000}}
  ]
}
```

---

## get_machinery_catalog_details

**Descripción:**  
Obtiene los detalles de una máquina del catálogo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machinery_id` (str): ID de la maquinaria.  
  Ejemplo: "cat1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_machinery_catalog_details("org123", "cat1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "cat1",
  "category": "TRACTOR",
  "model": "8R 410",
  "specs": {"power": 410, "weight": 15000}
}
```

---

## get_files

**Descripción:**  
Lista todos los archivos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_files("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "files": [
    {"id": "file1", "name": "Mapa de rendimiento 2024", "type": "yield_map"},
    {"id": "file2", "name": "Prescripción Sur", "type": "prescription"}
  ]
}
```

---

## get_file_details

**Descripción:**  
Obtiene los detalles de un archivo específico de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `file_id` (str): ID del archivo.  
  Ejemplo: "file1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_file_details("org123", "file1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "file1",
  "name": "Mapa de rendimiento 2024",
  "type": "yield_map",
  "size": "2MB",
  "created_at": "2024-03-01T12:00:00Z"
}
```

---

## get_prescriptions

**Descripción:**  
Lista las prescripciones de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `startDate` (str, opcional): Fecha de inicio. Ejemplo: "2024-03-01"
- `endDate` (str, opcional): Fecha de fin. Ejemplo: "2024-03-31"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_prescriptions("org123", fieldId="field123", startDate="2024-03-01", endDate="2024-03-31", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "prescriptions": [
    {
      "id": "presc1",
      "fieldId": "field123",
      "type": "VARIABLE_RATE",
      "crop": "CORN",
      "product": "NITROGEN",
      "applicationRate": {"min": 100, "max": 200, "unit": "LBS_PER_ACRE"},
      "boundaries": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}
    }
  ]
}
```

---

## get_yield_maps

**Descripción:**  
Lista los mapas de rendimiento de una organización, con filtros opcionales.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `fieldId` (str, opcional): ID del campo. Ejemplo: "field123"
- `year` (int, opcional): Año de cosecha. Ejemplo: 2024
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_yield_maps("org123", fieldId="field123", year=2024, env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "yield_maps": [
    {
      "id": "yield1",
      "fieldId": "field123",
      "year": 2024,
      "zones": [
        {"zone": 1, "yield": 12.5},
        {"zone": 2, "yield": 13.0}
      ]
    }
  ]
}
```

---

## get_guidance_systems

**Descripción:**  
Lista los sistemas de guiado de una organización, con filtro opcional por máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machineId` (str, opcional): ID de la máquina. Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_systems("org123", machineId="machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_systems": [
    {"id": "gs1", "machineId": "machine123", "mode": "AUTO", "accuracy": "HIGH"}
  ]
}
```

---

## get_guidance_lines

**Descripción:**  
Lista las líneas de guiado de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_guidance_lines("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "guidance_lines": [
    {"id": "gl1", "name": "Línea Norte", "type": "AB"}
  ]
}
```

---

## get_boundaries

**Descripción:**  
Lista los límites (boundaries) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_boundaries("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "boundaries": [
    {"id": "b1", "name": "Límite Norte", "geometry": {"type": "Polygon", "coordinates": [[[0,0],[0,1],[1,1],[1,0],[0,0]]]}}
  ]
}
```

---

## get_farms

**Descripción:**  
Lista las fincas de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_farms("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "farms": [
    {"id": "farm1", "name": "Finca Sur"}
  ]
}
```

---

## get_flags

**Descripción:**  
Lista las banderas (flags) de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_flags("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "flags": [
    {"id": "flag1", "name": "Bandera Sur", "color": "red"}
  ]
}
```

---

## get_products

**Descripción:**  
Lista los productos de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_products("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "products": [
    {"id": "prod1", "name": "Fertilizante A"}
  ]
}
```

---

## get_work_plans

**Descripción:**  
Lista los planes de trabajo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_plans("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "work_plans": [
    {"id": "wp1", "name": "Plan Siembra 2024"}
  ]
}
```

---

## get_field_operations

**Descripción:**  
Lista las operaciones de campo de una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_field_operations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "field_operations": [
    {"id": "fo1", "type": "PLANTING", "fieldId": "field123"}
  ]
}
```

---

## get_harvest_id_cotton

**Descripción:**  
Obtiene información de módulos de algodón en una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_harvest_id_cotton("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "harvest_id_cotton": [
    {"id": "cotton1", "fieldId": "field123", "year": 2024, "weight": 1200}
  ]
}
```

---

## get_dealer_locations

**Descripción:**  
Lista las ubicaciones de los concesionarios asociados a la organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_dealer_locations("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "dealers": [
    {"id": "dealer1", "name": "Concesionario Norte", "address": "Av. Principal 123"},
    {"id": "dealer2", "name": "Concesionario Sur", "address": "Ruta 8 km 200"}
  ]
}
```

---

## get_expert_services_jobs

**Descripción:**  
Lista los trabajos y checklists de Expert Services para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_expert_services_jobs("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "jobs": [
    {"id": "job1", "name": "Inspección de motor", "status": "COMPLETED"},
    {"id": "job2", "name": "Chequeo hidráulico", "status": "PENDING"}
  ]
}
```

---

## get_service_agreements

**Descripción:**  
Lista los contratos de servicio activos para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_service_agreements("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "agreements": [
    {"id": "agr1", "type": "MANTENIMIENTO", "start": "2024-01-01", "end": "2024-12-31"}
  ]
}
```

---

## get_supply_chain_orders

**Descripción:**  
Lista las órdenes de la cadena de suministro para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `status` (str, opcional): Estado de la orden. Ejemplo: "PENDING"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_orders("org123", status="PENDING", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "orders": [
    {"id": "sc1", "item": "Filtro de aceite", "status": "PENDING"}
  ]
}
```

---

## get_supply_chain_order_details

**Descripción:**  
Obtiene los detalles de una orden de la cadena de suministro.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `order_id` (str): ID de la orden.  
  Ejemplo: "sc1"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_supply_chain_order_details("org123", "sc1", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "id": "sc1",
  "item": "Filtro de aceite",
  "status": "PENDING",
  "quantity": 10,
  "expectedDelivery": "2024-05-10"
}
```

---

## get_precision_tech_settings

**Descripción:**  
Obtiene la configuración de tecnología de precisión para una máquina.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `machine_id` (str): ID de la máquina.  
  Ejemplo: "machine123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_precision_tech_settings("org123", "machine123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "settings": {
    "autoTrac": true,
    "sectionControl": true,
    "rateController": false
  }
}
```

---

## get_work_order_disregard_reasons

**Descripción:**  
Lista los motivos de cancelación de órdenes de trabajo para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `locale` (str, opcional): Localización. Ejemplo: "es-AR"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_work_order_disregard_reasons("org123", locale="es-AR", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "reasons": [
    {"code": "NO_PARTS", "description": "Faltan repuestos"},
    {"code": "CLIENT_CANCEL", "description": "Cancelado por el cliente"}
  ]
}
```

---

## get_customer_data_product

**Descripción:**  
Obtiene el producto de datos de cliente para una organización.

**Parámetros:**
- `org_id` (str): ID de la organización.  
  Ejemplo: "org123"
- `env` (str, opcional): "prod" o "sandbox". Por defecto "prod".

**Ejemplo de uso:**
```python
get_customer_data_product("org123", env="prod")
```

**Ejemplo de respuesta:**
```json
{
  "customer_data": [
    {"id": "cdp1", "name": "Juan Pérez", "activity": "Compra", "