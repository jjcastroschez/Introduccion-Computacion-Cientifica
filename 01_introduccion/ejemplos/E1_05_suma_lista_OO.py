# Implemantacion en Python, desde un enfoque Orientado a Objetos de la suma de una lista de numeros

# Definicion de una clase para almacenar la lista de numeros 
class ListSum:
# Metodo para inicializar los objetos de la clase    
    def __init__(self, numbers):
        self.numbers = numbers  # Guardamos la lista de números como atributo de instancia
# Metodo para realizar la suma
    def suma(self):
        total = 0 # Variable para acumular la suma, se inicializa a cero
        # Instruccion para iterar sobre los numeros en la lista
        for number in self.numbers:  
            total += number  # Acumulamos la suma
        return total  # Retornamos el total


# Crear una instancia (objeto) de la clase ListSum
list_sum = ListSum([1, 2, 3, 4, 5])

# Instruccion para imprimir por pantalla el resultado del metodo `suma` que obtiene la suma de los numeros de la lista
print(list_sum.suma())
