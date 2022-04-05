articulo = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""
partes_articulo = articulo.split('resumen:')
titulo = partes_articulo[0].strip()[8:]
resumen = partes_articulo[1].strip()

if len(titulo.split()) <= 10:
    print('-'*50 + '\nEl titulo esta ok')
else:
    print('-'*50 + f'\nEl titulo no esta ok, tiene {len(titulo.split())} palabras')

oraciones_resumen = resumen.split('.')
cantidades_oraciones = {'ora_faciles' : 0,'ora_aceptables' : 0,'ora_dificiles' : 0 ,'ora_muy_dificiles' : 0}

for oracion in oraciones_resumen:
    palabras_oracion = oracion.split()
    largo = len(palabras_oracion)

    # HACER CON IF ELSE
    match largo:
        case largo if largo in range(1,12):
            cantidades_oraciones['ora_faciles'] += 1
        case largo if largo in range(13,18):
            cantidades_oraciones['ora_aceptables'] += 1
        case largo if largo in range(18,26):
            cantidades_oraciones['ora_dificiles'] += 1
        case largo if largo > 25: 
            cantidades_oraciones['ora_muy_dificiles'] += 1

print(f'''Cantidad de oraciones:
Faciles de leer: {cantidades_oraciones['ora_faciles']}
Aceptables para leer: {cantidades_oraciones['ora_aceptables']}
Dificil de leer: {cantidades_oraciones['ora_dificiles']}
Muy dificil de leer: {cantidades_oraciones['ora_muy_dificiles']}''')