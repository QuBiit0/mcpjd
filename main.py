import os
import subprocess
import sys
import time
from pathlib import Path

REQUIRED_ENV_VARS = [
    "JOHN_DEERE_CLIENT_ID",
    "JOHN_DEERE_CLIENT_SECRET",
    "JOHN_DEERE_REDIRECT_URI",
    "JOHN_DEERE_REFRESH_TOKEN"
]

VENV_DIR = Path("venv")
ENV_FILE = Path(".env")
REQUIREMENTS_FILE = Path("requirements.txt")


def check_python_version():
    if sys.version_info < (3, 8):
        print("[ERROR] Se requiere Python 3.8 o superior.")
        sys.exit(1)
    print(f"[OK] Python {sys.version.split()[0]} detectado.")


def create_venv():
    if not VENV_DIR.exists():
        print("[INFO] Creando entorno virtual...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("[OK] Entorno virtual creado.")
    else:
        print("[OK] Entorno virtual detectado.")


def activate_venv():
    if os.name == "nt":
        activate_script = VENV_DIR / "Scripts" / "activate_this.py"
    else:
        activate_script = VENV_DIR / "bin" / "activate_this.py"
    if activate_script.exists():
        with open(activate_script) as f:
            exec(f.read(), {'__file__': str(activate_script)})
        print("[OK] Entorno virtual activado.")
    else:
        print("[ADVERTENCIA] No se pudo activar el entorno virtual automáticamente. Actívalo manualmente si tienes problemas de dependencias.")


def install_requirements():
    try:
        import pkg_resources
        with open(REQUIREMENTS_FILE) as f:
            required = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = [pkg for pkg in required if pkg.split('==')[0].lower() not in installed]
        if missing:
            print("[INFO] Instalando dependencias:", ", ".join(missing))
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)], check=True)
            print("[OK] Dependencias instaladas.")
        else:
            print("[OK] Todas las dependencias ya están instaladas.")
    except Exception as e:
        print("[ERROR] No se pudieron verificar/instalar las dependencias:", e)
        sys.exit(1)


def prompt_env_vars():
    env_vars = {
        "JOHN_DEERE_CLIENT_ID": "",
        "JOHN_DEERE_CLIENT_SECRET": "",
        "JOHN_DEERE_REDIRECT_URI": ""
    }
    for var in env_vars:
        value = os.getenv(var)
        if not value:
            value = input(f"Ingrese el valor para {var}: ")
        env_vars[var] = value
    # Guardar en .env
    with open(".env", "w") as f:
        for var, value in env_vars.items():
            f.write(f"{var}={value}\n")
    print("[OK] Archivo .env creado/actualizado.")
    # Recargar variables de entorno
    for var, value in env_vars.items():
        os.environ[var] = value


def check_env_vars():
    missing = [var for var in REQUIRED_ENV_VARS[:-1] if not os.getenv(var)]
    if missing:
        print("[ADVERTENCIA] Faltan variables de entorno:", ", ".join(missing))
        prompt_env_vars()
    else:
        print("[OK] Variables de entorno detectadas.")


def get_refresh_token():
    if not os.getenv("JOHN_DEERE_REFRESH_TOKEN"):
        print("[INFO] No se encontró refresh token. Ejecutando flujo de autenticación...")
        try:
            subprocess.run([sys.executable, "obtener_refresh_token.py"], check=True)
        except Exception as e:
            print("[ERROR] No se pudo obtener el refresh token:", e)
            sys.exit(1)
        print("[OK] Refresh token obtenido. Continúa con el despliegue.")
    else:
        print("[OK] Refresh token presente.")


def run_mcp_server():
    print("[INFO] Iniciando el servidor MCP (john_deere_mcp_server_full.py)...")
    print("El servidor MCP está corriendo y listo para recibir consultas desde LLMs compatibles (Claude, ChatGPT, etc.).")
    print("Presiona Ctrl+C para detener el servidor.")
    time.sleep(1)
    subprocess.run([sys.executable, "john_deere_mcp_server_full.py"])


def main():
    print("==============================")
    print("  DESPLIEGUE MCP JOHN DEERE   ")
    print("==============================")
    check_python_version()
    create_venv()
    #activate_venv()  # No es necesario en la mayoría de los casos si se ejecuta desde el entorno
    install_requirements()
    check_env_vars()
    get_refresh_token()
    run_mcp_server()

if __name__ == "__main__":
    main() 