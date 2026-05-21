"""
Validación robusta de entrada de usuario.

Pide un número entero entre 1 y 100 y sigue pidiendo (con un mensaje
claro de error) hasta que la entrada sea válida.

Tema 4 - Introducción a la Computación Científica (ICC).
"""
entrada_valida = False
while not entrada_valida:
    entrada = input("Introduce un número entero entre 1 y 100: ")
    try:
        n = int(entrada)
    except ValueError:
        print(f"  ❌ \"{entrada}\" no es un entero válido.")
    else:
        if 1 <= n <= 100:
            entrada_valida = True
        else:
            print(f"  ❌ {n} está fuera del rango [1, 100].")

print(f"✅ Has introducido el número {n}. ¡Gracias!")
