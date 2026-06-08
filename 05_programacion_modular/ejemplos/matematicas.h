/*
 * matematicas.h — Cabecera del módulo de utilidades matemáticas en C.
 *
 * En C, un "módulo" se compone de DOS archivos:
 *   - matematicas.h: declara las funciones (las "promete").
 *   - matematicas.c: implementa las funciones (las "cumple").
 *
 * Otros programas incluyen la cabecera con #include "matematicas.h"
 * y el compilador enlaza el .c en tiempo de compilación.
 *
 * Tema 5 - Introducción a la Computación Científica (ICC).
 */

#ifndef MATEMATICAS_H
#define MATEMATICAS_H

/* Aritmética entera */
int mcd(int a, int b);
int mcm(int a, int b);
int es_primo(int n);

/* Combinatoria */
long factorial(int n);
long combinatorio(int n, int k);

/* Métodos numéricos */
double raiz_babilonica(double a);

#endif
