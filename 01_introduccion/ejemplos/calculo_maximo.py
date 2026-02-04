def maximo(lista):
    max_valor = lista[0]
    for num in lista[1:]:
        if num > max_valor:
            max_valor = num
    return max_valor

# Uso de la función
numeros = [3, 5, 7, 2, 8, 1]
resultado = maximo(numeros)
print(f"El número máximo es: {resultado}")
