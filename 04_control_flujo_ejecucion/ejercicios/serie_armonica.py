"""
Ejercicio 5.2 — Serie armónica truncada.

Calcula H_N = sum 1/k desde k=1 hasta N, y encuentra el primer N tal
que H_N supera un umbral S dado.

Tema 4 - Introducción a la Computación Científica (ICC).
"""

import math

EULER_MASCHERONI = 0.5772156649015329


def H(n: int) -> float:
    """Calcula H_n = 1 + 1/2 + 1/3 + ... + 1/n."""
    suma = 0.0
    for i in range(1, n + 1):
        suma += 1 / i
    return suma


def primer_n_que_supera(s: float, max_iter: int = 10**8) -> tuple[int, float]:
    """Devuelve (n, H_n) tal que H_n es el primer parcial que supera s."""
    n = 0
    suma = 0.0
    while suma <= s and n < max_iter:
        n += 1
        suma += 1 / n

    if suma <= s:
        raise RuntimeError(f"No se superó el umbral {s} en {max_iter} iteraciones.")
    return n, suma


def main():
    n = int(input("N (cuántos términos sumar): "))
    suma = H(n)
    asintotica = math.log(n) + EULER_MASCHERONI
    print(f"H_{n} = {suma:.10f}")
    print(f"Aproximación asintótica ln(N) + γ = {asintotica:.10f}")
    print(f"Diferencia: {abs(suma - asintotica):.2e}")

    s = float(input("\nUmbral S: "))
    n_sup, h = primer_n_que_supera(s)
    print(f"H_{n_sup} = {h:.6f} > {s}")


if __name__ == "__main__":
    main()
