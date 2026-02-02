
class ViewCoins():
    
    def insertCoin(self):
        moneda = input("Ingrese un código de moneda ").upper()
        return moneda
    
    def viewListCoins(self,obj_modelo):
        print(f"Lista completa", obj_modelo.valores_lista)
        print(f"Total de código de monedas: ", len(obj_modelo.valores_lista))

    def viewRatesCoin(self,obj_modelo):
        print("Rates: ",modelo.respuesta["rates"])
        print("USD: ",round(modelo.respuesta["rates"]["USD"],2))
        print("USD: ",round(modelo.respuesta["rates"]["BTC"],2))
        print("USD: ",round(modelo.respuesta["rates"]["MXN"],2))
    
    def getError(self,error):
        print(error)