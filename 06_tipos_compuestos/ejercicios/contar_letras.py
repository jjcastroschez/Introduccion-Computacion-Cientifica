"""
Ejercicio 7 — Contador de letras.

Dado un texto, cuenta cuántas veces aparece CADA LETRA (a-z),
ignorando mayúsculas/minúsculas y sin contar espacios ni signos.

Es un problema de análisis de frecuencia útil en criptografía
clásica y en lingüística.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def contar_letras(texto: str) -> dict:
    """
    Devuelve un diccionario {letra: frecuencia} con solo las letras.
    :param texto: cadena de texto a analizar (string)
    :return: diccionario con la frecuencia de cada letra
    """
    contador = {}
    for c in texto.lower():
        if c.isalpha():                # solo letras, no espacios ni signos
            contador[c] = contador.get(c, 0) + 1
    return contador


def letras_mas_frecuentes(texto: str, n: int = 5) -> list:
    """Devuelve una lista de tuplas (letra, frecuencia) con las N más frecuentes.
    :param texto: cadena de texto a analizar (string)
    :param n: número de letras más frecuentes a devolver (int)
    :return: lista de tuplas (letra, frecuencia)"""
    c = contar_letras(texto)
    ordenado = sorted(c.items(), key=lambda par: par[1], reverse=True)
    return ordenado[:n]


def main():
    texto = "El rápido zorro marrón saltó sobre el perro perezoso"

    c = contar_letras(texto)
    print(f"Texto: '{texto}'")
    print(f"Letras distintas: {len(c)}")
    print(f"Total de letras:  {sum(c.values())}")

    print("\nTop 5 letras más frecuentes:")
    for letra, veces in letras_mas_frecuentes(texto, 5):
        barra = "★" * veces
        print(f"  '{letra}' : {veces:2d}  {barra}")

    # Comparación matemática: total de letras = suma de frecuencias
    total = sum(c.values())
    print(f"\n∑ frecuencias = {total}")


if __name__ == "__main__":
    main()
