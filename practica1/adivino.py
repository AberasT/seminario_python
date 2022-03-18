import random

numero_aleatorio = random.randrange(101) # 0 y 100 incluidos
gane = False
print("Tenés 5 intentos para divinar un número entre 0 y 100")
intento = 1
while intento < 6 and not gane:
    numero_ingresado = int(input('Ingresar número: '))
    if numero_ingresado == numero_aleatorio:
        print("Ganaste! y necesitaste {} intentos!!!".format(intento))
        gane = True
    else:
        if intento != 5 : print("Mmm... No, ese número no es...Seguí intentando")
        intento += 1
if not gane:
    print("\n Perdiste :(\n El número era: {}".format(numero_aleatorio))
    