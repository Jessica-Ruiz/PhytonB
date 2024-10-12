# Solicitar al usuario la cantidad de filas y columnas
filas = int(input("Introduce la cantidad de filas: "))
columnas = int(input("Introduce la cantidad de columnas: "))

# Crear el tablero de ajedrez
ajedrez = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        # Alternar entre 0 y 1
        if (i + j) % 2 == 0:
            fila.append(0)
        else:
            fila.append(1)
    ajedrez.append(fila)

# Imprimir el tablero
for fila in ajedrez:
    print(fila)
