"""Áreas y perímetros de figuras planas."""

import math


def area_circulo(radio: float) -> float:
    """Área de un círculo."""
    return math.pi * radio ** 2


def perimetro_circulo(radio: float) -> float:
    """Perímetro (longitud de la circunferencia)."""
    return 2 * math.pi * radio


def area_triangulo(base: float, altura: float) -> float:
    """Área de un triángulo dado base y altura."""
    return base * altura / 2


def area_rectangulo(base: float, altura: float) -> float:
    """Área de un rectángulo."""
    return base * altura


def hipotenusa(cateto1: float, cateto2: float) -> float:
    """Hipotenusa de un triángulo rectángulo."""
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2)
