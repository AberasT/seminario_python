from encodings import utf_8
import os

ruta_wd = os.getcwd();
ruta_nombres1 = os.path.join(ruta_wd,'nombres_1.txt')
ruta_nombres2 = os.path.join(ruta_wd,'nombres_2.txt')

nombres_1 = open(ruta_nombres1,encoding="utf_8")
nombres_2 = open(ruta_nombres2,encoding="utf_8")

lista_nombres1 = nombres_1.read().replace("'","").replace(" ","").strip('\n').split(',\n')
lista_nombres2 = nombres_2.read().lower().replace("'","").replace(" ","").strip('\n').split(',\n')
lista_repetidos = [nombre for nombre in lista_nombres1 if nombre.lower() in lista_nombres2]

print('*'*30)
print('Nombres que se encuentran en ambos archivos:\n')
print(lista_repetidos)
print('*'*60)
print('SEGUNDA PARTE DEL EJERCICIO\n')

ruta_eval1 = os.path.join(ruta_wd,'eval1.txt')
ruta_eval2 = os.path.join(ruta_wd,'eval2.txt')

eval1 = open(ruta_eval1,encoding="utf_8")
eval2 = open(ruta_eval2,encoding="utf_8")

lista_eval1 = eval1.read().replace("'","").replace(" ","").strip('\n').split(',\n')
lista_eval2 = eval2.read().lower().replace("'","").replace(" ","").strip('\n').split(',\n')

print(f'  NOMBRE         EVAL1    EVAL2        TOTAL')
for i in range(len(lista_nombres1)):
    total = int(lista_eval1[i]) + int(lista_eval2[i])
    print(f'{i:2} {lista_nombres1[i]:15} {lista_eval1[i]:8} {lista_eval2[i]:8} {total:6}')