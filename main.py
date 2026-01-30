import requests as consulta

#http://api.exchangeratesapi.io/v1/latest?access_key=4cff8ff3c7effbd2e294723f959fb196&base=EUR&symbols=USD,MXN,BTC

API_KEY = "4cff8ff3c7effbd2e294723f959fb196"
#moneda: "EUR"
moneda = input("Ingrese un código de moneda ").upper()

while moneda == "" or not moneda.isalpha():
    mondena = input("Ingrese un código de moneda ").upper()

response = consulta.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base={moneda}&symbols=USD,MXN,BTC")

""" <<<< CÓDIGOS DE REQUEST >>>>>
print("Código http de respuesta: ", response.status_code)
print("cabecera: ", response.headers["content-type"])
print("encoding: ", response.encoding)
print("Respuesta del string: ", response.text)
print("Respuesta en JSON", response.json())
"""
# EJERCICIO 1 Como capturamos la consulta con los rates
respuesta = response.json() #Obtener la respuesta en formato de diccionario

#Método con varios prints
"""
print("Rates: ",respuesta["rates"])
print("USD: ",respuesta["rates"]["USD"])
print("USD: ",respuesta["rates"]["MXN"])
print("USD: ",respuesta["rates"]["BTC"])
"""

#Método en un solo print usando fstring y saltos de linea

# print(f"Rates: {respuesta["rates"]},\nUSD: {respuesta["rates"]["USD"]},\nMXN: {respuesta["rates"]["MXN"]},\nBTC: {respuesta["rates"]["BTC"]}")


#Ejercicio 2 capturar errores de peticion http:
valor_error = {"error":{"code":"invalid_base_currency","message":"An unexpected error ocurred. [Technical Support: support@apilayer.com]"}}
if response.status_code == 200:
    print(f"Rates: {respuesta["rates"]},\nUSD: {respuesta["rates"]["USD"]},\nMXN: {respuesta["rates"]["MXN"]},\nBTC: {respuesta["rates"]["BTC"]}")

elif response.status_code >= 400:
    print(f"error: codigo:{ valor_error['error']['code']}, mensaje: { respuesta ['error']['message']}")