"""
Ejercicio 9 — Operaciones matemáticas sobre matriculados.

Dados los conjuntos de estudiantes matriculados en tres asignaturas,
responde a estas preguntas usando SOLO operaciones de conjuntos.

Es un ejercicio muy natural para un matemático: los operadores
|, &, - son literalmente los mismos que en teoría de conjuntos.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def alumnos_en_al_menos_una(a: set, b: set, c: set) -> set:
    """Unión: matriculados en al menos una asignatura.
    :param a: conjunto de alumnos de la asignatura A
    :param b: conjunto de alumnos de la asignatura B
    :param c: conjunto de alumnos de la asignatura C
    :return: conjunto de alumnos matriculados en al menos una asignatura"""
    return a | b | c


def alumnos_en_las_tres(a: set, b: set, c: set) -> set:
    """Intersección: matriculados en las tres a la vez.
    :param a: conjunto de alumnos de la asignatura A
    :param b: conjunto de alumnos de la asignatura B
    :param c: conjunto de alumnos de la asignatura C
    :return: conjunto de alumnos matriculados en las tres asignaturas
    """
    return a & b & c


def alumnos_solo_en_a(a: set, b: set, c: set) -> set:
    """Diferencia: en a pero no en las otras dos.
    :param a: conjunto de alumnos de la asignatura A
    :param b: conjunto de alumnos de la asignatura B
    :param c: conjunto de alumnos de la asignatura C
    :return: conjunto de alumnos matriculados solo en la asignatura A"""
    return a - b - c


def alumnos_en_exactamente_una(a: set, b: set, c: set) -> set:
    """
    Matriculados en EXACTAMENTE una de las tres.
    Truco: unión menos los que están en al menos dos.
    :param a: conjunto de alumnos de la asignatura A
    :param b: conjunto de alumnos de la asignatura B
    :param c: conjunto de alumnos de la asignatura C
    :return: conjunto de alumnos matriculados en exactamente una asignatura
    """
    en_al_menos_dos = (a & b) | (a & c) | (b & c)
    return (a | b | c) - en_al_menos_dos


def alumnos_en_al_menos_dos(a: set, b: set, c: set) -> set:
    """Matriculados en al menos dos (unión de intersecciones dos a dos).
    :param a: conjunto de alumnos de la asignatura A
    :param b: conjunto de alumnos de la asignatura B
    :param c: conjunto de alumnos de la asignatura C
    :return: conjunto de alumnos matriculados en al menos dos asignaturas"""
    return (a & b) | (a & c) | (b & c)


def main():
    algebra    = {"Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos"}
    analisis   = {"Luis", "Marta", "Carlos", "Elena", "Diego"}
    geometria  = {"Luis", "Pedro", "Sofía", "Carlos", "Isabel"}

    print(f"Álgebra:   {sorted(algebra)}")
    print(f"Análisis:  {sorted(analisis)}")
    print(f"Geometría: {sorted(geometria)}\n")

    print("En al menos una:")
    print(f"  {sorted(alumnos_en_al_menos_una(algebra, analisis, geometria))}")

    print("\nEn las tres:")
    print(f"  {sorted(alumnos_en_las_tres(algebra, analisis, geometria))}")

    print("\nSolo en álgebra:")
    print(f"  {sorted(alumnos_solo_en_a(algebra, analisis, geometria))}")

    print("\nEn al menos dos:")
    print(f"  {sorted(alumnos_en_al_menos_dos(algebra, analisis, geometria))}")

    print("\nEn exactamente una:")
    print(f"  {sorted(alumnos_en_exactamente_una(algebra, analisis, geometria))}")


if __name__ == "__main__":
    main()