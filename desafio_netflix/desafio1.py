import csv
import os

ruta =  os.getcwd()
ruta_archivo = os.path.join(ruta,"netflix_titles.csv")

archivo = open(ruta_archivo)
csvreader = csv.reader(archivo,delimiter=',')

encabezado = next(csvreader)
print(encabezado)





archivo.close()