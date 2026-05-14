#include <stdio.h>
#include <math.h>

int main() {
    // --- DECLARACION DE VARIABLES ---
    float pago_anual;
    float tasa_interes;
    float valor_perpetuidad;
    float valor_futuro;
    int k;  

    // --- ENTRADA DE DATOS --- 

    pago_anual = 100;  // La cantidad 'a'
    tasa_interes = 0.05;  // 5% de interés anual

    printf("\nPago anual prometido: %.2f€", pago_anual);
    printf("\nTasa de interés (descuento): %.1f%%", tasa_interes * 100);

    // --- CALCULOS --- 

    valor_perpetuidad = pago_anual / tasa_interes;

    printf("\nPara una tasa del %.1f%%, recibiendo %.2f€ anuales, el valor a perpetuidad es: %.2f€", tasa_interes * 100, pago_anual, valor_perpetuidad);

    printf("\nValor hoy del pago del año 5: %.2f€\n", (pago_anual/ pow((1+tasa_interes), 5)));
    printf("Valor hoy del pago del año 10: %.2f€\n", (pago_anual/ pow((1+tasa_interes), 10)));
    printf("Valor hoy del pago del año 25: %.2f€\n", (pago_anual/ pow((1+tasa_interes), 25)));
    printf("Valor hoy del pago del año 50: %.2f€\n", (pago_anual/ pow((1+tasa_interes), 50)));
    printf("Valor hoy del pago del año 100: %.2f€\n", (pago_anual/ pow((1+tasa_interes), 100)));

    // --- EXPERIMENTANDO (Aquí pedimos el día y lo usamos) ---

    printf("\nIntroduce el año k para ver el acumulado: ");
    scanf("%d", &k);

    valor_futuro = (pago_anual * (pow((1 + tasa_interes),k - 1))) / tasa_interes;

    printf("--- CAPITAL ACUMULADO ---\n");
    printf("En el año %d, con un pago de %.2f€ al %.1f%%, tendrás:\n", k, pago_anual, tasa_interes * 100);
    printf("%.2f€\n", valor_futuro);
    
    return 0;
}


