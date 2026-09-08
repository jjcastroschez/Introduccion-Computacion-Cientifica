"""
Ejercicio 9 — Consultar la PokéAPI (sin API Key).

Pregunta al usuario por el nombre de un Pokémon y muestra su
información básica (número, altura, peso, tipos y habilidades)
usando la PokéAPI.

Ventaja: la PokéAPI es gratuita y NO requiere clave.

Requisito previo: pip install requests

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import requests


def obtener_pokemon(nombre: str) -> dict:
    """Consulta la PokéAPI y devuelve los datos del Pokémon (o None si no existe)."""
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower().strip()}"

    try:
        respuesta = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None

    if respuesta.status_code == 200:
        return respuesta.json()
    elif respuesta.status_code == 404:
        print(f"❌ Pokémon '{nombre}' no encontrado.")
    else:
        print(f"❌ Error {respuesta.status_code}")
    return None


def mostrar_pokemon(datos: dict) -> None:
    """Muestra la información básica del Pokémon."""
    print(f"\n{'═' * 40}")
    print(f"  📋 {datos['name'].upper()}   Nº {datos['id']}")
    print(f"{'═' * 40}")
    print(f"  Altura:  {datos['height'] / 10:.1f} m")
    print(f"  Peso:    {datos['weight'] / 10:.1f} kg")

    # Tipos: lista de dicts, hay que extraer el nombre de cada uno
    tipos = [t["type"]["name"] for t in datos["types"]]
    print(f"  Tipos:   {', '.join(tipos)}")

    # Habilidades: idem
    habilidades = [h["ability"]["name"] for h in datos["abilities"]]
    print(f"  Habilidades: {', '.join(habilidades)}")

    # Estadísticas base
    print(f"\n  Estadísticas base:")
    for stat in datos["stats"]:
        nombre_stat = stat["stat"]["name"]
        valor = stat["base_stat"]
        barra = "█" * (valor // 5)
        print(f"    {nombre_stat:15} {valor:>3}  {barra}")


def main():
    nombre = input("Introduce el nombre de un Pokémon (ej. pikachu): ")

    datos = obtener_pokemon(nombre)
    if datos is not None:
        mostrar_pokemon(datos)


if __name__ == "__main__":
    main()
