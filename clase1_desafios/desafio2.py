print('*'*30)
es_multiplo = False
numero = int(input('Ingresar un número: '))
# No uso estructuras elif o case porque se pueden cumplir más de una condición
if numero % 2 == 0:
    print('El número es múltiplo de 2')
    es_multiplo = True
if numero % 3 == 0:
    print('El número es múltiplo de 3')
    es_multiplo = True
if numero % 5 == 0:
    print('El número es múltiplo de 5')
    es_multiplo = True
if not es_multiplo:
    print('El número no es múltiplo de 2, 3 ni 5!')
print('*'*30)