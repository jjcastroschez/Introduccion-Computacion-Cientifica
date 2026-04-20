#include <stdio.h>

int main() {
    float lado, area;

    // Pedir la entrada al usuario
    printf("Introduce la longitud del lado (en metros): ");
    scanf("%f", &lado);

    // Calcular el área
    area = lado * lado;

    // Mostrar el resultado con 2 decimales
    printf("El área es: %.2f m2\n", area);

    return 0;
}