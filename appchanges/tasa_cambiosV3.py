import requests as consulta
from config import API_KEY
from model import *

modelo = ModelCoins()
try:
    modelo.getAllCoins(API_KEY)
except Exception as error:
    print(error)
    pass

print(f"Lista completa", modelo.valores_lista)
print(f"Total de código de monedas: ", len(modelo.valores_lista))


moneda = input("Ingrese un código de moneda ").upper()

#El while controla que no se ingrese un valor erroneo o vacío
while moneda == "" or not moneda.isalpha() or moneda not in modelo.valores_lista:
    moneda = input("Ingrese un código de moneda ").upper()
try:
    modelo.updateExchanges(API_KEY,moneda)
    print("Rates: ",modelo.respuesta["rates"])
    print("USD: ",round(modelo.respuesta["rates"]["USD"],2))
    print("USD: ",round(modelo.respuesta["rates"]["BTC"],2))
    print("USD: ",round(modelo.respuesta["rates"]["MXN"],2))
except Exception as error:
    print(error)