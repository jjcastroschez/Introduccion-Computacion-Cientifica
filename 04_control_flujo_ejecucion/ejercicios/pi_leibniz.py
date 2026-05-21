"""
Ejercicio 3 — Aproximación de pi por la serie de Leibniz.

    pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...

Acumulamos N términos en una variable simple y multiplicamos por 4 al
final. Es un buen ejemplo de uso de bucle for + signo alternante.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math

n = int(input("Número de términos a sumar: "))

suma = 0.0
signo = 1   # alternará +1, -1, +1, -1...
for k in range(n):
    denominador = 2 * k + 1
    suma = suma + signo / denominador
    signo = -signo

pi_aprox = suma * 4
error = abs(pi_aprox - math.pi)

print(f"\nπ aproximado con {n} términos: {pi_aprox:.10f}")
print(f"π real:                       {math.pi:.10f}")
print(f"Error absoluto:               {error:.2e}")
