
# Solicitamos el radio al usuario y los convertimos a número decimal (float)
radio = float(input("Introduce el radio del círculo: "))

# Calculamos el área (pi * radio al cuadrado)
area = 3.141592653589793 * (radio ** 2)

# Mostramos el resultado redondeado a dos decimales
print(f"El área del círculo con radio {radio} es: {round(area, 2)}")
