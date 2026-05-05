"""
Ejercicio 3.2 — Método de la bisección.

Encuentra una raíz de f(x) = x³ - x - 2 en el intervalo [1, 2] usando
el método de la bisección.

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def f(x: float) -> float:
    return x**3 - x - 2


def biseccion(funcion, a: float, b: float, tol: float = 1e-10,
              max_iter: int = 100) -> tuple[float, int]:
    """
    Devuelve una raíz aproximada de `funcion` en el intervalo [a, b]
    junto con el número de iteraciones empleadas.
    """
    if funcion(a) * funcion(b) >= 0:
        raise ValueError(
            "No se garantiza la existencia de raíz en este intervalo."
        )

    iteracion = 0
    while (b - a) > tol and iteracion < max_iter:
        c = (a + b) / 2
        if funcion(a) * funcion(c) < 0:
            b = c
        else:
            a = c
        iteracion += 1

    return (a + b) / 2, iteracion


def main():
    raiz, iteraciones = biseccion(f, 1.0, 2.0)
    print(f"Raíz aproximada de x³ - x - 2 = 0 en [1, 2]: {raiz:.12f}")
    print(f"Iteraciones empleadas: {iteraciones}")


if __name__ == "__main__":
    main()
