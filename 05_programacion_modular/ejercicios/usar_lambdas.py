"""
Ejercicio 10 — Usar `lambda` para definir funciones cortas en una línea.

Las expresiones lambda son útiles cuando necesitamos pasar una función
PEQUEÑA y de UN SOLO USO a una función de orden superior. Aquí ilustramos
cómo se sustituyen def cortos por lambdas, y por qué a veces conviene
hacerlo y otras veces NO.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import math


def aplicar(f, x: float) -> float:
    """Función auxiliar: simplemente devuelve f(x)."""
    return f(x)


def integral_trapecio(f, a: float, b: float, n: int) -> float:
    """
    Regla del trapecio compuesta para aproximar ∫_a^b f(x) dx con n subintervalos.

    (Misma fórmula que viste en el ejemplo de primera clase.)
    """
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
    for i in range(1, n):
        suma = suma + f(a + i * h)
    return suma * h


def main():
    # Parte A: equivalencia entre def y lambda
    print("Parte A — Equivalencia de def y lambda")
    print("--------------------------------------")
    doble = lambda x: x * 2
    es_par = lambda n: n % 2 == 0
    suma = lambda a, b: a + b

    print(f"  doble(7) = {doble(7)}")
    print(f"  es_par(8) = {es_par(8)}")
    print(f"  suma(3, 5) = {suma(3, 5)}")

    # Parte B: usar lambda con funciones de orden superior
    print("\nParte B — Lambdas pasadas como argumento")
    print("--------------------------------------")
    print(f"  aplicar(lambda x: x**3, 4) = {aplicar(lambda x: x**3, 4)}")

    # Parte C: integrar varias funciones SIN definirlas con def
    print("\nParte C — Integrar con lambdas")
    print("--------------------------------------")
    print(f"  ∫₀¹ x² dx ≈ {integral_trapecio(lambda x: x**2, 0, 1, 1000):.6f}  (exacto 1/3)")
    print(f"  ∫₀¹ (x³+1) dx ≈ {integral_trapecio(lambda x: x**3 + 1, 0, 1, 1000):.6f}  (exacto 5/4)")
    print(f"  ∫₀^π sin(x) dx ≈ {integral_trapecio(lambda x: math.sin(x), 0, math.pi, 1000):.6f}  (exacto 2)")

    # Parte D: cuándo NO usar lambda
    print("\nParte D — Cuándo NO usar lambda")
    print("--------------------------------------")
    print("  Lo que sigue ES correcto pero NO debería escribirse con lambda:")
    print("    clasificar = lambda x: ('positivo' if x > 0 else 'negativo' if x < 0 else 'cero')")
    print("    → Mejor un def claro con su nombre descriptivo.")


if __name__ == "__main__":
    main()
