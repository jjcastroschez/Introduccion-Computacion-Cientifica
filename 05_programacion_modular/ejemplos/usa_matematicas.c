/*
 * usa_matematicas.c — Programa principal que usa nuestro módulo en C.
 *
 * Compilar con:
 *   gcc -o usa usa_matematicas.c matematicas.c -lm
 * Ejecutar con:
 *   ./usa
 *
 * Tema 5 - Introducción a la Computación Científica (ICC).
 */

#include <stdio.h>
#include "matematicas.h"


int main(void) {
    printf("Usando el módulo matematicas (C)\n");
    printf("================================\n\n");

    printf("MCD:\n");
    printf("  mcd(48, 18) = %d\n", mcd(48, 18));
    printf("  mcd(1071, 462) = %d\n\n", mcd(1071, 462));

    printf("Primos en [10, 30]:\n");
    for (int n = 10; n <= 30; n++) {
        if (es_primo(n)) printf("  %d es primo\n", n);
    }

    printf("\nFactorial y combinatorio:\n");
    printf("  5! = %ld\n", factorial(5));
    printf("  C(10, 3) = %ld\n", combinatorio(10, 3));

    printf("\nRaíz babilónica:\n");
    printf("  √2 ≈ %.15f\n", raiz_babilonica(2.0));

    return 0;
}
