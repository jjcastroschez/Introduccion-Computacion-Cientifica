/*
 * Versión corregida de programa_con_bugs.c.
 *
 * ⚠️ No mires este archivo hasta haber intentado encontrar y arreglar
 * el bug tú mismo. Depurar es lo que se aprende.
 *
 * Compilar con: gcc -o programa programa_corregido.c
 *
 * Tema 4 - Introducción a la Computación Científica (ICC).
 */

#include <stdio.h>

int main(void) {
    int n = 5;
    int suma = 0;
    int i = 0;

    while (i < n) {
        i = i + 1;
        suma = suma + 2 * i;   /* ✅ ya solo incrementamos una vez */
    }

    printf("Suma de los %d primeros pares: %d\n", n, suma);
    printf("Esperado: 30\n");

    return 0;
}
