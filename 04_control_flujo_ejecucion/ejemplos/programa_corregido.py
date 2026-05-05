"""
Versión corregida de `programa_con_bugs.py`.

⚠️ ¡No mires este archivo hasta haber intentado encontrar y arreglar
el bug tú mismo! El proceso de depurar es lo que se aprende.

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def contar_pares(numeros):
    contador = 0
    for n in numeros:
        if n % 2 == 0:
            contador = contador + 1     # ✅ ahora INCREMENTA
    return contador


def main():
    numeros = [4, 7, 12, 5, 8, 3, 10, 1, 6, 9]
    pares = contar_pares(numeros)

    esperado = 5
    print(f"Pares contados: {pares}")
    print(f"Pares reales:   {esperado}")
    if pares == esperado:
        print("✅ Correcto.")
    else:
        print(f"❌ Hay un bug. Diferencia: {esperado - pares}")


if __name__ == "__main__":
    main()
