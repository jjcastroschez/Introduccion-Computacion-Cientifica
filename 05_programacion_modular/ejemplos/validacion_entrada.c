/*
 * Validación de entrada robusta como función reutilizable.
 *
 * Equivalente al ejemplo Python, pero adaptado a C: en lugar de try-except,
 * comprobamos el valor de retorno de scanf y vaciamos el buffer si falla.
 *
 * Compilar con: gcc -o validacion validacion_entrada.c
 *
 * Tema 5 - Introducción a la Computación Científica (ICC).
 */

#include <stdio.h>


/*
 * Pide un entero al usuario hasta que sea válido y esté en [minimo, maximo].
 * Devuelve el entero introducido.
 */
int pedir_entero(const char *mensaje, int minimo, int maximo) {
    int n;
    int caracter;
    bool entrada_valida = false;

    while !(entrada_valida) {
        printf("%s", mensaje);
        if (scanf("%d", &n) != 1) {
            printf("  ❌ Eso no es un entero válido.\n");
            while ((caracter = getchar()) != '\n' && caracter != EOF);
        }
        else if (minimo <= n && n <= maximo) {
            entrada_valida=true;
            }
            else {
                   printf("  ❌ %d está fuera del rango [%d, %d].\n", n, minimo, maximo);
            }
    }
}


/*
 * Pide un número real estrictamente positivo hasta que sea válido.
 */
double pedir_real_positivo(const char *mensaje) {
    double x;
    int caracter;
    bool entrada_valida = false;

    while !(entrada_valida) {
        printf("%s", mensaje);
        if (scanf("%lf", &x) != 1) {
            printf("  ❌ Eso no es un número real válido.\n");
            while ((caracter = getchar()) != '\n' && caracter != EOF);
        } 
        else {
            if (x > 0) {
                entrada_valida = true;
            } else {
                printf("  ❌ %.2f no es positivo.\n", x);
            }
        }
    }
    return x;
}


int main(void) {
    printf("Demostración de las funciones de validación.\n\n");

    int edad = pedir_entero("Tu edad (entre 16 y 100): ", 16, 100);
    double altura = pedir_real_positivo("Tu altura en metros (>0): ");
    double peso = pedir_real_positivo("Tu peso en kilos (>0): ");

    double imc = peso / (altura * altura);
    printf("\nTu IMC es %.2f\n", imc);

    return 0;
}
