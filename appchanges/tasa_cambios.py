import requests as consulta
from config import API_KEY

moneda = input("Ingrese un código de moneda ").upper()

#El while controla que no se ingrese un valor erroneo o vacío
while moneda == "" or not moneda.isalpha():
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