"""
Algoritmo de Euclides para el cálculo del MCD de dos enteros positivos.

Tema 4 - Introducción a la Computación Científica (ICC).
"""
entrada_valida = False
while not entrada_valida:
    try:
        a = int(input("Primer entero positivo: "))
        b = int(input("Segundo entero positivo: "))
    except ValueError:
        print("⚠️ Tienes que introducir un número entero.")
    else:
        if a > 0 and b > 0:
            entrada_valida = True
            if a < b:
                a, b = b, a  # Intercambiamos para asegurar que a es el mayor

a_original = a
b_original = b

while b != 0:
    resto = a % b
    a = b
    b = resto

print(f"MCD({a_original}, {b_original}) = {a}")
