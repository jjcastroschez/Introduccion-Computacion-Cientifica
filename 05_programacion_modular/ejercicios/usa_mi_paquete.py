"""
usa_mi_paquete.py — Programa principal que importa varios submódulos.

Solución del ejercicio 8 del Tema 5: cómo importar y usar las funciones
de un paquete con submódulos.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import mi_paquete.analisis.sucesiones as suc
import mi_paquete.algebra.polinomios as pol


def main():
    print("Demostración de mi_paquete")
    print("==========================")

    # Submódulo análisis.sucesiones
    print("\nSerie armónica H_n para varios n:")
    for n in (1, 10, 100, 1000):
        print(f"  H_{n} = {suc.suma_armonica(n):.6f}")

    print("\nSuma aritmética: primero=1, diferencia=2, n=10 (esperado 100):")
    print(f"  {suc.suma_aritmetica(1, 2, 10)}")

    print("\nSuma geométrica: primero=1, razón=2, n=5 (esperado 31):")
    print(f"  {suc.suma_geometrica(1, 2, 5)}")

    # Submódulo álgebra.polinomios
    print("\nEvaluación de p(x) = x² - 3x + 2 en varios puntos:")
    for x in (0, 1, 2, 3):
        print(f"  p({x}) = {pol.evaluar_polinomio_simple(1, -3, 2, x)}")

    print(f"\nDiscriminante de x² - 3x + 2: {pol.discriminante(1, -3, 2)} (debe ser 1)")


if __name__ == "__main__":
    main()
