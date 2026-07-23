"""
Programación funcional aplicada a secuencias.

Muchos cálculos que hacíamos en el Tema 4 con bucles y acumuladores
se pueden expresar en una sola línea gracias a las funciones map, filter,
reduce, zip, enumerate, sorted, any y all combinadas con las lambdas del
Tema 5.

Este ejemplo compara ambos enfoques lado a lado.

Tema 6 - Introducción a la Computación Científica (ICC).
"""

from functools import reduce


def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # -----------------------------------------------------------------
    # MAP: aplicar una función a cada elemento
    # -----------------------------------------------------------------
    print("MAP — cuadrados de todos los números")
    print("  Con bucle (Tema 4):")
    cuadrados_bucle = []
    for x in numeros:
        cuadrados_bucle.append(x ** 2)
    print(f"    {cuadrados_bucle}")

    print("  Con map:")
    cuadrados_map = list(map(lambda x: x ** 2, numeros))
    print(f"    {cuadrados_map}")

    # -----------------------------------------------------------------
    # FILTER: quedarse con los que cumplen una condición
    # -----------------------------------------------------------------
    print("\nFILTER — números pares")
    pares_bucle = []
    for x in numeros:
        if x % 2 == 0:
            pares_bucle.append(x)
    print(f"  Con bucle:  {pares_bucle}")

    pares_filter = list(filter(lambda x: x % 2 == 0, numeros))
    print(f"  Con filter: {pares_filter}")

    # -----------------------------------------------------------------
    # REDUCE: acumular
    # -----------------------------------------------------------------
    print("\nREDUCE — producto de todos los números")
    prod_bucle = 1
    for x in numeros:
        prod_bucle = prod_bucle * x
    print(f"  Con bucle:  {prod_bucle}")

    prod_reduce = reduce(lambda a, b: a * b, numeros)
    print(f"  Con reduce: {prod_reduce}")   # = 10! = 3628800

    # -----------------------------------------------------------------
    # ZIP: combinar dos listas en pares
    # -----------------------------------------------------------------
    print("\nZIP — dos listas emparejadas")
    nombres = ["Ana", "Luis", "Marta"]
    edades = [25, 30, 22]

    pares = list(zip(nombres, edades))
    print(f"  {pares}")

    # Muy útil para calcular sobre dos listas paralelas:
    valores = [10, 20, 30]
    pesos   = [0.2, 0.5, 0.3]
    media_ponderada = sum(v * p for v, p in zip(valores, pesos))
    print(f"  Media ponderada: {media_ponderada}")

    # -----------------------------------------------------------------
    # ENUMERATE: iterar con índice
    # -----------------------------------------------------------------
    print("\nENUMERATE — recorrer con índice")
    equipos = ["Alavés", "Betis", "Celta"]
    for i, equipo in enumerate(equipos, start=1):
        print(f"  {i}º: {equipo}")

    # -----------------------------------------------------------------
    # SORTED con key: ordenar por un criterio
    # -----------------------------------------------------------------
    print("\nSORTED — ordenar por criterio")
    palabras = ["universidad", "ir", "ciencia", "de", "computacion"]
    por_longitud = sorted(palabras, key=len)
    print(f"  Por longitud: {por_longitud}")

    por_longitud_desc = sorted(palabras, key=len, reverse=True)
    print(f"  Longitud desc: {por_longitud_desc}")

    # -----------------------------------------------------------------
    # ANY y ALL: comprobar existencias / totalidad
    # -----------------------------------------------------------------
    print("\nANY / ALL — comprobar rápidamente")
    print(f"  ¿Hay algún número par? {any(x % 2 == 0 for x in numeros)}")
    print(f"  ¿Son todos positivos?  {all(x > 0 for x in numeros)}")
    print(f"  ¿Son todos pares?      {all(x % 2 == 0 for x in numeros)}")


if __name__ == "__main__":
    main()
