// Implementacion en C, desde un enfoque imperativo, del programa que calcula la suma de una lista de numeros

#include <stdio.h>

int sum(int array[], int size) {
    int total = 0; 
    for (int i = 0; i < size; i++) {
        total += array[i];
    }
    return total;
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    printf("Sum: %d\n", sum(numbers, size));  // Salida: 15
    return 0;
}
