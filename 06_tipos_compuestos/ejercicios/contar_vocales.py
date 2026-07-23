"""
Ejercicio 1 — Contar vocales de una cadena.

Función que recibe un texto y devuelve cuántas vocales (a, e, i, o, u)
contiene, sin distinguir mayúsculas/minúsculas.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def contar_vocales(texto: str) -> int:
    """Devuelve el número de vocales de un texto (sin acentos).
    :param texto: cadena de caracteres (string)
    :return total: número de vocales (int)
    """
    vocales = "aeiou"
    total = 0
    for letra in texto.lower():
        if letra in vocales:
            total = total + 1
    return total


def main():
    print(f"'hola'           → {contar_vocales('hola')} vocales")
    print(f"'programación'   → {contar_vocales('programación')} vocales (sin tildes)")
    print(f"'MATEMATICAS'    → {contar_vocales('MATEMATICAS')} vocales")
    print(f"'xyz'            → {contar_vocales('xyz')} vocales")
    print(f"''               → {contar_vocales('')} vocales")


if __name__ == "__main__":
    main()
