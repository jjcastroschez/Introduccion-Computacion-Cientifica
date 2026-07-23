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

# 📝 Ejercicios - Tema 6: Tipos de Datos Complejos 🧺

A continuación encontrarás ejercicios que te ayudarán a consolidar los tipos de datos complejos del Tema 6: **cadenas** (manipulación, slicing), **listas y tuplas**, **diccionarios**, **`namedtuple`**, **conjuntos**, y el estilo **funcional** con `map`, `filter`, `reduce`, `sorted` y `zip`.

> [!TIP]
> Cada ejercicio incluye:
> * 📋 **Enunciado** con un objetivo claro.
> * 🧮 **Pseudocódigo orientativo** que te guía sin darte la solución.
> * 🛠️ **Tareas** concretas.
> * 🫣 **Una solución plegable** para consultarla **solo después** de intentarlo.

> [!NOTE]
> Muchos de estos ejercicios se pueden resolver de **varias formas** — con bucles del [Tema 4](../../04_control_flujo_ejecucion/README.md), con métodos de listas del Tema 6, o con estilo funcional. Cuando puedas, ¡intenta las dos versiones y compara!

---

## 🟢 Bloque 1: Cadenas

### Ejercicio 1. Contar vocales 🔤

Escribe una función `contar_vocales(texto)` que devuelva el número de vocales (a, e, i, o, u) presentes en `texto`, sin distinguir mayúsculas ni minúsculas.

#### 🧮 Pseudocódigo orientativo

```text
función contar_vocales(texto):
    vocales = "aeiou"
    total = 0
    para cada letra en texto pasado a minúsculas:
        si letra está en vocales:
            total += 1
    devolver total
```

#### 🛠️ Tareas

1. Implementa la función.
2. Pruébala con al menos 4 casos, incluyendo:
   * Una cadena vacía (`""`).
   * Una cadena solo con consonantes (`"xyz"`).
   * Una cadena en mayúsculas.

> 💡 **Pista**: `texto.lower()` te devuelve el texto en minúsculas. El operador `in` comprueba si un carácter está en la cadena `"aeiou"`.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def contar_vocales(texto: str) -> int:
    vocales = "aeiou"
    total = 0
    for letra in texto.lower():
        if letra in vocales:
            total = total + 1
    return total
```

📄 [Solución completa: contar_vocales.py](./contar_vocales.py)
</details>

---

### Ejercicio 2. Invertir una cadena sin slicing 🔄

Escribe una función `invertir_manual(texto)` que devuelva el texto invertido, **sin usar el slicing `[::-1]`**. La idea es consolidar el patrón de recorrido carácter a carácter con acumulador.

#### 🧮 Pseudocódigo orientativo

```text
función invertir_manual(texto):
    resultado = ""
    para cada letra en texto:
        resultado = letra + resultado    # ← ojo: al PRINCIPIO
    devolver resultado
```

#### 🛠️ Tareas

1. Implementa `invertir_manual` sin usar slicing.
2. Comprueba que devuelve lo mismo que la versión con `[::-1]`.
3. **Reflexión**: ¿por qué en `resultado = letra + resultado` la letra va **al principio**? Prueba a ponerla al final y verás que el texto no se invierte.

> 💡 **Truco mental**: si vas recorriendo el texto de izquierda a derecha y quieres invertirlo, cada nueva letra debe quedar **más a la izquierda** que las anteriores. Por eso `letra + resultado`, no `resultado + letra`.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def invertir_manual(texto: str) -> str:
    resultado = ""
    for letra in texto:
        resultado = letra + resultado
    return resultado
```

📄 [Solución completa: invertir_string.py](./invertir_string.py)
</details>

---

## 🟡 Bloque 2: Listas y tuplas

### Ejercicio 3. Mínimo y máximo sin `min`/`max` 🔍

Implementa tus propias funciones `min_manual(lista)` y `max_manual(lista)` para encontrar el menor y el mayor elemento **sin usar** las funciones nativas `min()` y `max()`. Después crea una función `min_max(lista)` que devuelva **ambos a la vez** en un solo recorrido.

#### 🧮 Pseudocódigo orientativo (para `min_manual`)

```text
función min_manual(lista):
    si lista está vacía: lanzar ValueError
    candidato = lista[0]
    para cada x en lista:
        si x < candidato:
            candidato = x
    devolver candidato
```

#### 🛠️ Tareas

1. Implementa `min_manual` y `max_manual`.
2. Implementa `min_max(lista)` que devuelva una **tupla** `(mínimo, máximo)` haciendo **un solo recorrido**.
3. Compara los resultados con los nativos `min(lista)` y `max(lista)`.
4. **Reflexión**: `min_max` es más eficiente que llamar a `min_manual` y `max_manual` por separado. ¿Por qué?

> 💡 **Pista**: en `min_max`, inicializas `minimo = maximo = lista[0]` y luego con un solo `for` compruebas ambas condiciones.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def min_max(numeros: list) -> tuple:
    if len(numeros) == 0:
        raise ValueError("Lista vacía.")
    minimo = numeros[0]
    maximo = numeros[0]
    for x in numeros:
        if x < minimo:
            minimo = x
        if x > maximo:
            maximo = x
    return minimo, maximo
```

📄 [Solución completa: min_max_manual.py](./min_max_manual.py)
</details>

---

### Ejercicio 4. Histograma de calificaciones 📊

Dada una lista de notas (entre 0 y 10), clasifica cuántas caen en cada franja del sistema español de calificaciones:

| Franja | Rango |
|:---|:---:|
| Suspenso | [0, 5) |
| Aprobado | [5, 7) |
| Notable | [7, 9) |
| Sobresaliente | [9, 10] |

Devuelve el resultado como un **diccionario** `{franja: cuántas}`.

#### 🛠️ Tareas

1. Implementa `histograma(notas)` que devuelva el diccionario descrito.
2. Escribe una función `mostrar_histograma(h)` que imprima el histograma con **barras de estrellas** (una `★` por cada nota).
3. Verifica que la **suma de valores** del diccionario coincide con la longitud de la lista original.

> 💡 **Pista**: usa `elif` para clasificar cada nota en una franja. La comparación `nota < 5` cubre `[0, 5)`; luego `nota < 7` cubre `[5, 7)`; etc.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

Se combina un diccionario inicializado a cero con una cadena de `if/elif/else`. Ver detalles en la solución completa.

📄 [Solución completa: histograma.py](./histograma.py)
</details>

---

## 🟠 Bloque 3: Programación funcional

### Ejercicio 5. `map`, `filter`, `reduce` en acción λ

Dada la lista `[1, 2, 3, 4, 5, 6, 7]`, calcula usando **programación funcional**:

1. La **suma de los cuadrados** de los NÚMEROS PARES.
2. El **producto** de los NÚMEROS MAYORES QUE 3.

#### 🧮 Pseudocódigo orientativo (para el 1)

```text
1) filter para quedarnos con los pares
2) map para elevar al cuadrado
3) sum para sumar
```

#### 🛠️ Tareas

1. Implementa `suma_cuadrados_pares_funcional(numeros)` combinando `filter`, `map` y `sum`.
2. Implementa `producto_mayores_que_3_funcional(numeros)` combinando `filter` y `reduce`. Recuerda: `reduce` necesita `from functools import reduce`.
3. Escribe también las **versiones con bucle** (`_bucle`) y comprueba que dan el mismo resultado.
4. Los valores esperados son:
   * $2^2 + 4^2 + 6^2 = 4 + 16 + 36 = 56$
   * $4 \cdot 5 \cdot 6 \cdot 7 = 840$

> 💡 **Truco con `reduce`**: para no dar problemas con listas vacías, pásale un **valor inicial** como tercer argumento: `reduce(f, lista, valor_inicial)`. Para el producto, el neutro es `1`.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
from functools import reduce

def suma_cuadrados_pares_funcional(numeros: list) -> int:
    pares = filter(lambda x: x % 2 == 0, numeros)
    cuadrados = map(lambda x: x ** 2, pares)
    return sum(cuadrados)

def producto_mayores_que_3_funcional(numeros: list) -> int:
    mayores = filter(lambda x: x > 3, numeros)
    return reduce(lambda a, b: a * b, mayores, 1)
```

📄 [Solución completa: funcional_practica.py](./funcional_practica.py)
</details>

---

## 🔵 Bloque 4: Diccionarios

### Ejercicio 6. Agenda telefónica CRUD 📞

Implementa las cuatro operaciones básicas sobre una **agenda** almacenada como un diccionario `{nombre: telefono}`:

1. `anadir(agenda, nombre, telefono)`: añade un contacto (si ya existe, avisa y **no lo sobreescribe**).
2. `buscar(agenda, nombre)`: devuelve el teléfono (o `None` si no está).
3. `modificar(agenda, nombre, nuevo_telefono)`: cambia el teléfono (solo si el contacto ya existe).
4. `eliminar(agenda, nombre)`: elimina el contacto (con aviso si no existe).

Añade también `listar(agenda)` que muestre todos los contactos **por orden alfabético**.

#### 🛠️ Tareas

1. Implementa las 5 funciones.
2. Escribe un `main()` que las pruebe en secuencia (añadir varios, buscar, modificar, eliminar, listar).
3. **Reflexión**: ¿qué diferencia hay entre `agenda[nombre]` y `agenda.get(nombre)`? ¿Cuándo usarías cada uno?

> 💡 **Pistas**:
> * Para eliminar: `agenda.pop(nombre)` quita y devuelve el valor.
> * Para comprobar existencia: `if nombre in agenda: ...`
> * Para ordenar alfabéticamente al listar: `for n in sorted(agenda): ...`

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

📄 [Solución completa: agenda.py](./agenda.py)

Fíjate especialmente en el **patrón defensivo** de cada función: siempre comprueba primero si el contacto está o no está en la agenda antes de hacer nada, para evitar errores.
</details>

---

### Ejercicio 7. Contador de letras 📚

Escribe una función `contar_letras(texto)` que devuelva un **diccionario** `{letra: veces}` con la frecuencia de cada letra en el texto, **ignorando espacios y signos de puntuación**.

Y una función `letras_mas_frecuentes(texto, n)` que devuelva las `n` letras más frecuentes como una lista de tuplas `(letra, veces)`, ordenadas de mayor a menor.

#### 🧮 Pseudocódigo orientativo

```text
función contar_letras(texto):
    contador = {}
    para cada c en texto en minúsculas:
        si c es letra (c.isalpha()):
            contador[c] = contador.get(c, 0) + 1
    devolver contador
```

#### 🛠️ Tareas

1. Implementa `contar_letras` usando el patrón `dict.get(c, 0) + 1`.
2. Usa el método `.isalpha()` de string para ignorar espacios, dígitos y signos.
3. Implementa `letras_mas_frecuentes(texto, n)` ordenando el resultado con `sorted` + `key=lambda`.
4. **Aplicación clásica**: en español, la letra más frecuente es la 'e', seguida de la 'a'. En inglés es también la 'e', pero luego la 't'. ¿Es cierto en tu texto de prueba?

> 💡 **Contexto matemático**: el análisis de frecuencia de letras es la técnica principal para romper cifrados clásicos (César, Vigenère). Un texto en español tiene una "huella" de frecuencias muy característica.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def contar_letras(texto: str) -> dict:
    contador = {}
    for c in texto.lower():
        if c.isalpha():
            contador[c] = contador.get(c, 0) + 1
    return contador

def letras_mas_frecuentes(texto: str, n: int = 5) -> list:
    c = contar_letras(texto)
    ordenado = sorted(c.items(), key=lambda par: par[1], reverse=True)
    return ordenado[:n]
```

📄 [Solución completa: contar_letras.py](./contar_letras.py)
</details>

---

## 🟣 Bloque 5: Conjuntos y namedtuple

### Ejercicio 8. Quitar duplicados preservando el orden 🎯

Sabes que `set(lista)` elimina duplicados, pero **destruye el orden**. Escribe una función `quitar_duplicados(lista)` que elimine los duplicados **manteniendo el orden de la primera aparición** de cada elemento.

#### 🧮 Pseudocódigo orientativo

```text
función quitar_duplicados(lista):
    vistos = conjunto vacío
    resultado = lista vacía
    para cada x en lista:
        si x no está en vistos:
            añadir x a resultado
            añadir x a vistos
    devolver resultado
```

#### 🛠️ Tareas

1. Implementa la función combinando una **lista** (para conservar el orden) con un **conjunto** (para las consultas rápidas de "¿ya lo he visto?").
2. Compara con `sorted(set(lista))`: ¿en qué se diferencia?
3. **Reflexión**: ¿por qué usamos un **conjunto** para `vistos` y no otra lista? (Pista: `x in set` es mucho más rápido que `x in list` en colecciones grandes.)

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def quitar_duplicados(lista: list) -> list:
    vistos = set()
    resultado = []
    for x in lista:
        if x not in vistos:
            resultado.append(x)
            vistos.add(x)
    return resultado
```

📄 [Solución completa: quitar_duplicados.py](./quitar_duplicados.py)
</details>

---

### Ejercicio 9. Operaciones matemáticas sobre matriculados 🎓

Dados los conjuntos de estudiantes matriculados en tres asignaturas de primer curso (álgebra, análisis, geometría), responde a las siguientes preguntas usando **solo operaciones de conjuntos** (unión `|`, intersección `&`, diferencia `-`):

1. ¿Quiénes están matriculados en **al menos una** asignatura?
2. ¿Quiénes están matriculados en **las tres**?
3. ¿Quiénes están **solo en álgebra**?
4. ¿Quiénes están en **al menos dos**?
5. ¿Quiénes están en **exactamente una**?

#### 🛠️ Tareas

1. Implementa cinco funciones, una para cada pregunta.
2. Todas deben usar **solo** los operadores de conjuntos: `|`, `&`, `-`, `^`.
3. Piensa antes de escribir: por ejemplo, "al menos dos" no es lo mismo que "las tres". "Exactamente una" tampoco es lo mismo que "al menos una".

> 💡 **Ayuda matemática**: piensa en diagramas de Venn. "En exactamente una" = (unión total) − (los que están en al menos dos). "En al menos dos" = (A∩B) ∪ (A∩C) ∪ (B∩C).

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def alumnos_en_al_menos_una(a, b, c):
    return a | b | c

def alumnos_en_las_tres(a, b, c):
    return a & b & c

def alumnos_solo_en_a(a, b, c):
    return a - b - c

def alumnos_en_al_menos_dos(a, b, c):
    return (a & b) | (a & c) | (b & c)

def alumnos_en_exactamente_una(a, b, c):
    return (a | b | c) - ((a & b) | (a & c) | (b & c))
```

📄 [Solución completa: matriculados.py](./matriculados.py)
</details>

---

### Ejercicio 10. Puntos en el plano con `namedtuple` 📍

Define un tipo `Punto` con dos campos (`x`, `y`) usando `namedtuple`. Después, implementa las siguientes operaciones geométricas:

1. `distancia(p1, p2)`: distancia euclídea $\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$.
2. `punto_medio(p1, p2)`: devuelve un nuevo `Punto` con las coordenadas del punto medio del segmento.
3. `a_polares(p)`: devuelve una tupla `(r, θ)` con las coordenadas polares del punto.

#### 🛠️ Tareas

1. Importa `namedtuple` desde `collections` y define `Punto = namedtuple("Punto", ["x", "y"])`.
2. Implementa las tres funciones. Accede a los campos por nombre: `p.x`, `p.y`.
3. Prueba con `origen = Punto(0, 0)` y `a = Punto(3, 4)`:
   * `distancia(origen, a)` debería dar **5.0** (triángulo egipcio 3-4-5).
   * `punto_medio(origen, a)` debería dar `Punto(1.5, 2.0)`.
   * `a_polares(a)` debería dar aproximadamente `(5.0, 0.9273)` (que son 5 y 53.13°).

> 💡 **Ventaja de `namedtuple`**: puedes usar la sintaxis `p.x` para acceder por nombre **y también** `p[0]` como si fuera una tupla normal. Además puedes desempaquetar: `x, y = p`.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math
from collections import namedtuple

Punto = namedtuple("Punto", ["x", "y"])

def distancia(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def punto_medio(p1, p2):
    return Punto((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

def a_polares(p):
    r = math.sqrt(p.x**2 + p.y**2)
    theta = math.atan2(p.y, p.x)
    return r, theta
```

📄 [Solución completa: puntos.py](./puntos.py)
</details>

---

## 🎯 Reto final — Análisis de texto

Este reto **combina prácticamente todos los conceptos** del tema: cadenas, diccionarios, conjuntos, funciones de orden superior y modelado con listas.

> [!IMPORTANT]
> Este reto **no tiene solución publicada** en el repositorio. Es tu oportunidad de aplicar todo lo aprendido. El esqueleto está en [`reto_texto.py`](./reto_texto.py) — **complétalo tú**.

### 📋 Enunciado

Escribe un programa que, dado un texto (una cadena), calcule y muestre las siguientes estadísticas:

1. **Número total de palabras** (separadas por espacios).
2. **Número de palabras distintas**.
3. **Longitud media** de las palabras.
4. Las **5 palabras más frecuentes** (con su número de apariciones).
5. Las palabras que aparecen **exactamente una vez** (en lingüística se llaman *hapax legomena*).
6. Las palabras de **longitud ≥ 6** que aparecen **al menos 2 veces** (palabras "largas y frecuentes").

**Normalización previa** del texto:

* Pasar a minúsculas.
* Quitar signos de puntuación: `, . ; : ! ? ¡ ¿ " ' ( )`.
* Separar por espacios usando `.split()`.

### 🛠️ Tareas

1. Implementa una función `analizar(texto)` que devuelva un **diccionario** con las 6 estadísticas.
2. Escribe un `main()` que muestre los resultados de forma clara.
3. Verifica que tu solución da resultados consistentes: la suma de frecuencias del diccionario debe coincidir con el total de palabras.

### ★ Puntos extra (opcional)

#### ★ Índice de riqueza léxica

Calcula el **índice de riqueza léxica**:

$$\text{TTR} = \frac{\text{palabras distintas}}{\text{palabras totales}}$$

Es un ratio entre 0 y 1 que mide cuán variado es el vocabulario. Textos científicos suelen tener valores entre 0.5 y 0.7. Textos de temática restringida y con mucha repetición pueden bajar de 0.3.

#### ★★ Palabra más larga

Encuentra la **palabra más larga** del texto. Si hay empates, devuelve **todas** las palabras más largas. (Pista: `max(palabras, key=len)` te da una; para todas, filtra por esa longitud.)

#### ★★★ Anagramas

Encuentra los grupos de palabras que son **anagramas** entre sí. Dos palabras son anagramas si contienen exactamente las mismas letras en distinto orden.

**Idea clave**: dos palabras son anagramas si y solo si `sorted(palabra1) == sorted(palabra2)`.

**Truco**: usa un diccionario cuyas claves sean tuplas de letras ordenadas y cuyos valores sean **listas** de las palabras que producen esa combinación:

```python
grupos = {}
for palabra in palabras_distintas:
    clave = tuple(sorted(palabra))
    grupos[clave] = grupos.get(clave, []) + [palabra]
# Luego, los grupos con más de un elemento son grupos de anagramas
```

### 🧐 Para reflexionar

* ¿Qué palabras son las más frecuentes en la mayoría de textos en español? (Pista: las **palabras vacías** o *stopwords*: la, de, que, y, el...). En análisis de texto serio se suelen filtrar antes.
* ¿Cómo cambia el resultado si el texto está en inglés? ¿Y en un lenguaje aglutinante como el euskera?

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T6_ICC.md)              |     12       |
| 2      | [Recursos](../recursos/T6_RE_ICC.md)       |      7       |
| 3      | [Ejemplos](../ejemplos/T6_Ejem_ICC.md)     |      -       |
| 4      | **Ejercicios**                             |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
