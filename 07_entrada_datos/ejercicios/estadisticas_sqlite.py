"""
Ejercicio 7 — Estadísticas por grupos en SQLite.

Crea una tabla Ventas con datos de ventas por vendedor y por mes.
Luego calcula:
  a) Total vendido por vendedor.
  b) Total vendido por mes.
  c) Mes con más ventas totales.
  d) Vendedor con la venta promedio más alta.

Este ejercicio muestra el poder de GROUP BY y las funciones de agregación.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import sqlite3


def crear_tabla_ventas(cursor) -> None:
    """Crea la tabla e inserta datos de prueba."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vendedor TEXT,
            mes TEXT,
            importe REAL
        )
    """)
    cursor.execute("DELETE FROM Ventas")

    ventas = [
        ("Ana",   "enero",   1200.0),
        ("Ana",   "febrero", 1500.0),
        ("Ana",   "marzo",   1100.0),
        ("Luis",  "enero",   1800.0),
        ("Luis",  "febrero", 2100.0),
        ("Luis",  "marzo",   1600.0),
        ("Marta", "enero",    900.0),
        ("Marta", "febrero", 1300.0),
        ("Marta", "marzo",   1400.0),
    ]
    for v in ventas:
        cursor.execute("INSERT INTO Ventas (vendedor, mes, importe) VALUES (?, ?, ?)", v)


def main():
    conexion = sqlite3.connect("empresa.db")
    cursor = conexion.cursor()

    crear_tabla_ventas(cursor)
    conexion.commit()

    # a) Total por vendedor
    print("═══ Total vendido por vendedor ═══")
    cursor.execute("""
        SELECT vendedor, SUM(importe), COUNT(*)
        FROM Ventas
        GROUP BY vendedor
        ORDER BY SUM(importe) DESC
    """)
    for vendedor, total, ventas in cursor.fetchall():
        print(f"  {vendedor:6}: {total:>8.2f} € ({ventas} ventas)")

    # b) Total por mes
    print("\n═══ Total vendido por mes ═══")
    cursor.execute("""
        SELECT mes, SUM(importe)
        FROM Ventas
        GROUP BY mes
        ORDER BY SUM(importe) DESC
    """)
    for mes, total in cursor.fetchall():
        print(f"  {mes:8}: {total:>8.2f} €")

    # c) Mes con más ventas (con LIMIT 1)
    print("\n═══ Mejor mes ═══")
    cursor.execute("""
        SELECT mes, SUM(importe)
        FROM Ventas
        GROUP BY mes
        ORDER BY SUM(importe) DESC
        LIMIT 1
    """)
    mejor_mes, total = cursor.fetchone()
    print(f"  🏆 {mejor_mes} con {total:.2f} €")

    # d) Vendedor con mejor promedio
    print("\n═══ Vendedor con mejor promedio ═══")
    cursor.execute("""
        SELECT vendedor, AVG(importe)
        FROM Ventas
        GROUP BY vendedor
        ORDER BY AVG(importe) DESC
        LIMIT 1
    """)
    mejor_vendedor, media = cursor.fetchone()
    print(f"  🏆 {mejor_vendedor} con {media:.2f} € de media")

    conexion.close()


if __name__ == "__main__":
    main()
