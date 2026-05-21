calif1 = float(input("Calificación de la primera prueba (sobre 10): "))
calif2 = float(input("Calificación de la segunda prueba (sobre 10): "))
calif3 = float(input("Calificación de la tercera prueba (sobre 10): "))

nota = calif1 * 0.30 + calif2 * 0.40 + calif3 * 0.30

print(f"Nota obtenida: {nota:.2f}")

match nota:
    case _ if nota < 5:
        clasificacion = "Suspenso"
    case _ if nota < 7:
        clasificacion = "Aprobado"
    case _ if nota < 9:
        clasificacion = "Notable"
    case _ if nota < 9.5:
        clasificacion = "Sobresaliente"
    case _:
        clasificacion = "Matrícula de honor"

print(f"Clasificación: {clasificacion}")
