frase = 'Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres'
print(f'Frase: {frase}')
cadena = input('Ingresar string: ').lower()

frase_palabras = frase.lower().split()
cantidad = 0

for palabra in frase_palabras:
    if cadena in palabra:
        cantidad += 1
print(f'Cantidad: {cantidad}')