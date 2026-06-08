"""
Ejercicio 4 — Conversión a coordenadas polares.

Dadas las coordenadas cartesianas (x, y) de un punto, calcula sus
coordenadas polares (r, theta), donde:
    r     = sqrt(x² + y²)
    theta = atan2(y, x)  (en radianes, en el rango (-π, π])

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import math


def coordenadas_polares(x: float, y: float) -> tuple:
    """
    Devuelve (r, theta) en coordenadas polares.

    Usa math.atan2 para que el cuadrante sea correcto.
    :param x: Coordenada x (float).
    :param y: Coordenada y (float).
    :return: Tupla (r, theta) con r >= 0 y theta en radianes.
    """
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return r, theta


def mostrar(x: float, y: float) -> None:
    """Imprime las coordenadas polares de (x, y) formateadas.
    
    :param x: Coordenada x (float).
    :param y: Coordenada y (float).
    :return: None.
    """
    r, t = coordenadas_polares(x, y)
    print(f"({x:2}, {y:2}) → r = {r:.4f}, θ = {t:.4f} rad ({math.degrees(t):7.2f}°)")


def main():
    # Casos de prueba (sin listas: tema 6)
    mostrar(1, 0)     # → (1, 0)
    mostrar(0, 1)     # → (1, π/2)
    mostrar(-1, 0)    # → (1, π)
    mostrar(1, 1)     # → (√2, π/4)
    mostrar(-1, -1)   # → (√2, -3π/4)


if __name__ == "__main__":
    main()
