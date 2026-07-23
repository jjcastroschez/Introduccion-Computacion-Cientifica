"""
Datos de profesores — combinando listas, tuplas y desempaquetado.

Modelamos un grupo de profesores como una LISTA de TUPLAS, donde cada
tupla contiene los datos de un profesor: (nombre, correo, asignatura,
curso, cuatrimestre).

Este ejemplo enseña:
  - Cómo estructurar información con listas de tuplas.
  - Cómo recorrer con `for` y `for` con desempaquetado.
  - Cómo filtrar información por atributos.
  - Cómo ordenar por una clave.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def main():
    # Cada tupla: (nombre, correo, asignatura, curso, cuatrimestre)
    profesores = [
        ("Pepe",        "pepe@uclm.es",     "ICC",         1, 2),
        ("Ricardo",     "ricardo@uclm.es",  "Álgebra",     1, 1),
        ("José Carlos", "jcarlos@uclm.es",  "Análisis",    1, 1),
        ("Javier",      "javier@uclm.es",   "Geometría",   2, 1),
        ("Juan",        "juan@uclm.es",     "Estadística", 2, 2),
        ("Cristina",    "cris@uclm.es",     "Numérica",    3, 1),
    ]

    # 1) Recorrido simple: mostrar solo nombres
    print("=== Todos los profesores ===")
    for prof in profesores:
        print(f"  {prof[0]}")   # acceso por índice

    # 2) Recorrido con desempaquetado (mucho más legible)
    print("\n=== Datos completos ===")
    for nombre, correo, asig, curso, cuat in profesores:
        print(f"  {nombre:12} imparte {asig:14} en {curso}º curso, {cuat}º cuatrimestre")

    # 3) Filtrar por curso: solo los de segundo
    print("\n=== Solo los de 2º ===")
    for nombre, correo, asig, curso, cuat in profesores:
        if curso == 2:
            print(f"  {nombre} ({asig})")

    # 4) Ordenar por curso y luego por cuatrimestre usando sorted + lambda
    print("\n=== Ordenados por curso y cuatrimestre ===")
    ordenados = sorted(profesores, key=lambda p: (p[3], p[4]))
    for nombre, _, asig, curso, cuat in ordenados:
        print(f"  {curso}º-{cuat}º: {nombre} ({asig})")


if __name__ == "__main__":
    main()
