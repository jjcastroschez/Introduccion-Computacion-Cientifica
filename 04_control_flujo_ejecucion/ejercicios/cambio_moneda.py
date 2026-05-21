"""
Ejercicio 9 — Validación robusta del cálculo de cambio de moneda.

Revisita el ejercicio del Tema 3 añadiendo:
  - Validación de cada entrada con try-except (debe ser un número
    real positivo, o un porcentaje en [0, 100]).
  - Mensaje claro al usuario si la entrada no es válida y nueva
    petición sin que el programa se rompa.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

# --- Conversión de la moneda extranjera a dólares ---
while True:
    try:
        conv_moneda_dolares = float(input(
            "Valor de conversión de la moneda extranjera a dólares: "
        ))
        if conv_moneda_dolares <= 0:
            print("  ⚠️ Debe ser un valor positivo.")
            continue
        break
    except ValueError:
        print("  ⚠️ Debe ser un número.")

# --- Conversión del euro a dólares ---
while True:
    try:
        conv_euros_dolares = float(input("Valor de conversión del euro a dólares: "))
        if conv_euros_dolares <= 0:
            print("  ⚠️ Debe ser un valor positivo.")
            continue
        break
    except ValueError:
        print("  ⚠️ Debe ser un número.")

# --- Cantidad de moneda extranjera ---
while True:
    try:
        cantidad_moneda_extranj = int(input("Cantidad de moneda extranjera a cambiar: "))
        if cantidad_moneda_extranj <= 0:
            print("  ⚠️ Debe ser un entero positivo.")
            continue
        break
    except ValueError:
        print("  ⚠️ Debe ser un entero.")

# --- Porcentaje de ganancia del banco ---
while True:
    try:
        porc_ganancia_banco = float(input("Porcentaje de ganancia del banco (0-100): "))
        if porc_ganancia_banco < 0 or porc_ganancia_banco > 100:
            print("  ⚠️ Debe estar entre 0 y 100.")
            continue
        break
    except ValueError:
        print("  ⚠️ Debe ser un número.")

# --- Cálculos (igual que en el Tema 3) ---
cantidad_en_dolares = cantidad_moneda_extranj * conv_moneda_dolares
cantidad_en_euros = cantidad_en_dolares / conv_euros_dolares
cantidad_por_comision = cantidad_en_euros * porc_ganancia_banco / 100
cantidad_cambio_entrega = cantidad_en_euros - cantidad_por_comision

print(f"\nLa cantidad a entregar al cliente es: {cantidad_cambio_entrega:.2f} €")
