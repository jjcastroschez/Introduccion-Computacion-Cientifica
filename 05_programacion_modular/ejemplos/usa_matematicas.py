"""
usa_matematicas.py — Programa principal que importa nuestro módulo.

Demuestra cómo, una vez creado matematicas.py, podemos USARLO en cualquier
programa con un simple import. El módulo es ahora una caja de herramientas
reutilizable.

Tema 5 - Introducción a la Computación Científica (ICC).
"""

import matematicas as m


def main():
    print("Usando el módulo matematicas.py importado")
    print("=" * 45)

    # Calculamos el MCD y MCM de varios pares
    print("\nMáximo Común Divisor:")
    print(f"  mcd(48, 18) = {m.mcd(48, 18)}")
    print(f"  mcd(1071, 462) = {m.mcd(1071, 462)}")

    # Comprobamos primalidad
    print("\nPrimos en [10, 30]:")
    for n in range(10, 31):
        if m.es_primo(n):
            print(f"  {n} es primo")

    # Calculamos √2 sin importar math.sqrt
    print(f"\n√2 (método babilónico) ≈ {m.raiz_babilonica(2):.15f}")

    # Combinatoria
    print(f"\nC(10, 3) = {m.combinatorio(10, 3)} (esperado: 120)")
    print(f"5! = {m.factorial(5)} (esperado: 120)")


if __name__ == "__main__":
    main()
