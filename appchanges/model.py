import requests as consulta

class ModelCoins():
    def __init__(self):
        self.url=""
        self.response= None
        self.objeto_general= None
        self.valores_lista= []
        self.moneda= None
        self.respuesta= None

        
    def getAllCoins(self,apikey):
        self.url = f"https://api.exchangeratesapi.io/v1/latest?access_key={apikey}"
        self.response = consulta.get(self.url)
        if self.response.status_code != 200:
            raise Exception("Error en consulta http")
        self.objeto_general = self.response.json()
        self.valores_lista=[]
        for k,v in self.objeto_general["rates"].items():
            self.valores_lista.append(k)

    def updateExchanges(self,apikey,moneda):
        self.moneda = moneda
        response = consulta.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={apikey}&base={moneda}&symbols=USD,MXN,BTC")
        self.respuesta = response.json() #Obtener la respuesta en formato de diccionario
        
        if response.status_code == 200:
            self.respuesta["rates"]
            #print(f"Rates: {respuesta["rates"]},\nUSD: {respuesta["rates"]["USD"]},\nMXN: {respuesta["rates"]["MXN"]},\nBTC: {respuesta["rates"]["BTC"]}")
        elif response.status_code >= 400:
           raise Exception("error: codigo:"+ self.respuesta['error']['code']+ "mensaje: "+ self.respuesta ['error']['message'])