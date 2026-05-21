"""
Ejercicio 5 — Raíz cuadrada por el método babilónico.

Recurrencia:
    x_{n+1} = 0.5 * (x_n + a / x_n)

Iteramos con un bucle while hasta que la diferencia entre dos
estimaciones consecutivas sea menor que una tolerancia, con red de
seguridad contra bucles infinitos.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math

a = float(input("Calcular la raíz cuadrada de: "))

if a < 0:
    print("⚠️ No existe raíz real de un número negativo.")
elif a == 0:
    print("√0 = 0")
else:
    TOLERANCIA = 1e-12
    MAX_ITER = 100

    x = a / 2          # estimación inicial
    iteracion = 0
    diferencia = TOLERANCIA + 1   # para entrar al bucle al menos una vez

    while diferencia > TOLERANCIA and iteracion < MAX_ITER:
        x_nuevo = 0.5 * (x + a / x)
        diferencia = abs(x_nuevo - x)
        x = x_nuevo
        iteracion = iteracion + 1

    print(f"\n√{a} ≈ {x:.15f}")
    print(f"Resultado de math.sqrt:  {math.sqrt(a):.15f}")
    print(f"Iteraciones empleadas: {iteracion}")
