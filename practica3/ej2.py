import os
import csv
import datetime
import collections

ruta =  os.getcwd()
logs = 'BBB_nuevo.csv'
ruta_archivo = os.path.join(ruta,logs)


with open(ruta_archivo, encoding='utf-8') as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header, logs_recurso = next(data_logs), list(data_logs)


formato = "%d/%m/%Y %H:%M"
dias_semana = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']

lista_fechas = [datetime.datetime.strptime(linea[0],formato) for linea in logs_recurso]

contador_dias = collections.Counter(dias_semana[log.weekday()] for log in lista_fechas)

print(contador_dias)

ultima_fecha = lista_fechas[0]
primera_fecha = lista_fechas[len(lista_fechas)-1]
print(primera_fecha)
print(ultima_fecha)

print((ultima_fecha-primera_fecha).days)
