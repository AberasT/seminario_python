import csv
import json
import os
import collections
from consolemenu import *
from consolemenu.items import *

# ARCHIVOS
ruta =  os.getcwd()
ruta_archivo = os.path.join(ruta,"netflix_titles.csv")
archivo_netflix = open(ruta_archivo,encoding="utf-8")
# PARA MANIPULAR CSV
csvreader = csv.reader(archivo_netflix,delimiter=',')
encabezado = next(csvreader)

# LIST COMPREHENSION PARA FILTRAR PELICULAS DEL 2021
peliculas_2021 = [x for x in csvreader if "2021" in x[6] and x[1] == "Movie"]

# PARA EXPORTARLAS EN JSON, HAGO LISTA DE DICCIONARIOS
lista_json = []
for pelicula in peliculas_2021:
    peli_dic = {}
    for i in range(len(encabezado)):
        peli_dic[encabezado[i]] = pelicula[i]
    lista_json.append(peli_dic)

# EXPORTO EN JSON
archivo_nuevo = open("peliculas_2021.json","w")
json.dump(lista_json,archivo_nuevo)
print("*"*50)
print("Archivo con las peliculas agregadas en 2021 creado")
archivo_nuevo.close()

# COUNTER PARA CONTAR LOS PAISES CON MAS PRODUCCIONES EN NETFLIX
# NO SE TIENEN EN CUENTA LOS PAISES VACIOS
archivo_netflix.seek(0)
contador_paises = collections.Counter(x[5] for x in csvreader  if x[5] != "")
archivo_netflix.close()

menu = ConsoleMenu("Desafío con archivo de Netflix","Menú de opciones")

def mostrar_peliculas():
    aux_menu = ConsoleMenu("Películas agregadas Netflix en 2021")
    texto = ""
    for pelicula in peliculas_2021:
        texto += pelicula[2] + "\n"
    aux_menu.prologue_text = texto
    aux_menu.show()


def mostrar_top_paises():
    aux_menu = ConsoleMenu("Países con más producciones en Netflix")
    top_paises = contador_paises.most_common(5)
    texto = ""
    for pais in top_paises:
        texto += f"{pais[0]}: {pais[1]} producciones \n"
    aux_menu.prologue_text = texto
    aux_menu.show()

item_top = FunctionItem("Listar países con más producciones en Netflix",mostrar_top_paises)
item_pelis = FunctionItem("Listar películas agregadas en 2021",mostrar_peliculas)

menu.append_item(item_top)
menu.append_item(item_pelis)

menu.show()