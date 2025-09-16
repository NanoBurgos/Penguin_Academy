import random

filas = 15
columnas = 15

#crear tablero vacio
tablero = [['.' for j in range(columnas)] for i in range(filas)]

#Posicion aleatoria para el gato
gato_ini_x = random.randint(0, filas-1)
gato_ini_y = random.randint(0, columnas-1)
tablero[gato_ini_x][gato_ini_y] = 'G'

#Posicion aleatoria para el raton
raton_ini_x = random.randint(0, filas-1)
raton_ini_y = random.randint(0, columnas-1)

while gato_ini_x==raton_ini_x and gato_ini_y==raton_ini_y:
    raton_ini_x = random.randint(0, filas-1)
    raton_ini_y = random.randint(0, columnas-1)

tablero[raton_ini_x][raton_ini_y] = 'R'

for fila in tablero:
    print(' '.join(fila))