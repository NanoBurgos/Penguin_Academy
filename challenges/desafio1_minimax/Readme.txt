Empece creando el "laberinto":
1° Cree el tablero en "forma" de  matriz, resalto "forma", por que en realidad es una lista de listas

Cargar cosas en mi tablero: 
2° Aprendi a cargar al gato G, raton R y obstaculos # en el tablero
Al inicio asignaba manualmente, luego aprendi a usar random y con la funcion randint, hacia que mi gato y raton aparecieran en lugares al azar dentro del tablero
Luego de aprender de algunos errores, ponia una condicion para que mi gato y raton no aparezcan la primera vez en la misma posicion 

Experimente cosas para los movimientos:
3° Asigne los valores posibles para los movimientos
En esta parte, si tuve muchas complicaciones, por que segun la logica que queria aplicar, no se movia como yo queria que se mueva el personaje en mi tablero
De las 9 direcciones que asigne, todas funcionaban al reves, menos el (5) que era mantener posicion 

Luego experimente y aprendi a validar si el siguiente paso es posible:
4° Entendi y aplique las condicionales para cuando un personaje se encuentra en el borde del tablero
o tambien cuando hay obsataculos, entonces el movimiento a esa casilla deja de ser valido

Luego empece a investigar sobre minimax:
5° Empece leyendo sobre el algoritmo minimax,
Lei los recursos que los compañeros compartian en el grupo 
Lei foros, investigaba y trataba de entender lo que hacia el algoritmo que ponian como ejemplo, ahi me di cuenta que me faltaba investigar sobre otras cosas

6° Investigue sobre funciones recursivas, sobre distancia Manhattan

7° Cuando (crei) entender como funciona minimax, empece a hablar con los compañeros presentes 
Antes de empezar a aplicar el algoritmo minimax a mi codigo, empece a recorrer y a hablar con cualquiera que escuchaba que hablaban sobre minimax
preguntaba cuales eran los errores que estaban teniendo, o por que creian que su algoritmo no estaba respondiendo como esperaban, 

8° Implementacion de Minimmax (errores por todas partes)

El mejor "¡ajá!" durante el proceso. (o eso crei)
9° Encontre una forma (matematica) en la cual el gato siempre iba al raton, y el raton siempre escapaba del gato, usando la pendiente de la recta que pasa por los puntos(posiciones) 
del gato y del raton, luego me di cuenta de que no siempre era valido

Luego intente ver si podia hacer condicionales de los vecinos
10° Como el metodo que intente hacer, no me funcionaba para todos los casos, intente hacer sin usar minimax
y cree condiciones en donde se evaluaban:
Para el gato: la distancia de los vecinos del gato, a la posicion actual del raton , el que hacia que la distancia sea la mas "chica", guardaba en una variable
Para el raton: la distancia desde la posicion actual del gato, y la distancia a las posiciones de los vecinos del raton , el que hacia que la distancia sea la mas "grande", guardaba en una variable

11° El mejor "¡ajá!" durante el proceso 2.0
Fue cuando me di cuenta de que minimax ya estaba haciendo las comprobaciones de los vecinos, asi como intente hacer antes
y luego entendi mucho mejor el algoritmo, sobre como comprueba la posicion actual, y con la profundidad, como comprueba movimientos futuros

Luego de escuchar la charla sobre minimax que dieron los compañeros del Bach 2.0
Nos recomendaron el MVP, producto minimo viable
12° Despues de muchos errores, y encontrar que yo mismo me estaba complicando con muchas cosas, decidi sacar varias cosas que estaban "adornando" mi algoritmo
eran cosas "esteticas" como que mi tablero, al inicio era como un tablero de ajedrez, que en la parte superior y al costado tenia 00 01 02 03 etc

13° Removi que el usuario defina las dimensiones del tablero, 
Ahora:
Las dimensiones del tablero son fijas, 
La posicion inicial para el gato y para el raton son fijas,
Las ubicaciones de los obstaculos son fijos,
Removi el queso,

Muchas cosas removi y modifique, para llegar a mi MVP




DESASTRES DEL PROCESO
1° Pensar en una matriz, esto me hizo tener muchos errores al inicio, por que el concepto de matriz que conocemos no es lo mismo para la computadora(por lo menos por ahora)
Queria trabajar con una matriz, pero primero no encontraba la logica para mis movimientos, tuve que crear matrices e ir asignando valores manuales para ver como el bucle esta recorriendo
la "matriz"
Por ejemplo asignaba tablero[0][0] = 'G' luego tablero[0][1] = 'G' en otra impresion, para ir viendo como se recorre la "matriz"

Investigue y encontre que para trabajar con matrices en python, hay una biblioteca llamada numpy, pero no lo utilice

2° Al cargar cosas en mi tablero, y si el tablero era muy pequeño, solo me aparecia el raton, 
Por que como python lee hacia abajo, y al ser muy pequeño el tablero, el lugar del gato y el raton coincidian(no siempre), por eso solo me mostraba el raton cuando las posiciones
aleatorias que se generaban eran iguales para el gato y el raton

3° Segun yo, ya entendia como se recorria la "matriz", 
Para poner como ejemplo, si yo queria ir hacia arriba, yo le sumaba(0,1) a mi posicion actual y hacia lo contrario de lo que yo queria
Pero luego entendi la logica de los indices del tablero, me parecia poco intuitivo que para ir hacia arriba debia ser (0,-1)
Pero llegue a comprender y encontrarle el sentido de como nos movemos con los indices, y al ir hacia arriba, estoy restando uno a la posicion en las columnas 

4° Cuando ponia obstaculos en una posicion, mi personaje igual se posicionaba en esa casilla

5° Al principio no entendi absolutamente nada del codigo de minimax, por que me faltaban bases, no entendia que eran funciones recursivas, no sabia que eran los grafos, etc.

6° La parte de investigacion, el problema fue creer que entendi algunos conceptos cuando no era asi

7° El ponerme a hablar con los demas sobre como estaban aplicando minimax, me ayudo a darme cuenta de que hay cosas que crei entender, pero me estaba equivocando en el concepto
por ej: El concepto de profundidad, 

8° Intentar implementar minimax a mi algoritmo, fue un proceso dificil
No funcionaba como esperaba, los sujetos se movian de forma en que no tenia "logica"
Tuve que modificar algunas partes del "codigo" que ya tenia hecho

9° Encontre que siempre que el tablero este libre, 
El gato solo debe avanzar hacia el raton usando la misma pendiente 
y el raton solo tiene 3 mejores movimientos, alejarse sobre la misma pendiente, o moverse sobre la recta perpendicular
Dbiuje esto, trace las rectas y me di cuenta de que en algunas ocasiones la recta perpendicular, no pasa sobre un punto valido del tablero

10° No se si  considerar como desastre del proceso, pero si tuve problemas al hacer las comprobaciones de los vecinos para el gato y para el raton, funcionaba, tenia logica, pero no encontraba
como integrar las comprobaciones dentro de un bucle, hasta que pude crear la comprobacion en forma de funcion  

11° Cuando "entendi mejor" minimax e intente aplicarlo a mi codigo, volvieron los errores
