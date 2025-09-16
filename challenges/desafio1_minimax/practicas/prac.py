import random
#Pedimos al usuario que introduzca las dimensiones del tablero
filas = int(input('Ingresa la cantidad de filas del tablero: '))
columnas = int(input('Ingresa la cantidad de columnas del tablero: '))

tablero = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append('.')
    tablero.append(fila)
    
tablero[random.randint(0, filas-1)][random.randint(0, columnas-1)]='Q'
tablero[random.randint(0, filas-1)][random.randint(0, columnas-1)]='R'
    
for fila in tablero:
    print(' '.join(fila))