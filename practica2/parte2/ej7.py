import string

cadena = input('Ingresar string para comprobar heterograma: ')

cadena_letras = []
for car in cadena:
    if car in string.ascii_letters:
        cadena_letras.append(car)

cadena_letras_sin_repetir = set(cadena_letras)

if len(cadena_letras) == len(cadena_letras_sin_repetir):
    print('Es un heterograma')
else:
    print('La cadena no es un heterograma')

