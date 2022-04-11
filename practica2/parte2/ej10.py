import os
ruta = os.path.dirname(os.path.realpath('ej10'))
ruta_carpeta = os.path.join(ruta, "practica2","parte2","ej10")

ruta_nombres = os.path.join(ruta_carpeta, 'nombres_1.txt')
ruta_eval1 = os.path.join(ruta_carpeta, 'eval1.txt')
ruta_eval2 = os.path.join(ruta_carpeta, 'eval2.txt')

nombres = open(ruta_nombres, encoding="UTF-8")
eval1 = open(ruta_eval1, encoding="UTF-8",newline='\n')
eval2 = open(ruta_eval2, encoding="UTF-8",newline='\n')


lista_nombres = nombres.read().replace("'","").strip('\n').split(',\n')
lista_eval1 = eval1.read().replace("'","").strip('\n').split(',\n')
lista_eval2 = eval2.read().replace("'","").strip('\n').split(',\n')

listado_completo = []
suma = 0
for i in range(len(lista_nombres)):
    item = (lista_nombres[i] , int(lista_eval1[i]) + int(lista_eval2[i]))
    listado_completo.append(item)
    suma += item[1]

promedio = suma / len(listado_completo)

for item in listado_completo:
    if item[1] < promedio:
        print(item[0])

print(listado_completo)
print(promedio)