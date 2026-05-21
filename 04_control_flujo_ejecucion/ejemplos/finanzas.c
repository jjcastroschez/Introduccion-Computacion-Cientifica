/*
 * Valor presente de una anualidad finita.
 *
 * Calcula el valor presente de recibir un pago anual constante durante n
 * años, descontado a una tasa de interés:
 *     VP = sum_{t=1..n} pago / (1+i)^t
 *
 * Tema 4 - Introducción a la Computación Científica (ICC).
 *
 * Compilar con: gcc -o finanzas finanzas_icc.c -lm
 * Ejecutar con: ./finanzas
 *
 * Nota: -lm es necesario para enlazar la biblioteca matemática (pow).
 */

#include <stdio.h>
#include <math.h>

int main(void) {
    double pago_anual, tasa_interes, i, valor_presente;
    int annus, t;

    printf("Pago anual (€): ");
    scanf("%lf", &pago_anual);
    printf("Tasa de interés anual (en %%): ");
    scanf("%lf", &tasa_interes);
    printf("Años de la anualidad: ");
    scanf("%d", &annus);

    i = tasa_interes / 100.0;
    valor_presente = 0.0;

    for (t = 1; t <= annus; t++) {
        valor_presente += pago_anual / pow(1.0 + i, t);
    }

    printf("\nValor presente de la anualidad de %d años: %.2f €\n",
           annus, valor_presente);
    printf("Valor de la renta perpetua (Tema 3): %.2f €\n", pago_anual / i);

    return 0;
}
