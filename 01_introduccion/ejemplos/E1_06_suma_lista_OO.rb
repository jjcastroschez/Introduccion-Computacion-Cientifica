class ListSum
  def initialize(numbers)
    @numbers = numbers  # Los números se guardan como un atributo de instancia
  end

  def sum
    total = 0
    @numbers.each do |number|  # Iterar sobre cada número de la lista
      total += number  # Acumular la suma
    end
    total  # Retornar el total
  end
end

# Crear una instancia de ListSum
list_sum = ListSum.new([1, 2, 3, 4, 5])

# Llamar al método sum para obtener la suma de los números
puts list_sum.sum  # Salida: 15
