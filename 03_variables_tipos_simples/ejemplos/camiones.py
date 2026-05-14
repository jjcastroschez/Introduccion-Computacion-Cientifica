capacidad_mg=int(input("Dame la capacidad del vehículo más grande: "))
capacidad_mp=int(input("Dame la capacidad del vehículo más pequeño: "))
carga=int(input("Dame la carga que quieres distribuir: "))
inverso_cp_mp=int(input(f"Dame el inverso módulo {capacidad_mp} de {capacidad_mg}: "))

# Calculamos el número de vehículos grandes (x) usando la fórmula del inverso
num_vehiculos_g = (carga * inverso_cp_mp) % capacidad_mp

# Calculamos el número de vehículos pequeños (y) despejando la ecuación original: y = (c - ax) / b
num_vehiculos_p = (carga - capacidad_mg * num_vehiculos_g) // capacidad_mp

print(f"Se necesitan: Vehículos de capacidad {capacidad_mg} = {num_vehiculos_g}, Vehículos de capacidad {capacidad_mp} = {num_vehiculos_p}")
