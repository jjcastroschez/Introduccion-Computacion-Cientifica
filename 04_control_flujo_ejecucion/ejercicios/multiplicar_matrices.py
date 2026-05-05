"""
Ejercicio 4.2 — Multiplicación de matrices.

Implementación clásica con triple bucle anidado. Coste O(n³).

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def multiplicar(A, B):
    """Multiplica dos matrices representadas como listas de listas."""
    filas_A = len(A)
    cols_A = len(A[0])
    filas_B = len(B)
    cols_B = len(B[0])

    if cols_A != filas_B:
        raise ValueError(
            f"Dimensiones incompatibles: A es {filas_A}x{cols_A}, "
            f"B es {filas_B}x{cols_B}."
        )

    # Inicializamos C como matriz de ceros
    C = [[0] * cols_B for _ in range(filas_A)]

    # Triple bucle anidado
    for i in range(filas_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


def imprimir_matriz(M, nombre):
    print(f"{nombre} =")
    for fila in M:
        print(f"  {fila}")


def main():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    imprimir_matriz(A, "A")
    imprimir_matriz(B, "B")

    C = multiplicar(A, B)
    imprimir_matriz(C, "A·B")


if __name__ == "__main__":
    main()
