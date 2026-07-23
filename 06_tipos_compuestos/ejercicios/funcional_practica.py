"""
Ejercicio 5 — Programación funcional en acción.

Dada una lista de números, calcula usando programación funcional:
  1. La suma de los cuadrados de los NÚMEROS PARES.
  2. El producto de los NÚMEROS MAYORES QUE 3.

Todo con map, filter y reduce. Después compara con las versiones
"con bucle" del Tema 4.

Tema 6 - Introducción a la Computación Científica (ICC).
"""

from functools import reduce


# ---- Versión funcional -----------------------------------------------

def suma_cuadrados_pares_funcional(numeros: list) -> int:
    """Suma de cuadrados de los pares, con filter + map + sum.
    :param numeros: lista de números
    :return: suma de los cuadrados de los pares
    """
    pares = filter(lambda x: x % 2 == 0, numeros)
    cuadrados = map(lambda x: x ** 2, pares)
    return sum(cuadrados)


def producto_mayores_que_3_funcional(numeros: list) -> int:
    """Producto de los mayores que 3, con filter + reduce.
    :param numeros: lista de números
    :return: producto de los mayores que 3
    """
    mayores = filter(lambda x: x > 3, numeros)
    return reduce(lambda a, b: a * b, mayores, 1)  # 1 es el neutro del producto


# ---- Versión con bucle (Tema 4) --------------------------------------

def suma_cuadrados_pares_bucle(numeros: list) -> int:
    """Con bucle explícito (compara con la funcional).
    :param numeros: lista de números
    :return: suma de los cuadrados de los pares
    """
    suma = 0
    for x in numeros:
        if x % 2 == 0:
            suma = suma + x ** 2
    return suma


def producto_mayores_que_3_bucle(numeros: list) -> int:
    """Con bucle explícito.
    :param numeros: lista de números
    :return: producto de los mayores que 3
    """
    prod = 1
    for x in numeros:
        if x > 3:
            prod = prod * x
    return prod


# ---- Programa principal ---------------------------------------------

def main():
    numeros = [1, 2, 3, 4, 5, 6, 7]

    print(f"Números: {numeros}")

    r1_f = suma_cuadrados_pares_funcional(numeros)
    r1_b = suma_cuadrados_pares_bucle(numeros)
    print(f"\n1) Suma de cuadrados de los pares:")
    print(f"   Funcional: {r1_f}")
    print(f"   Bucle:     {r1_b}")
    print(f"   (2² + 4² + 6² = 4 + 16 + 36 = 56)")

    r2_f = producto_mayores_que_3_funcional(numeros)
    r2_b = producto_mayores_que_3_bucle(numeros)
    print(f"\n2) Producto de los mayores que 3:")
    print(f"   Funcional: {r2_f}")
    print(f"   Bucle:     {r2_b}")
    print(f"   (4 · 5 · 6 · 7 = 840)")


if __name__ == "__main__":
    main()
