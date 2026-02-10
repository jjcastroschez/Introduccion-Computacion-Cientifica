"""Tema 2 - Algoritmia
Ejemplo: MCD (algoritmo de Euclides).

Entrada: a, b (enteros positivos)
Salida: mcd(a, b)
"""

def mcd(a: int, b: int) -> int:
    # Algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a

def main() -> None:
    a = int(input("a (entero positivo): "))
    b = int(input("b (entero positivo): "))
    print("MCD(a, b) =", mcd(a, b))

if __name__ == "__main__":
    main()
