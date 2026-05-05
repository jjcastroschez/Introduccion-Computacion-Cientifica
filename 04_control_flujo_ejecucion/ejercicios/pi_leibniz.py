"""
Ejercicio 2.2 — Aproximación de π por la serie de Leibniz.

    π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...

Esta serie converge muy lentamente y es un buen ejemplo para ilustrar
las limitaciones de un método de aproximación.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math


def pi_leibniz(n_terminos: int) -> float:
    """Aproxima π usando los primeros n términos de la serie de Leibniz."""
    suma = 0.0
    for k in range(n_terminos):
        suma += ((-1) ** k) / (2 * k + 1)
    return suma * 4


def main():
    n = int(input("Número de términos: "))
    aprox = pi_leibniz(n)
    error = abs(aprox - math.pi)

    print(f"π aproximado con {n} términos: {aprox:.10f}")
    print(f"π real:                       {math.pi:.10f}")
    print(f"Error absoluto:               {error:.2e}")


if __name__ == "__main__":
    main()
