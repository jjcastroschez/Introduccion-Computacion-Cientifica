"""
Ejercicio 3 — Función que devuelve dos valores.

Implementación propia de divmod: dado un dividendo y un divisor, devuelve
una tupla (cociente, resto) sin usar el divmod() integrado de Python.

Tema 5 - Introducción a la Computación Científica (ICC).
"""


def divmod_entero(a: int, b: int) -> tuple:
    """
    División entera. Devuelve (cociente, resto) tal que
    a = b * cociente + resto, con 0 <= resto < |b|.

    :param a: Dividendo (entero).
    :param b: Divisor (entero, distinto de 0).
    :return: Tupla (cociente, resto) (enteros).
    :requisitos: b != 0
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0.")
    cociente = a // b
    resto = a % b
    return cociente, resto


def main():
    # Casos típicos
    print(divmod_entero(17, 5))     # (3, 2)
    print(divmod_entero(20, 4))     # (5, 0)
    print(divmod_entero(7, 3))      # (2, 1)

    # Asignación múltiple en el lado del que llama
    q, r = divmod_entero(100, 7)
    print(f"100 = 7 * {q} + {r}")

    # Manejo del error
    try:
        divmod_entero(5, 0)
    except ZeroDivisionError as e:
        print(f"Error capturado: {e}")


if __name__ == "__main__":
    main()
