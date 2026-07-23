"""
Ejercicio 10 — Punto en el plano con namedtuple.

Definimos un tipo `Punto` con dos campos (x, y) usando namedtuple.
Después implementamos operaciones típicas: distancia entre dos puntos,
punto medio, conversión a polares.

Es un ejemplo natural de por qué las namedtuple son ideales para
representar entidades matemáticas: campos con nombre, inmutables,
y ligeras.

Tema 6 - Introducción a la Computación Científica (ICC).
"""

import math
from collections import namedtuple

# Definimos el tipo Punto
Punto = namedtuple("Punto", ["x", "y"])


def distancia(p1: Punto, p2: Punto) -> float:
    """Distancia euclídea entre dos puntos.
    :param p1: Primer punto.
    :param p2: Segundo punto.
    :return: Distancia entre p1 y p2."""
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def punto_medio(p1: Punto, p2: Punto) -> Punto:
    """Punto medio del segmento p1-p2.
    :param p1: Primer punto.
    :param p2: Segundo punto.
    :return: Punto medio del segmento p1-p2.
    """
    return Punto((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


def a_polares(p: Punto) -> tuple:
    """Convierte un punto (x, y) a coordenadas polares (r, θ).
    
    Devuelve una tupla (radio, ángulo_en_radianes).
    
    :param p: Punto en coordenadas cartesianas.
    :return: Tupla (radio, ángulo_en_radianes).
    """
    r = math.sqrt(p.x ** 2 + p.y ** 2)
    theta = math.atan2(p.y, p.x)
    return r, theta


def main():
    origen = Punto(0, 0)
    a = Punto(3, 4)
    b = Punto(-1, 2)

    print(f"Origen: {origen}")
    print(f"A:      {a}")
    print(f"B:      {b}\n")

    print(f"Acceso por nombre:  a.x = {a.x}, a.y = {a.y}")
    print(f"Desempaquetado:     x, y = a → x = {a[0]}, y = {a[1]}\n")

    print(f"distancia(origen, A) = {distancia(origen, a)}  (esperado 5)")
    print(f"distancia(A, B)      = {distancia(a, b):.4f}")

    m = punto_medio(a, b)
    print(f"\npunto_medio(A, B) = {m}")

    r, theta = a_polares(a)
    print(f"\nA en polares: r = {r:.4f}, θ = {theta:.4f} rad ({math.degrees(theta):.2f}°)")


if __name__ == "__main__":
    main()
