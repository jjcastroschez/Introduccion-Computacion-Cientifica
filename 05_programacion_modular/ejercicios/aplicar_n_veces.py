"""
Ejercicio 9 — Función `aplicar_n_veces`.

Función de orden superior: recibe otra función f y un valor x y aplica
f a x un número dado de veces.

Generalización natural de aplicar_dos_veces visto en clase:
    aplicar_n_veces(f, x, 1) = f(x)
    aplicar_n_veces(f, x, 2) = f(f(x))
    aplicar_n_veces(f, x, n) = f(f(...f(x)...))   (n veces)

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import math


def aplicar_n_veces(f, x: float, n: int) -> float:
    """
    Aplica la función f al valor x un total de n veces.

    :param f: función real de una variable.
    :param x: valor inicial.
    :param n: número de aplicaciones (n >= 0).
    :return: el resultado de aplicar f a x, n veces.
    """
    resultado = x
    for _ in range(n):
        resultado = f(resultado)
    return resultado


def cuadrado(x: float) -> float:
    return x * x


def sumar_uno(x: float) -> float:
    return x + 1


def main():
    # Casos simples
    print(f"cuadrado aplicado 3 veces a 2: {aplicar_n_veces(cuadrado, 2, 3)}")
    print(f"  (2² = 4; 4² = 16; 16² = 256)")

    print(f"\nsumar_uno aplicado 10 veces a 0: {aplicar_n_veces(sumar_uno, 0, 10)}")

    # Una aplicación matemática preciosa:
    # Iterar coseno desde 0 converge al punto fijo de cos(x) = x
    # (aprox. 0.7390851332151607)
    print(f"\nIterar cos(x) desde x=0:")
    for n in (5, 10, 50, 100):
        valor = aplicar_n_veces(math.cos, 0, n)
        print(f"  tras {n:3d} iteraciones: {valor:.15f}")

    print(f"\n  (El punto fijo verdadero de cos es ≈ 0.7390851332151607)")


if __name__ == "__main__":
    main()
