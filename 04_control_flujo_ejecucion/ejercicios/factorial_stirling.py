"""
Ejercicio 4 — Factorial y verificación de la fórmula de Stirling.

Calcula n! con un bucle for, y compara el resultado con la
aproximación de Stirling:
    n! ≈ sqrt(2*pi*n) * (n/e)^n

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math

n = int(input("Calcular n! para n = "))

# Cálculo exacto con bucle for
factorial = 1
for i in range(2, n + 1):
    factorial = factorial * i

# Aproximación de Stirling
stirling = math.sqrt(2 * math.pi * n) * (n / math.e) ** n

# Error relativo (en %)
error_relativo = abs(factorial - stirling) / factorial * 100

print(f"\n{n}! exacto:               {factorial}")
print(f"Aproximación de Stirling: {stirling:.4e}")
print(f"Error relativo:           {error_relativo:.4f} %")
