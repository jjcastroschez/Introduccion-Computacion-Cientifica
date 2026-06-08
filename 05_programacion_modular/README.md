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

# 🧩 Tema 5: Programación Modular 🧱

Hasta ahora, tus programas han sido **monolíticos**: todo el código vivía dentro de un único fichero, ejecutándose desde la primera línea hasta la última. Era suficiente para los problemas que has resuelto, pero a partir de cierto tamaño se vuelve **inmanejable**: el código se repite, las variables se mezclan, y un cambio en una línea provoca efectos imprevistos en otras tres.

En este tema aprenderás la técnica que **resuelve este problema** y que define la programación profesional: la **programación modular**. La idea, en una frase, es muy simple: **divide y vencerás**. Romperás los problemas grandes en piezas pequeñas reutilizables (subprogramas, módulos, paquetes) que podrás combinar, probar y mantener por separado.

Aquí descubrirás cómo **crear tus propias funciones y procedimientos**, cómo **agruparlas en módulos** (esos `.py` que hasta ahora solo habías importado) y cómo **organizar módulos en paquetes** para construir bibliotecas que tus compañeros (o tú mismo en otros proyectos) podrán reutilizar 🚀.

> [!NOTE]
> El Tema 5 marca el momento en que tus programas dejan de ser "ejercicios de clase" y empiezan a parecerse al **software real**. Las funciones, los módulos y los paquetes son las construcciones con las que se levantan NumPy, SciPy, scikit-learn y cualquier herramienta científica que vayas a usar como matemático profesional.

---

## 📚 Contenido del Tema

### 🧩 ¿Qué es la programación modular?

Veremos por qué dividir un programa en partes lo hace **más legible, más mantenible y más reutilizable**. Aprenderás la diferencia entre la programación estructurada ([Tema 4](../04_control_flujo_ejecucion/README.md)) y la programación modular, y conocerás los **diagramas de descomposición funcional**, que representan visualmente la jerarquía de llamadas entre subprogramas.

### 🛠️ Subprogramas: funciones y procedimientos

Los **subprogramas** son las piezas básicas. Aprenderás:

- La diferencia entre **función** (devuelve un valor) y **procedimiento** (hace cosas pero no devuelve nada).
- Los conceptos de **definición** (escribir el subprograma una vez) y **llamada** (usarlo cuantas veces quieras).
- La sintaxis `def nombre(args):` en Python y su equivalente en C.
- Buenas prácticas para **nombrar** los subprogramas: verbos para procedimientos, sustantivos para funciones, `es/está/hay/tiene` para funciones booleanas.

### 📦 Parámetros: paso de información

Estudiaremos cómo se pasa la información del programa principal al subprograma y al revés:

- **Paso por valor** y **paso por referencia** en C.
- **Paso por referencia de objeto** en Python: por qué los objetos inmutables (`int`, `float`, `str`) se comportan como paso por valor, y los mutables (`list`, `dict`) como paso por referencia.
- **Parámetros variables** con `*args` y devolución de **varios valores** a la vez.
- Anotaciones de tipo (*type hints*) en Python: cuándo usarlas y por qué te van a ayudar.

### 🎯 Funciones como ciudadanos de primera clase

En Python (y en otros lenguajes funcionales), las funciones se pueden tratar como cualquier otro valor:

- **Asignarse a variables**.
- **Pasarse como argumentos** a otras funciones.
- **Devolverse como resultado** de otras funciones.

Esto abre la puerta a las **funciones de orden superior** y a un estilo de programación muy potente que verás en el Tema 6 con `map`, `filter` y `reduce`.

### λ Expresiones `lambda`

Cuando necesites una función **pequeña y de un solo uso**, no merece la pena escribir un `def` completo. Las expresiones `lambda` te permitirán definir funciones anónimas en una sola línea. Verás cuándo usarlas y, sobre todo, **cuándo no usarlas** (porque su abuso destroza la legibilidad).

### 📁 Módulos y paquetes

Un **módulo** no es más que un archivo `.py`. Un **paquete** es una carpeta de módulos relacionados (con un fichero especial `__init__.py`). Aprenderás a:

- Crear tus propios módulos y paquetes.
- Estructurar paquetes con **submódulos** para proyectos más grandes.
- Importarlos en tus programas con `import`, `import ... as alias` y `from ... import ...`.
- Comparar con la forma de hacerlo en C (cabeceras `.h` + implementación `.c`).

### 🚪 La función `main` y la directiva de protección

Conocerás la **convención profesional** para estructurar todo programa Python: encapsular la lógica principal dentro de una función `main()` y protegerla con `if __name__ == "__main__"`. Veremos qué hace exactamente esta línea misteriosa y por qué la verás en absolutamente todos los proyectos Python serios.

### 📖 Documentando código

Aprenderás a documentar tus funciones y módulos con **docstrings** (`"""..."""`), siguiendo convenciones estándar (`:param:`, `:return:`, `:requisitos:`). Un código bien documentado es un código que tu yo del futuro te agradecerá.

### 🔍 Ámbito, visibilidad y vigencia de las variables

¿Por qué una variable definida dentro de una función **no se ve** desde fuera? ¿Y por qué a veces una variable global parece "cambiar de valor" al entrar en un subprograma? Aprenderás los conceptos de **ámbito** (global vs. local), **visibilidad** y **vigencia**, y los relacionarás con cómo el ordenador gestiona internamente la **pila de llamadas**.

### 🪞 Recursividad

Una función puede **llamarse a sí misma**. Suena extraño, pero es la forma más elegante de resolver muchos problemas matemáticos (factoriales, sucesión de Fibonacci, recorridos de árboles). Verás sus **ventajas** (claridad, divide y vencerás natural) y sus **desventajas** (consumo de memoria, dificultad para depurar) para saber cuándo usarla y cuándo preferir la iteración del Tema 4.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema serás capaz de:

### 1. Fundamentos (el "qué" y el "por qué")

- **Comprender** el principio de "divide y vencerás" como herramienta para abordar problemas complejos.
- **Distinguir** entre subprograma, módulo y paquete.
- **Diferenciar** funciones de procedimientos según devuelvan o no un valor.
- **Reconocer** las ventajas de la programación modular: reutilización, mantenibilidad y trabajo en equipo.

### 2. Representación (el "cómo se expresa")

- **Escribir** la definición y la llamada de funciones y procedimientos en pseudocódigo.
- **Implementar** subprogramas en Python con `def`, parámetros, valor de retorno y anotaciones de tipo.
- **Conocer** cómo se hace lo mismo en C (cabeceras, paso por valor/referencia).
- **Documentar** correctamente las funciones y módulos con docstrings.

### 3. Capacidad aplicada (el "cómo se usa")

- **Descomponer** un problema en subprogramas con responsabilidades bien definidas.
- **Crear** módulos y paquetes para organizar código reutilizable.
- **Usar** funciones como ciudadanos de primera clase y expresiones `lambda` cuando convenga.
- **Estructurar** programas con `main()` y la guarda `if __name__ == "__main__"`.
- **Razonar** sobre el ámbito de las variables y diagnosticar errores frecuentes derivados de él.
- **Aplicar** la recursividad cuando aporte claridad al problema, y reconocer cuándo no es la mejor opción.

---

## ✅ Resultados de Aprendizaje

Podrás marcar como completados:

- [ ] **Definir** funciones y procedimientos en Python con la sintaxis `def`.
- [ ] **Pasar** parámetros y devolver uno o varios valores desde una función.
- [ ] **Usar** parámetros variables (`*args`) cuando el número de argumentos no se conoce de antemano.
- [ ] **Asignar** funciones a variables y **pasarlas** como argumentos a otras funciones.
- [ ] **Escribir** expresiones `lambda` para definir funciones de una sola línea.
- [ ] **Crear** módulos `.py` propios y **organizar** módulos relacionados en paquetes.
- [ ] **Importar** módulos y paquetes usando las distintas formas (`import`, `as`, `from`).
- [ ] **Estructurar** programas con una función `main()` y la guarda `if __name__ == "__main__"`.
- [ ] **Documentar** funciones y módulos siguiendo el formato estándar de docstrings.
- [ ] **Distinguir** entre variables locales y globales y razonar sobre su visibilidad.
- [ ] **Implementar** funciones recursivas con un caso base correcto.

---

## 🧭 Menú de Navegación en el Tema

| Orden | Material | Tiempo |
| ----- | ------- | ------ |
| 1     | [Teoría](./teoria/T5_ICC.md)       |   10   |
| 2     | [Recursos](./recursos/T5_RE_ICC.md)   |    6   |
| 3     | [Ejemplos](./ejemplos/T5_Ejem_ICC.md)   |    –   |
| 4     | [Ejercicios](./ejercicios/T5_Ejer_ICC.md) |    –   |
|       | [Menú de Temas](../README.md)                                     |    -   |
