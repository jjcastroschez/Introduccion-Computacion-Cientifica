"""Tema 2 - Algoritmia
Ejemplo: cálculo del área de un círculo.

Este script sirve para conectar:
- especificación (entrada/salida)
- algoritmo (pasos)
- implementación (Python)

Entrada: radio (real), pi (real)  -> aquí se usa pi = 3.141592653589793
Salida: area (real)
"""

def main() -> None:
    # Entrada
    radio = float(input("Introduce el radio del círculo: "))
    pi = 3.141592653589793

    # Proceso
    area = pi * radio * radio

    # Salida
    print(f"El área del círculo es: {area}")

if __name__ == "__main__":
    main()
