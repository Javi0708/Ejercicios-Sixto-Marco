matriz = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Ingrese el número para la celda ({i},{j}): "))

print("La matriz resultante es:")
for fila in matriz:
    print(fila)