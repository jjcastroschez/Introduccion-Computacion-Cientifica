"""Funciones para sumar series y calcular términos de sucesiones."""


def suma_armonica(n: int) -> float:
    """
    Suma de los n primeros términos de la serie armónica:
    H_n = 1 + 1/2 + 1/3 + ... + 1/n
    
    :param n: número de términos a sumar (entero positivo)
    :return: suma de los n primeros términos (float)    
    """
    if n < 1:
        return 0.0
    s = 0.0
    for k in range(1, n + 1):
        s = s + 1 / k
    return s


def suma_aritmetica(primero: float, diferencia: float, n: int) -> float:
    """
    Suma de los n primeros términos de una progresión aritmética con primer
    término `primero` y diferencia `diferencia`.

    Usa la fórmula cerrada:  S_n = n * (2*a + (n-1)*d) / 2
    
    :param primero: primer término de la progresión (float)
    :param diferencia: diferencia entre términos consecutivos (float)
    :param n: número de términos a sumar (entero positivo)
    :return: suma de los n primeros términos (float)
    """
    return n * (2 * primero + (n - 1) * diferencia) / 2


def suma_geometrica(primero: float, razon: float, n: int) -> float:
    """
    Suma de los n primeros términos de una progresión geométrica con primer
    término `primero` y razón `razon` (razón ≠ 1).
    
    :param primero: primer término de la progresión (float)
    :param razon: razón entre términos consecutivos (float, distinto de 1)
    :param n: número de términos a sumar (entero positivo)
    :return: suma de los n primeros términos (float)
    """
    
    if razon == 1:
        return primero * n
    return primero * (1 - razon ** n) / (1 - razon)
