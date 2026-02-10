"""Tema 2 - Algoritmia
Ejemplo: suma 1..n por dos métodos.

- Método A: iteración (bucle).
- Método B: fórmula S = n(n+1)/2.

Este ejemplo ilustra que distintos algoritmos pueden resolver el mismo problema
con costes distintos (tiempo/memoria).
"""

def suma_bucle(n: int) -> int:
    s = 0
    for k in range(1, n + 1):
        s += k
    return s

def suma_formula(n: int) -> int:
    return n * (n + 1) // 2

def main() -> None:
    n = int(input("Introduce n (entero >= 0): "))
    print("Suma por bucle:", suma_bucle(n))
    print("Suma por fórmula:", suma_formula(n))

if __name__ == "__main__":
    main()
