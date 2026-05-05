"""
Detección de olas de calor en una serie de temperaturas máximas diarias.

Una ola de calor se define como un periodo de al menos DIAS_MIN días
consecutivos con la temperatura máxima por encima del UMBRAL.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

UMBRAL = 36       # ºC
DIAS_MIN = 3      # Días consecutivos necesarios para una ola


def detectar_olas(temperaturas: list[float]) -> tuple[int, int]:
    """
    Cuenta las olas de calor en una lista de temperaturas.

    Devuelve (numero_de_olas, dias_totales_en_olas).
    """
    olas = 0
    dias_olas = 0
    racha = 0

    for t in temperaturas:
        if t > UMBRAL:
            racha += 1
            if racha == DIAS_MIN:
                olas += 1
                dias_olas += DIAS_MIN
            elif racha > DIAS_MIN:
                dias_olas += 1
        else:
            racha = 0

    return olas, dias_olas


def main():
    # Datos de ejemplo: temperaturas máximas de Ciudad Real (mes ficticio)
    temperaturas = [28, 31, 33, 35, 37, 38, 36, 34, 32, 30, 29, 31, 36, 38, 39, 41, 40, 37, 35, 33, 31, 29, 30, 32, 34, 36, 37, 38, 39, 36]

    olas, dias = detectar_olas(temperaturas)

    print(f"Periodo analizado: {len(temperaturas)} días")
    print(f"Olas de calor detectadas: {olas}")
    print(f"Días dentro de olas: {dias}")


if __name__ == "__main__":
    main()
