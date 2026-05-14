#include <stdio.h>

int main() {
    // --- DECLARACION DE VARIABLES ---
    float capital_inicial;
    float porcentaje_interes_anual;
    int  tiempo;

    float interes_anual;
    float interes_simple;
    float monto_final;

    // --- ENTRADA DE DATOS -- 

    printf("Capital inicial: ");
    scanf("%f", &capital_inicial);
    printf("Tasa de interés anual (%%): ");
    scanf("%f", &porcentaje_interes_anual);
    printf("Tiempo en años: ");
    scanf("%d", &tiempo);   

    // --- CÁLCULOS INICIALES ---
    
    interes_anual = porcentaje_interes_anual / 100.0;
    interes_simple = capital_inicial * interes_anual * tiempo;  
    monto_final = capital_inicial + interes_simple;
    

    // --- SALIDA DE RESULTADOS ---
    printf("\nInterés simple: %.2f\n", interes_simple);
    printf("Monto total: %.2f\n", monto_final);

    return 0;
}