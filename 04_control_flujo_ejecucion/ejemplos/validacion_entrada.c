/*
 * Validación robusta de entrada de usuario.
 *
 * Pide un número entero entre 1 y 100 y sigue pidiendo (con un mensaje
 * claro de error) hasta que la entrada sea válida.
 *
 * Tema 4 - Introducción a la Computación Científica (ICC).
 *
 * Compilar con: gcc -o validacion validacion_entrada_icc.c
 * Ejecutar con: ./validacion
 *
 * Nota: C NO dispone del manejo de excepciones (try-except) de Python.
 * En su lugar, hay que comprobar manualmente el valor de retorno de
 * scanf y vaciar el buffer de entrada cuando la lectura falla.
 */

#include <stdio.h>

int main(void) {
    int n;
    int valido = 0;
    int caracter;

    while (!valido) {
        printf("Introduce un número entero entre 1 y 100: ");
        if (scanf("%d", &n) != 1) {
            /* scanf no consiguió leer un entero */
            printf("  ❌ Eso no es un entero válido.\n");
            /* Vaciamos el buffer hasta el siguiente salto de línea */
            while ((caracter = getchar()) != '\n' && caracter != EOF);
            continue;
        }
        if (n < 1 || n > 100) {
            printf("  ❌ %d está fuera del rango [1, 100].\n", n);
            continue;
        }
        valido = 1;
    }

    printf("✅ Has introducido el número %d. ¡Gracias!\n", n);
    return 0;
}
