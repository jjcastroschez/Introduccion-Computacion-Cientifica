"""
Ejercicio 2.1 — Suma de los N primeros términos de Fibonacci.

Verifica además la identidad: sum_{n=0}^{N-1} F_n = F_{N+1} - 1.

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def suma_fibonacci(n: int) -> tuple[int, int]:
    """
    Suma los primeros n términos de Fibonacci y devuelve (suma, F_{n+1}).
    Útil para verificar la identidad sum = F_{n+1} - 1.
    """
    a, b = 0, 1
    suma = 0
    for _ in range(n):
        suma += a
        a, b = b, a + b
    return suma, b


def main():
    n = int(input("¿Cuántos términos de Fibonacci sumar?: "))
    suma, f_siguiente = suma_fibonacci(n)
    print(f"Suma de los primeros {n} términos: {suma}")
    print(f"Verificación: F_{n+1} - 1 = {f_siguiente - 1}")
    if suma == f_siguiente - 1:
        print("✅ Se cumple la identidad.")


if __name__ == "__main__":
    main()
