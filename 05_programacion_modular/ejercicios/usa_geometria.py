"""
usa_geometria.py — Programa principal que usa el módulo geometria.

Demuestra cómo, una vez creado geometria.py, lo podemos importar y usar
desde cualquier programa.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import geometria as g


def main():
    print("Calculadora de geometría plana")
    print("==============================")

    # Algunos cálculos típicos
    radio = 5
    print(f"\nCírculo de radio {radio}:")
    print(f"  Área:      {g.area_circulo(radio):.4f}")
    print(f"  Perímetro: {g.perimetro_circulo(radio):.4f}")

    base, altura = 6, 4
    print(f"\nRectángulo {base}x{altura}:")
    print(f"  Área:      {g.area_rectangulo(base, altura)}")
    print(f"  Perímetro: {g.perimetro_rectangulo(base, altura)}")

    a, b, c = 3, 4, 5
    print(f"\nTriángulo de lados {a}, {b}, {c} (rectángulo notable):")
    print(f"  Área (Herón):  {g.area_triangulo_heron(a, b, c)}")
    print(f"  Hipotenusa:    {g.hipotenusa(a, b)} (¿coincide con c={c}?)")


if __name__ == "__main__":
    main()
