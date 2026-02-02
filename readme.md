## Aplicación de consulta de api de valores de monedas internacionales

Programa hecho en python para recuperar el valor en monedas de euros(EUR) y dólares(USD)

# Instalación
-Obtener el apikey en https://api.exchangeratesapi.io
-Renombrar config_template.py a config.py
-Agregar la apikey dentro de config.py de la siguiente manera
```
API_KEY="Ingresa tu apikey"
```
# Instalacion de dependencias(librerias)
-Crear un entorno virtual de python con una de estas opciones

```
py -m venv entorno
python -m venv entorno
python3 -m venv entorno
```

-Activar el entorno e instalar los requerimientos

```
windows - .\entorno\Scripts\activate
mac o linux - source entorno/bin/activate

pip install -r requirements.txt

-Utilizamos las librerias de pytest y requests
```