"""
🎯 Reto final del Tema 6 — Análisis de texto.

⚠️ Este archivo contiene SOLO el esqueleto. La solución es PARA TI.
No hay versión "corregida" publicada en el repositorio. ¡Hazlo tú!

----------------------------------------------------------------------
ENUNCIADO

Escribe un programa que, dado un texto (una cadena), calcule y muestre
las siguientes estadísticas:

  1. Número total de PALABRAS (separando por espacios).
  2. Número de palabras DISTINTAS.
  3. Longitud media de las palabras.
  4. Las 5 PALABRAS más frecuentes (con su número de apariciones).
  5. Las palabras que aparecen SOLO UNA VEZ (a esto se le llama
     "hapax legomena" en lingüística).
  6. Las palabras de longitud ≥ 6 que aparecen al menos 2 veces
     (palabras "largas y frecuentes").

Debes normalizar el texto:
  * Pasar a minúsculas.
  * Quitar signos de puntuación: , . ; : ! ? ¡ ¿ " ' ( )
  * Separar por espacios (usa .split()).

----------------------------------------------------------------------
PISTAS

  * Los apartados 1-3 se resuelven con `.split()`, `set()`, `len()`, `sum()`.
  * El apartado 4 es como el Ejemplo 7 de contador de palabras.
  * El apartado 5 requiere iterar sobre el diccionario y quedarse
    con las claves cuyo valor sea 1.
  * El apartado 6 combina un filtro por longitud (len(palabra) >= 6)
    con un filtro por frecuencia (contador[palabra] >= 2). Se puede
    hacer con dos filter() encadenados o con un bucle.

----------------------------------------------------------------------
DATOS DE PRUEBA

texto = '''
La ciencia es una forma de pensar mucho más que un conjunto de
conocimientos. La ciencia nos enseña a dudar. Dudar es fundamental.
La computación científica combina matemáticas y ciencia para resolver
problemas complejos. Los matemáticos que aprenden computación pueden
resolver problemas antes inaccesibles. La ciencia avanza dudando.
'''

Verifica que:
  * Total de palabras: 43 (aprox., depende de cómo cuentes)
  * Palabras distintas: al menos 30
  * Las palabras "ciencia" y "la" están entre las más frecuentes.

----------------------------------------------------------------------
★ PUNTOS EXTRA (opcional)

  ★ Calcula el "índice de riqueza léxica": palabras_distintas / palabras_totales.
    Es un ratio entre 0 y 1 que mide cuán variado es el vocabulario.
    Textos científicos suelen tener ~0.5-0.7.

  ★★ Encuentra la palabra MÁS LARGA del texto. Si hay empates, devuelve
     todas las palabras más largas.

  ★★★ Encuentra las palabras que son ANAGRAMAS de otras en el texto.
     Dos palabras son anagramas si contienen exactamente las mismas
     letras (con las mismas frecuencias) pero en distinto orden.
     Ejemplo: "amor" y "roma" son anagramas.
     Pista: dos palabras son anagramas ↔ sorted(p1) == sorted(p2).

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def analizar(texto: str) -> dict:
    """
    Devuelve un diccionario con las estadísticas del texto.

    Estructura esperada del resultado:
    {
        "total": int,
        "distintas": int,
        "longitud_media": float,
        "top5": [(palabra, veces), ...],
        "hapax": [palabra, palabra, ...],
        "largas_frecuentes": [palabra, palabra, ...],
    }
    :param texto: Texto a analizar.
    :return: Diccionario con las estadísticas.
    """
    # ← Escribe tu código aquí
    pass


def main():
    texto = """
    La ciencia es una forma de pensar mucho más que un conjunto de
    conocimientos. La ciencia nos enseña a dudar. Dudar es fundamental.
    La computación científica combina matemáticas y ciencia para resolver
    problemas complejos. Los matemáticos que aprenden computación pueden
    resolver problemas antes inaccesibles. La ciencia avanza dudando.
    """

    resultado = analizar(texto)

    # ← Muestra los resultados de forma bonita
    pass


if __name__ == "__main__":
    main()
