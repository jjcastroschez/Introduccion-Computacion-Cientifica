"""
Ejercicio 5.1 — Conjetura de Collatz.

La famosa conjetura 3n+1: partiendo de cualquier entero positivo,
si es par se divide por 2, si es impar se multiplica por 3 y se suma 1.
Conjetura: siempre se llega a 1.

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def collatz(n: int) -> tuple[list[int], int]:
    """Devuelve la sucesión de Collatz desde n y el número de pasos."""
    if n <= 0:
        raise ValueError(f"Necesito un entero positivo, recibí {n}.")

    sucesion = [n]
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sucesion.append(n)
        pasos += 1
    return sucesion, pasos


def pedir_entero_positivo() -> int:
    """Pide un entero positivo, gestionando errores con try-except."""
    while True:
        try:
            n = int(input("Entero positivo: "))
            if n <= 0:
                print("Debe ser positivo.")
                continue
            return n
        except ValueError:
            print("Eso no es un entero válido.")


def main():
    n = pedir_entero_positivo()
    sucesion, pasos = collatz(n)
    print(f"Sucesión: {sucesion}")
    print(f"Pasos hasta llegar a 1: {pasos}")

    # Reto: el de trayectoria más larga del 1 al 100
    mas_largo = 1
    max_pasos = 0
    for i in range(1, 101):
        _, p = collatz(i)
        if p > max_pasos:
            max_pasos = p
            mas_largo = i

    print(f"\nDel 1 al 100, el de trayectoria más larga es {mas_largo} "
          f"({max_pasos} pasos).")


if __name__ == "__main__":
    main()
