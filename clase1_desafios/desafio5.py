print('*'*30)
cadena_uno = str(input('Ingresar la primera cadena: '))
cadena_dos = str(input('Ingresar la segunda cadena: '))
if len(cadena_uno) > len(cadena_dos):
    print('La primera cadena tiene más caracteres que la segunda')
elif len(cadena_uno) < len(cadena_dos): 
    print('La segunda cadena tiene más caracteres que la primera')
else:
    print('Las cadenas tienen la misma cantidad de caracteres!')
print('*'*30)