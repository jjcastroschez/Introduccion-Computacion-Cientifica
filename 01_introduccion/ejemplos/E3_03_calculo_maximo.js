class Calculadora {
  constructor() {}

  maximo(numeros) {
    let max_valor = numeros[0];
    numeros.forEach(num => {
      if (num > max_valor) {
        max_valor = num;
      }
    });
    return max_valor;
  }
}

// Uso de la clase Calculadora
const calculadora = new Calculadora();
const numeros = [3, 5, 7, 2, 8, 1];
const resultado = calculadora.maximo(numeros);
console.log(`El número máximo es: ${resultado}`);
