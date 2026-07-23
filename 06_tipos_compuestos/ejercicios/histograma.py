"""
Ejercicio 4 — Histograma de notas por franja.

Dada una lista de calificaciones (entre 0 y 10), clasifica cuántas
caen en cada franja del sistema español:
    Suspenso   [0, 5)
    Aprobado   [5, 7)
    Notable    [7, 9)
    Sobresal.  [9, 10]

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def histograma(notas: list) -> dict:
    """
    Devuelve un diccionario {franja: cuántas notas cayeron ahí}.
    :param notas: lista de calificaciones (float)
    :return resultado: diccionario con el histograma (dict)
    """
    resultado = {
        "Suspenso":     0,
        "Aprobado":     0,
        "Notable":      0,
        "Sobresaliente": 0,
    }
    for nota in notas:
        if nota < 5:
            resultado["Suspenso"] = resultado["Suspenso"] + 1
        elif nota < 7:
            resultado["Aprobado"] = resultado["Aprobado"] + 1
        elif nota < 9:
            resultado["Notable"] = resultado["Notable"] + 1
        else:
            resultado["Sobresaliente"] = resultado["Sobresaliente"] + 1
    return resultado


def mostrar_histograma(h: dict) -> None:
    """Imprime el histograma en formato de barras con estrellas.
    :param h: diccionario con el histograma (dict)
    """
    print("\nHistograma de calificaciones:")
    for franja, cuantas in h.items():
        barra = "★" * cuantas
        print(f"  {franja:14} {cuantas:3d}  {barra}")


def main():
    notas = [4.5, 5.0, 7.8, 9.2, 3.5, 6.0, 8.5, 5.5, 4.0, 9.5, 7.0, 6.5, 10, 2.0, 8.0]

    h = histograma(notas)
    print(f"Notas: {notas}")
    print(f"Total: {len(notas)}")
    mostrar_histograma(h)

    # Verificación: las cuentas deben sumar el total
    total = sum(h.values())
    print(f"\n  Total en histograma: {total} (debe ser {len(notas)})")


if __name__ == "__main__":
    main()
