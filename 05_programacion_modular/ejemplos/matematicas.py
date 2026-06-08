"""
matematicas.py — Módulo con funciones matemáticas útiles.

Este módulo reúne en un solo lugar varias funciones matemáticas que
implementamos como scripts independientes en el Tema 4 (Euclides, raíz
babilónica, criterios de Bézout). Al tenerlas como funciones dentro
de un módulo, podemos importarlas y reutilizarlas en cualquier programa.

Autor:        J.J. Castro-Schez (y estudiantes)
Fecha:        febrero 2026
Versión:      1.0
Python:       3.10+
Dependencias: math (estándar)
"""

import math


# ---------------------------------------------------------------------
# Aritmética entera
# ---------------------------------------------------------------------

def mcd(a: int, b: int) -> int:
    """
    Máximo Común Divisor por el algoritmo de Euclides.

    :param a: Primer entero positivo.
    :param b: Segundo entero positivo.
    :return: mcd(a, b).
    :requisitos: a, b > 0
    """
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


def mcm(a: int, b: int) -> int:
    """
    Mínimo Común Múltiplo, calculado a partir del MCD.
    
    :param a: Primer entero positivo.
    :param b: Segundo entero positivo.
    :return: mcm(a, b).
    :requisitos: a, b > 0
    """

    return abs(a * b) // mcd(a, b)

def es_primo(n: int) -> bool:
    """
    Devuelve True si n es primo.
    
    :param n: Entero positivo.
    :return: True si n es primo, False en caso contrario.
    :requisitos: n > 0
    """
    if n < 2 or n % 2 ==0: 
        primo=False
    elif n == 2: 
        primo=True
    else:
        primo=True
        i = 3
        while i * i <= n and primo:
            if n % i == 0: primo=False
            i = i + 2
    return primo


def inverso_modular(a: int, m: int) -> int:
    """
    Inverso de a módulo m, por búsqueda directa.

    :param a: Primer entero positivo.
    :param m: Segundo entero positivo.
    :return: un entero k tal que (a*k) % m == 1, o 0 si no existe.
    :requisitos: a, m > 0, mcd(a, m) = 1 para que el inverso exista.
    """
    inverso=0
    for k in range(1, m):
        if (a * k) % m == 1:
            inverso = k
            break
    return inverso


# ---------------------------------------------------------------------
# Métodos numéricos clásicos
# ---------------------------------------------------------------------

def raiz_babilonica(a: float, tolerancia: float = 1e-12,
                    max_iter: int = 100) -> float:
    """
    Raíz cuadrada de a por el método babilónico (Herón).

    :param a: Número no negativo (real).
    :param tolerancia: Criterio de parada por convergencia (real).
    :param max_iter: Número máximo de iteraciones (entero).  
    :requisitos: a >= 0
    :return: Aproximación de √a con la tolerancia indicada.
    """
    if a < 0:
        print("No existe raíz real de un negativo.")
        raiz=None
    elif a == 0:
        raiz=0.0
    else:
        raiz = a / 2
        for _ in range(max_iter):
            raiz_nueva = 0.5 * (raiz + a / raiz)
            if abs(raiz_nueva - raiz) < tolerancia:
                raiz=raiz_nueva
                break
            raiz = raiz_nueva
    return raiz # devuelve la mejor aproximación si no convergió


# ---------------------------------------------------------------------
# Combinatoria
# ---------------------------------------------------------------------

def factorial(n: int) -> int:
    """n! Factorial del número n calculado iterativamente.

    :param n: Numero no negativo (entero).
    :return: Numero (n!) (entero).
    :requisitos: n >= 0
    """
    if n < 0:
        print("El factorial no está definido para negativos.")
        resultado=None
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado


def combinatorio(n: int, k: int) -> int:
    """
    Número combinatorio C(n, k) = n! / (k! · (n-k)!).
    Implementación estable que evita calcular factoriales gigantes:
    C(n, k) = ∏ (n-i+1)/i para i de 1 a k.
    
    :param n: Número total de elementos (entero no negativo).
    :param k: Número de elementos a elegir (entero no negativo).
    :return: C(n, k).
    :requisitos: 0 ≤ k ≤ n
    """
    if k < 0 or k > n:
        print("Debe cumplirse 0 ≤ k ≤ n.")
        resultado=None
    else:
        resultado = 1
        for i in range(1, k + 1):
            resultado = resultado * (n - i + 1) // i
    return resultado


# ---------------------------------------------------------------------
# Si se ejecuta el módulo directamente, lanzamos algunos tests rápidos.
# Si se importa desde otro programa, este bloque NO se ejecuta.
# ---------------------------------------------------------------------

if __name__ == "__main__":
    print("Tests rápidos del módulo matematicas.py")
    print(f"  mcd(48, 18) = {mcd(48, 18)} (esperado: 6)")
    print(f"  mcm(4, 6) = {mcm(4, 6)} (esperado: 12)")
    print(f"  es_primo(7) = {es_primo(7)} (esperado: True)")
    print(f"  inverso_modular(7, 5) = {inverso_modular(7, 5)} (esperado: 3)")
    print(f"  raiz_babilonica(2) = {raiz_babilonica(2):.12f}")
    print(f"  math.sqrt(2)        = {math.sqrt(2):.12f}")
    print(f"  factorial(5) = {factorial(5)} (esperado: 120)")
    print(f"  combinatorio(5, 2) = {combinatorio(5, 2)} (esperado: 10)")