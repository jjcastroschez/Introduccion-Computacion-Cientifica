#include <stdio.h>

int main() {
    float gradosCelsius, gradosFahrenheit;

    // Entrada de datos
    printf("Dame la temperatura en Grados Celsius: ");
    scanf("%f", &gradosCelsius);

    // Cálculo de la conversión
    // Usamos 9.0 / 5.0 para asegurar que la división sea decimal
    gradosFahrenheit = (gradosCelsius * 9.0 / 5.0) + 32;

    // Salida de datos
    printf("La temperatura en Grados Fahrenheit es %.2f\n", gradosFahrenheit);

    return 0;
}