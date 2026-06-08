"""
Recursividad: factorial y Fibonacci.

Comparamos la versión RECURSIVA con la ITERATIVA (que ya sabemos hacer
desde el Tema 4) para ver qué aporta y qué cuesta cada enfoque.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import time


# ---------------------------------------------------------------------
# Factorial: dos versiones equivalentes
# ---------------------------------------------------------------------

def factorial_iterativo(n: int) -> int:
    """Versión clásica del Tema 4: bucle for con acumulador."""
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado


def factorial_recursivo(n: int) -> int:
    """
    Versión recursiva:
      - Caso base:    factorial(0) = factorial(1) = 1
      - Caso recursivo: factorial(n) = n * factorial(n-1)
    """
    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)


# ---------------------------------------------------------------------
# Fibonacci: dos versiones, pero ¡con un final muy distinto!
# ---------------------------------------------------------------------

def fibonacci_iterativo(n: int) -> int:
    """Versión del Tema 4: dos variables que se van actualizando."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursivo(n: int) -> int:
    """
    Versión recursiva "natural":
      - Caso base:    fib(0) = 0, fib(1) = 1
      - Caso recursivo: fib(n) = fib(n-1) + fib(n-2)

    ⚠️ Esta versión es elegante pero TERRIBLEMENTE ineficiente:
    para fib(40) hace más de 200 millones de llamadas.
    """
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# ---------------------------------------------------------------------
# Programa de demostración: comparamos los tiempos
# ---------------------------------------------------------------------

def main():
    n = 10
    print(f"Factorial de {n}:")
    print(f"  Iterativo:  {factorial_iterativo(n)}")
    print(f"  Recursivo:  {factorial_recursivo(n)}")
    print("  → Para el factorial ambos son igual de eficientes.\n")

    print(f"Fibonacci de {n}:")
    t0 = time.time()
    iter_res = fibonacci_iterativo(n)
    t_iter = time.time() - t0

    t0 = time.time()
    rec_res = fibonacci_recursivo(n)
    t_rec = time.time() - t0

    print(f"  Iterativo: {iter_res} ({t_iter*1e6:.1f} μs)")
    print(f"  Recursivo: {rec_res} ({t_rec*1e6:.1f} μs)")

    print(f"\n¡Ojo! con n=35, la recursiva tarda SEGUNDOS:")
    n = 35
    t0 = time.time()
    res = fibonacci_recursivo(n)
    t_rec = time.time() - t0
    print(f"  fibonacci_recursivo({n}) = {res} ({t_rec:.3f} s)")
    t0 = time.time()
    res = fibonacci_iterativo(n)
    t_iter = time.time() - t0
    print(f"  fibonacci_iterativo({n}) = {res} ({t_iter*1e6:.1f} μs)")


if __name__ == "__main__":
    main()
