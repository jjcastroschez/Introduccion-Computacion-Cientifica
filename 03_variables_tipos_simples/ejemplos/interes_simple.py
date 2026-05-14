#Entrada datos
capital_inicial = float(input("Capital inicial: "))
porcentaje_interes_anual = float(input("Tasa de interés anual (%): "))
tiempo = int(input("Tiempo en años: "))

# Cálculos
interes_anual = porcentaje_interes_anual / 100
interes_simple = capital_inicial * interes_anual * tiempo
monto_final= capital_inicial+ interes_simple

# Resultados
print(f" \nInterés simple: {interes_simple:.2f}")
print(f"Monto total: {monto_final:.2f}")
