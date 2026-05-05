"""
Programa con bugs deliberados para practicar depuración.

Se supone que este script cuenta cuántos números pares hay en una lista.
Tiene un bug; encuéntralo usando print debugging, pdb o el depurador de
VS Code.

Para depurar con pdb desde la terminal:
    python programa_con_bugs.py
La línea con `breakpoint()` detendrá la ejecución.

Tema 4 - Introducción a la Computación Científica (ICC).
"""


def contar_pares(numeros):
    contador = 0
    for n in numeros:
        breakpoint()           # ← descomenta esta línea para depurar con pdb
        if n % 2 == 0:
            contador = 1       # 🐛 BUG aquí: ¿debería ser 'contador += 1'?
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
