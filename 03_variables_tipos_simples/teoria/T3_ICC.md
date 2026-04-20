
<div align="center">
  <h1> Introducción a la Computación Científica (ICC)</h1>

  <sub>Autor:
<a href="https://www.esi.uclm.es/www/jjcastro/" target="_blank">J.J. Castro-Schez</a><br>
<small> Primera edición: febrero de 2026</small>
</sub>

  <a class="header-badge" target="_blank" href="https://jjcastroschez.github.io">
  <img alt="GitHub Page" src="https://img.shields.io/badge/github%20page-grey?style=for-the-badge&logo=github">
  </a>

</div>

# Teoría - Tema 3: Tipos de Datos Simples y Variables 🔢

En este tema daremos el salto de la lógica pura del algoritmo a la gestión real de la información. Aprenderás cómo los ordenadores almacenan datos y cómo nosotros, cuando programamos, los clasificamos y manipulamos mediante variables.

---

## 🏗️ Sección 1: El Dato: Hardware vs. Software

Como ya sabes, un programa no es más que un proceso que toma **datos de entrada** los procesa y genera una **salida**.

Para que un programa procese una información, esta debe residir en la memoria. Sin embargo, la forma en que el ordenador "ve" el dato es distinta a la nuestra.

### 🔌 Perspectiva del Hardware
Para la máquina, todo son **ceros y unos (bits)**. 
- Un **tipo de dato** en el hardware es un **método para interpretar secuencias de bits**.
- La unidad mínima es el **bit**. 8 bits forman un **byte**, que permite representar 256 estados (0-255).
- Dependiendo de cómo interpretemos esos bits, la misma secuencia puede ser un número, una letra o parte de una imagen.

### 💻 Perspectiva del Software
Desde el lenguaje de programación, un tipo de dato se define por:
1.  **Dominio**. El conjunto de valores posibles (ej. todos los números enteros).
2.  **Conjunto de operaciones**. Las acciones válidas que se pueden realizar sobre o con esos valores (ej. no puedes "restar" letras, pero sí números).

---

## 🧩 Sección 2: Tipos de Datos Simples (Básicos o Primitivos)

Los lenguajes de programación suelen ofrecer cuatro tipos fundamentales:

1.  **Caracteres (`char`)**: Símbolos individuales (letras, dígitos, signos). Se basan en codificaciones como ASCII o Unicode. No existen en todos los lenguajes (p.e. este tipo de dato en Python no existe).  
2.  **Enteros (`int`)**: Números sin decimales. En Python tienen precisión arbitraria (crecen según se necesite), mientras que en C tienen un límite fijo (habitualmente 32 o 64 bits).
3.  **Reales o Punto Flotante (`float`/`double`)**: Números con decimales. 
4.  **Booleanos o Lógicos (`bool`)**: Solo dos valores: `True` (Verdadero) o `False` (Falso).

> [!WARNING]
> Los ordenadores no pueden representar todos los números reales con precisión infinita. Esto implica que en computación científica debemos tener cuidado con los errores de redondeo.

### 🛠️ Manipulación de Datos: Operadores y Relaciones
Cada tipo de dato lleva asociado un conjunto de **operadores** específicos que definen cómo podemos interactuar con ellos:

* **Operadores Aritméticos**: Permiten manipular datos numéricos (`int`, `float`) para obtener nuevos valores. 
    * *Ejemplos*: `+` (suma), `-` (resta), `*` (producto), `/` (división), `%` (módulo o resto).
* **Operadores Relacionales**: Permiten comparar dos datos (normalmente del mismo tipo) para establecer una relación entre ellos. El resultado de estas operaciones siempre es un valor **booleano** (`True` o `False`).
    * *Ejemplos*: `==` (igualdad), `!=` (desigualdad), `<` (menor que), `>` (mayor que), `<=` o `>=`.
* **Operadores Lógicos**: Permiten combinar valores booleanos.
    * *Ejemplos*: `AND` (y), `OR` (o), `NOT` (no).

> [!WARNING]
> Intentar usar un operador en un tipo de dato que no lo admite (por ejemplo, intentar dividir dos caracteres) provocará un error de tipo (*TypeError*), ya que la operación no está definida en ese dominio.

> [!TIP]
> **Sobre la precisión:** En computación científica, nunca compares dos números `float` usando `==`. Debido a la representación en binario, `0.1 + 0.2` no es exactamente `0.3`. Usa una pequeña tolerancia o funciones como `math.isclose()`. Ya lo veremos.

--- 

### 📊 Tabla de Operadores por Tipo de Dato

La siguiente tabla resume las operaciones más comunes y su aplicabilidad según el tipo de dato en lenguajes como Python y C:

| Tipo de Dato | Aritméticos (`+`, `-`, `*`, `/`) | Relacionales (`==`, `!=`, `<`, `>`) | Lógicos (`and`, `or`, `not`) | Notas |
| :--- | :---: | :---: | :---: | :--- |
| **Enteros (`int`)** | ✅ Sí | ✅ Sí | ⚠️ (1) | Operación aritmética estándar. |
| **Reales (`float`)** | ✅ Sí | ✅ Sí | ❌ No | Cuidado con `==` por errores de precisión. |
| **Booleanos (`bool`)** | ⚠️ (2) | ✅ Sí | ✅ Sí | Base de la lógica de control. |
| **Caracteres (`char`)** | ⚠️ (3) | ✅ Sí | ❌ No | Se comparan según su valor ASCII/Unicode. |

**Notas aclaratorias para clase:**
1. **Lógicos en Enteros**: En lenguajes como C o Python, el `0` se interpreta como `False` y cualquier otro número como `True`, permitiendo el uso de operadores lógicos.
2. **Aritmética Booleana**: En Python, `True + True` es igual a `2`, ya que internamente heredan de los enteros, aunque no es una buena práctica en computación científica.
3. **Aritmética de Caracteres**: En C es común sumar valores a un `char` para desplazarse en la tabla ASCII (ej. `'a' + 1` resulta en `'b'`).

### ⚖️ Sobrecarga y Casting
* **Sobrecarga de operadores**: Es cuando un símbolo (como `+`) hace cosas distintas según el tipo de dato. Por ejemplo: `5 + 5` es `10`, pero `"Hola " + "Mundo"` es `"Hola Mundo"`.
* **Casting (Conversión de tipos)**: Proceso de transformar un dato de un tipo a otro.
    * **Implícito**: Lo hace el lenguaje automáticamente (ej. sumar un entero y un real).
    * **Explícito**: El programador lo fuerza (ej. `int(3.14)` en Python devuelve `3`).

### 🔢 Precedencia de Operadores Aritméticos

Cuando una expresión contiene varios operadores aritméticos, el ordenador los evalúa en el siguiente orden estricto (de mayor a menor prioridad). Si los operadores tienen la misma prioridad, se evalúan de **izquierda a derecha**.

| Prioridad | Operador | Descripción | Ejemplo | Resultado |
| :---: | :---: | :--- | :--- | :--- |
| **1º** | `( )` | Paréntesis (Agrupación) | `(2 + 3) * 4` | `20` |
| **2º** | `**` | Exponenciación (Potencia) | `2 * 3 ** 2` | `18` |
| **3º** | `+x`, `-x` | Identidad y Negación (Unarios) | `-3 + 5` | `2` |
| **4º** | `*`, `/`, `//`, `%` | Multiplicación, División, Div. Entera y Módulo | `10 + 6 / 2` | `13.0` |
| **5º** | `+`, `-` | Suma y Resta | `10 - 2 + 3` | `11` |

> [!IMPORTANT]
> **División en Python vs C:** 
> - En **Python**, `/` siempre devuelve un real (`float`), mientras que `//` devuelve la parte entera.
> - En **C**, si divides dos enteros con `/`, el resultado se trunca automáticamente a entero.    

### 🔝 Orden de Precedencia entre operadores de distinto tipo
Cuando en una misma expresión aparecen varios operadores, el ordenador los ejecuta siguiendo un orden jerárquico (precedencia). Si los operadores tienen la misma jerarquía, se evalúan de izquierda a derecha.

| Prioridad | Operador | Descripción |
| :---: | :--- | :--- |
| **1** | `( )` | Paréntesis (alteran el orden natural) |
| **2** | `**` | Exponente (en Python) |
| **3** | `*`, `/`, `%`, `//` | Multiplicación, división, módulo y división entera |
| **4** | `+`, `-` | Suma y resta |
| **5** | `==`, `!=`, `<`, `>`, `<=`, `>=` | Operadores relacionales (comparaciones) |
| **6** | `not` | Negación lógica |
| **7** | `and` | Conjunción lógica |
| **8** | `or` | Disyunción lógica |

> [!TIP]
> Ante la duda o en expresiones muy largas, **usa paréntesis**. No solo aseguran que el cálculo sea correcto, sino que hacen que el código sea mucho más fácil de leer para otros humanos.



---

## 📦 Sección 3: Variables e Identificadores

Una **variable** es un nombre que apunta a un lugar en la memoria donde guardamos un valor.

### 🏷️ Identificadores y Estilo
El nombre que damos a la variable es el **identificador**. Para escribir código profesional, debemos seguir reglas de estilo:
- **Descriptivos**: `precio_total` es mejor que `pt`.
- **CamelCase o snake_case**: Sé consistente. En Python se prefiere `nombre_variable` (Snake Case), en C es común `nombreVariable` (Camel Case).
- **Prohibiciones**: No pueden empezar por número ni contener espacios o caracteres especiales (excepto `_`).

### 🛡️ Clasificación de los Lenguajes por su Tipado
| Concepto | Descripción |
| :--- | :--- |
| **Tipado Estático** | El tipo de la variable se define al crearla y no cambia (C, Java). |
| **Tipado Dinámico** | El tipo se determina en tiempo de ejecución según el valor asignado (Python). |
| **Tipado Fuerte** | El lenguaje impide operaciones entre tipos incompatibles (Python). |
| **Tipado Débil** | El lenguaje intenta convertir tipos de forma automática, a veces con resultados inesperados (JavaScript). |

---

## ⌨️ Sección 4: Entrada, Salida y Asignación

Para interactuar con el usuario:
- **Asignación**: Guardar un valor en una variable usando el operador `=`.
- **Entrada**: Obtener datos del teclado (`input()` en Python, `scanf()` en C).
- **Salida**: Mostrar datos en pantalla (`print()` en Python, `printf()` en C).

---

## 🚀 Sección 5: Del Algoritmo al Código

Transformemos un algoritmo simple de suma de dos números:

**Pseudocódigo:**
```text
ALGORITMO suma_dos_numeros
    Entrada: operando_1, operando_2 (enteros)
    Intermedias: -
    Salida: resultado_suma (entero)
INICIO
    1: ESCRIBIR ("Dame el primer operando: ")
    2: LEER (operando_1)
    3: ESCRIBIR ("Dame el segundo operando: ")
    4: LEER (operando_2)
    5: resultado_suma ← operando_1 + operando_2
    6: ESCRIBIR ("Suma: ", resultado_suma)
FIN
```
**Implementación usando Python:**
```python
# Entrada (Python lee todo como texto, usamos int() para convertir)
operando_1 = int(input("Dame el primer operando: "))
operando_2 = int(input("Dame el segundo operando: "))

# Proceso
resultado_suma = operando_1 + operando_2

# Salida
print(f"Suma: {resultado_suma}")
```
**Implementación usando C:**
```c
#include <stdio.h>

int main() {
    int operando_1, operando_2, resultado; // Declaración (Tipado Estático)
    
    printf("Dame el primer operando: ");
    scanf("%d", &operando_1);
    
    printf("Dame el segundo operando: ");
    scanf("%d", &operando_2);
    
    resultado_suma = operando_1 + operando_2;
    
    printf("Suma: %d\n", resultado_suma);
    return 0;
}
```
---

## ✅ Mini-checklist de autoevaluación

Antes de dar por finalizado este tema, comprueba si has asimilado los conceptos clave:

- [ ] ¿Comprendes que para el hardware un tipo de dato es solo una regla de interpretación de bits?
- [ ] ¿Diferencias entre el dominio de un dato y sus operaciones asociadas?
- [ ] ¿Eres capaz de identificar cuándo se produce una sobrecarga de operadores (ej. el uso de `+`)?
- [ ] ¿Entiendes la diferencia entre una conversión (casting) implícita y una explícita?
- [ ] ¿Sabes distinguir entre un lenguaje de tipado estático (como C) y uno dinámico (como Python)?
- [ ] ¿Podrías explicar por qué es importante seguir un estilo de nombrado (como `snake_case`)?
- [ ] ¿Entiendes el orden de precedencia y cómo el uso de paréntesis puede evitar errores en fórmulas matemáticas?

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) | 
|:------:|:-------------------------------------------|:------------:|
| 1      | **Teoría** |      10      |
| 2      | [Recursos](../recursos/T3_RE_ICC.md)       |      5       |
| 3      | [Ejemplos](../ejemplos/T3_Ejem_ICC.md)     |      -       |
| 4      | [Ejercicios](../ejercicios/T3_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |