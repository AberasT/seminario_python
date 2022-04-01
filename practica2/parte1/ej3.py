import string

texto = 'Este es un texto de prueba para el ejercicio 3 de la practica 2 del Seminario de Python'
print('-'*30)
print(f'Texto: \n{texto}\n')
print('-'*30)
letra = input('Ingrese una letra: ')
if letra in string.ascii_letters:
    palabras = texto.split()
    palabras_con_letra = []
    for palabra in palabras:
        if palabra.lower().startswith(letra):
            palabras_con_letra.append(palabra)
else:  
    print('Lo ingresado no es una letra!')

palabras_con_letra = set(palabras_con_letra) # Elimino las repeticiones
if len(palabras_con_letra) != 0:
    print('Se imprimen las palabras del texto que comienzan con la letra ingresada: \n')
    for palabra in palabras_con_letra:
        print(f'- {palabra}')