"""
Ejercicio 2 — Contar líneas, palabras y caracteres de un fichero.

Implementa el equivalente Python del comando UNIX 'wc': dado un fichero,
devuelve una tupla con el número de líneas, palabras y caracteres.

Tema 7 - Introducción a la Computación Científica (ICC).
"""


def contar(fichero: str) -> tuple:
    """
    Devuelve (líneas, palabras, caracteres) del fichero.
    """
    lineas = 0
    palabras = 0
    caracteres = 0

    with open(fichero, "r") as f:
        for linea in f:
            lineas = lineas + 1
            palabras = palabras + len(linea.split())      # split() por espacios
            caracteres = caracteres + len(linea)

    return lineas, palabras, caracteres


def main():
    l, p, c = contar("mensaje.txt")

    print(f"Estadísticas de 'mensaje.txt':")
    print(f"  Líneas:     {l}")
    print(f"  Palabras:   {p}")
    print(f"  Caracteres: {c}")
    print()
    print(f"(Equivale a:  wc -lwc mensaje.txt)")


if __name__ == "__main__":
    main()
