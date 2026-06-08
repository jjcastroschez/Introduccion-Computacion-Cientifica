"""
Ejercicio 1 — Función `area_triangulo`.

Función simple con dos parámetros que devuelve un valor. La fórmula es:
    área = base * altura / 2

Tema 5 - Introducción a la Computación Científica (ICC).
"""


def area_triangulo(base: float, altura: float) -> float:
    """Devuelve el área de un triángulo dado base y altura."""
    return base * altura / 2


def main():
    print(f"area_triangulo(4, 3) = {area_triangulo(4, 3)}")
    print(f"area_triangulo(5, 8) = {area_triangulo(5, 8)}")
    print(f"area_triangulo(10, 7) = {area_triangulo(10, 7)}")


if __name__ == "__main__":
    main()
