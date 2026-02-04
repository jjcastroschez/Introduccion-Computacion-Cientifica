# Implemantacion en Python, desde un enfoque Imperativo de la suma de una lista de numeros

# Funcion para calcular la suma de una lista de numeros
def sum_list(numbers):
    total = 0 # Variable para acumular la suma, se inicializa a cero
    for number in numbers:  # Bucle para iterar sobre los numeros
        total += number  
    return total

# Variable con la Lista de números
numbers = [1, 2, 3, 4, 5]

# Instruccion para mostrar el resultado de la suma de la lista de numeros 
print(sum_list(numbers))  # Salida: 15
