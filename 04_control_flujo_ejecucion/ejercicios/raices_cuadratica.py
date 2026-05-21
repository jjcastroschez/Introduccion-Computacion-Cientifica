"""
Ejercicio 1 — Clasificación de raíces de ax^2 + bx + c = 0.

Según el signo del discriminante (D = b^2 - 4ac) se distingue entre:
  - D > 0: dos raíces reales distintas
  - D = 0: una raíz real doble
  - D < 0: raíces complejas conjugadas

Trata también el caso degenerado a = 0 (ecuación lineal).

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinitas soluciones (0 = 0).")
        else:
            print("Sin solución (la ecuación no se cumple para ningún x).")
    else:
        print(f"Ecuación lineal. Raíz única: x = {-c / b}")
else:
    discriminante = b ** 2 - 4 * a * c
    if discriminante > 0:
        sqrt_d = math.sqrt(discriminante)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        print(f"Dos raíces reales distintas: x1 = {x1}, x2 = {x2}")
    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"Raíz real doble: x = {x}")
    else:
        parte_real = -b / (2 * a)
        parte_imag = math.sqrt(-discriminante) / (2 * a)
        print(f"Raíces complejas conjugadas: {parte_real} ± {parte_imag}i")
