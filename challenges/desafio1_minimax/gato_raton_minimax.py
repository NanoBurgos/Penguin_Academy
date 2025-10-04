import random

######### Configuración variables del juego #########

filas = 10
columnas = 10

OBSTACULOS = {(1,0), (1,1), (1,3)}
GATO_INI = (0, 0)
RATON_INI = (5, 5)
LIMITE_TURNOS = 40
PROFUNDIDAD_MAX = 6

######### Movimientos posibles (teclado numérico) #########
MOVS = {
    1:(-1,1), 2:(0,1), 3:(1,1),
    4:(-1,0), 5:(0,0), 6:(1,0),
    7:(-1,-1), 8:(0,-1), 9:(1,-1)
}

######### Funciones #########

def en_rango(x,y):
    return 0 <= x < columnas and 0 <= y < filas and (x,y) not in OBSTACULOS

def heuristica(gato, raton, turno, limite):
    if gato == raton:
        return 1000 - turno
    
    if turno >= limite:
        return -1000
    
    gx, gy = gato
    rx, ry = raton
    
    return -(abs(gx-rx) + abs(gy-ry))

def movimientos(pos):
    movimientos_validos = []
    
    for dx,dy in MOVS.values():
        nx, ny = pos[0]+dx, pos[1]+dy
        
        if en_rango(nx, ny):
            movimientos_validos.append((nx,ny))
    
    return movimientos_validos

def imprimir_tablero(gato, raton):
    for y in range(filas):
        
        fila_str = ""
        
        for x in range(columnas):
            if (x,y) == gato and (x,y) == raton:
                fila_str += "X "
            elif (x,y) == gato:
                fila_str += "G "
            elif (x,y) == raton:
                fila_str += "R "
            elif (x,y) in OBSTACULOS:
                fila_str += "# "
            else:
                fila_str += ". "
        print(fila_str)
    print()

def mover_humano(pos, quien=""):
    while True:
        if quien:
            print(f"Turno del {quien}. Selecciona tu próximo movimiento:")
       
        print('7 = Diag, Arriba_izq     8 = Arriba               9 = Diag, Arriba_der')
        print('4 = Izquierda            5 = Mantener Lugar       6 = Derecha')
        print('1 = Diag, Abajo_izq      2 = Abajo                3 = Diag, Abajo_der')
        print()
       
        s = input("Movimiento (1-9): ").strip()
       
        if s not in ('1','2','3','4','5','6','7','8','9'):
            print("Entrada inválida. Usa teclas 1..9.\n")
            continue
       
        dx, dy = MOVS[int(s)]
       
        nuevo = (pos[0]+dx, pos[1]+dy)
       
        if en_rango(*nuevo):
            return nuevo
        
        print("Movimiento inválido (fuera del tablero u obstáculo). Intenta otra vez.\n")

#########Algoritmo Minimax (ambos jugadores)#########

def minimax(gato, raton, profundidad, max_turno, turno, limite, alpha, beta):
    if gato == raton or turno >= limite or profundidad == 0:
        return heuristica(gato, raton, turno, limite), None

    if max_turno:  ######### Gato = MAX
        mejor_val = -99999
        mejor_mov = None
        
        for m in movimientos(gato):
            val, _ = minimax(m, raton, profundidad-1, False, turno+1, limite, alpha, beta)
            
            if val > mejor_val:
                mejor_val = val
                mejor_mov = m
            alpha = max(alpha, val)
            
            if beta <= alpha:
                break
       
        return mejor_val, mejor_mov
    
    else:  #########Ratón = MIN
        peor_val = 99999
        peor_mov = None
        
        for m in movimientos(raton):
            val, _ = minimax(gato, m, profundidad-1, True, turno+1, limite, alpha, beta)
           
            if val < peor_val:
                peor_val = val
                peor_mov = m
            
            beta = min(beta, val)
            if beta <= alpha:
                break
        
        return peor_val, peor_mov

######### Control del Ratón (PC) con primeros 3 turnos aleatorios

def mover_raton_pc(raton, gato, turno_actual):
    if turno_actual < 3: 
       
        movs = movimientos(raton)
        if movs:
            return random.choice(movs)
        else:
            return raton
   
    else: #a partir del turno 4 minimax
        _, mov = minimax(gato, raton, PROFUNDIDAD_MAX, False, turno_actual, LIMITE_TURNOS, -99999, 99999)
        return mov if mov else raton


######### Bucle principal #########

def jugar():
    print("Elige modo de juego:")
    print("1. Usuario = Gato, PC = Ratón")
    print("2. Usuario = Ratón, PC = Gato")
    print("3. Ambos PC")
    
    eleccion = input("Opción: ").strip()

    gato, raton = GATO_INI, RATON_INI

    for turno in range(LIMITE_TURNOS):
        print(f"Turno {turno+1}:")
        imprimir_tablero(gato, raton)

        if gato == raton:
            print("¡El gato atrapó al ratón!")
            return

        # Movimiento del Gato 
        if eleccion == "1":  # Usuario elige mover gato
            gato = mover_humano(gato, "GATO")
        else:  # PC = gato
            _, mov = minimax(gato, raton, PROFUNDIDAD_MAX, True, turno, LIMITE_TURNOS, -99999, 99999)
            if mov:
                gato = mov

        if gato == raton:
            imprimir_tablero(gato, raton)
            print("¡El gato atrapó al ratón!")
            return

        # Movimiento del Ratón 
        if eleccion == "2":  # Usuario elige  raton
            raton = mover_humano(raton, "RATÓN")
        else:  # PC = ratón
            raton = mover_raton_pc(raton, gato, turno)

    print("¡El ratón logró escapar!")


# Ejecutar

if __name__ == "__main__":
    jugar()