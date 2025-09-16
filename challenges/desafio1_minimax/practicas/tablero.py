filas = 10        #definimos el ancho
columnas = 10     #definimos el largo

tablero = []       #creamos el tablero vacio

# Creamos una matriz con puntos que sera el tablero de juego
for i in range(filas): 
    fila = []
    for j in range(columnas):
        fila.append('.')
    tablero.append(fila)
    
# Para mostrar el tablero
for fila in tablero:
    print(' '.join(fila))

