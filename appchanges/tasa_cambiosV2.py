import requests as consulta
from config import API_KEY
#https://api.exchangeratesapi.io/v1/latest?access_key=4cff8ff3c7effbd2e294723f959fb196
url = f"https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}"

response = consulta.get(url)

if response.status_code != 200:
    raise Exception("Error en consulta http")

objeto_general = response.json()

valores_lista=[]

for k,v in objeto_general["rates"].items():
    valores_lista.append(k)

print(f"Lista completa", valores_lista)
print(f"Total de código de monedas: ", len(valores_lista))


moneda = input("Ingrese un código de moneda ").upper()

#El while controla que no se ingrese un valor erroneo o vacío
while moneda == "" or not moneda.isalpha() or moneda not in valores_lista:
    mondena = input("Ingrese un código de moneda ").upper()

response = consulta.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base={moneda}&symbols=USD,MXN,BTC")
respuesta = response.json() #Obtener la respuesta en formato de diccionario

valor_error = {"error":{"code":"invalid_base_currency","message":"An unexpected error ocurred. [Technical Support: support@apilayer.com]"}}
if response.status_code == 200:
    print("Rates: ",respuesta["rates"])
    print("USD: ",round(respuesta["rates"]["USD"],2))
    print("USD: ",round(respuesta["rates"]["MXN"],2))
    print("USD: ",round(respuesta["rates"]["BTC"],2))
    #print(f"Rates: {respuesta["rates"]},\nUSD: {respuesta["rates"]["USD"]},\nMXN: {respuesta["rates"]["MXN"]},\nBTC: {respuesta["rates"]["BTC"]}")
elif response.status_code >= 400:
    print(f"error: codigo:{ valor_error['error']['code']}, mensaje: { respuesta ['error']['message']}")