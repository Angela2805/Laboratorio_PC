import requests
import json
import os

#Angela Guadalupe García Ibarra

datos = []
def link(url):
    rq = requests.get(url)
    return (json.loads(rq.content))

Api_key = str(input("Por favor ingresa tu API key de OpenWeatherMap: "))
datos.append(link("https://api.openweathermap.org/data/2.5/weather?q=Barcelona&units=metric&appid="+ Api_key))
datos.append(link("https://api.openweathermap.org/data/2.5/weather?id="+ Api_key))
datos.append(link("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid="+ Api_key))

with open("Práctica1.txt","w+") as txt:
    for i in datos:
        txt.write(str(i)+"\n")
        os.system("cls")
        print("Se ha creado un documento txt con los datos de la API Key que ha proporcionado.")