"""
Ejercicio 5 — Potencia recursiva.

Implementa base^n recursivamente, sin usar el operador ** ni math.pow.

Recurrencia:
    base^0 = 1                     (caso base)
    base^n = base * base^(n-1)     (caso recursivo)

Tema 5 - Introducción a la Computación Científica (ICC).
"""


def potencia(base: float, n: int) -> float:
    """
    Devuelve base elevado a n por recursión.

    :param base: La base de la potencia (puede ser cualquier número real).
    :param n: El exponente (entero no negativo).
    :return: El resultado de base^n (número real).
    :requisitos: n >= 0 (entero no negativo)
    """
    if n < 0:
        raise ValueError("El exponente debe ser >= 0.")
    if n == 0:
        return 1.0
    return base * potencia(base, n - 1)


def main():
    # Comprobaciones rápidas
    print(f"2^10 = {potencia(2, 10)} (esperado 1024)")
    print(f"3^4 = {potencia(3, 4)} (esperado 81)")
    print(f"5^0 = {potencia(5, 0)} (esperado 1)")
    print(f"7^1 = {potencia(7, 1)} (esperado 7)")
    print(f"1.5^3 = {potencia(1.5, 3)} (esperado 3.375)")


if __name__ == "__main__":
    main()
