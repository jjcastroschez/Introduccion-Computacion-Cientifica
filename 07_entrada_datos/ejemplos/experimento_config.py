"""
Ejemplo — Configuración y resultados de un experimento numérico.

En investigación es MUY común separar el CÓDIGO del EXPERIMENTO
de sus PARÁMETROS de ejecución. Los parámetros suelen guardarse en un
fichero JSON (o YAML): cambiar el fichero → cambiar el experimento,
sin tocar el código.

Este ejemplo estima la integral de sin(x) entre 0 y π usando el
método de Monte Carlo:

    ∫₀^π sin(x) dx = 2

La configuración está en config.json (n_muestras, semilla, límites...)
y guardamos los resultados en otro JSON para poder analizarlos después.

Tema 7 - Introducción a la Computación Científica (ICC).
"""

import json
import math
import random


def cargar_config(fichero: str) -> dict:
    """Carga la configuración desde un fichero JSON."""
    with open(fichero, "r", encoding="utf-8") as f:
        return json.load(f)


def monte_carlo_seno(config: dict) -> dict:
    """
    Estima ∫ sin(x) dx entre los límites usando muestreo Monte Carlo.
    Devuelve un dict con los resultados.
    """
    a = config["parametros"]["limite_inferior"]
    b = config["parametros"]["limite_superior"]
    n = config["parametros"]["n_muestras"]
    semilla = config["parametros"]["semilla"]

    random.seed(semilla)                             # reproducibilidad

    # Media de sin(x) para muestras aleatorias en [a, b]
    suma = 0.0
    for _ in range(n):
        x = random.uniform(a, b)
        suma = suma + math.sin(x)

    estimacion = (b - a) * suma / n                  # fórmula MC clásica
    valor_real = math.cos(a) - math.cos(b)           # ∫ sin dx = -cos, cierra en 2
    error = abs(estimacion - valor_real)

    return {
        "estimacion":       estimacion,
        "valor_real":       valor_real,
        "error_absoluto":   error,
        "error_relativo":   error / valor_real,
        "n_muestras":       n,
        "semilla":          semilla,
    }


def guardar_resultados(resultados: dict, fichero: str) -> None:
    """Guarda los resultados como JSON legible."""
    with open(fichero, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)


def main():
    # 1) Cargar la configuración
    config = cargar_config("config.json")
    print(f"🧪 Ejecutando: {config['nombre']}")
    print(f"   Muestras:  {config['parametros']['n_muestras']:,}")
    print(f"   Semilla:   {config['parametros']['semilla']}")
    print()

    # 2) Ejecutar el experimento
    resultados = monte_carlo_seno(config)

    print(f"📊 Resultados:")
    print(f"   Estimación:   {resultados['estimacion']:.6f}")
    print(f"   Valor real:   {resultados['valor_real']:.6f}")
    print(f"   Error abs:    {resultados['error_absoluto']:.6f}")
    print(f"   Error rel:    {resultados['error_relativo']:.4%}")

    # 3) Guardar los resultados
    guardar_resultados(resultados, "resultado.json")
    print(f"\n✅ Resultados guardados en resultado.json")

    print("\n💡 Prueba a EDITAR config.json (cambia n_muestras a 1000000)")
    print("   y vuelve a ejecutar: verás cómo baja el error sin tocar el código.")


if __name__ == "__main__":
    main()
