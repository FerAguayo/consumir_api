import requests as consulta

#http://api.exchangeratesapi.io/v1/latest?access_key=4cff8ff3c7effbd2e294723f959fb196&base=EUR&symbols=USD,MXN,BTC

response = consulta.get("http://api.exchangeratesapi.io/v1/latest?access_key=4cff8ff3c7effbd2e294723f959fb196&base=EUR&symbols=USD,MXN,BTC")

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
print(f"Rates: {respuesta["rates"]},\nUSD: {respuesta["rates"]["USD"]},\nMXN: {respuesta["rates"]["MXN"]},\nBTC: {respuesta["rates"]["BTC"]}")