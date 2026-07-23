"""
Conjuntos: eliminar duplicados y operaciones matemáticas.

Los conjuntos (set) son perfectos para dos escenarios:
  1) Eliminar duplicados de una colección.
  2) Realizar operaciones matemáticas sobre conjuntos (unión,
     intersección, diferencia, diferencia simétrica).

En Python, los operadores de estas operaciones (|, &, -, ^) son
LITERALMENTE los mismos que en teoría de conjuntos matemática.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def main():
    # -----------------------------------------------------------------
    # 1) Eliminar duplicados
    # -----------------------------------------------------------------
    print("1) Eliminar duplicados con set(...)")
    print("-" * 40)
    notas_con_repes = [7, 5, 8, 5, 7, 9, 10, 7, 5, 8]
    notas_unicas = set(notas_con_repes)
    print(f"  Original:      {notas_con_repes}")
    print(f"  Únicas:        {notas_unicas}")
    print(f"  → Distintas:   {len(notas_unicas)}\n")

    # -----------------------------------------------------------------
    # 2) Operaciones matemáticas
    # -----------------------------------------------------------------
    print("2) Operaciones matemáticas de conjuntos")
    print("-" * 40)
    matriculados_algebra   = {"Ana", "Luis", "Marta", "Pedro", "Sofía"}
    matriculados_analisis  = {"Luis", "Marta", "Carlos", "Elena"}

    print(f"  Álgebra:  {sorted(matriculados_algebra)}")
    print(f"  Análisis: {sorted(matriculados_analisis)}\n")

    union = matriculados_algebra | matriculados_analisis
    print(f"  Unión (matriculados en alguna): {sorted(union)}")

    interseccion = matriculados_algebra & matriculados_analisis
    print(f"  Intersección (en las dos):      {sorted(interseccion)}")

    solo_algebra = matriculados_algebra - matriculados_analisis
    print(f"  Solo en álgebra:                {sorted(solo_algebra)}")

    solo_una = matriculados_algebra ^ matriculados_analisis
    print(f"  Solo en una (dif. simétrica):   {sorted(solo_una)}\n")

    # -----------------------------------------------------------------
    # 3) Uso más allá: comprobar pertenencia rápidamente
    # -----------------------------------------------------------------
    print("3) Pertenencia con in — rapidísimo, incluso con muchos elementos")
    print("-" * 40)
    vocales = {"a", "e", "i", "o", "u"}
    palabra = "murcielago"
    solo_vocales = ""
    for letra in palabra:
        if letra in vocales:
            solo_vocales = solo_vocales + letra
    print(f"  Vocales de '{palabra}': '{solo_vocales}'")

    # -----------------------------------------------------------------
    # 4) Método de conjuntos: add, remove, discard
    # -----------------------------------------------------------------
    print("\n4) Modificar un conjunto")
    print("-" * 40)
    numeros = {1, 2, 3}
    print(f"  Inicial:    {numeros}")
    numeros.add(4)
    print(f"  Tras add(4): {numeros}")
    numeros.add(2)                          # ya estaba: no cambia nada
    print(f"  Tras add(2) (que ya estaba): {numeros}")
    numeros.discard(3)
    print(f"  Tras discard(3): {numeros}")
    numeros.discard(99)                     # no estaba, sin error
    print(f"  Tras discard(99) (no estaba): {numeros}")


if __name__ == "__main__":
    main()
