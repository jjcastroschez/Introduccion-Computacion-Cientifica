"""
Ejemplo — Base de datos de una biblioteca con DOS TABLAS relacionadas.

Cuando los datos son más complejos, no basta con una sola tabla.
Aquí modelamos una biblioteca real con dos tablas:

  Libros(isbn, titulo, autor, ejemplares_totales)
  Prestamos(id, isbn, dni_usuario, fecha)

Ambas se relacionan por el campo 'isbn'. Es la primera vez que ves
esta idea de tablas conectadas — sin llegar a JOIN, se puede
consultar muchísimo con lo que sabemos.

Consultas incluidas:
  1) Libros que quedan por prestar (ejemplares_totales - prestamos_activos).
  2) Los 3 libros MÁS prestados.
  3) Actividad de un usuario.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import sqlite3


def crear_bbdd(bbdd: str) -> None:
    """Crea las tablas y las rellena con datos de ejemplo."""
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    # Limpiamos por si el fichero ya existía
    cursor.execute("DROP TABLE IF EXISTS Prestamos")
    cursor.execute("DROP TABLE IF EXISTS Libros")

    cursor.execute("""
        CREATE TABLE Libros (
            isbn                TEXT PRIMARY KEY,
            titulo              TEXT NOT NULL,
            autor               TEXT,
            ejemplares_totales  INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE Prestamos (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn         TEXT,
            dni_usuario  TEXT,
            fecha        TEXT
        )
    """)

    # Datos de prueba
    libros = [
        ("978-0-13-468599-1", "El Quijote",              "Cervantes",        3),
        ("978-0-201-89684-2", "Cálculo Infinitesimal",   "Michael Spivak",   2),
        ("978-0-13-235088-4", "Álgebra Lineal",          "Hoffman & Kunze",  2),
        ("978-0-262-03384-8", "Introduction to Algorithms", "Cormen et al.", 4),
        ("978-0-321-77640-3", "Análisis Real",           "Walter Rudin",     1),
    ]
    cursor.executemany("INSERT INTO Libros VALUES (?, ?, ?, ?)", libros)

    prestamos = [
        ("978-0-13-468599-1", "50123456A", "2026-01-15"),
        ("978-0-13-468599-1", "50234567B", "2026-02-10"),
        ("978-0-201-89684-2", "50345678C", "2026-01-20"),
        ("978-0-201-89684-2", "50456789D", "2026-02-05"),
        ("978-0-201-89684-2", "50123456A", "2026-03-12"),
        ("978-0-262-03384-8", "50123456A", "2026-01-22"),
        ("978-0-262-03384-8", "50567890E", "2026-02-14"),
        ("978-0-321-77640-3", "50345678C", "2026-03-01"),
    ]
    for p in prestamos:
        cursor.execute("INSERT INTO Prestamos (isbn, dni_usuario, fecha) VALUES (?, ?, ?)", p)

    conexion.commit()
    conexion.close()


def libros_mas_prestados(bbdd: str, cuantos: int = 3) -> None:
    """Muestra los libros más prestados (uso de GROUP BY y ORDER BY)."""
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    # Contamos préstamos por ISBN, y luego cruzamos con Libros a mano
    cursor.execute("""
        SELECT isbn, COUNT(*) AS n
        FROM Prestamos
        GROUP BY isbn
        ORDER BY n DESC
        LIMIT ?
    """, (cuantos,))
    top = cursor.fetchall()

    print(f"═══ Top {cuantos} libros más prestados ═══")
    for isbn, veces in top:
        # Buscamos el título en la otra tabla
        cursor.execute("SELECT titulo, autor FROM Libros WHERE isbn = ?", (isbn,))
        titulo, autor = cursor.fetchone()
        print(f"  📖 {titulo}  ({autor})  → {veces} préstamos")

    conexion.close()


def ejemplares_disponibles(bbdd: str) -> None:
    """Muestra cuántos ejemplares hay disponibles de cada libro."""
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    print("\n═══ Ejemplares disponibles ═══")
    cursor.execute("SELECT isbn, titulo, ejemplares_totales FROM Libros")
    libros = cursor.fetchall()

    for isbn, titulo, totales in libros:
        cursor.execute("SELECT COUNT(*) FROM Prestamos WHERE isbn = ?", (isbn,))
        prestados = cursor.fetchone()[0]
        disponibles = totales - prestados

        icono = "✅" if disponibles > 0 else "❌"
        print(f"  {icono} {titulo:30}   {disponibles} de {totales} disponibles")

    conexion.close()


def actividad_usuario(bbdd: str, dni: str) -> None:
    """Muestra los libros que ha prestado un usuario."""
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT p.fecha, p.isbn
        FROM Prestamos p
        WHERE p.dni_usuario = ?
        ORDER BY p.fecha
    """, (dni,))

    print(f"\n═══ Actividad del usuario {dni} ═══")
    for fecha, isbn in cursor.fetchall():
        cursor.execute("SELECT titulo FROM Libros WHERE isbn = ?", (isbn,))
        titulo = cursor.fetchone()[0]
        print(f"  {fecha}: {titulo}")

    conexion.close()


def main():
    bbdd = "biblioteca.db"
    crear_bbdd(bbdd)
    print(f"✅ Base de datos '{bbdd}' inicializada.\n")

    libros_mas_prestados(bbdd, 3)
    ejemplares_disponibles(bbdd)
    actividad_usuario(bbdd, "50123456A")


if __name__ == "__main__":
    main()
