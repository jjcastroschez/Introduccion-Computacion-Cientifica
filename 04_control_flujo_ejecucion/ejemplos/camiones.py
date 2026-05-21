"""
Logística y gestión de inventario: reparto de carga en camiones.

Versión mejorada del Tema 4 con respecto al Tema 3:
  - Verifica automáticamente la identidad de Bézout (mcd(a,b) divide r)
    con un bucle while (algoritmo de Euclides).
  - Calcula automáticamente el inverso modular con un bucle for
    (el usuario ya NO tiene que hacerlo a mano).
  - Comprueba que las soluciones (x, y) sean números naturales (>= 0).
  - Valida toda la entrada del usuario con try-except y while.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

# -----------------------------------------------------------------
# 1) Lectura validada de los datos del problema
# -----------------------------------------------------------------
entrada_valida = False
while not entrada_valida:
    try:
        capacidad_mg = int(input("Dame la capacidad del vehículo más grande: "))
    except ValueError:
        print("  ⚠️ Tienes que introducir un número entero.")
    else:
        if capacidad_mg <= 0:
            print("  ⚠️ La capacidad debe ser un entero positivo.")
        else:
            entrada_valida = True

entrada_valida = False
while not entrada_valida:
    try:
        capacidad_mp = int(input("Dame la capacidad del vehículo más pequeño: "))
    except ValueError:
        print("  ⚠️ Tienes que introducir un número entero.")
    else:
        if capacidad_mp <= 0 or capacidad_mp >= capacidad_mg:
            print("  ⚠️ La capacidad debe ser un entero positivo y estrictamente menor que la del vehículo grande.")
        else:
            entrada_valida = True

entrada_valida = False
while not entrada_valida:
    try:
        carga = int(input("Dame la carga que quieres distribuir: "))
    except ValueError:
        print("  ⚠️ Tienes que introducir un número entero.")
    else:
        if carga <= 0:
            print("  ⚠️ La carga debe ser un entero positivo.")
        else:      
            entrada_valida = True   

# -----------------------------------------------------------------
# 2) Verificar la identidad de Bézout: mcd(a, b) debe dividir a r
#    Calculamos mcd(capacidad_mg, capacidad_mp) por Euclides
# -----------------------------------------------------------------

a = capacidad_mg
b = capacidad_mp
while b != 0:
    resto = a % b
    a = b
    b = resto
mcd = a   # tras el bucle de Euclides, mcd está en a

print(f"\nmcd({capacidad_mg}, {capacidad_mp}) = {mcd}")

if carga % mcd != 0:
    print(f"❌ La identidad de Bézout NO se cumple: {mcd} no divide a {carga}.")
    print(f"   No existen soluciones enteras para repartir la carga.")
else:
    print(f"✅ La identidad de Bézout se cumple: {mcd} divide a {carga}.")

    # -----------------------------------------------------------------
    # 3) Calcular el inverso modular de capacidad_mg módulo capacidad_mp
    #    Buscamos k en [1, capacidad_mp - 1] tal que
    #    (capacidad_mg * k) mod capacidad_mp == 1
    # -----------------------------------------------------------------
    inverso = 0
    for k in range(1, capacidad_mp):
        if (capacidad_mg * k) % capacidad_mp == 1:
            inverso = k
            break

    if inverso == 0:
        print(f"❌ No existe inverso de {capacidad_mg} módulo {capacidad_mp}.")
    else:
        print(f"Inverso de {capacidad_mg} módulo {capacidad_mp} = {inverso}")

        # -----------------------------------------------------------------
        # 4) Calcular las soluciones x e y, igual que en el Tema 3
        # -----------------------------------------------------------------
        num_vehiculos_g = (carga * inverso) % capacidad_mp
        num_vehiculos_p = (carga - capacidad_mg * num_vehiculos_g) // capacidad_mp

        # -----------------------------------------------------------------
        # 5) Comprobar que las dos soluciones son números NATURALES
        # -----------------------------------------------------------------
        if num_vehiculos_g >= 0 and num_vehiculos_p >= 0:
            print(
                f"\n✅ Solución encontrada:\n"
                f"   {num_vehiculos_g} vehículos de capacidad {capacidad_mg}\n"
                f"   {num_vehiculos_p} vehículos de capacidad {capacidad_mp}\n"
                f"   Total transportado: "
                f"{num_vehiculos_g * capacidad_mg + num_vehiculos_p * capacidad_mp} "
                f"(debe coincidir con la carga {carga})."
            )
        else:
            print(
                f"\n⚠️ La ecuación tiene solución entera, pero NO con números"
                f" naturales: x = {num_vehiculos_g}, y = {num_vehiculos_p}."
            )
            print(
                "   No se puede repartir la carga con estos vehículos sin "
                "dejar mercancía en tierra o desperdiciar espacio."
            )