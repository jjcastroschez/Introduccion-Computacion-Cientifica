"""
Ejercicio 1.1 — Clasificación de un triángulo.

Dados los lados a, b, c, comprueba si forman un triángulo válido y lo
clasifica como equilátero, isósceles o escaleno. También indica si es
rectángulo (Teorema de Pitágoras).

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def clasificar(a: float, b: float, c: float) -> str:
    """Clasifica el triángulo o devuelve un mensaje de error."""
    # Comprobar desigualdad triangular
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo válido."

    if a == b == c:
        tipo = "Equilátero"
    elif a == b or b == c or a == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"

    # ¿Es rectángulo?
    TOL = 1e-9
    lados = sorted([a, b, c])  # el mayor en la última posición
    if abs(lados[0] ** 2 + lados[1] ** 2 - lados[2] ** 2) < TOL:
        tipo += " (y rectángulo)"

    return tipo


def main():
    a = float(input("Lado a: "))
    b = float(input("Lado b: "))
    c = float(input("Lado c: "))
    print(clasificar(a, b, c))


if __name__ == "__main__":
    main()
