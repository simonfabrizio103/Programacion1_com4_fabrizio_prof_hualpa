import random


# --- FUNCIÓN PARA MOSTRAR LOS TABLEROS ---
def imprimir_tablero(tablero, titulo):
    """Imprime un tablero con un formato claro."""
    print(f"\n--- {titulo} ---")
    # Imprime la cabecera con los números de columna
    print("  " + " ".join(str(i) for i in range(TAMANO_TABLERO)))
    # Imprime las filas con su número correspondiente
    for i, fila in enumerate(tablero):
        print(f"{i} " + " ".join(fila))
    print("-" * (TAMANO_TABLERO * 2 + 5))


# Definimos el tamaño del tablero del jugador
TAMANO_TABLERO = 5


# Definimos cada posible simbolo que pueda encontrarse en el tablero
SIMBOLO_AGUA = '0'
SIMBOLO_BARCO = '1'
SIMBOLO_ACIERTO = 'X'
SIMBOLO_FALLO = 'O'
SIMBOLO_VACIO = '-'


# Tablero 1: Océano con barcos colocados aleatoriamente
# Se crea una matriz para representar el tablero.
tablero_oceano = []
total_barcos = 0

for _ in range(TAMANO_TABLERO):
    fila = []
    for _ in range(TAMANO_TABLERO):

        # Se decide colocar agua o barco dependiendo del azar, hay 25% de chances de que haya un barco
        if random.randint(1, 4) == 1:
            fila.append(SIMBOLO_BARCO)
            total_barcos += 1
        else:
            fila.append(SIMBOLO_AGUA)
    tablero_oceano.append(fila)


# Vamos a asegurarnos que haya aunque sea 1 barco para que se pueda jugar
if total_barcos == 0:
    fila_aleatoria = random.randint(0, TAMANO_TABLERO - 1)
    col_aleatoria = random.randint(0, TAMANO_TABLERO - 1)
    tablero_oceano[fila_aleatoria][col_aleatoria] = SIMBOLO_BARCO
    total_barcos = 1


# Tablero 2: Disparos del jugador, inicialmente vacío
tablero_jugador = [[SIMBOLO_VACIO for _ in range(TAMANO_TABLERO)] for _ in range(TAMANO_TABLERO)]


# --- LÓGICA PRINCIPAL DEL JUEGO ---

barcos_hundidos = 0
print("¡Bienvenido al juego de Batalla Naval!")
print(f"Objetivo: Hundir los {total_barcos} barcos enemigos.")


# El juego sigue mientras no se hayan hundido todos los barcos
while barcos_hundidos < total_barcos:
    imprimir_tablero(tablero_jugador, "TUS DISPAROS")


    # --- Solicitar y validar coordenadas ---
    try:
        fila_disparo = int(input(f"Ingresa la fila para disparar (0-{TAMANO_TABLERO - 1}): "))
        col_disparo = int(input(f"Ingresa la columna para disparar (0-{TAMANO_TABLERO - 1}): "))


        # Validación 1: Coordenadas dentro del tablero
        if not (0 <= fila_disparo < TAMANO_TABLERO and 0 <= col_disparo < TAMANO_TABLERO):
            print("❌ ¡Error! Coordenadas fuera del tablero. Inténtalo de nuevo.")
            continue


        # Validación 2: Casilla no disparada previamente
        if tablero_jugador[fila_disparo][col_disparo] != SIMBOLO_VACIO:
            print("❌ ¡Error! Ya has disparado en esa casilla. Elige otra.")
            continue


        # --- Comprobar el resultado del disparo ---
        if tablero_oceano[fila_disparo][col_disparo] == SIMBOLO_BARCO:
            print("\n💥 ¡ACIERTO! Le has dado a un barco.")
            tablero_jugador[fila_disparo][col_disparo] = SIMBOLO_ACIERTO
            barcos_hundidos += 1
        else:
            print("\n💧 ¡AGUA! Has fallado.")
            tablero_jugador[fila_disparo][col_disparo] = SIMBOLO_FALLO

    except ValueError:
        print("❌ ¡Error! Debes ingresar un número válido.")
        continue


# --- FIN DEL JUEGO ---

print("\n======================================")
print("🎉 ¡FELICIDADES! HAS HUNDIDO TODOS LOS BARCOS. 🎉")
print("======================================")


# Se muestra el tablero del jugador con todos los disparos
imprimir_tablero(tablero_jugador, "RESULTADO FINAL DE TUS DISPAROS")


# Se revela la posición original de los barcos
imprimir_tablero(tablero_oceano, "POSICIÓN ORIGINAL DE LOS BARCOS")