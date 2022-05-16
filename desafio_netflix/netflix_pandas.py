import csv
import json
import os
import collections
import pandas as pd

# ARCHIVOS
ruta =  os.getcwd()
ruta_archivo = os.path.join(ruta,"netflix_titles.csv")
with open(ruta_archivo,encoding="utf-8") as archivo:
    dataset = pd.read_csv(archivo)
    print(dataset.columns)
    filtro = dataset[(dataset["release_year"] >= 2010) & (dataset["type"] == "Movie")]
    filtro_agrupado = filtro.groupby(["type", "release_year"])["title"].count()
    print(filtro_agrupado)
    filtro_agrupado.plot(kind="bar")
