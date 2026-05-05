"""
Ejercicio 4.1 — Criba de Eratóstenes.

Encuentra todos los números primos hasta N usando el clásico algoritmo
de la criba.

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def eratostenes(n: int) -> list[int]:
    """Devuelve la lista de primos menores o iguales que n."""
    if n < 2:
        return []

    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False

    p = 2
    while p * p <= n:
        if es_primo[p]:
            for multiplo in range(p * p, n + 1, p):
                es_primo[multiplo] = False
        p += 1

    return [i for i in range(n + 1) if es_primo[i]]


def main():
    n = int(input("Encontrar primos hasta: "))
    primos = eratostenes(n)
    print(f"Primos hasta {n}: {primos}")
    print(f"Cantidad: {len(primos)}")


if __name__ == "__main__":
    main()
