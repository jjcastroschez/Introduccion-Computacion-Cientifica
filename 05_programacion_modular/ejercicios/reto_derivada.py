"""
🎯 Reto final del Tema 5 — Derivada numérica por diferencias finitas.

⚠️ Este archivo contiene SOLO el esqueleto. La solución es PARA TI.
No hay versión "corregida" publicada en el repositorio. ¡Hazlo tú!

----------------------------------------------------------------------
ENUNCIADO

Implementa una función de orden superior

    derivada(f, x, h=1e-5) -> float

que reciba:
    - f: una función real de una variable (un objeto función),
    - x: un punto donde evaluar la derivada,
    - h: el paso de las diferencias finitas (parámetro con valor por defecto)

y devuelva una aproximación numérica de f'(x) usando la fórmula
de diferencias centradas:

                  f(x + h) - f(x - h)
    f'(x)  ≈  ─────────────────────────
                        2 * h

Pistas:
  - El argumento f es una función. Para evaluarla, escribe f(x + h), f(x - h).
  - El parámetro h tiene un valor por defecto (típicamente 1e-5).
  - El cuerpo de la función es UNA SOLA LÍNEA (después del docstring).

----------------------------------------------------------------------
PROGRAMA DE PRUEBAS

Después de implementar `derivada`, completa el `main()` para que pruebe
los siguientes casos. Como tienes acceso a las derivadas exactas, podrás
comprobar el error de aproximación.

    1) f(x) = x²        →  f'(x) = 2x        →  derivada(..., 3) ≈ 6
    2) f(x) = sin(x)    →  f'(x) = cos(x)    →  derivada(..., 0) ≈ 1
    3) f(x) = eˣ        →  f'(x) = eˣ        →  derivada(..., 1) ≈ e ≈ 2.718...

Puedes pasar las funciones de dos maneras:
    a) Como referencias del módulo math: math.sin, math.exp.
    b) Como lambdas: lambda x: x**2.

----------------------------------------------------------------------
PUNTOS EXTRA (opcional)

  ★ Repite las pruebas con h = 1e-3, 1e-5, 1e-7, 1e-9 y observa qué le pasa
    al error. Verás que el error PRIMERO disminuye (h pequeño = buena
    aproximación) pero DESPUÉS empieza a crecer (h demasiado pequeño = errores
    de redondeo). Esto es uno de los efectos más interesantes del cálculo
    en coma flotante. Pinta los resultados en una tabla.

  ★★ Implementa una versión recursiva `derivada_segunda(f, x, h)` que use
     tu propia `derivada`. ¡Es una función que recibe una función Y devuelve
     una función-resultado-de-aplicar-derivada-dos-veces! Tendrás que pensar
     bien cómo hacerlo. Una pista: usa una lambda intermedia.

Tema 5 - Introducción a la Computación Científica (ICC).
"""


def derivada(f, x: float, h: float = 1e-5) -> float:
    """Implementa la fórmula de diferencias centradas. (Hazlo tú.)"""
    pass   # ← elimina este pass y escribe tu código


def main():
    """Programa de pruebas. (Complétalo tú.)"""
    pass


if __name__ == "__main__":
    main()
