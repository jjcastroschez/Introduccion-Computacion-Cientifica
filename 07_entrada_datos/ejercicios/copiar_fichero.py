"""
Ejercicio 1 — Copiar un fichero de texto línea a línea.

Función que recibe dos rutas de fichero (origen y destino) y copia
el contenido del primero al segundo, sin modificarlo.

Es un patrón muy útil como base de otros ejercicios: leer, procesar,
escribir. Aquí no procesamos nada, solo copiamos.

Tema 7 - Introducción a la Computación Científica (ICC).
"""


def copiar_fichero(origen: str, destino: str) -> int:
    """
    Copia todas las líneas de 'origen' a 'destino'.
    Devuelve el número de líneas copiadas.
    """
    n = 0
    with open(origen, "r") as fin, open(destino, "w") as fout:
        for linea in fin:
            fout.write(linea)
            n = n + 1
    return n


def main():
    lineas = copiar_fichero("mensaje.txt", "copia.txt")
    print(f"✅ Copiadas {lineas} líneas de 'mensaje.txt' a 'copia.txt'")

    # Verificamos
    print("\n--- Contenido de la copia ---")
    with open("copia.txt") as f:
        print(f.read())


if __name__ == "__main__":
    main()
