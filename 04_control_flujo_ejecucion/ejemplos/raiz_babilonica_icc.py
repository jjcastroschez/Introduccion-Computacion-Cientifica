"""
Cálculo iterativo de la raíz cuadrada por el método babilónico (Herón).

    x_(n+1) = 0.5 * (x_n + a / x_n)

Tema 4 - Introducción a la Computación Científica (ICC).
"""

TOLERANCIA = 1e-10
MAX_ITER = 100


def raiz_babilonica(a: float) -> float:
    """
    Devuelve la raíz cuadrada aproximada de `a` por el método babilónico.

    Lanza ValueError si `a` es negativo.
    """
    if a < 0:
        raise ValueError(f"No existe raíz real de un número negativo ({a}).")
    if a == 0:
        return 0.0

    x = a / 2
    for _ in range(MAX_ITER):
        x_nuevo = 0.5 * (x + a / x)
        if abs(x_nuevo - x) < TOLERANCIA:
            return x_nuevo
        x = x_nuevo

    # Si llegamos aquí, no convergió (caso muy improbable)
    raise RuntimeError(
        f"El método no convergió en {MAX_ITER} iteraciones."
    )


def main():
    a = float(input("Calcular la raíz cuadrada de: "))
    try:
        resultado = raiz_babilonica(a)
        print(f"√{a} ≈ {resultado:.15f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
