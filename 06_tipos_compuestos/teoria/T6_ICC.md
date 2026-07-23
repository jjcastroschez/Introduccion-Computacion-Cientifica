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

# 📘 Teoría - Tema 6: Tipos de Datos Complejos 🧺

> [!NOTE]
> Este documento **no sustituye** a las transparencias de clase: las **complementa**. Aquí encontrarás analogías, intuiciones y advertencias que te ayudarán a evitar los errores más frecuentes con los tipos complejos, además de matices que suelen pasar desapercibidos la primera vez.

---

## 🧺 Una analogía para empezar: tu escritorio...

Imagina tu escritorio. Hasta ahora, cada "cosa" que tenías era **un objeto suelto**: un bolígrafo, una goma, una hoja. Cuando el escritorio se llena de objetos independientes, se vuelve un caos.

La solución que aplicamos en la vida real es agrupar cosas relacionadas en **organizadores** o **cajones**. Y elegimos el tipo de organizador y/o cajón según **qué queremos guardar** y **cómo queremos acceder**:

- Una **pizarra de corcho**: llegas por la mañana y pinchas notas sobre tareas que tienes pendientes, dándole un orden. Cada vez que completas una, la eliminas, pero si llega algo nuevo lo añades. ¿Dónde? Pues depende de la urgencia, si no es urgente irá al final. → **Secuencia** (`list`).
```python
# Tu pizarra de corcho con tus posibles notas
pizarra_corcho=["Divertirme: hacer un programa de Python", "Hacer ejercicios de Análisis Numérico", "Estudiar Matemáticas Discretas", "Repasar Métodos Numéricos", "Comprar abono autobús"]
```
- Un **cargador multipuerto**: el número de puertos es fijo e inmutable (no puedes añadir ninguno más), **el orden importa** (cada uno tiene una posición, una potencia y un tipo). → **Secuencia** (`tuple`).
```python
# Cargador con 3 puertos fijos de potencia en vatios
cargador_usb = (65, 30, 15)
```

- Una **carpeta con separadores por asignatura**: guarda documentos etiquetados; para encontrar los de "Matemáticas" no hace falta mirar el resto. → **Diccionario** (`dict`).
```python
# Tu carpeta con sus separadores de asignaturas
carpeta_estudios = {
    "Matemáticas": ["Apuntes Álgebra", "Ejercicios Geometría"],
    "Historia": ["Resumen Revolución Francesa"],
    "Programación": ["Guía de Tipos de Datos", "Código Pizarra Corcho"]
}
```
- Un **bote clasificador de marcadores de colores**: metes marcadores de colores y sabes qué colores hay, no puedes meter dos iguales y no importa el orden en el que los metes (si aguitas el bote cambian de posición). → **Conjunto** (`set`).
```python
# Definimos los colores de clips que tenemos en el bote
bote_marcadores = {"rojo", "azul", "verde", "amarillo"}
```

🎯 **Elegir bien el tipo de dato es como elegir bien el organizador o cajón**: no cambia lo que guardas, pero sí lo fácil que resulta encontrarlo y usarlo después.

---

## 📏 El "modelo mental" de una secuencia

En Python, cadenas, tuplas y listas comparten una idea común: son **secuencias**. Todas ellas se pueden imaginar como una **fila de cajitas numeradas** desde `0`:

```text
cadena  =  " P y t h o n "
índice       0 1 2 3 4 5
```

**Reglas universales de las secuencias**:

- Se accede a un elemento con `secuencia[i]` — como abrir una caja concreta.
- El primer índice es `0`, **no `1`** (Matlab es la excepción rara).
- El último es `len(secuencia) - 1`. Salirse provoca un `IndexError`.
- Los índices **negativos** cuentan desde el final: `-1` es el último, `-2` el penúltimo…

Esta imagen unificada te ahorra mucho esfuerzo: **lo que sabes hacer con una cadena lo sabes hacer con una lista y con una tupla**. Los métodos concretos cambian, pero la mecánica es idéntica.

---

## 🔪 Slicing: la forma más elegante de "cortar" secuencias

La notación `secuencia[inicio:fin:paso]` te da un **trozo** de la secuencia. Es una de las herramientas más poderosas de Python, pero también una de las que más confunde al principio. Vamos a fijarla con claridad:

| Notación | Qué hace |
|:---|:---|
| `s[a:b]` | Del índice `a` **incluido** al `b` **excluido** |
| `s[:b]` | Desde el principio hasta `b` excluido |
| `s[a:]` | Desde `a` incluido hasta el final |
| `s[:]` | **Copia** completa de la secuencia |
| `s[::2]` | Todos los elementos, saltando de 2 en 2 |
| `s[::-1]` | La secuencia **invertida** |
| `s[-3:]` | Los **últimos 3** elementos |

### ⚠️ El error más común

Muchos estudiantes escriben `s[1:5]` esperando obtener los caracteres en las posiciones 1, 2, 3, 4 **y 5**. Pero el `5` es el **límite excluido**, así que se quedan sin el último. Es una convención (llamada "*half-open*" o semi-abierta) que tiene una **ventaja preciosa**: `len(s[a:b]) == b - a` cuando ambos están dentro del rango. Esa fórmula facilita mucho los cálculos.

### 💡 Un truco memorable

Piensa en los índices como **posiciones entre los caracteres**, no como los propios caracteres:

```text
    ┌─┬─┬─┬─┬─┬─┬─┐
    │P│y│t│h│o│n│!│
    └─┴─┴─┴─┴─┴─┴─┘
     0 1 2 3 4 5 6 
    -7-6-5-4-3-2-1
```

Con este dibujo mental, `s[1:5]` es "todo lo que hay entre las posiciones 1 y 5", es decir, `ytho`. Es la mejor forma de no fallar nunca.

---

## 🪨 Inmutabilidad: la confusión más famosa de Python

Este es probablemente **el concepto que más despista** de todo el curso. Vamos con calma.

### Objetos inmutables vs. mutables

Todo objeto en Python es una de estas dos cosas:

- **Inmutable**: una vez creado, **no se puede modificar**. Solo se puede **reemplazar** por otro. Son inmutables: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`.
- **Mutable**: se puede modificar sin cambiar la referencia. Son mutables: `list`, `dict`, `set` y los objetos que definas tú.

### ¿Y qué diferencia hay en la práctica?

```python
# Con inmutable (cadena)
cadena = "hola"
cadena = cadena.upper()     # cadena.upper() DEVUELVE una cadena NUEVA
print(cadena)               # "HOLA"

# Con mutable (lista)
lista = [1, 2, 3]
lista.append(4)             # lista.append() MODIFICA la lista IN SITU
print(lista)                # [1, 2, 3, 4]
```

Fíjate en el detalle: `cadena.upper()` **no cambia** la cadena original, **devuelve** una nueva; por eso hace falta asignarla otra vez a `cadena`. En cambio, `lista.append(4)` **modifica** la lista que ya existe y **no devuelve nada** (o mejor dicho, devuelve `None`).

### ⚠️ El error que ves cientos de veces

```python
lista = [3, 1, 4, 1, 5]
lista = lista.sort()          # ⚠️ ¡ERROR conceptual!
print(lista)                  # → None
```

¿Por qué `None`? Porque `.sort()` **modifica la lista in situ** y no devuelve nada. Al asignar `lista = lista.sort()`, estás asignando ese `None`, y pierdes tu lista.

La versión correcta es una de estas dos, según lo que quieras:

```python
# Si quieres modificar la lista original:
lista.sort()

# Si prefieres una lista nueva ordenada, sin tocar la original:
ordenada = sorted(lista)
```

Regla mental: **si el nombre del método está en el objeto (mutable) y no devuelve nada, es que modifica in situ**. Si es una función independiente (`sorted`, `reversed`, `str.upper`), suele devolver un valor nuevo.

---

## 🎁 Tuplas y listas: cuándo usar cada una

En términos de "qué guardan" son casi iguales. La diferencia es la **mutabilidad**, y eso determina el uso:

| Situación | Elección típica |
|:---|:---|
| Devolver varios valores de una función | **Tupla**: `return media, desviacion` |
| Coordenadas de un punto fijo: `(x, y)` | **Tupla** |
| Fecha: `(2026, 3, 15)` | **Tupla** |
| Lista de calificaciones a la que puedes añadir más | **Lista** |
| Colección que vas a ordenar / filtrar | **Lista** |
| Clave de un diccionario | **Tupla** (las mutables no pueden ser claves) |

### 🧠 Regla mnemotécnica

- Tupla = **T**enazas apretadas: se queda como está.
- Lista = **L**iviana: se puede añadir y quitar.

---

## 🔄 El nuevo `for` de Python: iteración sobre secuencias

En el [Tema 4](../../04_control_flujo_ejecucion/README.md) usábamos `for i in range(n):` y accedíamos con índices: `secuencia[i]`. Es correcto, pero **muy poco pythonico**. La forma idiomática es:

```python
for elemento in secuencia:
    hacer_algo_con(elemento)
```

**Pyhonic** es más corto, más legible y sin `IndexError`. Solo cuando **necesites el índice** volvemos al de siempre, pero con `enumerate`:

```python
for indice, elemento in enumerate(secuencia):
    print(f"Posición {indice}: {elemento}")
```

> 🎯 **Regla de estilo**: no uses `range(len(x))` a menos que lo necesites de verdad. Prefiere el `for e in x` o `for i, e in enumerate(x)`. Tu código será más limpio.

---

## 📤 Desempaquetado: una tacada, varias variables

Una característica muy elegante:

```python
punto = (3, 5)
x, y = punto          # x=3, y=5

datos = ["Juan", 30, "Madrid"]
nombre, edad, ciudad = datos
```

Funciona porque Python cuenta los elementos de la izquierda y los de la derecha, y **hacen falta el mismo número**. Si no coinciden, saltará un `ValueError`.

### Aplicaciones muy útiles

- **Intercambio de variables** en una línea: `a, b = b, a` (¡adiós al típico truco de la variable temporal!)
- **Devolver varias cosas de una función** y desempaquetarlas al llamarla: `q, r = divmod(a, b)`
- **Recorrer una lista de tuplas** directamente:

```python
puntos = [(1, 2), (3, 4), (5, 6)]
for x, y in puntos:
    print(f"({x}, {y})")
```

---

## 🎭 Programación funcional: cuando el bucle se convierte en una línea

Cuando ya sabes recorrer secuencias, Python te ofrece **funciones de orden superior** (Tema 5) para operar sobre colecciones enteras a la vez, sin escribir bucles explícitos.

Vamos a experimentar con esta lista:

```python
numeros=[2,4,6,8]
```

### `map`: aplicar una función a cada elemento

```python
# Con bucle
cuadrados = []
for x in numeros:
    cuadrados.append(x**2)

# Con map (una sola línea)
cuadrados = list(map(lambda x: x**2, numeros))
```

### `filter`: quedarse con los que cumplen una condición

```python
# Con bucle
pares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)

# Con filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
```

### `reduce`: acumular todos los elementos en uno solo

```python
from functools import reduce

# Con bucle (tema 4)
suma = 0
for x in numeros:
    suma = suma + x

# Con reduce
suma = reduce(lambda a, b: a + b, numeros)
```

### 🎯 ¿Por qué molestarse en aprender esto si ya sabes hacerlo con bucles?

Tres razones:

1. **Legibilidad**: `list(map(cuadrado, numeros))` se lee como "aplica cuadrado a cada número". Es más directo que un bucle con acumulador.
2. **Menos errores**: no puedes olvidarte de inicializar el acumulador, ni de incrementar el índice, ni de escribir el `else` correcto.
3. **Base para NumPy y Pandas**: cuando llegues al Tema 9, verás que las operaciones vectorizadas de NumPy son exactamente esta misma idea llevada al extremo.

> [!WARNING]
> **Aviso importante**: `map`, `filter` y `zip` **no devuelven listas**, devuelven **iteradores**. Un iterador es un objeto que produce sus elementos uno a uno, **y solo puedes consumirlos una vez**:
>
> ```python
> resultado = map(cuadrado, [1, 2, 3])
> print(list(resultado))      # [1, 4, 9]
> print(list(resultado))      # []  ← ¡ya está agotado!
> ```
>
> Si necesitas usarlo varias veces, guárdalo en una lista con `list(...)` desde el principio.

---

## 🗂️ Diccionarios: acceso por nombre, no por posición

Cuando lo que quieres guardar son **datos heterogéneos** que representan una entidad (una persona, un libro, un experimento…), las listas y tuplas se quedan cortas: obligan a **recordar en qué posición** está cada cosa:

```python
# ¿Qué era carnet_estudiante[2]? ¿el dni? ¿una fecha? Hay que ir a mirarlo.
carnet_estudiante = ["Alberto Gómez Aranda", 2006, "20264708", "Matemáticas"]

# Mucho más claro:
carnet_estudiante = {
    "nombre": "Alberto Gómez Aranda",
    "anio_nacimiento": 2006,
    "matricula": "20264708",
    "estudios": "Matemáticas"
}
libro["anio_nacimiento"]   # → 2006
```

Un diccionario es una colección de **pares clave-valor** (`key: value`). Se piensa en él como una **agenda** o un **índice de un libro** o una **ficha identificativa**: buscas por clave y obtienes el valor.

### ⚠️ Reglas importantes

- Las **claves deben ser inmutables** (`str`, `int`, `tuple`), **nunca** `list` ni `dict`.
```python
registro_notas = {
    ("ICC",1): 8.5,
    ("ICC",2): 9.0,
    ("ICC",3): 5.0,
    ("ANA",1): 7.2,
    ("EA", 1): 5.4,
    ("EA", 2): 6.1
}

# Accedes a la nota de ICC del segundo ejercicio puntuable:
print(registro_notas[("ICC", 2)])
```
- Las claves son **únicas**: si asignas dos veces la misma clave, la segunda pisa a la primera.
- **No hay orden garantizado entre elementos** (aunque desde Python 3.7 se conserva el orden de inserción; **no** te fíes de él para lógica del programa).

### 🎯 Cuándo usar diccionario y cuándo lista

| Situación | Elección |
|:---|:---|
| Colección de elementos del mismo tipo (notas, temperaturas...) | **Lista** |
| Registro de una entidad con atributos con nombre (libro, persona) | **Diccionario** |
| Búsqueda rápida por una clave (traducción español-inglés, DNI-nombre) | **Diccionario** |
| Recorrer todos los elementos en orden | **Lista** |

---

## 📦 `namedtuple` y `dataclass`: registros con más "personalidad"

Los diccionarios son flexibles pero **verbosos** (`carnet_estudiante["anio_nacimiento"]`) y **frágiles** (una errata en la clave y no salta ningún error hasta que ejecutas). Python ofrece dos alternativas más elegantes para modelar **entidades fijas**:

### `namedtuple`: tupla + nombres

```python
from collections import namedtuple

Estudiante = namedtuple("Estudiante", ["nombre", "anio_nacimiento", "matricula", "estudios"])
estudiante_delegado = Estudiante("Alberto Gómez Aranda", 2006, "20264708", "Matemáticas")
estudiante_delegado.nombre    # → "Alberto Gómez Aranda"
estudiante_delegado[0]        # → "Alberto Gómez Aranda" (también funciona por índice, como una tupla)
```

➕ **Ventajas**: acceso por nombre (`estudiante_delegado.nombre`), es una tupla (rápido, inmutable, poco costoso en memoria).  
➖ **Desventajas**: es inmutable (no puedes modificar campos).

### `dataclass`: la opción moderna

```python
from dataclasses import dataclass

@dataclass
class Estudiante:
    nombre: str
    anio_nacimiento: int
    matricula: str
    estudios: str

estudiante_delegado = Estudiante("Alberto Gómez Aranda", 2006, "20264708", "Matemáticas")
estudiante_delegado.nombre    # → "Alberto Gómez Aranda"
estudiante_delegado.estudios = "Física"   # ✅ mutable
```

➕ **Ventajas**: sintaxis clara, es mutable, se integra bien con el resto del ecosistema Python.  
➖ **Desventajas**: un poco más "pesado" que `namedtuple`.

### 🎯 Cuál elegir

| Necesitas... | Usa |
|:---|:---|
| Un registro rápido, "de una sola vez" | **`dict`** |
| Una entidad **inmutable** con nombres | **`namedtuple`** |
| Una entidad **mutable** con nombres | **`dataclass`** |
| Muchas instancias (rendimiento) | **`namedtuple`** o **`dataclass(slots=True)`** |

---

## 🔵 Conjuntos: cuando el orden no importa y no quieres duplicados

Los conjuntos (`set`) son distintos de todo lo anterior:

- **No tienen orden**: no puedes hacer `conjunto[0]`.
- **No permiten duplicados**: si añades algo que ya está, no pasa nada.
- **Búsqueda muy rápida**: `elemento in conjunto` es prácticamente instantáneo, incluso con millones de elementos (mucho más rápido que `elemento in lista`).

### Casos de uso típicos

1. **Eliminar duplicados** de una colección:

   ```python
   unicos = list(set([1, 2, 2, 3, 3, 3, 4]))
   # → [1, 2, 3, 4]  (orden no garantizado)
   ```

2. **Comprobar si un elemento pertenece** a una colección grande:

   ```python
   validas = {"a", "e", "i", "o", "u"}
   if letra in validas:
       ...
   ```

3. **Operaciones matemáticas de conjuntos**:

   ```python
   A = {1, 2, 3, 4}
   B = {3, 4, 5, 6}
   A | B     # unión:              {1, 2, 3, 4, 5, 6}
   A & B     # intersección:       {3, 4}
   A - B     # diferencia (A \ B): {1, 2}
   A ^ B     # diferencia simétrica: {1, 2, 5, 6}
   ```

### 🎓 Conexión matemática

Aquí Python es transparente para un matemático: los operadores `|`, `&`, `-`, `^` son literalmente los mismos que en teoría de conjuntos ($\cup$, $\cap$, $\setminus$, $\triangle$). Si quieres modelar problemas donde interviene la teoría de conjuntos (probabilidad, lógica proposicional, combinatoria), `set` es tu amigo.

---

## 🧮 Un cuadro de resumen para llevar

| Tipo | Ordenado | Mutable | Duplicados | Acceso | Ejemplo |
|:---:|:---:|:---:|:---:|:---:|:---|
| `str` | ✅ | ❌ | ✅ | Por índice | `"hola"` |
| `tuple` | ✅ | ❌ | ✅ | Por índice | `(1, 2, 3)` |
| `list` | ✅ | ✅ | ✅ | Por índice | `[1, 2, 3]` |
| `dict` | ✅* | ✅ | ❌ (en claves) | Por clave | `{"a": 1}` |
| `set` | ❌ | ✅ | ❌ | No indexable | `{1, 2, 3}` |
| `frozenset` | ❌ | ❌ | ❌ | No indexable | `frozenset([1, 2])` |

*El orden de inserción se conserva en Python ≥ 3.7 pero **no** debe usarse como parte de la lógica del programa.

---

## 🚀 Reflexión final

Los tipos complejos son la puerta a **modelar problemas de verdad**. Un problema realista rara vez opera con un único número: procesa listas de mediciones, conjuntos de resultados, diccionarios de configuración.

Al final de este tema, deberías ser capaz de leer un enunciado como *"dados los pesos de una muestra de 30 personas, calcula el índice de masa corporal medio, agrupado por rango de edad"* y **elegir de un vistazo** qué estructuras necesitas: probablemente una **lista de diccionarios** (o una `namedtuple`) donde cada diccionario representa una persona, y luego un **diccionario** cuyas claves son los rangos de edad y cuyos valores son listas de IMCs.

```python
personas = [
    {"peso": 70, "estatura": 1.75, "edad": 22},
    {"peso": 85, "estatura": 1.80, "edad": 35},
    {"peso": 62, "estatura": 1.65, "edad": 19},
    # ... hasta 30
]

rangos = {
    "18-29": [],
    "30-44": [],
    "45-59": [],
    "60+": []
}

```

> [!TIP]
> 💡 **Para llevar a casa**: la mayor parte del "arte" de programar con soltura es **elegir bien las estructuras de datos**. Si eliges bien, el código se escribe casi solo. Si eliges mal, cada operación se convierte en un dolor de cabeza. Este tema es donde empiezas a afinar esa intuición.

---

## 🧭 Menú de Navegación

| Orden | Material | Tiempo |
|:-----:|:---------|:------:|
| 1     | **Teoría**                                |   12   |
| 2     | [Recursos](../recursos/T6_RE_ICC.md)      |    7   |
| 3     | [Ejemplos](../ejemplos/T6_Ejem_ICC.md)    |    –   |
| 4     | [Ejercicios](../ejercicios/T6_Ejer_ICC.md)|    –   |
|       | [Menú del Tema actual](../README.md)      |    -   |
