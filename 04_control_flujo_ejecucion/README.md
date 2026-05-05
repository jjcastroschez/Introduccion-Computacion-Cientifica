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

# 🧠 Tema 4: Control del Flujo de Ejecución 🔀

En este tema aprenderás a **dirigir el orden en el que se ejecutan las instrucciones de un programa**. Hasta ahora has visto programas en los que las sentencias se ejecutan una tras otra, en el orden en el que aparecen escritas. Pero los problemas reales rara vez se resuelven así de simple: a veces necesitarás **decidir** entre varios caminos, y otras veces necesitarás **repetir** un mismo bloque de código muchas veces.

Aquí descubrirás las dos estructuras que cambian las reglas del juego: las **sentencias condicionales** (decidir) y las **sentencias de repetición o bucles** (iterar). Con ellas, junto a la secuencia, podrás construir cualquier programa imaginable —así lo demuestra el *Teorema de la Programación Estructurada* que viste en el Tema 2—.

Además, aprenderás a **gestionar errores de forma elegante** con el manejo de excepciones, evitando que tu programa se rompa ante imprevistos durante la ejecución 🛡️.

---

## 📚 Contenido del Tema

### 🧱 Estructura secuencial y la (mala) historia del `goto`

Veremos por qué la secuencialidad por sí sola no basta para resolver cualquier problema, y conocerás la antigua sentencia `goto`: por qué se inventó, por qué hoy está en desuso y por qué Python directamente no la incluye.

### 🔀 Sentencias condicionales

Aprenderás a **tomar decisiones** en tu código según se cumpla o no una condición:

* `if` simple — ejecutar un bloque sólo si se cumple la condición.
* `if-else` — elegir entre dos bloques alternativos.
* `if-elif-else` — encadenar varias condiciones sin anidar.
* `match-case` en Python (≥ 3.10), `switch` en C, y construcciones equivalentes en otros lenguajes.

También trabajarás con la representación en **pseudocódigo** y los **bloques de código** (delimitados por `{}` en C/Java o por **indentación** en Python).

### 🔁 Sentencias de repetición (bucles)

Verás los tres tipos principales de bucles y cuándo conviene usar cada uno:

* **`for`** — cuando se conoce de antemano cuántas veces hay que repetir. Aprenderás a usar `range()` en Python.
* **`while`** — repetición controlada por una condición evaluada *antes* de cada iteración.
* **`do-while`** — repetición controlada por una condición evaluada *después* de cada iteración (no existe en Python, pero veremos cómo simularlo).

### 🪺 Bucles anidados

Aprenderás a meter un bucle dentro de otro para recorrer estructuras complejas como matrices o tablas. Imprescindible para resolver problemas matemáticos con datos bidimensionales.

### 🚪 Romper el flujo: `break`, `continue` y `pass`

Verás cómo alterar el comportamiento normal de un bucle:

* `break` — salir del bucle inmediatamente.
* `continue` — saltar a la siguiente iteración.
* `pass` — marcador para código futuro o sin acción.

Y, sobre todo, **cuándo NO usarlos** para no romper los principios de la programación estructurada.

### 🛡️ Manejo de excepciones

Aprenderás a capturar y gestionar los errores que se producen *durante la ejecución* (no en compilación) usando `try`, `except`, `else` y `finally` en Python. Trabajaremos los errores más frecuentes: `ZeroDivisionError`, `TypeError` y `ValueError`.

### ⚠️ Buenas prácticas

Cerramos el tema con una serie de **avertencias** —principios de la programación estructurada que te ayudarán a escribir código limpio, legible y mantenible—:

* Un único punto de entrada y un único punto de salida por bloque.
* La condición del bucle siempre clara, al principio o al final.
* Evita el `while True` salvo cuando esté justificado.
* No modifiques la variable de control de un `for` dentro de su cuerpo.
* No abuses de `break`, `continue` ni `pass`.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema serás capaz de:

### 1. Fundamentos (el “qué” y el “por qué”)

* **Comprender** por qué la secuencialidad sola no basta para resolver cualquier problema computable.
* **Reconocer** las dos estructuras de control que, junto a la secuencia, permiten construir cualquier programa: selección e iteración.
* **Distinguir** entre los distintos tipos de bucle y saber cuándo usar cada uno.

### 2. Representación (el “cómo se expresa”)

* **Escribir** sentencias condicionales y bucles en pseudocódigo.
* **Implementar** estas estructuras en Python, conociendo además cómo se expresan en C, MatLab y otros lenguajes.
* **Aplicar** correctamente la indentación de los bloques de código en Python.

### 3. Capacidad aplicada (el “cómo se usa”)

* **Diseñar** soluciones a problemas que requieran tomar decisiones o repetir cálculos.
* **Combinar** condicionales y bucles (incluso anidados) para resolver problemas más complejos.
* **Gestionar** errores en tiempo de ejecución usando excepciones.
* **Aplicar** las buenas prácticas de la programación estructurada.

---

## ✅ Resultados de Aprendizaje

Podrás marcar como completados:

* **Implementar** sentencias condicionales `if`, `if-else` e `if-elif-else` en Python.
* **Usar** la sentencia `match-case` de Python para decisiones múltiples.
* **Escribir** bucles `for` con `range()` para repeticiones controladas por contador.
* **Escribir** bucles `while` para repeticiones controladas por condición.
* **Simular** el comportamiento `do-while` en Python.
* **Construir** bucles anidados para recorrer estructuras bidimensionales.
* **Utilizar** `break`, `continue` y `pass` cuando sea apropiado.
* **Manejar** excepciones con `try`, `except`, `else` y `finally`.
* **Aplicar** los principios de la programación estructurada al diseñar programas con flujo controlado.

---

## 🧭 Menú de Navegación en el Tema

| Orden | Material | Tiempo |
| --- | --- | --- |
| 1 | [Teoría](./teoria/T4_ICC.md) | 8 |
| 2 | [Recursos](./recursos/T4_RE_ICC.md) | 5 |
| 3 | [Ejemplos](./ejemplos/T4_Ejem_ICC.md) | – |
| 4 | [Ejercicios](./ejercicios/T4_Ejer_ICC.md) | – |
|  | [Menú de Temas](../README.md) | - |
