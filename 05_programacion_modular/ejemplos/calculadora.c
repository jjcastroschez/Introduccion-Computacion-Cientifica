/*
 * Calculadora científica modular.
 *
 * Pequeña calculadora que ofrece varias operaciones científicas implementadas
 * como funciones independientes.
 *
 * Compilar con: gcc -o calculadora calculadora.c -lm
 * Ejecutar con: ./calculadora
 *
 * Nota: -lm es necesario para enlazar la biblioteca matemática (sqrt, M_PI).
 *
 * Tema 5 - Introducción a la Computación Científica (ICC).
 */

#include <stdio.h>
#include <math.h>


/* ------------------------------------------------------------------
 * Prototipos de las funciones (en C es buena práctica declararlos
 * arriba para que el compilador los conozca antes de usarlos).
 * ------------------------------------------------------------------ */

double area_circulo(double radio);
double hipotenusa(double cateto1, double cateto2);
double grados_a_radianes(double grados);
int es_par(int n);


/* ------------------------------------------------------------------
 * Fíjate la diferencia entre esta función main() y la de los ejemplos anteriores. 
 * Aquí el main se encarga de mostrar el menú, de la interacción con el usuario y de llamar a las funciones que hacen el trabajo
 * ------------------------------------------------------------------ */

int main(void) {
    int opcion;

    printf("Calculadora científica modular\n");
    printf("------------------------------\n");
    printf("1) Área de un círculo\n");
    printf("2) Hipotenusa de un triángulo rectángulo\n");
    printf("3) Conversión de grados a radianes\n");
    printf("4) ¿Es un número par?\n");
    printf("\nElige una opción [1-4]: ");
    scanf("%d", &opcion);

    switch (opcion) {
        case 1: {
            double r;
            printf("Radio: ");
            scanf("%lf", &r);
            printf("Área = %.4f\n", area_circulo(r));
            break;
        }
        case 2: {
            double a, b;
            printf("Cateto 1: ");
            scanf("%lf", &a);
            printf("Cateto 2: ");
            scanf("%lf", &b);
            printf("Hipotenusa = %.4f\n", hipotenusa(a, b));
            break;
        }
        case 3: {
            double g;
            printf("Ángulo en grados: ");
            scanf("%lf", &g);
            printf("%.1f° = %.6f rad\n", g, grados_a_radianes(g));
            break;
        }
        case 4: {
            int n;
            printf("Entero: ");
            scanf("%d", &n);
            if (es_par(n)) {
                printf("%d es par\n", n);
            } else {
                printf("%d es impar\n", n);
            }
            break;
        }
        default:
            printf("Opción no válida.\n");
    }

    return 0;
}


/* ------------------------------------------------------------------
 * Definición de las funciones.
 * ------------------------------------------------------------------ */

double area_circulo(double radio) {
    return M_PI * radio * radio;
}

double hipotenusa(double cateto1, double cateto2) {
    return sqrt(cateto1 * cateto1 + cateto2 * cateto2);
}

double grados_a_radianes(double grados) {
    return grados * M_PI / 180.0;
}

int es_par(int n) {
    return n % 2 == 0;
}
