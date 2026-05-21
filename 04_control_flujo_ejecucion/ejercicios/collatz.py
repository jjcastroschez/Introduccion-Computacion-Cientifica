"""
Ejercicio 6 — Conjetura de Collatz para un número.

Dado un entero positivo n, aplica la sucesión:
    si n es par:    n -> n/2
    si n es impar:  n -> 3n+1
hasta llegar a 1. Cuenta el número de pasos y, opcionalmente, muestra
la sucesión por pantalla.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

while True:
    try:
        n = int(input("Entero positivo: "))
        if n <= 0:
            print("⚠️ Debe ser positivo.")
            continue
        break
    except ValueError:
        print("⚠️ Eso no es un entero válido.")

n_original = n
pasos = 0

print(f"Sucesión partiendo de {n}: ", end="")
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    pasos = pasos + 1
    print(f" → {n}", end="")

print(f"\n\nPartiendo de {n_original}, llegamos a 1 en {pasos} pasos.")
