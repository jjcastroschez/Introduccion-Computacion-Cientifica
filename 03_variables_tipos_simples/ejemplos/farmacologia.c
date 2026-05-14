#include <stdio.h>
#include <math.h>

int main() {

        // --- CONFIGURACIÓN DE LA SIMULACIÓN ---
    int dosis_diaria = 100;           // mg
    float porcentaje_eliminado = 0.2;
    float r = 1.0f - porcentaje_eliminado; // Fracción que permanece (0.8)
    int dia_tratamiento = 15;
    float cantidad_en_cuerpo;
    float limite_estacionario;

    printf("Dosis: %d mg\n", dosis_diaria);
    printf("Factor de permanencia (r): %.2f\n", r);
    
    limite_estacionario = dosis_diaria / (1.0f - r);

    printf("A largo plazo, el paciente tendrá un nivel estable de: %.2f mg\n", limite_estacionario);
    printf("Este es el 'Estado Estacionario'.\n");

    cantidad_en_cuerpo = dosis_diaria * (1.0f - pow(r, dia_tratamiento)) / (1.0f - r);

    printf("La cantidad de medicamento el día %d es %.2f mg\n", dia_tratamiento, cantidad_en_cuerpo);

    printf("Introduce el día de tratamiento: ");
    scanf("%d", &dia_tratamiento);

    cantidad_en_cuerpo = dosis_diaria * (1.0f - pow(r, dia_tratamiento)) / (1.0f - r);
    printf("La cantidad de medicamento el día %d es %.2f mg\n", dia_tratamiento, cantidad_en_cuerpo);

    return 0;
}


