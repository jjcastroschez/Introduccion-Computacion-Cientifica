"""
Ejercicio 2 — Cálculo de la nota final con clasificación.

Revisita un ejercicio del Tema 3 ampliándolo con la clasificación del
estudiante en suspenso, aprobado, notable, sobresaliente o matrícula
de honor según los criterios académicos estándar.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

calif1 = float(input("Calificación de la primera prueba (sobre 10): "))
calif2 = float(input("Calificación de la segunda prueba (sobre 10): "))
calif3 = float(input("Calificación de la tercera prueba (sobre 10): "))

# Cálculo de la nota como media ponderada de las tres pruebas
# (pesos: 30%, 40% y 30%)
nota = calif1 * 0.30 + calif2 * 0.40 + calif3 * 0.30

print(f"\nNota obtenida: {nota:.2f}")

# La novedad del Tema 4: clasificación con if-elif-else
if nota < 5:
    clasificacion = "Suspenso"
elif nota < 7:
    clasificacion = "Aprobado"
elif nota < 9:
    clasificacion = "Notable"
elif nota < 9.5:
    clasificacion = "Sobresaliente"
else:
    clasificacion = "Matrícula de honor"

print(f"Clasificación: {clasificacion}")
