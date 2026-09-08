"""
Ejemplo — Posición actual de la Estación Espacial Internacional (ISS).

Consulta la API pública 'wheretheiss.at' (sin API Key) que devuelve
la posición actual de la ISS: latitud, longitud, altitud y velocidad.

Además, calcula la distancia GEODÉSICA (la distancia sobre la esfera
terrestre) entre la ISS y Ciudad Real, usando la FÓRMULA DEL HAVERSINE:

    d = 2R · arcsin( √(sin²(Δφ/2) + cos(φ₁)·cos(φ₂)·sin²(Δλ/2)) )

donde φ es latitud, λ longitud (en radianes), y R el radio terrestre.

Requisito: pip install requests

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import math
import requests


# Coordenadas de Ciudad Real (para calcular la distancia a la ISS)
CIUDAD_REAL = (38.9856, -3.9271)
RADIO_TIERRA_KM = 6371.0

URL_ISS = "https://api.wheretheiss.at/v1/satellites/25544"


def obtener_iss() -> dict:
    """Consulta la posición actual de la ISS. Devuelve dict o None si falla."""
    try:
        respuesta = requests.get(URL_ISS, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"❌ Sin conexión: {e}")
        return None

    if respuesta.status_code != 200:
        print(f"❌ Error HTTP {respuesta.status_code}")
        return None

    return respuesta.json()


def distancia_geodesica(punto1: tuple, punto2: tuple) -> float:
    """
    Devuelve la distancia sobre la esfera terrestre en km entre dos
    puntos dados como tuplas (latitud, longitud) en grados.
    """
    lat1, lon1 = math.radians(punto1[0]), math.radians(punto1[1])
    lat2, lon2 = math.radians(punto2[0]), math.radians(punto2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    return RADIO_TIERRA_KM * c


def main():
    datos = obtener_iss()
    if datos is None:
        return

    lat = datos["latitude"]
    lon = datos["longitude"]
    altitud = datos["altitude"]
    velocidad = datos["velocity"]

    print(f"🛰️  Estación Espacial Internacional")
    print(f"   Latitud:    {lat:.4f}°")
    print(f"   Longitud:   {lon:.4f}°")
    print(f"   Altitud:    {altitud:.1f} km")
    print(f"   Velocidad:  {velocidad:.0f} km/h")

    # Calcular distancia a Ciudad Real
    iss = (lat, lon)
    dist_horizontal = distancia_geodesica(iss, CIUDAD_REAL)
    dist_directa = math.sqrt(dist_horizontal ** 2 + altitud ** 2)

    print(f"\n📍 Ciudad Real:  {CIUDAD_REAL[0]}° N,  {CIUDAD_REAL[1]}° E")
    print(f"   Distancia sobre el suelo:   {dist_horizontal:>8.1f} km")
    print(f"   Distancia real (con altura): {dist_directa:>8.1f} km")

    if dist_horizontal < 500:
        print("\n   👀 ¡La ISS está prácticamente sobre nosotros!")
    elif dist_horizontal < 2000:
        print("\n   😊 La ISS está bastante cerca.")


if __name__ == "__main__":
    main()
