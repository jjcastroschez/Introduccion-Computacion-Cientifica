#include <stdio.h>
#include <math.h>

int main() {
    // --- CONFIGURACIÓN INICIAL ---
    int dosis_diaria = 100;
    float porcentaje_eliminado = 0.20;
    float r = 1.0 - porcentaje_eliminado;
    float cantidad_en_cuerpo;
    int dia_tratamiento;

    // --- CÁLCULOS INICIALES (Mismos que el script original) ---
    printf("Dosis: %d mg\n", dosis_diaria);
    printf("Factor de permanencia (r): %.2f\n", r);
    printf("A largo plazo (limite): %.2f mg\n", dosis_diaria / (1.0 - r));
    
    // Mostramos el valor por defecto del día 15
    dia_tratamiento = 15;
    cantidad_en_cuerpo = dosis_diaria * (1.0 - pow(r, dia_tratamiento)) / (1.0 - r);
    printf("La cantidad el día %d es %.2f mg\n", dia_tratamiento, cantidad_en_cuerpo);

    // --- EXPERIMENTA (Aquí pedimos el día y lo usamos) ---
    // En Python: dia_tratamiento = int(input("..."))
    printf("\nIntroduce el día de tratamiento: ");
    scanf("%d", &dia_tratamiento); 

    // Calculamos de nuevo usando el valor que el usuario acaba de escribir
    cantidad_en_cuerpo = dosis_diaria * (1.0 - pow(r, dia_tratamiento)) / (1.0 - r);
    
    printf("La cantidad de medicamento el día %d es %.2f mg\n", dia_tratamiento, cantidad_en_cuerpo);

    return 0;
}