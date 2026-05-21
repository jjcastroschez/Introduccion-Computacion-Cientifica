/*
 * Algoritmo de Euclides para el cálculo del MCD de dos enteros positivos.
 *
 * Tema 4 - Introducción a la Computación Científica (ICC).
 *
 * Compilar con: gcc -o euclides euclides_icc.c
 * Ejecutar con: ./euclides
 */

#include <stdio.h>

int main(void) {
    int a, b, a_original, b_original, resto;
    int entrada_valida = 0;

    /* Bucle de validación de entrada equivalente al try-except de Python */
    while (!entrada_valida) {
        printf("Primer entero positivo: ");
        if (scanf("%d", &a) != 1 || a <= 0) {
            printf("  ⚠️ Tienes que introducir un entero positivo.\n");
            /* Vaciar el buffer de entrada en caso de error */
            while (getchar() != '\n');
            continue;   
        }
        printf("Segundo entero positivo: ");
        if (scanf("%d", &b) != 1 || b <= 0) {
            printf("  ⚠️ Tienes que introducir un entero positivo.\n");
            while (getchar() != '\n');
            continue;
        }
        entrada_valida = 1;
    }

    a_original = a;
    b_original = b;

    while (b != 0) {
        resto = a % b;
        a = b;
        b = resto;
    }

    printf("MCD(%d, %d) = %d\n", a_original, b_original, a);

    return 0;
}
