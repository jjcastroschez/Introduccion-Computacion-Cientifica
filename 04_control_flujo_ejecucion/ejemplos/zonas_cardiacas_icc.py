"""
Zonas de entrenamiento por frecuencia cardíaca.

Clasifica las pulsaciones del usuario en las 5 zonas estándar de
entrenamiento, según el porcentaje de su Frecuencia Cardíaca Máxima
(FCM) calculada con la fórmula de Tanaka et al. (2001):
    FCM = 208 - 0.7 * edad

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def calcular_fcm(edad: int) -> float:
    """Devuelve la frecuencia cardíaca máxima (Tanaka)."""
    return 208 - 0.7 * edad


def clasificar_zona(porcentaje: float) -> str:
    """Devuelve la etiqueta de la zona según el porcentaje de FCM."""
    if porcentaje < 50:
        return "Z0 — Reposo / muy ligero"
    elif porcentaje < 60:
        return "Z1 — Calentamiento"
    elif porcentaje < 70:
        return "Z2 — Quema de grasa"
    elif porcentaje < 80:
        return "Z3 — Aeróbica"
    elif porcentaje < 90:
        return "Z4 — Umbral anaeróbico"
    elif porcentaje <= 100:
        return "Z5 — Máxima"
    else:
        return "⚠️ Por encima de la FCM teórica (revisar medición)"


def main():
    edad = int(input("Edad: "))
    ppm = int(input("Pulsaciones actuales (ppm): "))

    fcm = calcular_fcm(edad)
    porcentaje = (ppm / fcm) * 100
    zona = clasificar_zona(porcentaje)

    print(f"FCM estimada: {fcm:.0f} ppm")
    print(f"Trabajas al {porcentaje:.1f}% de tu FCM")
    print(f"Zona: {zona}")


if __name__ == "__main__":
    main()
