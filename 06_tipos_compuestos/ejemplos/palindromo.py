"""
Palíndromo — trabajando con cadenas.

Un palíndromo es una palabra o frase que se lee igual de izquierda a
derecha que de derecha a izquierda. Este ejemplo muestra cómo aplicar
métodos de string (lower, replace) y slicing para resolver un problema
clásico de forma muy elegante.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def es_palindromo(texto: str) -> bool:
    """
    Devuelve True si texto es un palíndromo, ignorando mayúsculas,
    espacios y signos de puntuación.

    Estrategia:
      1. Normalizamos el texto: minúsculas y sin espacios/puntuación.
      2. Comparamos con su versión invertida (slicing [::-1]).
    
    :param texto: Texto que se quiere comprobar si es palíndromo.  
    :return: True si es palíndromo, False en caso contrario.  
    """
    # Paso 1: pasar a minúsculas
    normalizado = texto.lower()

    # Paso 2: quitar espacios y signos comunes
    normalizado = normalizado.replace(" ", "")
    for signo in ",.;:!?¡¿-'\"()":
        normalizado = normalizado.replace(signo, "")

    # Paso 3: comparar con su inverso usando slicing
    return normalizado == normalizado[::-1]


def main():
    ejemplos = (
        "Ana",
        "reconocer",
        "hola",
        "A ti no, bonita",
        "Somos o no somos",
        "Casa",
        "Anita lava la tina",
    )
    for frase in ejemplos:
        marca = "✅" if es_palindromo(frase) else "❌"
        print(f"  {marca}  '{frase}'")


if __name__ == "__main__":
    main()
