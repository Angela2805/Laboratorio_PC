import requests
from bs4 import BeautifulSoup
import io
import sys, re, string
import bs4 as bs
import urllib.request
 
#Angela Guadalupe García Ibarra

#Script que habla de mi primer banda favorita llamada fifth harmony :p

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def soup_info_wiki():
    print("\n Información del grupo \n")
    url = "https://es.wikipedia.org/wiki/Fifth_Harmony"
    texto=BeautifulSoup(urllib.request.urlopen(url)).get_text()
    print(texto)
    print("\n")

def soup_imagenes():
    print("\n Link de las imagenes utilizadas\n")
    soup = get_soup("https://es.wikipedia.org/wiki/Fifth_Harmony")
    images = soup.find_all('img')
    t = [{'src': image.get('src'), 'alt' : image.get('alt')} for image in images]
    print(f"{t}")
    print("\n")

def soup_tabla():
    print("\n Información de las tablas\n")
    soup = get_soup("https://es.wikipedia.org/wiki/Fifth_Harmony")
    tr = soup.find_all('tr')
    for row in tr:
        cols = row.find_all('td')
        t= [ele.text.strip() for ele in cols]
        print(f"{t}")


input("Este programa recolecta información de mi banda favorita de todos los tiempos")

soup_info_wiki()
soup_imagenes()
soup_tabla()