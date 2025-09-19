#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Portabilidad Linux / Windows
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

#define PAREDES   '#'
#define CAMINOS   ' '
#define SOLUCION  '*'

int filas, columnas;
int tablero_filas, tablero_columnas;
char *laberinto;

// Macros para índice en matriz 1D
#define IDX(f, c) ((f) * tablero_columnas + (c))

// Funciones para limpieza
void clear_screen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void sleep_ms(int ms) {
#ifdef _WIN32
    Sleep(ms);          // Windows usa milisegundos
#else
    usleep(ms * 1000);  // Linux usa microsegundos
#endif
}

// Funciones
void mostrar_laberinto(int p_fila, int p_columna);
void mostrar_jugador_laberinto(int p_fila, int p_columna, int pasos_recorridos);
void crear_laberinto(int f, int c);
int resolver_laberinto_bfs();
void juego_usuario();

// Mostrar el laberinto normal
void mostrar_laberinto(int p_fila, int p_columna) {
    clear_screen();
    for (int f = 0; f < tablero_filas; f++) {
        for (int c = 0; c < tablero_columnas; c++) {
            if (f == 1 && c == 0)
                putchar('E'); // entrada
            else if (f == tablero_filas - 2 && c == tablero_columnas - 1)
                putchar('S'); // salida
            else if (f == p_fila && c == p_columna)
                putchar('P'); // jugador
            else
                putchar(laberinto[IDX(f, c)]);
        }
        putchar('\n');
    }
}

// Mostrar laberinto con el jugador
void mostrar_jugador_laberinto(int p_fila, int p_columna, int pasos_recorridos) {
    clear_screen();
    for (int f = 0; f < tablero_filas; f++) {
        for (int c = 0; c < tablero_columnas; c++) {
            if (f == 1 && c == 0)
                putchar('E');
            else if (f == tablero_filas - 2 && c == tablero_columnas - 1)
                putchar('S');
            else if (f == p_fila && c == p_columna)
                putchar('P');
            else if (pasos_recorridos && laberinto[IDX(f,c)] == '.')
                putchar('.');
            else
                putchar(laberinto[IDX(f,c)]);
        }
        putchar('\n');
    }
}

// Inicializar con muros
void laberinto_inicial() {
    laberinto = malloc(tablero_filas * tablero_columnas);
    for (int f = 0; f < tablero_filas; f++)
        for (int c = 0; c < tablero_columnas; c++)
            laberinto[IDX(f, c)] = PAREDES;
}

// DFS recursivo para generar laberinto
void crear_laberinto(int f, int c) {
    int direcciones[4][2] = {{0,2},{0,-2},{2,0},{-2,0}};
    for (int i = 0; i < 4; i++) {
        int j = rand() % 4;
        int tmp0 = direcciones[i][0], tmp1 = direcciones[i][1];
        direcciones[i][0] = direcciones[j][0]; direcciones[i][1] = direcciones[j][1];
        direcciones[j][0] = tmp0; direcciones[j][1] = tmp1;
    }

    for (int i = 0; i < 4; i++) {
        int nf = f + direcciones[i][0];
        int nc = c + direcciones[i][1];

        if (nf > 0 && nf < tablero_filas-1 && nc > 0 && nc < tablero_columnas-1
            && laberinto[IDX(nf,nc)] == PAREDES) {
            laberinto[IDX(f + direcciones[i][0]/2, c + direcciones[i][1]/2)] = CAMINOS;
            laberinto[IDX(nf,nc)] = CAMINOS;
            mostrar_laberinto(-1, -1);
            sleep_ms(50);
            crear_laberinto(nf,nc);
        }
    }
}

// BFS para resolver laberinto automáticamente
typedef struct { int f, c; } Node;

int resolver_laberinto_bfs() {
    int visitados[tablero_filas][tablero_columnas];
    Node padre[tablero_filas][tablero_columnas];

    for (int f = 0; f < tablero_filas; f++)
        for (int c = 0; c < tablero_columnas; c++) {
            visitados[f][c] = 0;
            padre[f][c] = (Node){-1,-1};
        }

    Node queue[tablero_filas * tablero_columnas];
    int front = 0, back = 0;

    Node start = {1,0};
    Node end   = {tablero_filas-2, tablero_columnas-1};

    queue[back++] = start;
    visitados[start.f][start.c] = 1;

    int direcciones[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

    while (front < back) {
        Node cur = queue[front++];
        if (cur.f == end.f && cur.c == end.c) break;

        for (int i = 0; i < 4; i++) {
            int nf = cur.f + direcciones[i][0];
            int nc = cur.c + direcciones[i][1];
            if (nf >= 0 && nf < tablero_filas && nc >= 0 && nc < tablero_columnas
                && !visitados[nf][nc] && laberinto[IDX(nf,nc)] == CAMINOS) {
                visitados[nf][nc] = 1;
                padre[nf][nc] = cur;
                queue[back++] = (Node){nf,nc};
                laberinto[IDX(nf,nc)] = '.';
                mostrar_laberinto(-1,-1);
                sleep_ms(20);
            }
        }
    }

    Node cur = end;
    while (!(cur.f == start.f && cur.c == start.c)) {
        if (!(cur.f == end.f && cur.c == end.c))
            laberinto[IDX(cur.f,cur.c)] = SOLUCION;
        cur = padre[cur.f][cur.c];
        mostrar_laberinto(-1,-1);
        sleep_ms(50);
    }

    return 1;
}

// Juego animado
void juego_usuario() {
    int p_fila = 1, p_columna = 0;
    time_t tiempo_inicio = time(NULL);

    mostrar_jugador_laberinto(p_fila, p_columna, 0);

    while (!(p_fila == tablero_filas-2 && p_columna == tablero_columnas-1)) {
        char eleccion_usuario;
        scanf(" %c", &eleccion_usuario); 
        int nf = p_fila, nc = p_columna;
        if(eleccion_usuario == 'w') nf--;
        else if(eleccion_usuario == 's') nf++;
        else if(eleccion_usuario == 'a') nc--;
        else if(eleccion_usuario == 'd') nc++;

        if(nf >= 0 && nf < tablero_filas && nc >=0 && nc < tablero_columnas
           && laberinto[IDX(nf,nc)] != PAREDES) {
            laberinto[IDX(p_fila,p_columna)] = '.'; // marca camino recorrido
            p_fila = nf; p_columna = nc;
        }
        mostrar_jugador_laberinto(p_fila, p_columna, 1);
        sleep_ms(50); // pausa para animación
    }

    time_t tiempo_fin = time(NULL);
    printf("¡Felicidades! Encontraste la salida en %ld segundos.\n", tiempo_fin - tiempo_inicio);
}


// Programa principal
int main(int argumentos_c, char *argumentos_usuarios[]) {
    if (argumentos_c < 3) {
        printf("No se indicaron dimensiones, usando 10x10 por defecto.\n");
        filas = 10;
        columnas = 10;
    } else {
        filas = atoi(argumentos_usuarios[1]);
        columnas = atoi(argumentos_usuarios[2]);
    }

    if (filas < 2 || columnas < 2) {
        printf("Error: dimensiones minimas 2x2.\n");
        return 1;
    }

    tablero_filas = filas * 2 + 1;
    tablero_columnas = columnas * 2 + 1;

    srand(time(NULL));
    laberinto_inicial();

    laberinto[IDX(1,0)] = CAMINOS;
    laberinto[IDX(tablero_filas-2, tablero_columnas-1)] = CAMINOS;
    laberinto[IDX(1,1)] = CAMINOS;

    //medir tiempo de creación del laberinto
    clock_t inicio_generacion = clock();
    crear_laberinto(1,1);
    clock_t final_generacion = clock();
    double tiempo_transc_gen_laberinto = (double)(final_generacion - inicio_generacion) / CLOCKS_PER_SEC;
    printf("\nEl laberinto se genero en %.3f segundos.\n", tiempo_transc_gen_laberinto);

    int eleccion;
    printf("Elige una opcion:\n1. Jugar\n2. Ver animacion de resolucion\nOpcion: ");
    scanf("%d", &eleccion);

    if(eleccion == 1) {
        juego_usuario();
    } else {
        clock_t inicio_resolucion = clock();
        resolver_laberinto_bfs();
        clock_t fin_resolucion = clock();
        double tiempo_transc_resolv_laberinto = (double)(fin_resolucion - inicio_resolucion) / CLOCKS_PER_SEC;
        mostrar_laberinto(-1,-1);
        printf("\nEl laberinto se resolvio en %.3f segundos.\n", tiempo_transc_resolv_laberinto);
    }

    free(laberinto);
    return 0;
}
