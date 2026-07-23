"""
Contador de palabras con diccionario.

Dado un texto, cuenta cuántas veces aparece cada palabra. Es un ejemplo
clásico donde el diccionario brilla: la clave es la palabra y el valor
es su contador. Se usa .get() con valor por defecto para simplificar
la lógica de incremento.

Este ejemplo muestra también:
  - Métodos de string: lower(), split()
  - El método .get() de diccionarios con valor por defecto
  - Iteración sobre un diccionario con .items()
  - Ordenar un diccionario por valor usando sorted() con key

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def contar_palabras(texto: str) -> dict:
    """
    Devuelve un diccionario {palabra: número_de_apariciones}
    a partir de un texto.

    Normaliza pasando a minúsculas y eliminando puntuación básica.
    :param texto: Texto a analizar (string)
    :return: Diccionario con palabras y su número de apariciones
    """
    # Normalización: minúsculas y quitar puntuación
    texto = texto.lower()
    for signo in ",.;:!?¡¿()\"'":
        texto = texto.replace(signo, "")

    # Contar cada palabra
    contador = {}
    for palabra in texto.split():
        # .get(clave, 0) devuelve 0 si la palabra no está aún → +1 = 1
        # Si ya existe, devuelve su valor actual → +1 lo incrementa
        contador[palabra] = contador.get(palabra, 0) + 1

    return contador


def main():
    texto = (
        "La ciencia es una forma de pensar mucho más que "
        "un conjunto de conocimientos. La ciencia nos enseña a dudar."
    )

    print(f"Texto: '{texto}'\n")

    contador = contar_palabras(texto)

    # Ordenar por número de apariciones (de más a menos)
    ordenado = sorted(contador.items(), key=lambda par: par[1], reverse=True)

    print(f"Palabras totales:   {sum(contador.values())}")
    print(f"Palabras distintas: {len(contador)}\n")

    print("Ranking de palabras:")
    for palabra, veces in ordenado:
        marca = "★" * veces
        print(f"  {palabra:15} {veces:3d}  {marca}")


if __name__ == "__main__":
    main()
