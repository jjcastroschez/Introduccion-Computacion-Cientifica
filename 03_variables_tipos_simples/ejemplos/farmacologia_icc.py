dosis_diaria = 100  # mg\n
porcentaje_eliminado = 0.20
r = 1 - porcentaje_eliminado  # Fracción que permanece (0.8)
 
print(f"Dosis: {dosis_diaria} mg")
print(f"Factor de permanencia (r): {r}")
 
limite_estacionario = dosis_diaria / (1 - r)

print(f"A largo plazo, el paciente tendrá un nivel estable de: {limite_estacionario} mg")
print(f"Este es el 'Estado Estacionario'.")
 
dia_tratamiento=15
cantidad_en_cuerpo = dosis_diaria * (1-r**dia_tratamiento)/(1-r)
print(f"La cantidad de medicamento el día {dia_tratamiento} es {cantidad_en_cuerpo:.2f} mg")

dia_tratamiento=int(input("Introduce el día de tratamiento: "))
cantidad_en_cuerpo = dosis_diaria * (1-r**dia_tratamiento)/(1-r)
print(f"La cantidad de medicamento el día {dia_tratamiento} es {cantidad_en_cuerpo:.2f} mg")