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

# 🧺 Tema 6: Tipos de Datos Complejos 🎒

Hasta ahora has trabajado con **valores sueltos**: un entero, un real, un booleano. Con esos tipos primitivos ([Tema 3](../03_variables_tipos_simples/README.md)) has aprendido a tomar decisiones ([Tema 4](../04_control_flujo_ejecucion/README.md)), a estructurar tu código, creando tus propias funciones, módulos y programas ([Tema 5](../05_programacion_modular/README.md)). Pero muchos problemas reales no encajan bien con datos sueltos: cuando queremos representar **una colección de calificaciones**, **un conjunto de coordenadas de un experimento** o **la ficha de un libro**, se nos quedan cortos.

En este tema conocerás los **tipos de datos complejos**: estructuras que agrupan varios valores bajo un único nombre. Aprenderás a usar **secuencias** (cadenas, tuplas y listas), **registros** (diccionarios, `namedtuple`, `dataclass` en Python; `struct` en C), y **conjuntos**, y descubrirás por qué la elección del tipo adecuado hace tu código más **claro**, más **corto** y más **rápido**.

Además, cuando ya sepas manipular colecciones enteras a la vez, descubrirás las **funciones de programación funcional** de Python (`map`, `filter`, `reduce`, `zip`, `enumerate`, `sorted`, `any`, `all`) que convierten muchos bucles del Tema 4 en **una sola línea legible** 🚀.

> [!NOTE]
> Este es probablemente el tema con **más carga práctica** de todo el curso. Cada nuevo tipo de dato abre un abanico de posibilidades: verás que muchos problemas del Tema 4 que resolvíamos con acumuladores se convierten aquí en operaciones directas sobre listas.

---

## 📚 Contenido del Tema

### 🔤 Cadenas de caracteres (`str`)

Ya has usado `str` en temas anteriores, pero como si fueran **valores atómicos**. En este tema descubrirás que las cadenas son **secuencias de caracteres** que puedes **indexar** (acceder por posición) y **rebanar** (extraer trozos con *slicing*), tanto con índices positivos como negativos. Verás también los **métodos** más útiles del tipo `str` (`upper`, `lower`, `strip`, `replace`, `split`, `isdigit`...) y aprenderás que las cadenas son **inmutables**: cualquier operación que "modifica" una cadena en realidad crea una **cadena nueva**.

### 📐 Arrays (en C) vs. listas y tuplas (en Python)

En C (y en la mayoría de lenguajes tradicionales), la estructura básica para agrupar datos ordenados del mismo tipo se llama **array**. Se declaran con un tamaño fijo (`int notas[10];`) y se accede a cada elemento por su índice. Verás cómo se declaran, inicializan y usan en C, y por qué son tan eficientes… pero también tan rígidos.

> [!IMPORTANT]
>**Python no tiene arrays nativos**. En su lugar te ofrece dos alternativas mucho más flexibles: las **listas** y las **tuplas**. Aprenderás cuándo usar una u otra.

### 📝 Tuplas (`tuple`) y listas (`list`)

Son los dos tipos "estrella" de Python para representar secuencias:

- **Tuplas** (`(1, 2, 3)`): **inmutables**. Ideales cuando los elementos no deben cambiar (coordenadas, fechas, parámetros de una función).
- **Listas** (`[1, 2, 3]`): **mutables**. Ideales cuando necesitas añadir, eliminar o modificar elementos.

Ambas soportan indexación, *slicing*, concatenación (`+`), repetición (`*`), y comparación. Aprenderás también los **métodos específicos** de cada una y las **operaciones comunes** a todas las secuencias.

### 🔄 Recorrido con `for` y **desempaquetado**

Descubrirás la variante **más idiomática** de `for` en Python:

```python
for elemento in secuencia:
    ...
```

Y una característica muy elegante: el **desempaquetado** (`unpacking`), que permite asignar en una sola línea los elementos de una secuencia a variables independientes:

```python
x, y = coordenadas
nombre, edad, ciudad = datos_usuario
```

### λ Programación funcional aplicada a secuencias

Cuando ya sabes manipular colecciones enteras, Python te ofrece un arsenal de **funciones de orden superior** que dan un salto cualitativo enorme:

- **`map(f, seq)`**: aplica `f` a cada elemento.
- **`filter(pred, seq)`**: se queda con los elementos que cumplen `pred`.
- **`reduce(f, seq)`**: acumula los elementos con `f`.
- **`zip(seq1, seq2)`**: combina dos secuencias en pares.
- **`enumerate(seq)`**: itera con índice y valor.
- **`sorted(seq, key=...)`**: ordena según un criterio.
- **`any(seq)`** / **`all(seq)`**: comprueban si alguno/todos son verdaderos.

Muchas de estas funciones aprovechan las **`lambda`** del Tema 5, y verás cómo un cálculo que en el Tema 4 ocupaba 10 líneas puede quedarse en **una**.

### 🗂️ Registros: diccionarios, `namedtuple` y `dataclass`

Cuando lo que quieres agrupar son **datos heterogéneos** (un nombre, una edad, una nota media...), las listas y tuplas se quedan cortas: obligan a recordar en qué posición está cada cosa. Es mucho más claro **acceder por nombre**:

```python
libro["titulo"]         # con dict
libro.titulo            # con namedtuple / dataclass
```

Estudiaremos las tres opciones que ofrece Python:

- **Diccionarios (`dict`)**: pares clave-valor. Flexibles, mutables, dinámicos.
- **`namedtuple`**: tuplas con nombres para sus campos. Inmutables, muy ligeras.
- **`dataclass`**: clases-con-atributos, mutables, muy cómodas para modelar entidades.

Y verás también el equivalente clásico en **C**: la palabra clave `struct`.

### 🔵 Conjuntos (`set`)

El último tipo es especial: los **conjuntos** guardan una colección **desordenada** de elementos **únicos** (sin duplicados). Son ideales cuando:

- Quieres **eliminar duplicados** de una colección.
- Necesitas hacer **operaciones matemáticas** sobre conjuntos (unión, intersección, diferencia, diferencia simétrica).

Descubrirás también el `frozenset`, la versión inmutable.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema serás capaz de:

### 1. Fundamentos (el "qué" y el "por qué")

- **Distinguir** entre tipos de datos primitivos y compuestos.
- **Clasificar** los tipos de datos complejos según sean **secuencias** (ordenadas, indexables), **registros** (con campos con nombre) o **conjuntos** (desordenados, sin duplicados).
- **Elegir** el tipo de dato adecuado para representar la información de un problema.
- **Comprender** las implicaciones de la **mutabilidad**.

### 2. Representación (el "cómo se expresa")

- **Indexar y rebanar** (*slicing*) secuencias con índices positivos y negativos.
- **Construir** cadenas, listas, tuplas, diccionarios, `namedtuple` y conjuntos con la sintaxis correcta.
- **Comparar** cómo estos conceptos se implementan en Python y en C.

### 3. Capacidad aplicada (el "cómo se usa")

- **Recorrer** secuencias con `for … in …` y con desempaquetado.
- **Modificar** listas (añadir, eliminar, reemplazar) con sus métodos específicos.
- **Aplicar** funciones de programación funcional (`map`, `filter`, `reduce`, `zip`, `enumerate`, `sorted`) para escribir código más conciso.
- **Modelar** entidades del mundo real con diccionarios, `namedtuple` o `dataclass`.
- **Realizar** operaciones matemáticas con conjuntos: unión, intersección, diferencia.

---

## ✅ Resultados de Aprendizaje

Podrás marcar como completados:

- [ ] **Acceder** a los caracteres de una cadena y **rebanarla** con la notación `[inicio:fin:paso]`.
- [ ] **Aplicar** los métodos más comunes de las cadenas (`upper`, `lower`, `strip`, `replace`, `split`, `join`).
- [ ] **Comprender** qué es un `array` en C y cómo se declara, inicializa y accede.
- [ ] **Crear y manipular** tuplas y listas: acceso, *slicing*, concatenación, repetición.
- [ ] **Modificar** listas usando `append`, `insert`, `remove`, `pop`, `sort`, `reverse`.
- [ ] **Recorrer** secuencias con `for … in …` combinado con `enumerate` o `zip`.
- [ ] **Desempaquetar** secuencias en variables independientes.
- [ ] **Aplicar** `map`, `filter`, `reduce`, `sorted`, `any`, `all` con funciones nombradas y con `lambda`.
- [ ] **Crear y consultar** diccionarios usando claves.
- [ ] **Definir** un `namedtuple` o un `dataclass` para modelar una entidad con campos.
- [ ] **Escribir** una `struct` en C y acceder a sus campos.
- [ ] **Crear y operar** con conjuntos: `add`, `remove`, unión, intersección, diferencia.
- [ ] **Convertir** entre los distintos tipos de secuencia con `list()`, `tuple()`, `set()`, `str()`.

---

## 🧭 Menú de Navegación en el Tema

| Orden | Material | Tiempo |
| ----- | -------- | ------ |
| 1     | [Teoría](./teoria/T6_ICC.md)       |   12   |
| 2     | [Recursos](./recursos/T6_RE_ICC.md)   |    7   |
| 3     | [Ejemplos](./ejemplos/T6_Ejem_ICC.md)   |    –   |
| 4     | [Ejercicios](./ejercicios/T6_Ejer_ICC.md) |    –   |
|       | [Menú de Temas](../README.md)                                     |    -   |
