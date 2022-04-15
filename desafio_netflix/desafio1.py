import csv
import json
import os
import collections

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
top_paises = contador_paises.most_common(5)
print("*"*50)
print("Los 5 paises con mas producciones en Netflix: ")
for pais in top_paises:
    print(pais)

archivo_netflix.close()