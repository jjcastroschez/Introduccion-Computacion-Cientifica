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

# 🔗 Recursos - Tema 6: Tipos de Datos Complejos 🧺

Los tipos complejos son un tema donde **la práctica y la referencia se retroalimentan**: cuanto más código escribas, más veces necesitarás recordar la sintaxis exacta de un método o el nombre de una función. Aquí tienes las mejores referencias oficiales y algunas herramientas visuales que te ayudarán a fijar los conceptos.

---

## 📚 Documentación oficial

### 🐍 Python: documentación de los tipos incorporados

- 📍 **[Tipos incorporados (`str`, `list`, `tuple`, `dict`, `set`)](https://docs.python.org/es/3/library/stdtypes.html)** — la referencia completa, con todos los métodos y su comportamiento exacto.
- 📍 **[Tutorial oficial: estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html)** — capítulo del tutorial oficial que cubre exactamente la materia de este tema, con muchos ejemplos.
- 📍 **[Módulo `collections`](https://docs.python.org/es/3/library/collections.html)** — para `namedtuple`, `Counter`, `defaultdict`, `deque` y otras estructuras avanzadas.
- 📍 **[Módulo `dataclasses`](https://docs.python.org/es/3/library/dataclasses.html)** — para crear clases-registro de forma cómoda.
- 📍 **[Módulo `functools`](https://docs.python.org/es/3/library/functools.html#functools.reduce)** — donde vive `reduce` (que ya no está en el espacio de nombres global).

### 📜 Métodos de cadenas

- 📍 **[Métodos de `str`](https://docs.python.org/es/3/library/stdtypes.html#string-methods)** — la lista completa: `upper`, `lower`, `strip`, `split`, `join`, `replace`, `find`, `startswith`, `endswith`, `isdigit`, `isnumeric`, `isalpha`, `title`, `capitalize`, `count`, `format`…
- 📍 **[Formato con f-strings](https://docs.python.org/es/3/tutorial/inputoutput.html#formatted-string-literals)** — cómo formatear números y cadenas con precisión (`f"{x:.4f}"`, `f"{n:>5d}"`, etc.).

### 🎯 Referencias específicas por tipo

- 📍 **[Métodos de listas](https://docs.python.org/es/3/tutorial/datastructures.html#more-on-lists)** — `append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`, `index`, `count`.
- 📍 **[Métodos de diccionarios](https://docs.python.org/es/3/library/stdtypes.html#dict)** — `keys`, `values`, `items`, `get`, `setdefault`, `update`, `pop`.
- 📍 **[Métodos de conjuntos](https://docs.python.org/es/3/library/stdtypes.html#set-types-set-frozenset)** — `add`, `remove`, `discard`, `union`, `intersection`, `difference`, `symmetric_difference`.

### 🇺🇸 En inglés (a menudo más completa)

- 📍 **[Python *Data Structures* tutorial (inglés)](https://docs.python.org/3/tutorial/datastructures.html)**
- 📍 **[Real Python: Lists and Tuples](https://realpython.com/python-lists-tuples/)**
- 📍 **[Real Python: Dictionaries](https://realpython.com/python-dicts/)**
- 📍 **[Real Python: Sets](https://realpython.com/python-sets/)**

---

## 🛠️ Herramientas para visualizar y practicar

### 🎨 Python Tutor

- 📍 **[Python Tutor](https://pythontutor.com/)** — te permite ejecutar tu código **paso a paso** y **ver visualmente** cómo se crean las listas, cómo se modifican los diccionarios, y qué pasa con las referencias en memoria. **Absolutamente imprescindible** para entender la mutabilidad y el paso de parámetros.

### 🎮 Practica interactiva

- 📍 **[Exercism – Python track](https://exercism.org/tracks/python)** — cientos de ejercicios con retroalimentación de mentores voluntarios.
- 📍 **[LeetCode – Easy problems](https://leetcode.com/problemset/all/?difficulty=EASY&topicSlugs=array%2Chash-table%2Cstring)** — muchos problemas clásicos con listas, strings y diccionarios.
- 📍 **[Rosetta Code](https://rosettacode.org/)** — el mismo problema resuelto en decenas de lenguajes. Buenísimo para comparar.

### 📓 Notebooks de referencia

- 📍 **[Jupyter Notebooks de "A Whirlwind Tour of Python" (*VanderPlas, gratis*)](https://github.com/jakevdp/WhirlwindTourOfPython)** — notebooks concisos y bien explicados. Los capítulos sobre listas, tuplas y diccionarios son especialmente recomendables.

---

## 📊 Cheatsheets visuales

- 📍 **[Python Data Structures Cheatsheet](https://learnxinyminutes.com/docs/python/)** — todo Python en una página larga, muy útil como referencia rápida.
- 📍 **[Python String Methods Cheatsheet](https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings)** — todos los métodos de string con ejemplo mínimo.
- 📍 **[Complexity Cheatsheet](https://wiki.python.org/moin/TimeComplexity)** — la **complejidad temporal** de cada operación sobre listas, diccionarios y conjuntos. Muy útil para entender por qué `x in set` es mucho más rápido que `x in lista` en colecciones grandes.

---

## 🧩 Comprensiones de listas (*list comprehensions*)

Las **comprensiones de listas** son una sintaxis muy elegante y muy popular en Python que permite construir listas a partir de otras secuencias **en una sola expresión**. En este curso **no se estudian formalmente** (para no sobrecargarte), pero **las encontrarás en prácticamente cualquier código Python que leas fuera del aula**. Merece la pena echarles un vistazo por tu cuenta cuando termines el tema.

La idea básica es que estas dos construcciones son equivalentes:

```python
# Con bucle (lo que ya sabes)
cuadrados = []
for x in numeros:
    cuadrados.append(x ** 2)

# Con list comprehension (la sintaxis nueva)
cuadrados = [x ** 2 for x in numeros]
```

Y con filtro:

```python
pares_al_cuadrado = [x ** 2 for x in numeros if x % 2 == 0]
```

Son equivalentes a combinar `map` y `filter`, pero **muchos programadores las prefieren** por ser más legibles.

### 📚 Recursos para aprenderlas por tu cuenta

- 📍 **[Tutorial oficial de Python: List Comprehensions](https://docs.python.org/es/3/tutorial/datastructures.html#list-comprehensions)** — la referencia oficial, con ejemplos claros y progresivos. Empieza por aquí.
- 📍 **[Real Python: When to Use a List Comprehension in Python](https://realpython.com/list-comprehension-python/)** — artículo detallado con ejemplos, comparaciones con bucles y cuándo NO usarlas.
- 📍 **[W3Schools: Python List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)** — introducción rápida y visual, con ejemplos interactivos.
- 📍 **[Programiz: Python List Comprehension](https://www.programiz.com/python-programming/list-comprehension)** — muy didáctica, con esquemas visuales de la sintaxis.

### 🎁 Bonus: los otros tipos de comprensiones

Una vez que entiendes las comprensiones de listas, las hay también para diccionarios y conjuntos, con sintaxis análoga:

```python
# Dict comprehension: crea un diccionario
cuadrados_dict = {x: x**2 for x in range(5)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension: crea un conjunto
letras_unicas = {c for c in "murcielago"}
# → {'m', 'u', 'r', 'c', 'i', 'e', 'l', 'a', 'g', 'o'}
```

- 📍 **[Real Python: Dict and Set Comprehensions](https://realpython.com/python-dictionary-comprehension/)** — cubre las tres variantes con ejemplos comparativos.

> [!WARNING]
> Aunque son concisas, **cuando se abusa de ellas se vuelven ilegibles**. Una comprensión con dos `for` anidados y varios `if` puede ser peor que un bucle explícito. La regla práctica: **si no cabe cómodamente en una línea o si tienes que releerla dos veces para entenderla, mejor un bucle**.

---

## 🧾 Comparativa entre lenguajes

### Estructuras equivalentes en distintos lenguajes

| Python | C | MATLAB | Java |
|:---:|:---:|:---:|:---:|
| `list` | `int[]` (fijo) o dinámico manual | vectores `[1, 2, 3]` | `ArrayList` |
| `tuple` | `struct` con campos numéricos | no nativas | `record` (Java 14+) |
| `dict` | `struct` + funciones o `hashmap` de librería | `struct`, `containers.Map` | `HashMap` |
| `set` | conjuntos manuales o `hashset` | no nativas | `HashSet` |
| `str` | `char *` o `char[]` | `'string'` | `String` |

> [!NOTE]
> Python te da estas estructuras "gratis", listas para usar. En C tendrías que implementarlas tú (o usar bibliotecas externas). Cuando dominas los tipos de Python, dominas también los conceptos que hay detrás de casi cualquier estructura de datos en cualquier lenguaje.

---

## 🐛 Errores más frecuentes y cómo diagnosticarlos

| Error | Causa habitual | Solución |
|:---|:---|:---|
| `IndexError: list index out of range` | Accediste a un índice que no existe | Comprueba `len(lista)` antes; usa `for e in lista` en vez de `range(len(lista))` |
| `KeyError: 'clave'` | Buscaste una clave que no está en el diccionario | Usa `dict.get(clave, valor_por_defecto)` o `if clave in dict` |
| `TypeError: 'tuple' object does not support item assignment` | Intentaste modificar una tupla | Conviértela a lista con `list(tupla)` |
| `AttributeError: 'list' object has no attribute 'add'` | Confundiste métodos de `list` (`.append`) con `set` (`.add`) | Comprueba el tipo con `type(objeto)` |
| `TypeError: unhashable type: 'list'` | Intentaste usar una lista como clave de diccionario o elemento de conjunto | Usa una **tupla** en su lugar |
| Resultado inesperado tras `lista.sort()` | El método `.sort()` devuelve `None`, no la lista ordenada | Usa `sorted(lista)` si necesitas el valor devuelto |

---

## 🎓 Módulos que te resultarán útiles

- 📍 **[`string`](https://docs.python.org/es/3/library/string.html)** — constantes útiles: `string.ascii_lowercase`, `string.digits`, `string.punctuation`.
- 📍 **[`collections.Counter`](https://docs.python.org/es/3/library/collections.html#collections.Counter)** — cuenta ocurrencias en una secuencia (muy útil para el ejercicio de "palabra más frecuente").
- 📍 **[`itertools`](https://docs.python.org/es/3/library/itertools.html)** — combinaciones, permutaciones, producto cartesiano… todo un mundo de utilidades para iterables.
- 📍 **[`statistics`](https://docs.python.org/es/3/library/statistics.html)** — funciones de estadística básica (`mean`, `median`, `stdev`) implementadas de forma pura en Python (sin necesidad de NumPy).

> [!TIP]
> **Estos módulos ya están en la biblioteca estándar** (no requieren `pip install`). Los verás mencionados de pasada durante el tema, pero merece la pena echarles un vistazo por tu cuenta.

---

## 🃏 Chuletas propias — hazte la tuya

Un consejo pedagógico: **imprime una hoja con los métodos que más usas** para tenerla al lado del ordenador durante las primeras semanas. Un modelo mínimo:

```text
=== LISTAS ===
lista.append(x)      añade x al final
lista.pop()          quita y devuelve el último
lista.pop(i)         quita y devuelve el i-ésimo
lista.remove(x)      quita la primera ocurrencia de x
lista.sort()         ordena in situ
sorted(lista)        devuelve una lista NUEVA ordenada

=== DICCIONARIOS ===
d[clave]             lanza KeyError si no está
d.get(clave, def)    devuelve def si no está
d.keys()             iterable de claves
d.values()           iterable de valores
d.items()            iterable de pares (clave, valor)

=== CONJUNTOS ===
s.add(x)             añade x
s.remove(x)          quita x (KeyError si no está)
s.discard(x)         quita x (sin error si no está)
a | b                unión
a & b                intersección
a - b                diferencia
a ^ b                diferencia simétrica
```

Con esa hoja delante, escribirás mucho más rápido durante las prácticas.

---

## 🧭 Menú de Navegación

| Orden | Material | Tiempo |
|:-----:|:---------|:------:|
| 1     | [Teoría](../teoria/T6_ICC.md)             |  12   |
| 2     | **Recursos**                              |   7   |
| 3     | [Ejemplos](../ejemplos/T6_Ejem_ICC.md)    |   –   |
| 4     | [Ejercicios](../ejercicios/T6_Ejer_ICC.md)|   –   |
|       | [Menú del Tema actual](../README.md)      |   -   |
