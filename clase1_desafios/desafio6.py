print('*'*30)
cadena = str(input('Ingresar un cadena: '))
cantidad_a = 0
for car in cadena:
    if car == 'a':
        cantidad_a += 1
print('Cadena: \"{}\" \nCantidad de caracteres \"a\": {}'.format(cadena,cantidad_a))
print('*'*30)