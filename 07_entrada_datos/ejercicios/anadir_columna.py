"""
Ejercicio 3 — Añadir una columna calculada a un CSV.

Dado el fichero notas_clase.csv, genera un CSV nuevo con una columna
adicional 'estado' cuyo valor es 'Aprobado' o 'Suspenso' según si la
nota es >= 5 o < 5.

Es un patrón MUY habitual en análisis de datos: leer, calcular, escribir.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import csv


def anadir_estado(csv_origen: str, csv_destino: str) -> None:
    """Lee csv_origen, añade la columna 'estado', y escribe en csv_destino."""

    with open(csv_origen, "r") as fin:
        lector = csv.DictReader(fin)

        # Los campos originales + el nuevo
        campos = list(lector.fieldnames) + ["estado"]

        with open(csv_destino, "w", newline="") as fout:
            escritor = csv.DictWriter(fout, fieldnames=campos)
            escritor.writeheader()

            for fila in lector:
                nota = float(fila["nota"])
                fila["estado"] = "Aprobado" if nota >= 5 else "Suspenso"
                escritor.writerow(fila)


def main():
    anadir_estado("notas_clase.csv", "notas_con_estado.csv")
    print("✅ Fichero notas_con_estado.csv creado.\n")

    # Mostramos el resultado
    print("--- Contenido ---")
    with open("notas_con_estado.csv") as f:
        print(f.read())


if __name__ == "__main__":
    main()
