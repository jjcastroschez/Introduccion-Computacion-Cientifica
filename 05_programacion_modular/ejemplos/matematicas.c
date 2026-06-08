/*
 * matematicas.c — Implementación de las funciones declaradas en matematicas.h.
 *
 * Compilar (junto con el programa que lo usa):
 *   gcc -o programa programa.c matematicas.c -lm
 *
 * Tema 5 - Introducción a la Computación Científica (ICC).
 */

#include <math.h>
#include <stdlib.h> // para poder usar abs() en mcm()
#include "matematicas.h"

/* Aritmética entera */

int mcd(int a, int b) {
    int resto;
    while (b != 0) {
        resto = a % b;
        a = b;
        b = resto;
    }
    return a;
}

int mcm(int a, int b) {
    int resultado;
    int x = abs(a);
    int y = abs(b);

    if (x==0 || y==0) resultado=0;
      else resultado=(x / mcd(x, y)) * y;
    return resultado;
}

int es_primo(int n) {
    int primo = 1;

    if (n < 2) {
        primo = 0;
    } else if (n == 2) {
        primo = 1;
    } else if (n % 2 == 0) {
        primo = 0;
    } else {
        // Tu bucle optimizado con break
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                primo = 0;
                break; // Excelente adición
            }
        }
    }

    return primo;
}
/* Combinatoria */

long factorial(int n) {
    long resultado = 1;
    for (int i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

long combinatorio(int n, int k) {
    long resultado = 1;
    for (int i = 1; i <= k; i++) {
        resultado = resultado * (n - i + 1) / i;
    }
    return resultado;
}

/* Métodos numéricos */

double raiz_babilonica(double a) {
    if (a < 0) return -1.0;
    if (a == 0) return 0.0;

    double x = a / 2.0;
    double x_nuevo;
    double tol = 1e-12;

    for (int i = 0; i < 100; i++) {
        x_nuevo = 0.5 * (x + a / x);
        if (x_nuevo > x) {
            if (x_nuevo - x < tol) return x_nuevo;
        } else {
            if (x - x_nuevo < tol) return x_nuevo;
        }
        x = x_nuevo;
    }
    return x;
}
