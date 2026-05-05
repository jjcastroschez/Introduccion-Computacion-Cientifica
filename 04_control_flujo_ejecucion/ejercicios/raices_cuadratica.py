"""
Ejercicio 1.2 — Raíces de una ecuación de 2º grado.

Clasifica las raíces de ax² + bx + c = 0 según el discriminante.
Trata además los casos degenerados a=0 (ecuación lineal o sin solución).

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math


def resolver(a: float, b: float, c: float) -> str:
    """Resuelve la ecuación y devuelve un texto descriptivo del resultado."""
    if a == 0:
        # Caso degenerado: ecuación lineal bx + c = 0
        if b == 0:
            if c == 0:
                return "Infinitas soluciones (0 = 0)."
            else:
                return "Sin solución."
        else:
            return f"Raíz única: x = {-c / b}"

    discriminante = b**2 - 4 * a * c
    if discriminante > 0:
        sqrt_d = math.sqrt(discriminante)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return f"Dos raíces reales distintas: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2 * a)
        return f"Raíz real doble: x = {x}"
    else:
        parte_real = -b / (2 * a)
        parte_imag = math.sqrt(-discriminante) / (2 * a)
        return f"Raíces complejas conjugadas: {parte_real} ± {parte_imag}i"


def main():
    a = float(input("Coeficiente a: "))
    b = float(input("Coeficiente b: "))
    c = float(input("Coeficiente c: "))
    print(resolver(a, b, c))


if __name__ == "__main__":
    main()
