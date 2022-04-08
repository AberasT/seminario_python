import string

celdas = [
'-*-*-',
'--*--',
'----*',
'*----',
]

def iniciar_mapa(matriz,alto,ancho):
    """ Los espacios en los que no hay minas, los inicia en 0, para luego comenzar el conteo de cercanía """
    for i in range(alto):
        for j in range(ancho):
            if matriz[i][j] == '-':
                matriz[i][j] = 0
    return matriz

def transformar_a_matriz(alto):
    """ Devuelve el mapa de celdas original, pero en forma de matriz.
    Asi, se puede acceder a cada elemento por separado mediante 2 indices """
    celdas_matriz = []
    for i in range(alto):
        celdas_matriz.append(list(celdas[i]))
    return celdas_matriz

def matriz_a_string(matriz):
    """ Devuelve el mapeo en matriz en forma de lista de strings, como el mapa original """
    mapa_minas = []
    for linea in matriz:
        mapa_minas.append(''.join(str(item) for item in linea))

def calcular_minas():
    """ """
    alto = len(celdas)
    ancho = len(celdas[0])

    celdas_matriz = transformar_a_matriz((alto,ancho))
    celdas_matriz = sumar_cercanias(celdas_matriz,alto,ancho)
    celdas_numeros = matriz_a_string(celdas_matriz)

    return celdas_numeros

def sumar_cercanias(celdas,alto,ancho):
    """"""
    iniciar_mapa(celdas,alto,ancho)
    for i in range(alto):
        for j in range(ancho):
            if celdas[i][j] == '*':
                match(i):
                    case 0:
                        celdas[i+1][j] += 1
                    case i if i == (alto-1):
                        celdas[i-1][j] += 1
                    case _:
                        celdas[i+1][j] += 1
                        celdas[i-1][j] += 1
                match(j):
                    case 0:
                        celdas[i][j+1] += 1
                    case j if j == (ancho - 1):
                        celdas[i][j-1] += 1
                    case _:
                        celdas[i][j+1] += 1
                        celdas[i][j-1] += 1
                if (i-1) in range(alto) and (j-1) in range(ancho):
                    if celdas[i-1][j-1] != '*':
                        celdas[i-1][j-1] += 1
                if (i-1) in range(alto) and (j+1) in range(ancho):
                    if celdas[i-1][j+1] != '*':
                        celdas[i-1][j+1] += 1
                if (i+1) in range(alto) and (j+1) in range(ancho):
                    if celdas[i+1][j+1] != '*':
                        celdas[i+1][j+1] += 1
                if (i+1) in range(alto) and (j-1) in range(ancho):
                    if celdas[i+1][j-1] != '*':
                        celdas[i+1][j-1] += 1

print(calcular_minas())