tabla = (['AEIOULNRST', 1],['DG' ,2],['BCMP', 3],['FHVWY', 4],['K', 5],['J,X', 8],['ZQ',10])

cadena = input('Ingresar string para calcular valor: ').upper()

valor = 0

for car in cadena:
    for item in tabla:
        if car in item[0]:
            valor += item[1]
            print(f'{car} : {item[1]} puntos')
            break

print(f'Valor total de la palabra: {valor}')

