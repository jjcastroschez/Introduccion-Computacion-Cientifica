"""
Ejemplo — Análisis léxico de un fichero de texto.

Lee un fichero completo y calcula:
  - Número total de palabras y palabras distintas.
  - Palabra más larga y palabra más frecuente.
  - Longitud media de las palabras.
  - Frecuencia de cada letra del alfabeto.

Este ejemplo combina I/O con lo aprendido en el T6 sobre
diccionarios: son la estructura ideal para acumular frecuencias.

Tema 7 - Introducción a la Computación Científica (ICC).
"""


def leer_palabras(fichero: str) -> list:
    """Lee el fichero y devuelve la lista de palabras en minúsculas, sin puntuación.
    :param fichero: nombre del fichero de texto (string)
    :return: lista de palabras (list)"""
    with open(fichero, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Quitamos los signos de puntuación más comunes y separamos
    for signo in ".,;:!?()¿¡\"'":
        contenido = contenido.replace(signo, " ")

    return contenido.lower().split()


def frecuencias(palabras: list) -> dict:
    """Devuelve un dict {palabra: cuántas_veces_aparece}.
    :param palabras: lista de palabras (list)
    :return: diccionario con la frecuencia de cada palabra (dict)"""
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador


def letras(palabras: list) -> dict:
    """Frecuencia de cada letra alfabética.
    :param palabras: lista de palabras (list)
    :return: diccionario con la frecuencia de cada letra (dict)"""
    conteo = {}
    for palabra in palabras:
        for letra in palabra:
            if letra.isalpha():
                conteo[letra] = conteo.get(letra, 0) + 1
    return conteo


def main():
    fichero = "texto.txt"
    palabras = leer_palabras(fichero)

    # Estadísticas globales
    print(f"═══ Análisis de '{fichero}' ═══\n")
    print(f"Palabras totales:    {len(palabras)}")
    print(f"Palabras distintas:  {len(set(palabras))}")

    # Longitud media
    longitud_total = sum(len(p) for p in palabras)
    print(f"Longitud media:      {longitud_total / len(palabras):.2f} letras")

    # Palabra más larga
    mas_larga = max(palabras, key=len)
    print(f"Palabra más larga:   '{mas_larga}' ({len(mas_larga)} letras)")

    # Top 5 palabras más frecuentes
    print("\n─── Top 5 palabras más frecuentes ───")
    frecs = frecuencias(palabras)
    ordenadas = sorted(frecs.items(), key=lambda par: par[1], reverse=True)
    for palabra, veces in ordenadas[:5]:
        print(f"  {palabra:15} → {veces} veces")

    # Top 5 letras
    print("\n─── Top 5 letras más frecuentes ───")
    letras_frec = letras(palabras)
    ordenadas_l = sorted(letras_frec.items(), key=lambda par: par[1], reverse=True)
    for letra, veces in ordenadas_l[:5]:
        barra = "█" * (veces // 2)
        print(f"  {letra} ({veces:2}) {barra}")


if __name__ == "__main__":
    main()
