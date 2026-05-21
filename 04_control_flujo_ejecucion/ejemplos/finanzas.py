"""
Valor presente de una anualidad finita.

Calcula el valor presente de recibir un pago anual constante durante n
años, descontado a una tasa de interés:
    VP = sum_{t=1..n} pago / (1+i)^t

Tema 4 - Introducción a la Computación Científica (ICC).
"""

pago_anual = float(input("Pago anual (€): "))
tasa_interes = float(input("Tasa de interés anual (en %): "))
anios = int(input("Años de la anualidad: "))

i = tasa_interes / 100
valor_presente = 0

for t in range(1, anios + 1):
    valor_presente = valor_presente + pago_anual / ((1 + i) ** t)

print(f"\nValor presente de la anualidad de {anios} años: {valor_presente:.2f} €")
print(f"Valor de la renta perpetua (Tema 3): {pago_anual / i:.2f} €")
