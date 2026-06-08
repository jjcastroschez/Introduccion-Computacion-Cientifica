"""
usa_paquete.py — Cómo usar un paquete con submódulos.

Demuestra varias formas de importar funciones desde una estructura
jerárquica de paquetes y submódulos.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

# Forma 1: importar el submódulo completo con alias
import paq_matematicas.aritmetica.enteros as aritm
import paq_matematicas.geometria.plana as geo


def main():
    print("Demostración del paquete paq_matematicas")
    print("=" * 42)

    print("\nAritmética entera (paq_matematicas.aritmetica.enteros):")
    print(f"  mcd(48, 18) = {aritm.mcd(48, 18)}")
    print(f"  mcm(4, 6) = {aritm.mcm(4, 6)}")
    print(f"  es_primo(17) = {aritm.es_primo(17)}")

    print("\nGeometría plana (paq_matematicas.geometria.plana):")
    print(f"  área círculo r=5: {geo.area_circulo(5):.4f}")
    print(f"  hipotenusa (3,4): {geo.hipotenusa(3, 4):.4f}")
    print(f"  área triángulo b=4, h=3: {geo.area_triangulo(4, 3):.4f}")


if __name__ == "__main__":
    main()
