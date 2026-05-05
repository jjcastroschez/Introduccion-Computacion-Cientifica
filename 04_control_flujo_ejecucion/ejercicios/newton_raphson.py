"""
Ejercicio 3.3 — Método de Newton-Raphson.

Implementación genérica del método para encontrar raíces de cualquier
función diferenciable. Se aplica a:
  1. Cálculo de √2 (función f(x) = x² - a)
  2. Constante de Dottie (raíz de cos(x) - x = 0)

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math


def newton_raphson(f, df, x0: float, tol: float = 1e-12,
                   max_iter: int = 100) -> tuple[float, int]:
    """
    Devuelve una raíz aproximada de `f`, partiendo de `x0`.

    Parámetros:
      f, df:    función y su derivada
      x0:       estimación inicial
      tol:      tolerancia
      max_iter: máximo de iteraciones (red de seguridad)
    """
    x = x0
    for iteracion in range(max_iter):
        x_nuevo = x - f(x) / df(x)
        if abs(x_nuevo - x) < tol:
            return x_nuevo, iteracion + 1
        x = x_nuevo
    raise RuntimeError(f"No convergió en {max_iter} iteraciones")


def main():
    # 1. √2 con Newton-Raphson
    a = 2.0
    raiz, iteraciones = newton_raphson(
        f=lambda x: x**2 - a,
        df=lambda x: 2 * x,
        x0=a / 2,
    )
    print(f"√{a} ≈ {raiz} en {iteraciones} iteraciones")

    # 2. Constante de Dottie: cos(x) = x
    dottie, iteraciones = newton_raphson(
        f=lambda x: math.cos(x) - x,
        df=lambda x: -math.sin(x) - 1,
        x0=0.5,
    )
    print(f"Constante de Dottie ≈ {dottie} en {iteraciones} iteraciones")


if __name__ == "__main__":
    main()
