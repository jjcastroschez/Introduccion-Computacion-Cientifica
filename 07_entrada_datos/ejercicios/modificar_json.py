"""
Ejercicio 5 — Modificar un JSON y guardarlo.

Carga libro.json, incrementa el número de páginas en 10, añade un
nuevo tema a la lista 'temas' y guarda el resultado en libro_modificado.json.

Muestra el patrón típico de modificación: leer → modificar → escribir.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import json


def main():
    # 1) Leer el JSON
    with open("libro.json", "r") as f:
        datos = json.load(f)

    print("--- Datos originales ---")
    print(f"Título:   {datos['titulo']}")
    print(f"Páginas:  {datos['paginas']}")
    print(f"Temas:    {datos['temas']}")

    # 2) Modificar
    datos["paginas"] = datos["paginas"] + 10   # nueva edición con más páginas
    datos["temas"].append("edición ampliada")   # añadir un tema

    print("\n--- Datos modificados ---")
    print(f"Título:   {datos['titulo']}")
    print(f"Páginas:  {datos['paginas']}")
    print(f"Temas:    {datos['temas']}")

    # 3) Guardar
    with open("libro_modificado.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

    print("\n✅ libro_modificado.json guardado.")


if __name__ == "__main__":
    main()
