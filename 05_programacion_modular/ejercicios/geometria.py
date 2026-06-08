"""
geometria.py — Módulo propio con funciones de geometría plana.

Solución del ejercicio 7 del Tema 5.

Autor:        (estudiantes)
Fecha:        febrero 2026
Versión:      1.0
Dependencias: math (estándar)
"""

import math


def area_circulo(radio: float) -> float:
    """Área del círculo de radio dado.
    
    :param radio: Radio del círculo (float)).
    :return: Área del círculo (float).
    :requisitos: radio > 0.
    """
    return math.pi * radio ** 2


def perimetro_circulo(radio: float) -> float:
    """Longitud de la circunferencia.
    
    :param radio: Radio de la circunferencia (float).
    :return: Longitud de la circunferencia (float).
    :requisitos: radio > 0.
    """
    return 2 * math.pi * radio


def area_triangulo(base: float, altura: float) -> float:
    """Área de un triángulo dado base y altura.

    :param base: Base del triángulo (float).
    :param altura: Altura del triángulo (float).
    :return: Área del triángulo (float).
    :requisitos: base > 0, altura > 0.
    """
    return base * altura / 2


def area_rectangulo(base: float, altura: float) -> float:
    """Área de un rectángulo.
    
    :param base: Base del rectángulo (float).
    :param altura: Altura del rectángulo (float).
    :return: Área del rectángulo (float).
    :requisitos: base > 0, altura > 0.
    """
    return base * altura


def perimetro_rectangulo(base: float, altura: float) -> float:
    """Perímetro de un rectángulo.
    
    :param base: Base del rectángulo (float).
    :param altura: Altura del rectángulo (float).
    :return: Perímetro del rectángulo (float).
    :requisitos: base > 0, altura > 0.
    """
    return 2 * (base + altura)


def hipotenusa(cateto1: float, cateto2: float) -> float:
    """Hipotenusa de un triángulo rectángulo (Pitágoras).
    
    :param cateto1: Primer cateto del triángulo (float).
    :param cateto2: Segundo cateto del triángulo (float).
    :return: Hipotenusa del triángulo (float).
    :requisitos: cateto1 > 0, cateto2 > 0.
    """
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2)


def area_triangulo_heron(a: float, b: float, c: float) -> float:
    """
    Área de un triángulo dados sus tres lados (fórmula de Herón).

    :param a: Lado a del triángulo (float).
    :param b: Lado b del triángulo (float).
    :param c: Lado c del triángulo (float).
    :return: Área del triángulo (float).
    :requisitos: a, b, c forman un triángulo válido.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Tests rápidos cuando se ejecuta directamente
if __name__ == "__main__":
    print(f"Área círculo r=1:        {area_circulo(1):.4f} (esperado π ≈ 3.1416)")
    print(f"Perímetro círculo r=1:   {perimetro_circulo(1):.4f} (esperado 2π ≈ 6.2832)")
    print(f"Área triángulo (4,3):    {area_triangulo(4, 3)} (esperado 6)")
    print(f"Área rectángulo (4,5):   {area_rectangulo(4, 5)} (esperado 20)")
    print(f"Hipotenusa (3,4):        {hipotenusa(3, 4)} (esperado 5)")
    print(f"Heron (3,4,5):           {area_triangulo_heron(3, 4, 5)} (esperado 6)")
