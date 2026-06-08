"""
Validación de entrada robusta como función reutilizable.

En el Tema 4 escribimos un bucle while + try-except cada vez que necesitábamos
pedir un número al usuario. Con cada nueva entrada, copiábamos y pegábamos
el mismo patrón. Ahora encapsulamos esa lógica en una función.

Tema 5 - Introducción a la Computación Científica (ICC).
"""


def pedir_entero(mensaje: str, minimo: int, maximo: int) -> int:
    """
    Pide al usuario un entero hasta que sea válido y esté en [minimo, maximo].

    :param mensaje: Texto que se muestra al usuario al pedir el dato.
    :param minimo: Valor mínimo aceptado (incluido).
    :param maximo: Valor máximo aceptado (incluido).
    :return: El entero introducido por el usuario, garantizado en rango.
    """
    entrada_correcta = False
    while not entrada_correcta:
        entrada = input(mensaje)
        try:
            n = int(entrada)
        except ValueError:
            print(f'  ❌ "{entrada}" no es un entero válido.')
        else:
            if minimo <= n <= maximo:
                entrada_correcta = True
            else:
                print(f"  ❌ {n} está fuera del rango [{minimo}, {maximo}].")
    return n

def pedir_real_positivo(mensaje: str) -> float:
    """
    Pide al usuario un número real estrictamente positivo hasta que sea válido.

    :param mensaje: Texto que se muestra al usuario al pedir el dato.
    :return: El número real introducido, garantizado > 0.
    """
    entrada_correcta = False
    while not entrada_correcta:
        entrada = input(mensaje)
        try:
            x = float(entrada)
        except ValueError:
            print(f'  ❌ "{entrada}" no es un número real válido.')
        else:
            if x > 0:
                entrada_correcta = True
            else:
                print(f"  ❌ {x} no es positivo.")
    return x

def main():
    print("Demostración de las funciones de validación.\n")

    edad = pedir_entero("Tu edad (entre 16 y 100): ", 16, 100)
    altura = pedir_real_positivo("Tu altura en metros (>0): ")
    peso = pedir_real_positivo("Tu peso en kilos (>0): ")

    imc = peso / (altura ** 2)
    print(f"\nTu IMC es {imc:.2f}")


if __name__ == "__main__":
    main()
