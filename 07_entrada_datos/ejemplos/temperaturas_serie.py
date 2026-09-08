"""
Ejemplo — Análisis de una serie temporal de temperaturas.

Lee un CSV con las temperaturas mínima y máxima de cada día de un mes
(en Ciudad Real, julio de 2026) y responde:

  - Día más caluroso y día más frío.
  - Promedios de mínimas y máximas mensuales.
  - Media semanal de la máxima (agrupando por semanas naturales).
  - Cuántos días superaron los 35 °C (olas de calor).

Es un patrón MUY común en programación científica: leer una serie
temporal y calcular estadísticas por período.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import csv
from datetime import date


def leer_temperaturas(fichero: str) -> list:
    """Devuelve una lista de tuplas (fecha, temp_min, temp_max)."""
    datos = []
    with open(fichero, "r") as f:
        for fila in csv.DictReader(f):
            fecha = date.fromisoformat(fila["fecha"])   # convierte '2026-07-01' → date
            tmin = float(fila["temp_min"])
            tmax = float(fila["temp_max"])
            datos.append((fecha, tmin, tmax))
    return datos


def main():
    datos = leer_temperaturas("temperaturas_ciudad_real.csv")

    print(f"═══ Serie de {len(datos)} días ═══\n")

    # 1) Día más caluroso y más frío
    dia_mas_caluroso = max(datos, key=lambda d: d[2])   # d[2] = tmax
    dia_mas_frio = min(datos, key=lambda d: d[1])       # d[1] = tmin
    print(f"🔥 Día más caluroso:  {dia_mas_caluroso[0]}  ({dia_mas_caluroso[2]} °C)")
    print(f"❄️  Día más frío:      {dia_mas_frio[0]}  ({dia_mas_frio[1]} °C)")

    # 2) Promedios del mes
    minimas = [d[1] for d in datos]
    maximas = [d[2] for d in datos]
    print(f"\nPromedio mínimas:  {sum(minimas) / len(minimas):.1f} °C")
    print(f"Promedio máximas:  {sum(maximas) / len(maximas):.1f} °C")

    # 3) Media semanal de la máxima (agrupamos con un dict)
    #    date.isocalendar()[1] devuelve el número de semana ISO
    por_semana = {}
    for fecha, tmin, tmax in datos:
        semana = fecha.isocalendar()[1]
        if semana not in por_semana:
            por_semana[semana] = []
        por_semana[semana].append(tmax)

    print("\n─── Media de la máxima por semana ISO ───")
    for semana in sorted(por_semana):
        maximas_semana = por_semana[semana]
        media = sum(maximas_semana) / len(maximas_semana)
        barra = "▓" * int(media - 20)
        print(f"  Semana {semana}  ({len(maximas_semana)} días)  media: {media:.1f} °C  {barra}")

    # 4) Días con máxima >= 35 °C ("ola de calor")
    dias_calor = [d for d in datos if d[2] >= 35]
    print(f"\n🌡️  Días con máxima ≥ 35 °C: {len(dias_calor)} de {len(datos)}")
    for fecha, tmin, tmax in dias_calor:
        print(f"    {fecha}: {tmax} °C")


if __name__ == "__main__":
    main()
