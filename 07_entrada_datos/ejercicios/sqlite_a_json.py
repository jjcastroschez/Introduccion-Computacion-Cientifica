"""
Ejercicio 10 — Exportar el contenido de una tabla SQLite a JSON.

Lee la tabla Alumnos de clase.db (creada en el ejercicio 8) y exporta
todo su contenido a un fichero JSON.

Este ejercicio muestra el flujo inverso al 8: BBDD → JSON.
Es útil para hacer copias de seguridad, enviar datos a un servicio
web, o publicar datos abiertos.

Requisito previo: haber ejecutado el ejercicio 8 (csv_a_sqlite.py)
antes, para tener clase.db con datos.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import json
import sqlite3


def exportar_tabla_a_json(bbdd: str, tabla: str, fichero_json: str) -> int:
    """
    Lee todos los registros de 'tabla' en 'bbdd' y los guarda como JSON.
    Devuelve el número de registros exportados.
    """
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    # Obtener el nombre de las columnas
    cursor.execute(f"SELECT * FROM {tabla}")
    columnas = [descripcion[0] for descripcion in cursor.description]

    # Convertir cada fila (tupla) en dict
    registros = []
    for fila in cursor.fetchall():
        registro = {}
        for i, columna in enumerate(columnas):
            registro[columna] = fila[i]
        registros.append(registro)

    conexion.close()

    # Guardar como JSON
    with open(fichero_json, "w", encoding="utf-8") as f:
        json.dump(registros, f, indent=2, ensure_ascii=False)

    return len(registros)


def main():
    n = exportar_tabla_a_json("clase.db", "Alumnos", "alumnos_export.json")
    print(f"✅ {n} registros exportados a alumnos_export.json\n")

    # Mostrar una muestra
    with open("alumnos_export.json") as f:
        contenido = f.read()
    print("--- Primeros 400 caracteres ---")
    print(contenido[:400])
    print("...")


if __name__ == "__main__":
    main()
