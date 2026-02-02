import requests as consulta

class ModelCoins():
    def __init__(self):
        self.url=""
        self.response = None
        self.objeto_general=None
        self.valores_lista=[]

        pass
    def getAllCoins(self,apikey):
        self.url = f"https://api.exchangeratesapi.io/v1/latest?access_key={apikey}"
        self.response = consulta.get(self.url)

        if self.response.status_code != 200:
            raise Exception("Error en consulta http")

        self.objeto_general = self.response.json()

        self.valores_lista=[]

        for k,v in self.objeto_general["rates"].items():
            self.valores_lista.append(k)