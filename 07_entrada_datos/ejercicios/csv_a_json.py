"""
Ejercicio 6 — Convertir un CSV a JSON.

Lee notas_clase.csv y produce un JSON con la misma información pero
estructurado como lista de diccionarios. Cada estudiante será un objeto
JSON con sus tres campos.

Este ejercicio muestra cómo combinar los dos formatos: leer con csv
y escribir con json.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import csv
import json


def csv_a_json(csv_origen: str, json_destino: str) -> int:
    """
    Convierte csv_origen (con cabeceras) en json_destino (lista de dicts).
    Devuelve el número de registros convertidos.
    """
    estudiantes = []

    with open(csv_origen, "r") as f:
        for fila in csv.DictReader(f):
            # Convertir tipos: los CSV vienen como strings
            estudiantes.append({
                "nombre": fila["nombre"],
                "curso":  int(fila["curso"]),
                "nota":   float(fila["nota"]),
            })

    with open(json_destino, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, indent=2, ensure_ascii=False)

    return len(estudiantes)


def main():
    n = csv_a_json("notas_clase.csv", "notas_clase.json")
    print(f"✅ Convertidos {n} estudiantes a notas_clase.json\n")

    # Verificación: leer el JSON y mostrar
    with open("notas_clase.json") as f:
        contenido = f.read()
    print("--- Primeros 500 caracteres del JSON ---")
    print(contenido[:500])
    print("...")


if __name__ == "__main__":
    main()
