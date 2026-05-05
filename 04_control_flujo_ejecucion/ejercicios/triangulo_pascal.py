"""
Ejercicio 4.3 — Triángulo de Pascal.

Imprime las primeras n filas del triángulo de Pascal, donde cada fila
se construye sumando elementos adyacentes de la anterior.

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def triangulo_pascal(n: int) -> None:
    """Imprime las primeras n filas del triángulo de Pascal centradas."""
    fila = [1]

    # Calculamos el ancho de la fila más larga para centrar
    fila_grande = [1]
    for i in range(n - 1):
        nueva = [1]
        for k in range(len(fila_grande) - 1):
            nueva.append(fila_grande[k] + fila_grande[k + 1])
        nueva.append(1)
        fila_grande = nueva
    ancho = len("   ".join(str(x) for x in fila_grande))

    for _ in range(n):
        cadena = "   ".join(str(x) for x in fila)
        print(cadena.center(ancho))

        # Calcular siguiente fila
        nueva_fila = [1]
        for k in range(len(fila) - 1):
            nueva_fila.append(fila[k] + fila[k + 1])
        nueva_fila.append(1)
        fila = nueva_fila


def main():
    n = int(input("Número de filas: "))
    triangulo_pascal(n)


if __name__ == "__main__":
    main()
