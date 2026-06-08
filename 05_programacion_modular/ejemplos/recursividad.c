/*
 * Recursividad en C: factorial y Fibonacci.
 *
 * Comparamos la versión RECURSIVA con la ITERATIVA (que ya sabemos hacer
 * desde el Tema 4) para ver qué aporta y qué cuesta cada enfoque.
 *
 * Compilar con: gcc -o recursividad recursividad.c
 *
 * Tema 5 - Introducción a la Computación Científica (ICC).
 */

#include <stdio.h>
#include <time.h>


/* Factorial: dos versiones equivalentes */

long factorial_iterativo(int n) {
    long resultado = 1;
    for (int i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

long factorial_recursivo(int n) {
    if (n <= 1) return 1;
    return n * factorial_recursivo(n - 1);
}


/* Fibonacci: dos versiones, pero ¡con un final muy distinto! */

long fibonacci_iterativo(int n) {
    if (n <= 1) return n;
    long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

long fibonacci_recursivo(int n) {
    if (n <= 1) return n;
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2);
}


int main(void) {
    int n = 10;
    printf("Factorial de %d:\n", n);
    printf("  Iterativo:  %ld\n", factorial_iterativo(n));
    printf("  Recursivo:  %ld\n", factorial_recursivo(n));
    printf("  → Para el factorial ambos son igual de eficientes.\n\n");

    printf("Fibonacci de %d:\n", n);
    printf("  Iterativo: %ld\n", fibonacci_iterativo(n));
    printf("  Recursivo: %ld\n", fibonacci_recursivo(n));

    printf("\n¡Ojo! con n=35, la recursiva tarda lo suyo:\n");
    n = 35;

    clock_t t0 = clock();
    long res_r = fibonacci_recursivo(n);
    double t_rec = (double)(clock() - t0) / CLOCKS_PER_SEC;
    printf("  fibonacci_recursivo(%d) = %ld (%.3f s)\n", n, res_r, t_rec);

    t0 = clock();
    long res_i = fibonacci_iterativo(n);
    double t_iter = (double)(clock() - t0) / CLOCKS_PER_SEC;
    printf("  fibonacci_iterativo(%d) = %ld (%.6f s)\n", n, res_i, t_iter);

    return 0;
}
