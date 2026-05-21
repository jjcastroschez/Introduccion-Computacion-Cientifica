"""
Acumulación de fármacos — versión iterativa.

Simula día a día la concentración de un fármaco en el cuerpo de un
paciente, aplicando la recurrencia:
    cantidad(dia) = cantidad(dia-1) * r + dosis
donde r = 1 - porcentaje_eliminado / 100.

A diferencia del Tema 3, no usamos la fórmula cerrada de la serie
geométrica, sino que simulamos el proceso día a día con un bucle.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

dosis = float(input("Dosis diaria (mg): "))
porcentaje_elim = float(input("Porcentaje eliminado cada día (0-100): "))
dias = int(input("Días que queremos simular: "))

r = 1 - porcentaje_elim / 100
cantidad = 0

for dia in range(1, dias + 1):
    cantidad = cantidad * r + dosis
    print(f"Día {dia:3}: {cantidad:.4f} mg en el cuerpo")

print(f"\nValor límite teórico (serie geométrica): {dosis / (1 - r):.4f} mg")
