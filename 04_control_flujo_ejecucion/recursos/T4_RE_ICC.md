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

# 🎓 Recursos - Tema 4: Control del Flujo de Ejecución 🔀

En este apartado encontrarás herramientas y documentación para **entender, visualizar y depurar** el flujo de ejecución de tus programas. El control del flujo es donde más se nota la diferencia entre *leer* código y *entender* código: cuando entran en juego decisiones, bucles y excepciones, **ver** lo que está pasando es la mejor forma de aprender.

---

## 🎬 Visualizadores paso a paso

Cuando un programa tiene un `if`, un `for` anidado o una excepción, el orden en que se ejecutan las instrucciones deja de ser obvio. Los **visualizadores paso a paso** son la herramienta más útil de este tema: te permiten ejecutar el código línea a línea y ver en cada momento *qué bloque se está ejecutando, qué decisión se ha tomado y cómo cambian las variables*.

### ⭐ Python Tutor (recurso estrella)

**[Python Tutor](https://pythontutor.com/)** es una herramienta web gratuita que ya conociste en el [Tema 3](../../03_variables_tipos_simples/recursos/T3_RE_ICC.md). En este tema cobra **especial relevancia** porque permite:

- Ver una **flecha** que se mueve por las líneas del código indicando dónde está la ejecución.
- Comprobar **qué rama** del `if-elif-else` se ha tomado en cada momento.
- Observar el **valor del contador** dentro de un `for` o `while` en cada iteración.
- Ver cómo se **propaga una excepción** a través de los bloques `try-except`.

> [!TIP]
> Pega cualquiera de los [ejemplos del tema](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/T4_Ejem_ICC.md) en Python Tutor y dale a "Visualize Execution". Verás cómo el "puntero" salta entre las distintas ramas del `if` o gira dentro del bucle. Es la mejor forma de *ver* lo que se está aprendiendo.

### 🔍 Otros visualizadores recomendados

- **[Thonny](https://thonny.org/)**: IDE de Python pensado para principiantes (recomendado en el [Tema 1](../../01_introduccion/recursos/T1_RE_ICC.md)). Tiene un **debugger visual** integrado que muestra los valores de las variables a la vez que se ejecuta el código. Muy recomendado si Python Tutor se queda corto.
- **[VS Code Python Debugger](https://code.visualstudio.com/docs/python/debugging)**: si ya usas VS Code (recomendado en el [Tema 1](../../01_introduccion/recursos/T1_RE_ICC.md)), puedes usar su depurador para poner **puntos de ruptura** y avanzar paso a paso. La curva de aprendizaje es algo mayor pero, una vez dominado, es una herramienta poderosísima.

---

## 🐞 Depuración (debugging)

Cuando un programa con bucles o condicionales **no hace lo que esperabas**, no se trata de adivinar dónde está el error. Hay que **depurarlo**: ejecutarlo paso a paso y comprobar las variables. Este tema es el primero donde la depuración se vuelve realmente útil.

### Conceptos clave que conviene conocer

- **Punto de ruptura (*breakpoint*)**: marca una línea del código en la que el programa se detendrá durante la ejecución para que puedas inspeccionar las variables.
- **Paso a paso (*step over* / *step into*)**: ejecutar una sola instrucción cada vez, viendo cómo cambia el estado.
- **Pila de llamadas (*call stack*)**: la lista de funciones que están "abiertas" en un momento dado. Importante en el Tema 5, pero ya útil para entender excepciones.
- **Inspección de variables**: ver el valor actual de cualquier variable sin tener que añadir un `print()`.

### 🛠️ Herramientas de depuración

- **[VS Code Debugger para Python](https://code.visualstudio.com/docs/python/debugging)**: el más cómodo para empezar. Pulsas F5, marcas un breakpoint con click en el margen y listo.
- **[`pdb` (Python Debugger)](https://docs.python.org/es/3/library/pdb.html)**: el depurador integrado de Python en línea de comandos. Útil cuando trabajas en un servidor sin interfaz gráfica.
- **[`ipdb`](https://pypi.org/project/ipdb/)**: una versión de `pdb` con autocompletado y resaltado de sintaxis. Se usa mucho en Jupyter.

> [!NOTE]
> **Truco de principiante**: antes de aprender a usar un depurador, casi todo el mundo "depura" añadiendo `print()` por todas partes. Es una técnica perfectamente válida llamada *print debugging*. El depurador es más eficiente, pero `print()` siempre funciona.

---

## 📊 Diagramas de flujo (recordatorio)

En el [Tema 2](../../02_algoritmos/recursos/T2_RE_ICC.md) ya conociste herramientas para crear diagramas de flujo. En este tema, **dibujar el diagrama antes de escribir el código** es especialmente útil cuando hay condicionales encadenados o bucles anidados.

Las herramientas más cómodas para diagramas con muchas decisiones y bucles son:

- **[draw.io](https://www.drawio.com)**: gratuito, intuitivo, exporta a SVG/PNG/PDF. Recomendado para principiantes.
- **[Mermaid](https://mermaid.live/)**: permite escribir el diagrama en **texto plano** y verlo renderizado al instante. Lo mejor: GitHub lo soporta de forma nativa, así que puedes incrustarlo directamente en tus archivos `.md`.

> [!TIP]
> **Mermaid en GitHub**: si en un fichero `.md` escribes un bloque marcado como `mermaid`, GitHub lo dibuja automáticamente. Por ejemplo:
>
> ````markdown
> ```mermaid
> flowchart TD
>     A[Inicio] --> B{edad >= 18?}
>     B -->|Sí| C[Mayor de edad]
>     B -->|No| D[Menor de edad]
>     C --> E[Fin]
>     D --> E
> ```
> ````
>
> Resulta cómodo para incluir un diagrama rápido en tus notas o entregas sin necesidad de subir imágenes aparte.

---

## 📚 Documentación de Referencia

### Python — Control de flujo

- **[Tutorial oficial: Control flow](https://docs.python.org/es/3/tutorial/controlflow.html)**: el capítulo del tutorial oficial dedicado a `if`, `for`, `while`, `break`, `continue`, `pass` y `match`. **Lectura altamente recomendable**.
- **[Compound statements (referencia oficial)](https://docs.python.org/es/3/reference/compound_stmts.html)**: la referencia formal de la sintaxis de las sentencias compuestas. Más densa, pero exhaustiva.
- **[Built-in `range()`](https://docs.python.org/es/3/library/stdtypes.html#range)**: la función más usada con `for`. Conviene leer su documentación con detenimiento para evitar errores *off-by-one*.

### Python — Manejo de excepciones

- **[Tutorial oficial: Errors and Exceptions](https://docs.python.org/es/3/tutorial/errors.html)**: explicación accesible del modelo `try-except-else-finally`.
- **[Built-in Exceptions (lista oficial)](https://docs.python.org/es/3/library/exceptions.html)**: el catálogo completo de excepciones de Python. Te servirá como referencia para saber qué tipo de error capturar.

### Python — `match-case` (Pattern Matching)

- **[PEP 634: Structural Pattern Matching: Specification](https://peps.python.org/pep-0634/)**: la propuesta formal que introdujo `match-case` en Python 3.10.
- **[PEP 636: Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)**: tutorial **muy didáctico** sobre `match-case`, con ejemplos progresivos.

### Lenguaje C — Control de flujo

- **[C Control Statements (Programiz)](https://www.programiz.com/c-programming/c-if-else-statement)**: guía visual sobre `if`, `switch`, `for`, `while` y `do-while` en C. Útil para ver las diferencias sintácticas con Python.
- **[Format Specifiers en C (recordatorio)](https://www.geeksforgeeks.org/format-specifiers-in-c/)**: imprescindible si comparas ejemplos de bucles con `printf()`.

---

## 🎨 Guías de estilo

Cuando un programa tiene varios niveles de bucles e `if` anidados, **el estilo importa más que nunca**: una mala indentación o un nombre de variable poco descriptivo pueden hacer ilegible un trozo de código.

- **[PEP 8 — Indentation](https://peps.python.org/pep-0008/#indentation)**: reglas de indentación oficiales para Python. Recordatorio: 4 espacios, nunca tabuladores mezclados.
- **[PEP 8 — Maximum Line Length](https://peps.python.org/pep-0008/#maximum-line-length)**: límite de 79 caracteres por línea. Especialmente relevante en bucles anidados con condiciones largas.
- **[Hitchhiker's Guide to Python — Code Style](https://docs.python-guide.org/writing/style/)**: una guía de estilo más amena que el PEP 8, con ejemplos comentados.

---

## ⚠️ Errores típicos y cómo evitarlos

El control del flujo es donde más se cometen errores sutiles. Estos recursos te ayudarán a identificarlos y prevenirlos:

- **[The Off-By-One Error (Wikipedia)](https://en.wikipedia.org/wiki/Off-by-one_error)**: el error más típico al trabajar con bucles. Famoso entre programadores: *"There are only two hard things in computer science: cache invalidation and naming things — and off-by-one errors"*.
- **[Floating Point Arithmetic (oficial)](https://docs.python.org/es/3/tutorial/floatingpoint.html)**: por qué `0.1 + 0.2 != 0.3` y cómo lidiar con ello en condiciones que comparen `float`.
- **[Common Mistakes in Python Loops (Real Python)](https://realpython.com/python-for-loop/)**: artículo accesible sobre los errores más frecuentes en bucles `for`. Inglés, pero muy claro.

---

## 📖 Hojas de referencia rápida (cheatsheets)

Para tener a mano la sintaxis sin tener que buscar en la documentación:

- **[Python Cheatsheet — Control Flow](https://www.pythoncheatsheet.org/cheatsheet/control-flow)**: tabla compacta con la sintaxis de `if`, `for`, `while`, `break`, `continue` y `pass`.
- **[Python Cheatsheet — Exception Handling](https://www.pythoncheatsheet.org/cheatsheet/exception-handling)**: cheatsheet específico de `try-except-else-finally`.
- **[OverAPI Python](https://overapi.com/python)**: índice visual con enlaces directos a la documentación oficial. Ideal para estudiantes que quieren consultar rápido.

---

## 🧠 Para practicar (problemas guiados)

La mejor forma de interiorizar el control del flujo es **escribir mucho código con bucles y condicionales**. Estos sitios ofrecen problemas progresivos y autoevaluables:

- **[HackerRank — Python (Introduction)](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-introduction)**: problemas básicos centrados en `if`, `for`, `while`. Cada uno con tests automáticos.
- **[Exercism — Python Track](https://exercism.org/tracks/python)**: ejercicios con *mentoring* gratuito por programadores reales. Perfecto si quieres feedback sobre tu código.
- **[Codewars](https://www.codewars.com/?language=python)**: retos cortos clasificados por dificultad. Hay miles de problemas que requieren bucles y condicionales.
- **[Project Euler](https://projecteuler.net/)**: problemas matemáticos resolubles con programación. Muchos requieren bucles bien diseñados.

> [!TIP]
> Empieza por los problemas más sencillos (en HackerRank verás un ranking de dificultad) e intenta resolverlos **dibujando primero el diagrama de flujo en papel**. Notarás cómo, después de unas semanas, el flujograma deja de ser necesario porque tu cerebro ya "lo dibuja solo".

---

## Sumario de enlaces interesantes

### Visualizadores y depuradores

- [Python Tutor](https://pythontutor.com/)
- [Thonny](https://thonny.org/)
- [VS Code Python Debugger](https://code.visualstudio.com/docs/python/debugging)
- [pdb (oficial)](https://docs.python.org/es/3/library/pdb.html)
- [ipdb](https://pypi.org/project/ipdb/)

### Diagramas de flujo

- [draw.io](https://www.drawio.com)
- [Mermaid Live Editor](https://mermaid.live/)
- [Mermaid: documentación oficial](https://mermaid.js.org/syntax/flowchart.html)

### Documentación oficial

- [Tutorial: Control flow (Python)](https://docs.python.org/es/3/tutorial/controlflow.html)
- [Tutorial: Errors and Exceptions (Python)](https://docs.python.org/es/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/es/3/library/exceptions.html)
- [PEP 634 — Pattern Matching: Specification](https://peps.python.org/pep-0634/)
- [PEP 636 — Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)

### Cheatsheets

- [Python Cheatsheet — Control Flow](https://www.pythoncheatsheet.org/cheatsheet/control-flow)
- [Python Cheatsheet — Exception Handling](https://www.pythoncheatsheet.org/cheatsheet/exception-handling)
- [OverAPI Python](https://overapi.com/python)

### Plataformas para practicar

- [HackerRank Python](https://www.hackerrank.com/domains/python)
- [Exercism Python Track](https://exercism.org/tracks/python)
- [Codewars](https://www.codewars.com/?language=python)
- [Project Euler](https://projecteuler.net/)

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T4_ICC.md)              |      8       |
| 2      | **Recursos**                               |      5       |
| 3      | [Ejemplos](../ejemplos/T4_Ejem_ICC.md)     |      -       |
| 4      | [Ejercicios](../ejercicios/T4_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
