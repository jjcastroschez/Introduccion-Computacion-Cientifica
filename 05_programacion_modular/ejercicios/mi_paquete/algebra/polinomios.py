"""Operaciones simples con polinomios representados por sus coeficientes."""


def evaluar_polinomio_simple(a: float, b: float, c: float, x: float) -> float:
    """
    Evalúa el polinomio cuadrático p(x) = a*x² + b*x + c en el punto x.

    (Versión sencilla; en el Tema 6 generalizaremos con listas de coeficientes.)
    """
    return a * x ** 2 + b * x + c


def discriminante(a: float, b: float, c: float) -> float:
    """Discriminante de ax² + bx + c."""
    return b ** 2 - 4 * a * c
