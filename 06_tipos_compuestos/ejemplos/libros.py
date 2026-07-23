"""
Representar un libro — tres formas: dict, namedtuple y dataclass.

Cuando queremos agrupar datos heterogéneos (título, autor, año...) bajo
un mismo objeto, Python nos da varias opciones. Este ejemplo compara
las tres principales para que veas las diferencias en la práctica.

Tema 6 - Introducción a la Computación Científica (ICC).
"""

from collections import namedtuple
from dataclasses import dataclass


# ---------------------------------------------------------------------
# OPCIÓN 1 — diccionario
# ---------------------------------------------------------------------

def crear_libro_dict(titulo: str, autor: str, anio: int, paginas: int) -> dict:
    """Crea un libro representado como un diccionario.
    
    :param titulo: título del libro (string)
    :param autor: autor del libro (string)
    :param anio: año de publicación (int)
    :param paginas: número de páginas (int)
    :return: diccionario con los datos del libro
    """
    return {
        "titulo": titulo,
        "autor": autor,
        "año": anio,
        "paginas": paginas,
    }


# ---------------------------------------------------------------------
# OPCIÓN 2 — namedtuple (inmutable, ligera)
# ---------------------------------------------------------------------

Libro = namedtuple("Libro", ["titulo", "autor", "anio", "paginas"])


# ---------------------------------------------------------------------
# OPCIÓN 3 — dataclass (mutable, moderna)
# ---------------------------------------------------------------------

@dataclass
class LibroDC:
    titulo: str
    autor: str
    anio: int
    paginas: int


# ---------------------------------------------------------------------
# Programa principal — mostrar las tres opciones
# ---------------------------------------------------------------------

def main():
    print("=" * 60)
    print("Opción 1: DICCIONARIO")
    print("=" * 60)
    d = crear_libro_dict("Bowie: Una Biografía", "M. Hesse", 2019, 167)
    print(f"Acceso:      d['titulo']  = {d['titulo']}")
    print(f"Con get:     d.get('anio') = {d.get('anio')}")
    d["isbn"] = "978-84-264-0465-7"      # se puede añadir claves nuevas
    print(f"Añadido isbn: {d['isbn']}")
    d["paginas"] = 200                    # y modificar existentes
    print(f"Modificado paginas → {d['paginas']}")
    print(f"Todas las claves: {list(d.keys())}")

    print()
    print("=" * 60)
    print("Opción 2: NAMEDTUPLE")
    print("=" * 60)
    nt = Libro("Bowie: Una Biografía", "M. Hesse", 2019, 167)
    print(f"Acceso por nombre:  nt.titulo = {nt.titulo}")
    print(f"Acceso por índice:  nt[0]     = {nt[0]}")
    print(f"Desempaquetado: título, autor, ano, paginas = nt")
    titulo, autor, anio, paginas = nt
    print(f"  → título={titulo!r}, autor={autor!r}, año={anio}, páginas={paginas}")
    try:
        nt.paginas = 200
    except AttributeError as e:
        print(f"⚠️ Intentar modificar → AttributeError: {e}")

    print()
    print("=" * 60)
    print("Opción 3: DATACLASS")
    print("=" * 60)
    dc = LibroDC("Bowie: Una Biografía", "M. Hesse", 2019, 167)
    print(f"Acceso:            dc.titulo = {dc.titulo}")
    print(f"Repr automático:   {dc}")
    dc.paginas = 200                     # ✅ mutable
    print(f"Modificado:        dc.paginas = {dc.paginas}")


if __name__ == "__main__":
    main()
