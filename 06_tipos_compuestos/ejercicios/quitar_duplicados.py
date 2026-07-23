"""
Ejercicio 8 — Quitar duplicados preservando el orden.

`set(lista)` elimina duplicados PERO destruye el orden. Cuando queremos
mantener el orden de la PRIMERA aparición de cada elemento, hay que
combinar un CONJUNTO (para saber "qué ya hemos visto") con una LISTA
(para conservar el orden).

Es un patrón muy útil.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def quitar_duplicados(lista: list) -> list:
    """
    Devuelve una nueva lista con los elementos de `lista` sin duplicados,
    conservando el orden de la primera aparición.
    :param lista: lista de elementos (pueden ser de cualquier tipo)
    :return: nueva lista sin duplicados, en el mismo orden de aparición
    """
    vistos = set()
    resultado = []
    for x in lista:
        if x not in vistos:            # ← chequeo rapidísimo con set
            resultado.append(x)
            vistos.add(x)
    return resultado


def main():
    a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
    print(f"Original:               {a}")
    print(f"set(a) (pierde orden):  {sorted(set(a))}")
    print(f"quitar_duplicados:      {quitar_duplicados(a)}")

    palabras = ["hola", "mundo", "hola", "python", "mundo", "chao"]
    print(f"\nPalabras:               {palabras}")
    print(f"quitar_duplicados:      {quitar_duplicados(palabras)}")


if __name__ == "__main__":
    main()
