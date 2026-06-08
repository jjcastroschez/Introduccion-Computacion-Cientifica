import math # <-- En un módulo, es común importar otras librerías que se necesiten. En este caso, math para la función sqrt.

"""Funciones de aritmética entera: MCD, MCM, primos."""


def mcd(a: int, b: int) -> int:
    """Algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a


def mcm(a: int, b: int) -> int:
    """Mínimo común múltiplo."""
    return abs(a * b) // mcd(a, b)

'''
Otra versión del es_primo, con el uso del for y range. 
'''

def es_primo(n: int) -> bool:
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False 
    return True
