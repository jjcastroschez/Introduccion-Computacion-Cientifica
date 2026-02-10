"""Tema 2 - Algoritmia
Ejemplo: máximo de tres números.

Este problema se usa para practicar el diseño de algoritmos con selección.
"""

def main() -> None:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    maximo = a
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c

    print("El máximo es:", maximo)

if __name__ == "__main__":
    main()
