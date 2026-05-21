/*
 * Acumulación de fármacos — versión iterativa.
 *
 * Simula día a día la concentración de un fármaco en el cuerpo de un
 * paciente, aplicando la recurrencia:
 *     cantidad(dia) = cantidad(dia-1) * r + dosis
 * donde r = 1 - porcentaje_eliminado / 100.
 *
 * A diferencia del Tema 3, no usamos la fórmula cerrada de la serie
 * geométrica, sino que simulamos el proceso día a día con un bucle.
 *
 * Tema 4 - Introducción a la Computación Científica (ICC).
 * En Mac:
 * Compilar con: gcc -o farmacologia farmacologia.c
 * Ejecutar con: ./farmacologia
 * En Windows (PowerShell):
 * Compilar con: gcc -o farmacologia.exe farmacologia.c
 * Ejecutar con: .\farmacologia.exe
 */

#include <stdio.h>

int main(void) {
    double dosis, porcentaje_elim, r, cantidad;
    int dias, dia;

    printf("Dosis diaria (mg): ");
    scanf("%lf", &dosis);
    printf("Porcentaje eliminado cada día (0-100): ");
    scanf("%lf", &porcentaje_elim);
    printf("Días que queremos simular: ");
    scanf("%d", &dias);

    r = 1.0 - porcentaje_elim / 100.0;
    cantidad = 0.0;

    for (dia = 1; dia <= dias; dia++) {
        cantidad = cantidad * r + dosis;
        printf("Día %3d: %.4f mg en el cuerpo\n", dia, cantidad);
    }

    printf("\nValor límite teórico (serie geométrica): %.4f mg\n",
           dosis / (1.0 - r));

    return 0;
}
