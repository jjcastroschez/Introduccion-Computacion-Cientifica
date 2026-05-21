"""
Versión corregida de programa_con_bugs.py.

⚠️ No mires este archivo hasta haber intentado encontrar y arreglar
el bug tú mismo. Depurar es lo que se aprende.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

n = 5

suma = 0
i = 0
while i < n:
    i = i + 1
    suma = suma + 2 * i   # ✅ ya solo incrementamos una vez

print(f"Suma de los {n} primeros pares: {suma}")
print("Esperado: 30")
