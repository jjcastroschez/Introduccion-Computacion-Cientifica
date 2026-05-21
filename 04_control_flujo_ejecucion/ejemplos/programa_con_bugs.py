"""
Programa con un bug deliberado para practicar depuración.

Se supone que calcula la suma de los N primeros números pares
(2 + 4 + 6 + ... + 2N), pero da un resultado incorrecto.

Para depurar con pdb desde la terminal:
    python programa_con_bugs.py
La línea con breakpoint() detendrá la ejecución.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

n = 5      # esperamos: 2+4+6+8+10 = 30

suma = 0
i = 0
while i < n:
    breakpoint()         # ← inicia el depurador en cada vuelta
    i = i + 1
    suma = suma + 2 * i
    i = i + 1            # 🐛 BUG: incremento de más

print(f"Suma de los {n} primeros pares: {suma}")
print("Esperado: 30")
