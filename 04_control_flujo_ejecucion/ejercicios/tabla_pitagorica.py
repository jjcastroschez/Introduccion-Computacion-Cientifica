"""
Ejercicio 8 — Tabla pitagórica con dos bucles anidados.

Imprime la tabla pitagórica de 1x1 hasta NxN sin usar listas.
Se utiliza print(..., end="") para mantener todo en la misma línea
y un print() vacío para saltar de fila.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

n = int(input("Tamaño de la tabla pitagórica: "))

# Cabecera
print("    |", end="")
for j in range(1, n + 1):
    print(f"{j:4}", end="")
print()
print("-" * (5 + 4 * n))

# Cuerpo
for i in range(1, n + 1):
    print(f"{i:3} |", end="")
    for j in range(1, n + 1):
        print(f"{i*j:4}", end="")
    print()   # salto de línea al acabar la fila
