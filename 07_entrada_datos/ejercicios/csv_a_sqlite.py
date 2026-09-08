"""
Ejercicio 8 — Cargar un CSV a una tabla de SQLite.

Este ejercicio combina CSV con SQLite: lee todos los estudiantes de
notas_clase.csv y los inserta en una tabla Alumnos de la BBDD clase.db.

Al final, muestra por pantalla el contenido de la tabla usando SELECT.

Es un patrón muy usado en la vida real: importar un CSV a una BBDD.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import csv
import sqlite3


def cargar_csv_a_bbdd(csv_origen: str, bbdd: str) -> int:
    """
    Carga notas_clase.csv en la tabla Alumnos de bbdd.
    Devuelve el número de filas insertadas.
    """
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    # Crear tabla y limpiar
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            curso INTEGER,
            nota REAL
        )
    """)
    cursor.execute("DELETE FROM Alumnos")

    # Cargar CSV
    n = 0
    with open(csv_origen, "r") as f:
        for fila in csv.DictReader(f):
            cursor.execute(
                "INSERT INTO Alumnos (nombre, curso, nota) VALUES (?, ?, ?)",
                (fila["nombre"], int(fila["curso"]), float(fila["nota"]))
            )
            n = n + 1

    conexion.commit()
    conexion.close()
    return n


def mostrar_alumnos(bbdd: str) -> None:
    """Muestra todos los alumnos ordenados por nota descendente."""
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, curso, nota FROM Alumnos ORDER BY nota DESC")
    print(f"{'Nombre':<20} {'Curso':>6} {'Nota':>6}")
    print("─" * 34)
    for nombre, curso, nota in cursor.fetchall():
        print(f"{nombre:<20} {curso:>6} {nota:>6.2f}")

    conexion.close()


def main():
    n = cargar_csv_a_bbdd("notas_clase.csv", "clase.db")
    print(f"✅ {n} alumnos cargados en clase.db\n")

    mostrar_alumnos("clase.db")


if __name__ == "__main__":
    main()
