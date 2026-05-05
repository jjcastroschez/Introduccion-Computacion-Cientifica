"""
Ejercicio 3.1 — Algoritmo de Euclides para el MCD.

Calcula el máximo común divisor (MCD) de dos enteros positivos por el
método de Euclides, y como bonus también calcula el mínimo común
múltiplo (MCM).

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def mcd(a: int, b: int) -> int:
    """Devuelve el máximo común divisor de a y b por el algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a


def mcm(a: int, b: int) -> int:
    """Devuelve el mínimo común múltiplo de a y b."""
    return abs(a * b) // mcd(a, b)


def main():
    a = int(input("a: "))
    b = int(input("b: "))

    print(f"MCD({a}, {b}) = {mcd(a, b)}")
    print(f"MCM({a}, {b}) = {mcm(a, b)}")


if __name__ == "__main__":
    main()
