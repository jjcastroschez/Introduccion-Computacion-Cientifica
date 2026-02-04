class ListSum
  # El método initialize es el constructor de la clase. Se invoca cuando creas una nueva instancia de ListSum.
  # Recibe una lista de números como argumento y la almacena en la variable de instancia @numbers.
  def initialize(numbers)
    @numbers = numbers  # Guardamos la lista de números como un atributo de instancia de la clase
  end

  # Este método sum utiliza un enfoque funcional mediante el método `reduce` de Ruby.
  # `reduce` es una función de orden superior que aplica una operación acumulativa a todos los elementos de la lista.
  def sum
    # `reduce(0)` significa que inicializamos el acumulador en 0, y luego sumamos cada número de la lista.
    # Dentro del bloque, `total` es el acumulador y `number` es el elemento actual de la lista.
    @numbers.reduce(0) { |total, number| total + number }
  end
end

# Aquí estamos creando una instancia de la clase ListSum. Le pasamos la lista de números [1, 2, 3, 4, 5] como argumento.
list_sum = ListSum.new([1, 2, 3, 4, 5])

# Luego, llamamos al método sum de la instancia list_sum.
# Este método calculará la suma de los números en la lista usando el enfoque funcional de `reduce`.
puts list_sum.sum  # Imprimimos el resultado, que debería ser 15.
