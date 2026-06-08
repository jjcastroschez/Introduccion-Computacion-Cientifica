"""
Ejercicio 2 — Refactorizar el clasificador de raíces como función.

En el Tema 4 escribimos un script para clasificar las raíces de una ecuación
cuadrática según el signo del discriminante. Ahora lo convertimos en una
función reutilizable.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import math


def clasificar_raices(a: float, b: float, c: float) -> str:
    """
    Clasifica las raíces de ax² + bx + c = 0 y devuelve una cadena
    descriptiva.

    Trata también el caso degenerado a = 0 (ecuación lineal).
    
    :param a: Coeficiente cuadrático (real)
    :param b: Coeficiente lineal (real)
    :param c: Término independiente
    :return: Descripción de las raíces (string)
    """
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinitas soluciones (0 = 0)."
            return "Sin solución."
        return f"Ecuación lineal. Raíz única: x = {-c / b}"

    discriminante = b ** 2 - 4 * a * c
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
    print(clasificar_raices(1, -5, 6))    # raíces 2 y 3
    print(clasificar_raices(1, -4, 4))    # raíz doble 2
    print(clasificar_raices(1, 1, 1))     # complejas
    print(clasificar_raices(0, 2, 4))     # lineal
    print(clasificar_raices(0, 0, 0))     # infinitas
    print(clasificar_raices(0, 0, 5))     # sin solución


if __name__ == "__main__":
    main()
