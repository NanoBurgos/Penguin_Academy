import random

filas = 5
columnas=5

#crear tablero vacio
tablero = []       

# Creamos una matriz con puntos que sera el tablero de juego
for i in range(filas): 
    fila = []
    for j in range(columnas):
        fila.append('.')
    tablero.append(fila)

#Posicion aleatoria para el gato
gato_ini_x = random.randint(0, filas-1)
gato_ini_y = random.randint(0, columnas-1)
tablero[gato_ini_x][gato_ini_y] = 'G'

#Posicion aleatoria para el raton
raton_ini_x = random.randint(0, filas-1)
raton_ini_y = random.randint(0, columnas-1)

#Condicion para que nunca el raton(aleatorio) este en la misma posicion del gato(aleatorio)
while raton_ini_x == gato_ini_x and  gato_ini_y == raton_ini_y : 
    raton_ini_x = random.randint(0, filas-1)
    raton_ini_y = random.randint(0, columnas-1)

tablero[raton_ini_x][raton_ini_y] = 'R'

# Mostrar tablero
for fila in tablero:
    print(" ".join(fila))