"""
Ejemplo — Consultar la API de Hipolabs (universidades del mundo).

La API pública de Hipolabs devuelve una lista de universidades de un
país. Es GRATUITA y SIN API Key. La URL es:

    http://universities.hipolabs.com/search?country=NombrePais

Este ejemplo permite al usuario buscar por país, muestra las 10
primeras universidades, y guarda TODA la lista en un JSON para
poder analizarla más tarde.

Requisito: pip install requests

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import json
import requests


URL = "http://universities.hipolabs.com/search"


def buscar_universidades(pais: str) -> list:
    """Devuelve una lista de dicts con las universidades del país (o [] si error)."""
    parametros = {"country": pais}

    try:
        respuesta = requests.get(URL, params=parametros, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"❌ Sin conexión: {e}")
        return []

    if respuesta.status_code != 200:
        print(f"❌ Error HTTP {respuesta.status_code}")
        return []

    return respuesta.json()


def guardar_json(datos: list, fichero: str) -> None:
    """Guarda la lista completa en un JSON legible."""
    with open(fichero, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def main():
    pais = input("País (en inglés, ej: Spain): ").strip()

    universidades = buscar_universidades(pais)
    if not universidades:
        print("No se han encontrado universidades.")
        return

    print(f"\n🎓 {len(universidades)} universidades encontradas en {pais}\n")

    # Mostramos las 10 primeras
    print("─── Primeras 10 ───")
    for i, u in enumerate(universidades[:10], 1):
        nombre = u["name"]
        web = u["web_pages"][0] if u["web_pages"] else "(sin web)"
        print(f"  {i:2}. {nombre}")
        print(f"      🌐 {web}")

    # Estadísticas: dominios más comunes de web
    dominios = {}
    for u in universidades:
        if u["domains"]:
            dominio = u["domains"][0]
            # Extraemos el TLD (última parte)
            tld = dominio.split(".")[-1]
            dominios[tld] = dominios.get(tld, 0) + 1

    print(f"\n─── Dominios (TLD) más comunes ───")
    ordenados = sorted(dominios.items(), key=lambda p: p[1], reverse=True)
    for tld, veces in ordenados[:5]:
        print(f"  .{tld:5} → {veces} universidades")

    # Guardamos el listado completo
    fichero_json = f"universidades_{pais.lower().replace(' ', '_')}.json"
    guardar_json(universidades, fichero_json)
    print(f"\n✅ Listado completo guardado en {fichero_json}")


if __name__ == "__main__":
    main()
