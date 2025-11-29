#
print("\n Importacao e uso de um modulo de terceiros")
import requests

url = "https://www.example.com"

response = requests.get(url)
print(f"Solicitacao de HTTP para {url} retornou o status {response.status_code}")