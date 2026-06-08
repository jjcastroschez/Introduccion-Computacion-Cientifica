"""
Ejercicio 6 — Algoritmo de Euclides RECURSIVO.

En el Tema 4 implementamos el algoritmo de Euclides con un bucle while.
Aquí lo refactorizamos en una función recursiva, aprovechando que la
propia identidad de Euclides es recursiva:

    mcd(a, b) = a              si b == 0   (caso base)
    mcd(a, b) = mcd(b, a % b)  si b != 0   (caso recursivo)

Tema 5 - Introducción a la Computación Científica (ICC).
"""


def mcd_recursivo(a: int, b: int) -> int:
    """
    Máximo Común Divisor por recursión, usando la identidad de Euclides.
    
    :param a: Primer número entero no negativo.
    :param b: Segundo número entero no negativo.
    :return: El máximo común divisor de a y b (entero no negativo).
    :requisitos: a, b enteros no negativos, no ambos cero.
    """
    if b == 0:
        return a
    return mcd_recursivo(b, a % b)


def mcd_iterativo(a: int, b: int) -> int:
    """Versión iterativa para comparar (la del Tema 4).
    
    :param a: Primer número entero no negativo.
    :param b: Segundo número entero no negativo.
    :return: El máximo común divisor de a y b (entero no negativo). 
    """
    
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


def comparar(a: int, b: int) -> None:
    """Imprime una línea comparando recursivo vs iterativo para (a, b).
    
    :param a: Primer número entero no negativo.
    :param b: Segundo número entero no negativo.
    :return: None.
    """
    r = mcd_recursivo(a, b)
    i = mcd_iterativo(a, b)
    marca = "✅" if r == i else "❌"
    print(f"{a:>5} {b:>5} {r:>14} {i:>14}  {marca}")


def main():
    print(f"{'a':>5} {'b':>5} {'mcd recursivo':>14} {'mcd iterativo':>14}")
    comparar(48, 18)
    comparar(1071, 462)
    comparar(100, 75)
    comparar(7, 5)
    comparar(12, 8)


if __name__ == "__main__":
    main()
