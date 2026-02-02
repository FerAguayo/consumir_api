from appchanges.model import ModelCoins
from appchanges.config import *

def test_allcoins():
    objetoMoneda = ModelCoins()# Creando un objeto de la clase o instanciando la clase
    objetoMoneda.getAllCoins(API_KEY)
    lista = objetoMoneda.valores_lista
    assert lista != None