import urllib.parse
import requests
import os

print("=== Obtener refresh token de John Deere (OAuth2) ===\n")

# 1. Solicitar datos al usuario
def pedir_dato(nombre, ejemplo):
    valor = input(f"Introduce {nombre} (ejemplo: {ejemplo}): ").strip()
    if not valor:
        print(f"[ERROR] Debes ingresar {nombre}.")
        exit(1)
    return valor

client_id = pedir_dato("tu client_id", "EXAMPLE_CLIENT_ID")
client_secret = pedir_dato("tu client_secret", "EXAMPLE_CLIENT_SECRET")
redirect_uri = pedir_dato("tu redirect_uri", "http://localhost:9090/callback")

scopes = "offline_access ag1 ag2 ag3 eq1 eq2 org1 org2 files"

# 2. Generar URL de autorización
auth_params = {
    "response_type": "code",
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "scope": scopes,
    "state": "xyz123"
}
auth_url = "https://signin.deere.com/oauth2/aus78tnlaysMraFhC1t7/v1/authorize?" + urllib.parse.urlencode(auth_params)

print("\n1. Abre la siguiente URL en tu navegador e inicia sesión con tu cuenta John Deere:")
print(auth_url)
print("\n2. Autoriza la aplicación. Serás redirigido a tu redirect_uri con un parámetro 'code' en la URL.")
print("   Ejemplo: http://localhost:9090/callback?code=XXXXX&state=xyz123\n")

# 3. Solicitar el código de autorización
code = input("3. Copia y pega aquí el valor de 'code' de la URL de redirección: ").strip()
if not code:
    print("[ERROR] Debes ingresar el código de autorización.")
    exit(1)

# 4. Intercambiar el código por el refresh token
token_url = "https://signin.deere.com/oauth2/aus78tnlaysMraFhC1t7/v1/token"
data = {
    "grant_type": "authorization_code",
    "code": code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri
}
print("\nSolicitando tokens a John Deere...")
response = requests.post(token_url, data=data)
try:
    tokens = response.json()
except Exception:
    print("[ERROR] No se pudo decodificar la respuesta JSON.")
    print(response.text)
    exit(1)

def guardar_en_env(client_id, client_secret, redirect_uri, refresh_token):
    env_path = ".env"
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.strip().split("=", 1)
                    env_vars[k] = v
    env_vars["JOHN_DEERE_CLIENT_ID"] = client_id
    env_vars["JOHN_DEERE_CLIENT_SECRET"] = client_secret
    env_vars["JOHN_DEERE_REDIRECT_URI"] = redirect_uri
    env_vars["JOHN_DEERE_REFRESH_TOKEN"] = refresh_token
    with open(env_path, "w", encoding="utf-8") as f:
        for k, v in env_vars.items():
            f.write(f"{k}={v}\n")
    print(f"\nCredenciales guardadas/actualizadas en {env_path}")

if "refresh_token" in tokens:
    print("\n=== ¡Éxito! ===")
    print(f"refresh_token: {tokens['refresh_token']}")
    print(f"access_token: {tokens['access_token']}")
    guardar_en_env(client_id, client_secret, redirect_uri, tokens['refresh_token'])
else:
    print("\n[ERROR] No se obtuvo refresh_token. Respuesta completa:")
    print(tokens) 