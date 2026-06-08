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

# 📘 Teoría - Tema 5: Programación Modular 🧩

> [!NOTE]
> Este documento **no sustituye** a las transparencias de clase: las **complementa**. Aquí encontrarás analogías, intuiciones, errores típicos que cometen los estudiantes principiantes, y matices que cuesta ver la primera vez que se estudia el tema. Apóyalo siempre con los ejemplos prácticos de la sección [Ejemplos](../ejemplos/T5_Ejem_ICC.md) y los [Ejercicios](../ejercicios/T5_Ejer_ICC.md).

---

## 🍳 Una analogía para empezar: la cocina

Imagina que quieres preparar una cena para 8 personas. Si tu única estrategia fuera **escribir todos los pasos en un único folio gigantesco**, acabarías con algo así:

> *"Pela 3 patatas; corta las patatas en dados; pon una sartén al fuego; añade aceite; cuando esté caliente echa las patatas; pela 4 cebollas; corta las cebollas en juliana; pon otra sartén al fuego..."*

Funcionar, funcionaría. Pero cuando dentro de tres meses quieras volver a hacer esa cena, **tendrás que volver a leer y descifrar el folio entero**. Y si tu amigo te pide la receta, tendrás que copiárselo todo. Y si te das cuenta de que el corte de la patata se podría mejorar… **tendrás que rehacer el folio entero**.

Una alternativa mucho mejor es **organizar la información por recetas**:

> *"Para la cena: 1) hacer guarnición de patatas; 2) hacer salsa de cebollas; 3) cocinar el pescado..."*

Y luego, **en otro folio aparte**, tener la receta detallada de cada cosa. Si quieres mejorar el corte de patata, **solo tocas un folio**. Si tu amigo quiere la receta de la salsa, **le das solo ese folio**.

Eso es **programación modular**. Cada "receta" se llama **subprograma** (también: función, procedimiento, rutina, método...). El "folio principal" se llama **programa principal**, y el conjunto de folios relacionados que entregas a un compañero se llama **módulo** o **paquete**.

> 🎯 **La idea fuerza del tema, en una frase**: un programa bien escrito **no se lee de arriba abajo**, se lee **por niveles de abstracción**. Primero lees el programa principal y entiendes qué hace en general. Solo bajas a leer los detalles de un subprograma si te interesan.

---

## 🔧 Función vs. procedimiento: la diferencia que más cuesta

Si lees con atención las transparencias, verás esta distinción:

* **Función**: subprograma que **calcula y devuelve un valor**.
* **Procedimiento**: subprograma que **hace cosas** pero **no devuelve** nada.

En la práctica, ambos se escriben igual en Python (`def nombre(args):`), pero **conceptualmente son distintos** y dan pistas sobre cómo usarlos:

| Función | Procedimiento |
|:---|:---|
| Se invoca dentro de una expresión: `x = raiz(2)` | Se invoca como sentencia: `imprimir_tabla(5)` |
| Tiene un `return valor` al final | No tiene `return` (o tiene `return` "vacío") |
| Su nombre suele ser un **sustantivo**: `area`, `media`, `factorial` | Su nombre suele ser un **verbo**: `dibujar`, `guardar`, `imprimir` |
| Idealmente, **sin efectos colaterales**: solo calcula y devuelve | Su trabajo **son** los efectos colaterales (escribir en pantalla, en disco...) |

> 💡 **¿Por qué importa esta distinción si Python no la marca sintácticamente?** Porque al **leer** un código bien escrito, ver `media(notas)` te dice instantáneamente que ahí se está calculando algo útil, mientras que `imprimir(notas)` te dice que ahí se está produciendo un efecto. **El nombre comunica la intención**. Cuando escribas tus subprogramas, decide primero **qué clase de subprograma estás escribiendo** y elige el nombre acorde.

### ⚠️ Anti-patrón típico

Lo peor que puedes hacer es escribir un subprograma que **mezcla** ambos roles:

```python
def calcular_media(notas):
    suma = 0
    for n in notas:
        suma = suma + n
    media = suma / len(notas)
    print(f"La media es {media}")    # ⚠️ efecto colateral
    return media                      # ⚠️ y además devuelve
```

¿Para qué te sirve este subprograma? Si solo quieres calcular la media en silencio (porque la vas a usar después), el `print` te molesta. Si solo quieres mostrarla por pantalla, y no sabes qué hacer con el valor calculado por qué lo devuelves. **Un subprograma, una responsabilidad**. Separa: `calculo_media` o `media`(función pura que devuelve) y `mostrar_media` (procedimiento que imprime).

---

## 📦 El gran misterio del paso de parámetros en Python

Esta es probablemente la **fuente número uno de bugs** que escribirás en tu carrera de matemático-programador. Vamos despacio.

En las transparencias se habla de "paso por **referencia de objeto**". Suena raro, ¿verdad? Te explico qué quiere decir realmente.

### 🎨 La imagen mental correcta

Cuando escribes `x = 5` en Python, no estás diciendo *"la caja x contiene el valor 5"*. Estás diciendo:

> *"En algún lugar de la memoria existe un objeto entero con valor 5. La etiqueta `x` apunta a ese objeto."*

Cuando llamas a una función `f(x)`, Python **no copia el objeto**. Lo que hace es **darle una nueva etiqueta** al objeto, dentro de la función. Esa etiqueta es el parámetro:

```python
def f(parametro):
    # Aquí "parametro" apunta al mismo objeto que "x" en el exterior
    ...
```

### 🪨 Objetos inmutables: parecen paso por valor

Si el objeto es **inmutable** (`int`, `float`, `str`, `tuple`, `bool`), no puedes modificarlo. Solo puedes **hacer que la etiqueta apunte a otro objeto distinto**:

```python
def f(parametro):
    parametro = parametro + 1   # crea un NUEVO objeto y reasigna la etiqueta local

x = 5
f(x)
print(x)   # → 5 (intacto)
```

Aquí, dentro de `f`, la etiqueta `parametro` deja de apuntar al `5` y pasa a apuntar a un objeto nuevo `6`. Pero la etiqueta `x` del exterior **sigue apuntando al `5` original**. Parece paso por valor.

### 🌊 Objetos mutables: parecen paso por referencia

Si el objeto es **mutable** (`list`, `dict`, `set`), puedes modificarlo **sin reasignar**:

```python
def f(parametro):
    parametro.append(99)   # modifica el objeto ¡sin reasignar!

lista = [1, 2, 3]
f(lista)
print(lista)   # → [1, 2, 3, 99]   ⚠️ ¡ha cambiado!
```

Aquí la etiqueta `parametro` apunta al mismo objeto lista que `lista`. Al hacer `.append`, modificamos **el objeto** (no la etiqueta). Como ambas etiquetas apuntan al mismo objeto, ambas "ven" el cambio.

> ⚠️ **Aviso para el Tema 6**: en el Tema 5 trabajarás casi exclusivamente con tipos simples (inmutables), así que parecerá que Python pasa "por valor". **No te confundas**: cuando lleguemos a listas y diccionarios verás el otro comportamiento. La regla mental correcta es: **Python siempre comparte etiquetas, nunca copia objetos**.

---

## 🎁 Funciones que devuelven varias cosas

Una utilidad muy bonita de Python es que las funciones pueden devolver **varios valores a la vez**:

```python
def estadisticas(*args):
    suma = sum(args)
    media = suma / len(args)
    return suma, media

s, m = estadisticas(3, 5, 10, 12)
```

> 💡 **¿Cómo lo hace si la mayoría de los lenguajes solo permiten un `return`?** Lo que devuelve realmente es **una tupla** `(suma, media)`, y al hacer `s, m = ...` Python la "desempaqueta" automáticamente en las dos variables. Es elegante y muy útil, pero recuerda que **es una tupla**: si lo asignas a una sola variable, recibirás la tupla entera.
>
> ```python
> resultado = estadisticas(3, 5, 10, 12)
> # resultado = (30, 7.5)
> ```
> 🗣️ Ya entenderás en el Tema 6 qué es una **tupla**. 
---

## 🎭 Funciones como ciudadanos de primera clase

Este es el concepto que más **wow** suele causar a los estudiantes la primera vez. La idea es que en Python una función **es un valor más**, igual que un número o una cadena. Y puedes hacer con ella las mismas cosas:

```python
# 1) Asignarla a una variable
saludo = print
saludo("Hola")   # equivale a print("Hola")

# 2) Pasarla como argumento
def aplicar(funcion, valor):
    return funcion(valor)

aplicar(abs, -7)   # → 7

# 3) Devolverla como resultado
def multiplicador(factor):
    def aux(x):
        return x * factor
    return aux

triple = multiplicador(3)
triple(10)   # → 30
```

> 🤔 **¿Para qué sirve esto realmente?** En el Tema 6 lo verás claro: muchas funciones útiles (`map`, `filter`, `sorted`, `min` con `key=...`) **reciben otras funciones como argumento**. Sin esta característica, sería imposible escribir código tan elegante como `sorted(personas, key=edad)`. La librería NumPy también usa esto para vectorizar operaciones.

### 🪶 La `lambda`: una función "de usar y tirar"

Cuando necesites una función **minúscula** que solo vas a usar **una vez**, no merece la pena escribir un `def` completo. Para eso existe `lambda`:

```python
# En vez de:
def doble(x):
    return x * 2
ordenado = sorted(numeros, key=doble)

# Puedes hacer:
ordenado = sorted(numeros, key=lambda x: x * 2)
```

> ⚠️ **¡Cuidado con abusar de las lambdas!** Son fantásticas para una expresión simple, pero **destruyen la legibilidad** si las usas para lógica complicada. Regla práctica: si tu `lambda` tiene más de una expresión, si necesita un `if`, o si **tendrías que explicarla** a un compañero, ¡usa un `def` con nombre descriptivo!

---

## 📁 Módulos, paquetes y el misterio de `__init__.py`

**Un módulo es un archivo `.py`**. Eso es todo. Cuando escribes `import math`, Python busca un archivo `math.py` (o equivalente compilado) y ejecuta su contenido para ponerlo a tu disposición.

**Un paquete es una carpeta de módulos**. Para que Python reconozca una carpeta como paquete, históricamente se necesitaba un archivo especial llamado `__init__.py` dentro de ella. Hoy en día (Python 3.3+) ya no es estrictamente obligatorio, pero **se sigue usando** porque permite:

- Decidir **qué se exporta** cuando alguien hace `from mi_paquete import *`.
- Ejecutar **código de inicialización** del paquete.
- Mantener la **compatibilidad** con herramientas antiguas.

Por convención, en este curso lo incluiremos siempre (aunque sea vacío).

### 🗂️ Las cinco formas de importar

Hay varias maneras de importar cosas. Cada una tiene su momento:

```python
# 1) Importar el módulo entero
import math
math.sqrt(2)

# 2) Importar el módulo con un alias
import numpy as np
np.array([1, 2, 3])

# 3) Importar solo lo que necesitas
from math import sqrt, pi
sqrt(pi)

# 4) Importar con alias específico
from math import sqrt as raiz
raiz(2)

# 5) Importar TODO (¡desaconsejado!)
from math import *
sqrt(2)
```

> ⚠️ **Sobre el `from módulo import *`**: aunque parece cómodo, **es una mala práctica**. Mete todos los nombres del módulo en tu espacio de nombres global y puede sobrescribir cosas tuyas silenciosamente. Por ejemplo, si haces `from math import *` y luego defines `sum = 0`, acabas de pisar la función `sum` integrada de Python. **Importa explícitamente lo que necesites**.

---

## 🚪 La función `main` y la guarda mágica

Verás esta construcción en absolutamente todos los programas Python serios:

```python
def main():
    ...   # toda la lógica del programa va aquí

if __name__ == "__main__":
    main()
```

¿Qué significa? Cuando Python ejecuta un archivo, le asigna automáticamente una variable interna llamada `__name__`. Esta variable vale:

- `"__main__"` si el archivo se está **ejecutando directamente** (`python mi_programa.py`).
- `"nombre_del_modulo"` si el archivo se está **importando desde otro** (`import mi_programa`).

> 💡 **¿Para qué sirve esta distinción?** Imagina que escribes `mi_modulo.py` con varias funciones útiles, y al final pones `print("Hola")`. Si alguien hace `import mi_modulo`, ¡le saldrá "Hola" por pantalla sin esperarlo! Con la guarda `if __name__ == "__main__"`, ese `print` (y toda la lógica de prueba) **solo se ejecuta cuando el archivo se lanza directamente**, no cuando se importa.

Es **la forma profesional** de escribir un módulo Python que puede usarse tanto como programa ejecutable como librería para otros programas.

---

## 🔍 Ámbito de variables: el origen de muchos bugs

Una variable definida **dentro de una función** es **local**: solo existe mientras la función está ejecutándose y **no se ve desde fuera**:

```python
def f():
    x = 10
    print(x)   # 10

f()
print(x)   # ❌ NameError: x no existe aquí
```

Una variable definida **fuera de cualquier función** es **global**: la pueden **leer** todas las funciones, pero **modificarla** requiere la palabra clave `global` (en general, **evítalo**):

```python
y = 5

def f():
    print(y)   # ✅ lee la global
    y = 100    # ⚠️ esto NO modifica la global: crea una local NUEVA

f()
print(y)   # → 5 (la global no cambia)
```

> 🎯 **La regla práctica para sobrevivir**: las funciones deberían **comunicarse a través de parámetros y valores de retorno**, no a través de variables globales. Si una función necesita un dato, **pásaselo como parámetro**. Si calcula algo, **devuélvelo**. El uso de variables globales `global` es casi siempre síntoma de un diseño que se puede mejorar.

### 🔬 Un caso especialmente confuso

Mira este ejemplo (basado en uno de las transparencias):

```python
def A():
    print(f"{b} y {c} en A")    # ⚠️ trata de leer b y c
    c = 4                        # ⚠️ pero más abajo creas c local

b = 3
c = 5
A()
```

¿Qué crees que pasará? **Error**. Python, al ver el `c = 4` dentro de `A`, deduce que `c` es una variable **local** de la función. Por tanto, cuando intenta leerla en el `print` (que está antes), no la encuentra inicializada. **No usa la `c` global del exterior**, porque Python ya ha decidido que `c` es local en `A`.

Es un fenómeno llamado **"hoisting" implícito de Python**: la decisión sobre si una variable es local o global se toma **mirando toda la función**, no línea a línea.

> 💡 **Truco mental**: si en algún punto del cuerpo de una función **asignas** a una variable, esa variable es **local** en toda la función. No hay punto intermedio.

---

## 🪞 Recursividad: cuando una función se llama a sí misma

La recursividad suena rara cuando se ve por primera vez: ¿cómo va a llamarse una función a sí misma sin caer en un bucle infinito?

La clave está en que **cada llamada se hace con un argumento distinto** (normalmente más pequeño), de manera que tarde o temprano se llega a un **caso base** que se resuelve sin más llamadas:

```python
def factorial(n):
    if n <= 1:           # caso base: corta la recursión
        return 1
    return n * factorial(n - 1)   # caso recursivo: llamada más pequeña
```

Funciona porque cada `factorial(n)` queda "esperando" el resultado de `factorial(n-1)`, que a su vez espera `factorial(n-2)`, ..., hasta llegar a `factorial(1)` que devuelve 1 directamente. Entonces los valores **van subiendo** y multiplicándose hasta llegar al resultado final.

### ✅ Cuándo usar recursividad

- Cuando el problema tiene **estructura recursiva natural**: factoriales, sucesiones definidas por recurrencia (Fibonacci), recorridos de árboles, problemas de divide y vencerás (mergesort, quicksort)...
- Cuando la **versión recursiva es notablemente más clara** que la iterativa.

### ⚠️ Cuándo NO usar recursividad

- **Cuando una iteración hace lo mismo más rápido y con menos memoria**. La recursividad consume pila: cada llamada anidada ocupa un trozo de memoria, y Python tiene un **límite por defecto de 1000** llamadas anidadas (puedes verlo con `sys.getrecursionlimit()`).
- **Para problemas con solapamiento masivo de subproblemas sin memorización**. El ejemplo clásico es la Fibonacci recursiva ingenua: `fib(50)` puede tardar minutos porque recalcula los mismos valores millones de veces.
- **Cuando depurar resulta una pesadilla**: rastrear el estado mental de una recursión profunda no es divertido.

> 🎯 **Regla de oro**: prueba primero con iteración. Si la versión iterativa se vuelve oscura o tu problema es recursivo por naturaleza, entonces sí, recursión.

---

## ✅ Mini-checklist antes de dar una función por buena

Antes de considerar terminada una función, repasa:

- [ ] **Una sola responsabilidad**: ¿hace una cosa o varias? Si son varias, divídela.
- [ ] **Nombre descriptivo**: verbo si es procedimiento, sustantivo si es función. ¿Se entiende sin leer el cuerpo?
- [ ] **Pocos parámetros**: idealmente 0-3. Más de 5 es señal de que algo se puede agrupar o reorganizar.
- [ ] **Sin efectos sorpresa**: una función llamada `calcular_media` no debería escribir en disco. Si modifica argumentos mutables, **documéntalo explícitamente**.
- [ ] **Docstring**: al menos una línea explicando qué hace, qué espera y qué devuelve.
- [ ] **Tipos**: añade *type hints* si la función va a usarse en algún sitio importante.
- [ ] **Caso base** (si es recursiva): ¿está claramente identificado? ¿siempre se llega a él?

---

## 🚀 Reflexión final

La programación modular es **el** salto cualitativo en tu aprendizaje. Hasta ahora has escrito programas; a partir de aquí escribirás **sistemas**. La diferencia es importante:

- Un **programa** resuelve un problema concreto.
- Un **sistema** está hecho de piezas que pueden combinarse para resolver muchos problemas.

NumPy, SciPy, Matplotlib o Pandas —las herramientas que te acompañarán toda tu carrera como matemático— **son sistemas modulares**. Cuando escribes `numpy.linalg.solve(A, b)`, estás invocando una función dentro del submódulo `linalg` del paquete `numpy`. Es exactamente lo mismo que aprenderás a hacer **tú** en este tema.

> 💡 **Para llevarte a casa**: al final de este tema, deberías ser capaz de **leer el código de un paquete pequeño** y entender cómo está organizado. Esa es la habilidad que separa al estudiante del usuario profesional de Python.

---

## 🧭 Menú de Navegación

| Orden | Material | Tiempo |
|:-----:|:---------|:------:|
| 1     | **Teoría**                                |   10  |
| 2     | [Recursos](../recursos/T5_RE_ICC.md)      |    6  |
| 3     | [Ejemplos](../ejemplos/T5_Ejem_ICC.md)    |    –  |
| 4     | [Ejercicios](../ejercicios/T5_Ejer_ICC.md)|    –  |
|       | [Menú del Tema actual](../README.md)      |    -  |
