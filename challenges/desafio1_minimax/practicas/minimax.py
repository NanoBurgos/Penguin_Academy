# Todos los movimientos posibles: 8 direcciones + quedarse quieto
movimientos = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1),(0,0)]

def distancia(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def minimax(gato, raton, depth, max_depth, turno_gato, n):
    if depth == max_depth or gato == raton:
        return -distancia(gato, raton), None

    if turno_gato:  
        mejor_valor = -9999
        mejor_movimiento = None
        for m in movimientos:
            nuevo_gato = (gato[0]+m[0], gato[1]+m[1])
            if 0 <= nuevo_gato[0] < n and 0 <= nuevo_gato[1] < n:
                valor, _ = minimax(nuevo_gato, raton, depth+1, max_depth, False, n)
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = nuevo_gato
        return mejor_valor, mejor_movimiento
    else:  
        mejor_valor = 9999
        mejor_movimiento = None
        for m in movimientos:
            nuevo_raton = (raton[0]+m[0], raton[1]+m[1])
            if 0 <= nuevo_raton[0] < n and 0 <= nuevo_raton[1] < n:
                valor, _ = minimax(gato, nuevo_raton, depth+1, max_depth, True, n)
                if valor < mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = nuevo_raton
        return mejor_valor, mejor_movimiento

n = 5
gato = (0,0)
raton = (3,2)

# Turno del gato
valor_g, mov_g = minimax(gato, raton, 0, 3, True, n)
print("Valor (gato):", valor_g)
print("Mejor movimiento del gato:", mov_g)

# Turno del ratón
valor_r, mov_r = minimax(gato, raton, 0, 3, False, n)
print("Valor (ratón):", valor_r)
print("Mejor movimiento del ratón:", mov_r)