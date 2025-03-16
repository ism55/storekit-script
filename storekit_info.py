import jwt
import time
import requests
import json

# Datos necesarios
KEY_ID = "KEY_ID"
ISSUER_ID = "issuer-id-from-app-store"
BUNDLE_ID = "<com.tuapp>"
PRIVATE_KEY_PATH = "<PRIVATE_KEY_PATH>"
TRANSACTION_ID = "TRANSACTION_ID"

# Generar timestamps
current_time = int(time.time())
expiration_time = current_time + (20 * 60)  # 20 minutos

# Crear payload
payload = {
    "iss": ISSUER_ID,
    "iat": current_time,
    "exp": expiration_time,
    "aud": "appstoreconnect-v1",
    "bid": BUNDLE_ID
}

# Leer clave privada
with open(PRIVATE_KEY_PATH, "r") as key_file:
    private_key = key_file.read().strip()  # Eliminar espacios en blanco

# Generar JWT
token = jwt.encode(
    payload,
    private_key,
    algorithm="ES256",
    headers={"alg": "ES256", "kid": KEY_ID, "typ": "JWT"}
)

print("Token generado:", token)
print(f"iat: {current_time} ({time.ctime(current_time)})")
print(f"exp: {expiration_time} ({time.ctime(expiration_time)})")

url = f"https://api.storekit.itunes.apple.com/inApps/v1/subscriptions/{TRANSACTION_ID}"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

try:
    response = requests.get(url, headers=headers)
    print("Código de respuesta:", response.status_code)
    print("Respuesta:", response.text)
    resp = response.text
    data = json.loads(resp)
    signedTransactionInfo = data["data"][0]["lastTransactions"][0]["signedTransactionInfo"]
    signedTransactionInfoDecoded = jwt.decode(signedTransactionInfo, options={"verify_signature": False})
    print("signedTransactionInfo:", signedTransactionInfoDecoded)
    signedRenewalInfo = data["data"][0]["lastTransactions"][0]["signedRenewalInfo"]
    signedRenewalInfoDecoded = jwt.decode(signedRenewalInfo, options={"verify_signature": False})
    print("signedRenewalInfo:", signedRenewalInfoDecoded)
except:
  print("An exception occurred")