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
print(encabezado)
lista = [x for x in csvreader]

def paises_productores(lista):
    paises = set()
    for linea in lista:
        paises_show = set(linea[5].split(','))
        for pais in paises_show:
            if pais != '': paises.add(pais)
    return paises

def forma_parte(pais,linea):
    return pais.lower() in linea[5].lower()

paises = paises_productores(lista)

def tipos_show_pais(lista,pais):
    tipos = set()
    for linea in lista:
        if forma_parte(pais,linea): tipos.add(linea[1])
    return tipos

print('*'*30)
pais = 'uruguay'
tipos_pais = tipos_show_pais(lista,pais)
print('*'*30)

print(pais)
print(tipos_pais)

print('*'*30)
paises = list(paises)
paises.sort()
print(paises)