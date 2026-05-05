"""
Validación robusta de entrada de usuario.

Pide un número entero en el rango [1, 100] y sigue pidiendo hasta que la
entrada sea válida, gestionando dos tipos de error:
  - ValueError (la entrada no es un entero)
  - Fuera de rango (entero pero no en [1, 100])

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def pedir_entero(minimo: int, maximo: int, mensaje: str) -> int:
    """Pide un entero al usuario hasta que esté en [minimo, maximo]."""
    while True:
        entrada = input(mensaje)
        try:
            n = int(entrada)
        except ValueError:
            print(f'  ❌ "{entrada}" no es un entero válido. Inténtalo de nuevo.')
            continue
        if minimo <= n <= maximo:
            return n
        print(f"  ❌ {n} está fuera del rango [{minimo}, {maximo}]. Inténtalo de nuevo.")


def main():
    n = pedir_entero(1, 100, "Introduce un número entero entre 1 y 100: ")
    print(f"✅ Has introducido el número {n}. ¡Gracias!")


if __name__ == "__main__":
    main()
