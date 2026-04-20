#include <stdio.h>

// Definición de constantes para los pesos
#define PESO1PRUEBA 0.10
#define PESO2PRUEBA 0.15
#define PESO3PRUEBA 0.10

int main() {
    float califPrimeraPrueba, califSegundaPrueba, califTerceraPrueba;
    float calif1, calif2, calif3, notaPruebasProgreso;

    // Entrada de datos
    printf("Dame la calificación de la primera prueba: ");
    scanf("%f", &califPrimeraPrueba);

    printf("Dame la calificación de la segunda prueba: ");
    scanf("%f", &califSegundaPrueba);

    printf("Dame la calificación de la tercera prueba: ");
    scanf("%f", &califTerceraPrueba);

    // Cálculos
    calif1 = califPrimeraPrueba * PESO1PRUEBA;
    calif2 = califSegundaPrueba * PESO2PRUEBA;
    calif3 = califTerceraPrueba * PESO3PRUEBA;

    notaPruebasProgreso = calif1 + calif2 + calif3;

    // Salida de datos
    printf("La calificación obtenida es: %.2f sobre 4\n", notaPruebasProgreso);

    return 0;
}