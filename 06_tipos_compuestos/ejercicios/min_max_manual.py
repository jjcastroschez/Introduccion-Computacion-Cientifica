"""
Ejercicio 3 — Encontrar mínimo y máximo SIN usar min() ni max().

Consolidación del patrón "recorrer manteniendo estado": vamos comparando
cada elemento con el mejor candidato conocido hasta ese momento.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def min_manual(numeros: list) -> float:
    """
    Devuelve el mínimo de una lista.

    Estrategia: guardamos como candidato el primer elemento y vamos
    actualizándolo cada vez que encontramos uno más pequeño.

    :requisitos: la lista no puede estar vacía.
    :param numeros: lista de números (float o int)
    :return: mínimo de la lista (float)
    """
    if len(numeros) == 0:
        raise ValueError("Lista vacía: no hay mínimo.")
    minimo = numeros[0]
    for x in numeros:
        if x < minimo:
            minimo = x
    return minimo


def max_manual(numeros: list) -> float:
    """
    Análogo a min_manual, pero buscando el mayor.
    :param numeros: lista de números (float o int)
    :return: máximo de la lista (float)
    """
    if len(numeros) == 0:
        raise ValueError("Lista vacía: no hay máximo.")
    maximo = numeros[0]
    for x in numeros:
        if x > maximo:
            maximo = x
    return maximo


def min_max(numeros: list) -> tuple:
    """
    Devuelve (mínimo, máximo) en un solo recorrido. Es MÁS EFICIENTE
    que llamar a min_manual() y max_manual() por separado, porque
    recorre la lista UNA sola vez en lugar de dos.
    :param numeros: lista de números (float o int)
    :return: tupla (mínimo, máximo)
    """
    if len(numeros) == 0:
        raise ValueError("Lista vacía.")
    minimo = numeros[0]
    maximo = numeros[0]
    for x in numeros:
        if x < minimo:
            minimo = x
        if x > maximo:
            maximo = x
    return minimo, maximo


def main():
    datos = [7, 3, 8, 1, 9, 4, 6, 2, 5]
    print(f"Lista: {datos}")
    print(f"  min_manual = {min_manual(datos)} (esperado 1)")
    print(f"  max_manual = {max_manual(datos)} (esperado 9)")

    mi, ma = min_max(datos)
    print(f"  min_max    = ({mi}, {ma})")

    # Verificar con los nativos
    print(f"\nComparación con nativos: min={min(datos)}, max={max(datos)}")


if __name__ == "__main__":
    main()
