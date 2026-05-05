"""
Ejercicio 5.3 — Integración numérica por la regla del trapecio.

Implementa la regla del trapecio compuesta y la verifica con dos
integrales de prueba:
  - ∫₀¹ x² dx = 1/3
  - ∫₀^π sin(x) dx = 2

Comprueba empíricamente la convergencia O(h²): al duplicar n el error
se divide por 4.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math


def trapecio(f, a: float, b: float, n: int) -> float:
    """Integral aproximada de f en [a, b] por la regla del trapecio compuesta."""
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
    for i in range(1, n):
        suma += f(a + i * h)
    return suma * h


def main():
    print("∫₀¹ x² dx (exacta = 0.333333...)")
    for n in [10, 100, 1000, 10000]:
        aprox = trapecio(lambda x: x**2, 0, 1, n)
        error = abs(aprox - 1/3)
        print(f"  n={n:5d}: aprox = {aprox:.10f}, error = {error:.2e}")

    print("\n∫₀^π sin(x) dx (exacta = 2.0)")
    for n in [10, 100, 1000, 10000]:
        aprox = trapecio(math.sin, 0, math.pi, n)
        error = abs(aprox - 2)
        print(f"  n={n:5d}: aprox = {aprox:.10f}, error = {error:.2e}")


if __name__ == "__main__":
    main()
