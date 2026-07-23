"""
Estadísticas de una lista de calificaciones.

Introduce las calificaciones de un grupo de estudiantes y calcula
sobre ellas la media, la desviación estándar, el máximo, el mínimo
y cuántos han aprobado (nota >= 5).

Este ejemplo muestra:
  - Recorrido de listas con `for e in lista`
  - Uso de len() para determinar el número de elementos
  - Métodos `.append()` para construir una lista dinámicamente
  - Comprobación con `try-except` para la entrada del usuario
  - Uso de sum(), min(), max()

Tema 6 - Introducción a la Computación Científica (ICC).
"""

import math


def leer_calificaciones() -> list:
    """
    Pide al usuario notas hasta que introduce una cadena vacía.

    Devuelve la lista de notas leídas.
    :return notas: lista de notas (float) entre 0 y 10
    """
    notas = []
    print("Introduce las calificaciones (una por línea).")
    print("Deja la línea en blanco para terminar.")
    entrada = input("Nota: ")
    while entrada!= "":
        try:
            nota = float(entrada)
        except ValueError:
            print(f"  ⚠️ '{entrada}' no es un número. Sigue intentándolo.")
        else:
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print(f"  ⚠️ '{entrada}' no es un número válido. Sigue intentándolo.")
        finally:
            entrada = input("Nota: ")   
    return notas


def media(notas: list) -> float:
    """Media aritmética de la lista de notas.
    :param notas: lista de notas (float)
    :return: media aritmética de las notas
    """
    return sum(notas) / len(notas)


def desviacion_estandar(notas: list) -> float:
    """
    Desviación estándar poblacional:
      σ = sqrt( (1/N) * Σ(xᵢ - μ)² )
    :param notas: lista de notas (float)
    :return: desviación estándar poblacional de las notas
    """
    mu = media(notas)
    suma_cuadrados = 0
    for x in notas:
        suma_cuadrados = suma_cuadrados + (x - mu) ** 2
    return math.sqrt(suma_cuadrados / len(notas))


def contar_aprobados(notas: list, corte: float = 5.0) -> int:
    """Cuenta cuántas notas son >= corte.
    :param notas: lista de notas (float)
    :param corte: nota mínima para aprobar (float)
    :return aprobados: número de notas >= corte
    """
    aprobados = 0
    for nota in notas:
        if nota >= corte:
            aprobados = aprobados + 1
    return aprobados


def main():
    notas = leer_calificaciones()

    if len(notas) == 0:
        print("No introdujiste ninguna nota. Terminando.")
        return

    print(f"\nResumen del grupo ({len(notas)} estudiantes)")
    print(f"  Media:     {media(notas):.2f}")
    print(f"  Desv. est: {desviacion_estandar(notas):.2f}")
    print(f"  Mínimo:    {min(notas):.2f}")
    print(f"  Máximo:    {max(notas):.2f}")
    print(f"  Aprobados: {contar_aprobados(notas)} de {len(notas)}")


if __name__ == "__main__":
    main()
