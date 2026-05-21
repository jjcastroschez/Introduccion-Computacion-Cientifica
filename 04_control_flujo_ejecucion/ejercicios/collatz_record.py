"""
Ejercicio 7 — Récord de Collatz en [1, N].

Encuentra cuál es el entero entre 1 y N que tarda más pasos en llegar
a 1 según la conjetura de Collatz. Combina dos bucles anidados (uno
externo for, uno interno while) sin usar listas.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

n_max = int(input("Buscar el récord entre 1 y N. Introduce N: "))

# Variables simples para guardar el mejor (sin usar listas)
mejor_numero = 1
max_pasos = 0

for inicio in range(1, n_max + 1):
    # Bucle interno: aplicamos Collatz al número 'inicio'
    n = inicio
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos = pasos + 1

    # ¿Es este el nuevo récord?
    if pasos > max_pasos:
        max_pasos = pasos
        mejor_numero = inicio

print(f"\nDel 1 al {n_max}, el número con más pasos es {mejor_numero} "
      f"({max_pasos} pasos).")
