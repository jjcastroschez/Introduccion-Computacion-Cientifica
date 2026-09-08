"""
Ejercicio 4 — Filtrar un CSV según una condición.

Dado el fichero notas_clase.csv, escribe un CSV con solo los estudiantes
que han obtenido nota >= 7 (notables o superiores), MANTENIENDO exactamente
las mismas columnas.

El patrón que usarás aparecerá en muchos programas de análisis de datos.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import csv


def filtrar_csv(origen: str, destino: str, umbral: float = 7.0) -> int:
    """
    Copia de origen a destino solo las filas con nota >= umbral.
    Devuelve el número de filas escritas.
    """
    n = 0
    with open(origen, "r") as fin:
        lector = csv.DictReader(fin)

        with open(destino, "w", newline="") as fout:
            escritor = csv.DictWriter(fout, fieldnames=lector.fieldnames)
            escritor.writeheader()

            for fila in lector:
                if float(fila["nota"]) >= umbral:
                    escritor.writerow(fila)
                    n = n + 1
    return n


def main():
    n = filtrar_csv("notas_clase.csv", "notables.csv", umbral=7.0)
    print(f"✅ Escritos {n} estudiantes con nota >= 7 en notables.csv\n")

    print("--- Contenido ---")
    with open("notables.csv") as f:
        print(f.read())


if __name__ == "__main__":
    main()
