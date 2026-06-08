"""
Calculadora científica modular.

Pequeña calculadora que ofrece varias operaciones científicas implementadas
como funciones independientes. El usuario elige la operación y la función
correspondiente hace el trabajo.

Es el primer ejemplo donde **escribimos nuestras propias funciones**, en
lugar de limitarnos a usar las que vienen con Python.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import math


# ---------------------------------------------------------------------
# Funciones de la calculadora
# ---------------------------------------------------------------------

def area_circulo(radio: float) -> float:
    """Devuelve el área de un círculo de radio dado."""
    return math.pi * radio ** 2


def hipotenusa(cateto1: float, cateto2: float) -> float:
    """Devuelve la hipotenusa de un triángulo rectángulo (Pitágoras)."""
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2)


def grados_a_radianes(grados: float) -> float:
    """Convierte un ángulo de grados sexagesimales a radianes."""
    return grados * math.pi / 180


def es_par(n: int) -> bool:
    """Devuelve True si n es par, False en caso contrario."""
    return n % 2 == 0


# ---------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------

def mostrar_menu():
    print("\nCalculadora científica modular")
    print("------------------------------")
    print("1) Área de un círculo")
    print("2) Hipotenusa de un triángulo rectángulo")
    print("3) Conversión de grados a radianes")
    print("4) ¿Es un número par?")

def seleccion_opcion():
    
    opcion = input("\nElige una opción [1-4]: ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        print("Entrada no válida.")  
        opcion = input("\nPor favor, elija una opción [1-4]: ")
    return opcion

def ejercutar_logica(opcion):  
    match opcion:
        case "1":
            r = float(input("Radio: "))
            print(f"Área = {area_circulo(r):.4f}")
        case "2":
            a = float(input("Cateto 1: "))
            b = float(input("Cateto 2: "))
            print(f"Hipotenusa = {hipotenusa(a, b):.4f}")
        case "3":
            g = float(input("Ángulo en grados: "))
            print(f"{g}° = {grados_a_radianes(g):.6f} rad")
        case "4":
            n = int(input("Entero: "))
            if es_par(n):
                print(f"{n} es par")
            else:
                print(f"{n} es impar")
        case _:
            print("Opción no válida.")

def main():
    
    mostrar_menu()
    opcion = seleccion_opcion()   
    ejercutar_logica(opcion)

if __name__ == "__main__":
    main()