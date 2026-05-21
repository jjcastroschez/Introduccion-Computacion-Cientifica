/*
 * Programa con un bug deliberado para practicar depuración.
 *
 * Se supone que calcula la suma de los N primeros números pares
 * (2 + 4 + 6 + ... + 2N), pero da un resultado incorrecto.
 *
 * Compilar (con símbolos de depuración):
 *     gcc -g -o programa_bug programa_con_bugs.c
 *
 * Depurar con gdb:
 *     gdb ./programa_bug
 *     (gdb) break 20      # poner breakpoint en la línea 20
 *     (gdb) run           # ejecutar hasta el breakpoint
 *     (gdb) print i       # ver el valor de i
 *     (gdb) print suma
 *     (gdb) next          # ejecutar la siguiente línea
 *     (gdb) continue      # seguir hasta el siguiente breakpoint o el final
 *     (gdb) quit
 *
 * Tema 4 - Introducción a la Computación Científica (ICC).
 */

#include <stdio.h>

int main(void) {
    int n = 5;       /* esperamos: 2+4+6+8+10 = 30 */
    int suma = 0;
    int i = 0;

    while (i < n) {
        i = i + 1;
        suma = suma + 2 * i;
        i = i + 1;   /* 🐛 BUG: incremento de más */
    }

    printf("Suma de los %d primeros pares: %d\n", n, suma);
    printf("Esperado: 30\n");

    return 0;
}
