
raton=[2,3] #Definimos una posicion inicial para el raton

movimientos = { } #Creamos diccionario con los movimientos disponibles

movimientos['8'] = [0,-1]
movimientos['4'] = [-1,0]
movimientos['5'] = [0,0]
movimientos['6'] = [1,0]
movimientos['2'] = [0,1]


pos_actual_raton = [raton[0],raton[1]] #guardamos la posicion actual del raton en una variable

print(f'La posicion actual del raton es: {pos_actual_raton}') #Mostramos la posicion actual del raton

continuar = True #inicializamos la variable continuar en True, para que entre por lo menos la primera vez en el buble


while continuar:

    print('Lista de movimientos disponibles: ') #Imprimimos las opciones para que el usuario pueda ver
    print('7 =                   8 = Arriba                9 =         ')
    print('4 = Izquierda         5 = Mantener posicion     6 = Derecha ')
    print('1 =                   2 = Abajo                 3 =         ')

    print('Ingrese 0 para salir') #Le damos la opcion de salir del bucle al usuario
    seleccion_usuario = input('Ingresa el numero de acuerdo al movimiento que desea realizar')
    
    if seleccion_usuario == '0': #condicion para parar el bucle
        continuar = False
        break
    

    
    mov_selecc = movimientos[seleccion_usuario] #guardamos la seleccion del mov elegido por el usuario en una variable
    
    raton = [pos_actual_raton[0] + mov_selecc[0] , pos_actual_raton[1] + mov_selecc[1]] #actualizamos la posicion del raton 
    
    pos_actual_raton = raton #actualizamos la posicion inicial
    
    print(' ')
    print(f'La posicion actual del raton es: {pos_actual_raton}') #Mostramos la posicion actual del raton
    

 
    

