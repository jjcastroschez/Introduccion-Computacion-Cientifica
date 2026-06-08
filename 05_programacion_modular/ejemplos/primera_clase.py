"""
Funciones como ciudadanos de primera clase.

En Python las funciones son valores como cualquier otro: se pueden
asignar a variables, pasar como argumentos a otras funciones y devolver
como resultado. Esta característica abre la puerta a un estilo de
programación muy elegante (programación funcional) que profundizaremos
en el Tema 6.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import math


# ---------------------------------------------------------------------
# 1) Funciones asignadas a variables (alias)
# ---------------------------------------------------------------------

def saludar(nombre: str) -> None:
    """Procedimiento simple que saluda."""
    print(f"¡Hola, {nombre}!")


# La función saludar es un VALOR; podemos asignarla a otra variable
saluda = saludar          # ahora 'saluda' es otra etiqueta para la misma función
# Y se puede invocar como cualquier función: saluda("María")


# ---------------------------------------------------------------------
# 2) Funciones como argumento: aplicar una función dos veces
# ---------------------------------------------------------------------

def aplicar_dos_veces(f, x: float) -> float:
    """
    Devuelve f(f(x)). Función de orden superior:
    recibe OTRA función f como argumento.
    """
    return f(f(x))


def cuadrado(x: float) -> float:
    return x * x


# ---------------------------------------------------------------------
# 3) Funciones que devuelven funciones (closures)
# ---------------------------------------------------------------------

def crear_potencia(exponente: float):
    """
    Devuelve una NUEVA función que eleva su argumento al exponente dado.

    Es una función "fábrica" de funciones.
    """
    def potencia(base: float) -> float:
        return base ** exponente
    return potencia


# ---------------------------------------------------------------------
# 4) Expresiones lambda: funciones de una sola línea
# ---------------------------------------------------------------------
# Las dos siguientes definiciones son equivalentes:

def doble_def(x: float) -> float:
    return x * 2

doble_lambda = lambda x: x * 2

# El uso de lambda brilla cuando hay que pasar una función como
# argumento solo una vez. Por ejemplo, integrar una función numérica
# por la regla del trapecio simple sin tener que definirla con def:


def integral_trapecio(f, a: float, b: float, n: int) -> float:
    """
    Aproxima la integral de f entre a y b con la regla del trapecio
    compuesta (n subintervalos).
    """
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
    for i in range(1, n):
        suma = suma + f(a + i * h)
    return suma * h


# ---------------------------------------------------------------------
# Programa de demostración
# ---------------------------------------------------------------------

def main():
    print("1) Funciones como variables")
    print("-" * 30)
    saluda("Luis")

    print("\n2) Pasar funciones como argumento")
    print("-" * 30)
    print(f"cuadrado(3) = {cuadrado(3)}")
    print(f"aplicar_dos_veces(cuadrado, 3) = (3²)² = {aplicar_dos_veces(cuadrado, 3)}")

    print("\n3) Funciones que devuelven funciones")
    print("-" * 30)
    elevar_al_cubo = crear_potencia(3)
    raiz_cuadrada = crear_potencia(0.5)
    print(f"elevar_al_cubo(2) = {elevar_al_cubo(2)}")
    print(f"raiz_cuadrada(9)  = {raiz_cuadrada(9)}")

    print("\n4) Expresiones lambda")
    print("-" * 30)
    print(f"doble_def(7) = {doble_def(7)}")
    print(f"doble_lambda(7) = {doble_lambda(7)}")

    print("\n   Integrar funciones con lambdas:")
    # ∫₀¹ x² dx = 1/3
    print(f"     ∫₀¹ x² dx ≈ {integral_trapecio(lambda x: x**2, 0, 1, 1000):.6f}  (exacto 0.333333...)")
    # ∫₀^π sin(x) dx = 2
    print(f"     ∫₀^π sin(x) dx ≈ {integral_trapecio(math.sin, 0, math.pi, 1000):.6f}  (exacto 2)")
    # Combinación: ∫₀¹ x² + 1 dx = 4/3
    print(f"     ∫₀¹ (x² + 1) dx ≈ {integral_trapecio(lambda x: x**2 + 1, 0, 1, 1000):.6f}  (exacto 1.333333...)")


if __name__ == "__main__":
    main()
