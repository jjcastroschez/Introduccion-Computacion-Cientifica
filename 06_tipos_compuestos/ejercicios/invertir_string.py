"""
Ejercicio 2 — Invertir una cadena SIN usar slicing [::-1].

El objetivo es consolidar los patrones de recorrido de cadenas
que aprendimos en el Tema 4, ahora aplicados al Tema 6.
Después comparamos con la versión "elegante" con slicing.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def invertir_manual(texto: str) -> str:
    """
    Invierte una cadena carácter a carácter, sin usar slicing.

    Estrategia: recorremos el texto original y vamos concatenando
    cada carácter al principio del resultado.
    :param texto: cadena de caracteres (string)
    :return resultado: cadena invertida (string)
    """
    resultado = ""
    for letra in texto:
        resultado = letra + resultado    # 🔑 letra AL PRINCIPIO
    return resultado


def invertir_slicing(texto: str) -> str:
    """Versión elegante con slicing (para comparar).
    :param texto: cadena de caracteres (string)
    :return: cadena invertida (string)"""
    return texto[::-1]


def main():
    print(f"invertir_manual('hola')       = '{invertir_manual('hola')}'")
    print(f"invertir_manual('reconocer')  = '{invertir_manual('reconocer')}'")
    print(f"invertir_manual('Python')     = '{invertir_manual('Python')}'")
    print(f"invertir_manual('')           = '{invertir_manual('')}'")

    print("\nComparación con la versión slicing:")
    for palabra in ("hola", "reconocer", "Python"):
        m = invertir_manual(palabra)
        s = invertir_slicing(palabra)
        marca = "✅" if m == s else "❌" # Interesante asignación condicional
        print(f"  {palabra:15} → manual='{m}' slicing='{s}' {marca}")


if __name__ == "__main__":
    main()
