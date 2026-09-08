"""
Ejemplo — Fusionar dos CSVs por una clave común.

Muchas veces los datos vienen repartidos en varios ficheros:
  - estudiantes.csv     : dni, nombre, curso
  - calificaciones.csv  : dni, algebra, analisis, programacion

Queremos combinar ambos en un único CSV, cruzando por 'dni'. Es el
equivalente informal de un JOIN en SQL, pero hecho a mano con
diccionarios (T6) y ficheros (T7).

Además calculamos una columna nueva 'media' con la nota media del
estudiante en las tres asignaturas.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import csv


def leer_calificaciones(fichero: str) -> dict:
    """
    Devuelve un dict {dni: {algebra:.., analisis:.., programacion:..}}
    Usar el DNI como clave hace la búsqueda posterior ¡instantánea!
    """
    califs = {}
    with open(fichero, "r") as f:
        for fila in csv.DictReader(f):
            dni = fila["dni"]
            califs[dni] = {
                "algebra":      float(fila["algebra"]),
                "analisis":     float(fila["analisis"]),
                "programacion": float(fila["programacion"]),
            }
    return califs


def fusionar(csv_estudiantes: str, csv_calificaciones: str, csv_salida: str) -> int:
    """
    Une los dos CSVs por DNI y escribe un CSV combinado con:
    dni, nombre, curso, algebra, analisis, programacion, media
    """
    calificaciones = leer_calificaciones(csv_calificaciones)

    campos = ["dni", "nombre", "curso", "algebra", "analisis", "programacion", "media"]
    n_escritas = 0

    with open(csv_estudiantes, "r") as fin, open(csv_salida, "w", newline="") as fout:
        lector = csv.DictReader(fin)
        escritor = csv.DictWriter(fout, fieldnames=campos)
        escritor.writeheader()

        for fila in lector:
            dni = fila["dni"]

            # ¿Tenemos calificaciones para este DNI?
            if dni not in calificaciones:
                print(f"⚠️  Sin notas para {fila['nombre']} ({dni})")
                continue

            notas = calificaciones[dni]
            media = (notas["algebra"] + notas["analisis"] + notas["programacion"]) / 3

            # Construimos la fila fusionada
            fila_completa = {
                "dni":          dni,
                "nombre":       fila["nombre"],
                "curso":        fila["curso"],
                "algebra":      notas["algebra"],
                "analisis":     notas["analisis"],
                "programacion": notas["programacion"],
                "media":        round(media, 2),
            }
            escritor.writerow(fila_completa)
            n_escritas = n_escritas + 1

    return n_escritas


def main():
    n = fusionar("estudiantes.csv", "calificaciones.csv", "expediente.csv")
    print(f"✅ Fusionadas {n} filas → expediente.csv\n")

    print("─── Contenido de expediente.csv ───")
    with open("expediente.csv") as f:
        print(f.read())


if __name__ == "__main__":
    main()
