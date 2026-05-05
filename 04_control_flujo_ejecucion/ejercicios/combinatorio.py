"""
Ejercicio 2.3 — Factorial y número combinatorio.

Implementa C(n, k) de dos maneras:
  1. Usando factoriales (educativa).
  2. Versión estable que evita calcular factoriales gigantes.

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def factorial(n: int) -> int:
    """Devuelve n!"""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def combinatorio(n: int, k: int) -> int:
    """C(n, k) usando factoriales."""
    return factorial(n) // (factorial(k) * factorial(n - k))


def combinatorio_estable(n: int, k: int) -> int:
    """
    C(n, k) sin calcular factoriales completos.
    Va dividiendo en cada paso, manteniendo los números pequeños.
    """
    resultado = 1
    for i in range(1, k + 1):
        resultado = resultado * (n - i + 1) // i
    return resultado


def main():
    n = int(input("n: "))
    k = int(input("k: "))

    if k < 0 or k > n:
        print("⚠️ Debe cumplirse 0 ≤ k ≤ n.")
        return

    print(f"C({n}, {k}) = {combinatorio(n, k)}")
    print(f"C({n}, {k}) = {combinatorio_estable(n, k)}  (versión estable)")


if __name__ == "__main__":
    main()
