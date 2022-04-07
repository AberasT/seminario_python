import string

celdas = [
'-*-*-',
'--*--',
'----*',
'*----',
]

alto = len(celdas)
ancho = len(celdas[0])

celdas_matriz = []

for i in range(alto):
    celdas_matriz.append(list(celdas[i]))


for i in range(alto):
    for j in range(ancho):
        if celdas_matriz[i][j] == '-':
            celdas_matriz[i][j] = 0


for i in range(alto):
    for j in range(ancho):
        if celdas_matriz[i][j] == '*':
            match(i):
                case 0:
                    celdas_matriz[i+1][j] += 1
                case i if i == (alto-1):
                    celdas_matriz[i-1][j] += 1
                case _:
                    celdas_matriz[i+1][j] += 1
                    celdas_matriz[i-1][j] += 1
            match(j):
                case 0:
                    celdas_matriz[i][j+1] += 1
                case j if j == (ancho - 1):
                    celdas_matriz[i][j-1] += 1
                case _:
                    celdas_matriz[i][j+1] += 1
                    celdas_matriz[i][j-1] += 1
            if (i-1) in range(alto) and (j-1) in range(ancho):
                if celdas_matriz[i-1][j-1] != '*':
                    celdas_matriz[i-1][j-1] += 1
            if (i-1) in range(alto) and (j+1) in range(ancho):
                if celdas_matriz[i-1][j+1] != '*':
                    celdas_matriz[i-1][j+1] += 1
            if (i+1) in range(alto) and (j+1) in range(ancho):
                if celdas_matriz[i+1][j+1] != '*':
                    celdas_matriz[i+1][j+1] += 1
            if (i+1) in range(alto) and (j-1) in range(ancho):
                if celdas_matriz[i+1][j-1] != '*':
                    celdas_matriz[i+1][j-1] += 1

mapa_minas = []

for linea in celdas_matriz:
    mapa_minas.append(''.join(str(item) for item in linea))

for linea in mapa_minas: print(linea)
