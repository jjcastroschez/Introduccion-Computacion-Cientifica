"""
Ejemplo — Registrar eventos en un log.

Los ficheros de log son un caso de uso muy habitual del modo "a" (append):
el programa va AÑADIENDO líneas al final del fichero, sin borrar lo que
ya hay. Cada vez que ocurre algo interesante (un error, una llamada
importante, el arranque del programa...), se anota una línea.

Este ejemplo compara los tres modos de apertura:
  - "w" — BORRA el contenido cada vez que se ejecuta (peligroso para logs)
  - "a" — AÑADE al final (lo correcto para logs)
  - "r" — solo lectura

Tema 7 - Introducción a la Computación Científica (ICC).
"""

from datetime import datetime


def registrar(fichero: str, nivel: str, mensaje: str) -> None:
    """
    Añade una línea al log con formato: [YYYY-MM-DD HH:MM:SS] NIVEL: mensaje
    Modo "a" para NO borrar el histórico.
    :param fichero: nombre del fichero de log (string)
    :param nivel: nivel del evento (string)
    :param mensaje: descripción del evento (string)
    :return: None
    """
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{ahora}] {nivel:5} {mensaje}\n"

    with open(fichero, "a") as f:               # ← "a" es la clave
        f.write(linea)


def mostrar_log(fichero: str, ultimas: int = 10) -> None:
    """Muestra las últimas 'ultimas' líneas del log.
    :param fichero: nombre del fichero de log (string)
    :param ultimas: número de líneas a mostrar (int)
    :return: None"""
    with open(fichero, "r") as f:
        lineas = f.readlines()

    print(f"───── {fichero} ({len(lineas)} entradas totales) ─────")
    for linea in lineas[-ultimas:]:
        print(linea.rstrip())


def main():
    log = "eventos.log"

    # Simulamos varios eventos que ocurren en un programa
    registrar(log, "INFO",  "Arranque del programa")
    registrar(log, "INFO",  "Configuración cargada correctamente")
    registrar(log, "WARN",  "Fichero de caché no encontrado, se creará uno nuevo")
    registrar(log, "INFO",  "Conectando a la base de datos")
    registrar(log, "ERROR", "Timeout esperando respuesta del servidor")
    registrar(log, "INFO",  "Reintentando conexión")
    registrar(log, "INFO",  "Programa finalizado sin errores")

    # Vemos el resultado
    mostrar_log(log)

    print("\n💡 Si vuelves a ejecutar el programa, verás que las nuevas")
    print("   entradas se AÑADEN al final, sin borrar las anteriores.")
    print("   Eso es lo que hace el modo 'a'. Con modo 'w' habrías perdido")
    print("   todo el historial cada vez.")


if __name__ == "__main__":
    main()
