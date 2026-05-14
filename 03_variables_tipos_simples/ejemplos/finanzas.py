pago_anual = 100  # La cantidad 'a'
tasa_interes = 0.05  # 5% de interés anual

print(f"Pago anual prometido: {pago_anual}€")
print(f"Tasa de interés (descuento): {tasa_interes * 100}%")

valor_perpetuidad = pago_anual / tasa_interes

print(f"Para una tasa del {tasa_interes*100:.1f}%, recibiendo {pago_anual}€ anuales, el valor a perpetuidad es: {valor_perpetuidad:.2f}€")


print(f"Valor hoy del pago del año 5: {(pago_anual/ (1+tasa_interes)**5):.2f}€")
print(f"Valor hoy del pago del año 10: {(pago_anual/ (1+tasa_interes)**10):.2f}€")
print(f"Valor hoy del pago del año 25: {(pago_anual/ (1+tasa_interes)**25):.2f}€")
print(f"Valor hoy del pago del año 50: {(pago_anual/ (1+tasa_interes)**50):.2f}€")
print(f"Valor hoy del pago del año 100: {(pago_anual/ (1+tasa_interes)**100):.2f}€")


k = int(input("Introduce el año k para ver el acumulado: "))

valor_futuro = (pago_anual * ((1 + tasa_interes)**k - 1)) / tasa_interes

print(f"--- CAPITAL ACUMULADO ---")
print(f"En el año {k}, con un pago de {pago_anual}€ al {tasa_interes*100}%, tendrás:")
print(f"{valor_futuro:.2f}€")