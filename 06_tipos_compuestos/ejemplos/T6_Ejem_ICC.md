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

# 🧐 Ejemplos - Tema 6: Tipos de Datos Complejos 🧺

En esta carpeta encontrarás Notebooks de Jupyter y scripts que muestran los distintos **tipos de datos complejos** del Tema 6: cadenas, listas, tuplas, diccionarios, `namedtuple`, `dataclass` y conjuntos. Verás también cómo estos tipos abren la puerta a un estilo más elegante de programación con las **funciones de orden superior** (`map`, `filter`, `reduce`, `zip`, `enumerate`, `sorted`).

> [!NOTE]
> A partir de este tema, muchos programas del Tema 4 se pueden **reescribir de forma más concisa y clara**. Verás varios ejemplos de esa evolución: donde antes usábamos acumuladores, ahora usamos listas y funciones agregadas.

## Contenido

En los temas anteriores has aprendido a resolver problemas usando **variables sueltas** ([Tema 3](../../03_variables_tipos_simples/README.md)), a **tomar decisiones y repetir cálculos** ([Tema 4](../../04_control_flujo_ejecucion/README.md)) y a **estructurar** tu código con funciones y módulos ([Tema 5](../../05_programacion_modular/README.md)). Ahora, con los **tipos de datos complejos**, damos otro salto: podemos **modelar problemas del mundo real** usando estructuras que agrupan varios valores relacionados.

Los ejemplos que verás a continuación te enseñarán a:

* **Manipular cadenas** con métodos y *slicing* para resolver problemas clásicos.
* **Guardar colecciones ordenadas** en listas y tuplas, y elegir con criterio entre unas y otras.
* **Modelar entidades** (personas, libros, coordenadas) con diccionarios, `namedtuple` o `dataclass`.
* **Comparar** cómo Python y C resuelven estos mismos problemas.
* **Aplicar operaciones de conjuntos** en su sintaxis matemática natural.
* **Reemplazar bucles largos** por expresiones cortas con `map`, `filter`, `reduce`, `zip`, `enumerate` y `sorted`.

### Ejemplo 1. Detector de palíndromos

Un problema clásico y muy elegante para inaugurar el trabajo con cadenas. Un **palíndromo** es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda: *Ana*, *reconocer*, *Anita lava la tina*.

Aprenderás:

* Los métodos más útiles del tipo `str`: `.lower()`, `.replace()`.
* El **slicing con paso negativo** `cadena[::-1]`, que invierte una cadena **en una sola expresión**.
* La **inmutabilidad de las cadenas**: por qué hay que reasignar los resultados de los métodos.

**Lo que aporta el Tema 6**: con solo el slicing `[::-1]`, un problema que en el Tema 4 requería un bucle explícito de dos punteros se resuelve **en una línea**.

#### Empleando Python:

👉 Notebook explicado paso a paso: [palindromo_exp_py.ipynb](./palindromo_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar: [palindromo.py](./palindromo.py).

### Ejemplo 2. Estadísticas de una lista de calificaciones

Introduce las notas de un grupo de estudiantes y calcula sobre ellas la **media**, la **desviación estándar**, el **máximo**, el **mínimo** y **cuántos han aprobado**. Es la evolución natural del cálculo con acumuladores del [Tema 4](../../04_control_flujo_ejecucion/README.md): ahora guardamos todos los datos en una **lista** para poder recorrerla varias veces.

Aprenderás:

* Construcción **dinámica** de una lista con `.append()`.
* Uso de las funciones agregadas `sum()`, `len()`, `min()`, `max()` sobre secuencias.
* Cómo escribir funciones que **reciben una lista como argumento** (integración con [Tema 5](../../05_programacion_modular/README.md)).
* Manejo de la validación de entrada del usuario con `try-except`.

**Lo que aporta el Tema 6**: guardar los datos en una lista nos permite calcular **cualquier estadística** las veces que queramos, sin tener que volver a leer los datos.

#### Empleando Python:

👉 Notebook explicado paso a paso: [estadisticas_exp_py.ipynb](./estadisticas_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar: [estadisticas.py](./estadisticas.py).

### Ejemplo 3. Datos de profesores: lista de tuplas con desempaquetado

Modelamos un grupo de profesores como una **lista de tuplas**, donde cada tupla contiene los datos de un profesor (nombre, correo, asignatura, curso, cuatrimestre). Después, hacemos varias operaciones típicas: recorrerlos, filtrar por curso, ordenar por criterio.

Aprenderás:

* Cómo estructurar información con **listas de tuplas**.
* El **desempaquetado** en el `for`, que hace el código mucho más legible que acceder por índice (`prof[3]`).
* Uso de `sorted()` con **`key=lambda`** para ordenar por criterios personalizados.
* Ordenar por **varios criterios a la vez** devolviendo una tupla en la lambda.

**Lo que aporta el Tema 6**: el desempaquetado y las funciones de ordenación transforman código con bucles anidados en pocas líneas muy legibles.

#### Empleando Python:

👉 Notebook explicado paso a paso: [profesores_exp_py.ipynb](./profesores_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar: [profesores.py](./profesores.py).

### Ejemplo 4. Programación funcional aplicada a secuencias

Este ejemplo compara **lado a lado** cómo se resolvían ciertos problemas en el [Tema 4 (con bucles y acumuladores)](../../04_control_flujo_ejecucion/ejemplos/T4_Ejem_ICC.md) y cómo se resuelven ahora, con las **funciones de orden superior** de Python: `map`, `filter`, `reduce`, `zip`, `enumerate`, `sorted`, `any` y `all`.

Verás:

* La transición **bucle → funcional** para cada una de estas funciones.
* Cuándo usar cada una y cuándo seguir con el bucle explícito.
* Un caso matemático muy limpio: **media ponderada** con `zip` en una sola línea.
* Uso de **generadores** dentro de `any` y `all` para comprobaciones rápidas.

**Lo que aporta el Tema 6**: muchos cálculos sobre colecciones enteras se pueden expresar de forma **declarativa** ("qué queremos") en lugar de **imperativa** ("cómo hacerlo paso a paso"). Es un cambio de perspectiva importante.

#### Empleando Python:

👉 Notebook explicado paso a paso: [funcional_exp_py.ipynb](./funcional_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar: [funcional.py](./funcional.py).

### Ejemplo 5. Representar un libro: `dict`, `namedtuple` y `dataclass`

Cuando queremos agrupar **datos heterogéneos** de una entidad (título, autor, año...), Python nos ofrece **tres opciones**: diccionarios, `namedtuple` y `dataclass`. Este ejemplo compara las tres para que veas cuándo conviene cada una.

Aprenderás:

* Cómo crear y usar cada tipo.
* Diferencias en **mutabilidad**: `dict` y `dataclass` son mutables, `namedtuple` no.
* Cómo **desempaquetar** una `namedtuple` como si fuera una tupla.
* El uso del **decorador `@dataclass`** de la biblioteca estándar.

Y en la versión C verás el **`struct`** clásico, que es el ancestro conceptual de todos estos tipos en cualquier lenguaje.

**Lo que aporta el Tema 6**: elegir bien el tipo de estructura para representar información hace tu código **más claro** y **menos propenso a errores**.

#### Empleando Python:

👉 Notebook explicado paso a paso: [libros_exp_py.ipynb](./libros_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar: [libros.py](./libros.py).

#### Empleando C:

👉 Notebook explicado paso a paso: [libros_exp_c.ipynb](./libros_exp_c.ipynb).  
👉 Programa `.c` listo para compilar y ejecutar: [libros.c](./libros.c).

### Ejemplo 6. Conjuntos: unicidad y operaciones matemáticas

Los **conjuntos** (`set`) son el tipo especial de este tema: guardan una colección **desordenada** y sin **duplicados**. En este ejemplo verás sus dos usos estrella:

1. **Eliminar duplicados** de una colección con una simple llamada a `set()`.
2. **Operaciones matemáticas de conjuntos**: unión (`|`), intersección (`&`), diferencia (`-`), diferencia simétrica (`^`) — usando **los mismos operadores** que en teoría de conjuntos matemática.

Aprenderás también:

* Por qué `{}` no crea un conjunto vacío (crea un diccionario).
* El poder de la **comprobación de pertenencia** con `in` sobre conjuntos (¡velocidad casi constante!).
* Los métodos `.add()`, `.discard()`, `.remove()`.

**Lo que aporta el Tema 6**: para un matemático, Python ofrece los conjuntos con sintaxis natural y potencia inigualable. Muchos problemas de combinatoria y probabilidad se traducen directamente.

#### Empleando Python:

👉 Notebook explicado paso a paso: [conjuntos_exp_py.ipynb](./conjuntos_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar: [conjuntos.py](./conjuntos.py).

### Ejemplo 7. Contador de palabras con diccionario

Un problema clásico donde el diccionario brilla: dado un texto, contamos **cuántas veces aparece cada palabra**. Es el ejemplo perfecto de un diccionario como estructura clave-valor, donde la clave es la palabra y el valor es el contador.

Aprenderás:

* El patrón **`dict.get(clave, 0) + 1`** para contar apariciones sin `if/else`.
* Métodos de string aplicados: `.lower()`, `.replace()`, `.split()`.
* Iteración sobre `dict.items()` para acceder a claves y valores simultáneamente.
* Ordenación del resultado con `sorted(dict.items(), key=lambda par: par[1])`.
* Como alternativa moderna: **`collections.Counter`**, la clase específica para conteo de la biblioteca estándar.

**Lo que aporta el Tema 6**: el conteo con diccionarios es una operación **fundamental** en cualquier tipo de análisis de datos. Aparece en lingüística, bioinformática (contar bases en un ADN), estadística, machine learning...

#### Empleando Python:

👉 Notebook explicado paso a paso: [contador_palabras_exp_py.ipynb](./contador_palabras_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar: [contador_palabras.py](./contador_palabras.py).

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T6_ICC.md)              |     12       |
| 2      | [Recursos](../recursos/T6_RE_ICC.md)       |      7       |
| 3      | **Ejemplos**                               |      -       |
| 4      | [Ejercicios](../ejercicios/T6_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
