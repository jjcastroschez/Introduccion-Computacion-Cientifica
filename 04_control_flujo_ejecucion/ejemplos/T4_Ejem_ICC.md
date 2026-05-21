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

# 🧐 Ejemplos - Tema 4: Control del Flujo de Ejecución 🔀

En esta carpeta encontrarás algunos documentos Notebooks de Jupyter y scripts preparados para mostrarte problemas solucionados usando las nuevas construcciones del Tema 4: **condicionales**, **bucles** (`for`, `while`) y **manejo de excepciones** (`try-except`).

> [!NOTE]
> Aún no se emplean **estructuras de datos compuestas** (`list`, `tuple`, `dict`...) ni se definen **funciones propias**: esos contenidos se ven en los **Temas 5 y 6**. Aquí seguimos trabajando con tipos simples (`int`, `float`, `bool`), pero por primera vez podemos hacer que el programa **tome decisiones** y **repita cálculos** las veces que haga falta 💪.

## Contenido

En el [Tema 3](../../03_variables_tipos_simples/ejemplos/T3_Ejem_ICC.md) vimos cómo aplicar fórmulas matemáticas cerradas (series geométricas, rentas perpetuas) a problemas reales de medicina y finanzas. Esas fórmulas son **muy potentes** porque te dan el resultado en una sola línea, pero tienen una limitación: solo sirven cuando el problema encaja exactamente con la fórmula.

Ahora, con las construcciones del Tema 4, vas a poder **simular el proceso paso a paso**, lo que te permitirá:

* Tratar **casos que la fórmula cerrada no contempla** (datos irregulares, condiciones de parada arbitrarias…).
* **Validar la entrada del usuario** para que tus programas no se rompan.

Y también aprenderás a ver **cómo evoluciona** el sistema, no solo a dónde llega.

### Ejemplo 1. Acumulación de fármacos — versión iterativa

¿Te acuerdas del problema de [acumulación de fármacos](../../03_variables_tipos_simples/ejemplos/farmacologia_exp_py.ipynb) que resolviste en el Tema 3?

* Cada día el paciente toma una dosis $a$ de medicamento (por ejemplo, 100mg).
* Cada día su cuerpo elimina un porcentaje constante (por ejemplo, el 20%).
* La pregunta: **¿cuánto fármaco acumulará a largo plazo?**

En el Tema 3 lo resolviste con la **fórmula cerrada** de la serie geométrica infinita: $$S_\infty = \frac{a}{1 - r}$$ 

Esta fórmula te daba el **valor límite**, pero no te decía nada del proceso.

**Lo que aporta el Tema 4**: ahora podemos **simular día a día** lo que va pasando, ver cómo se acerca al valor límite y, lo más importante, **podemos parar cuando queramos** (por ejemplo, cuando la concentración ya se haya estabilizado por debajo de una tolerancia dada).

#### Empleando Python:

👉 Notebook explicado paso a paso: [farmacologia_exp_py.ipynb](./farmacologia_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar con una solución general: [farmacologia.py](./farmacologia.py).

#### Empleando C:

👉 Notebook explicado paso a paso: [farmacologia_exp_c.ipynb](./farmacologia_exp_c.ipynb). 
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [farmacologia.c](./farmacologia.c). 

> [!TIP]
> Descarga los archivos, examínalos y ejecútalos. Compara el resultado de la simulación con el de la fórmula del Tema 3. ¿Cuándo coinciden? ¿Cuándo es mejor una u otra? 😜

### Ejemplo 2. Finanzas — anualidad finita

El otro problema del [Tema 3](../../03_variables_tipos_simples/ejemplos/finanzas_exp_py.ipynb) era el de las rentas perpetuas: un banco que te promete pagar 100 € **para siempre**.

La fórmula del Tema 3, nos daba el valor presente de esa renta perpetua: $$VP_\infty =\frac{a}{i}$$ 

Pero la realidad es que **casi nunca** firmamos productos financieros perpetuos. Las hipotecas son a 25 años, las anualidades duran 10 o 20 años, las pensiones son vitalicias…

**Lo que aporta el Tema 4**: con un bucle `for` podemos calcular el valor presente de una anualidad de $n$ años:

$$ VP_n = \sum_{t=1}^{n} \frac{a}{(1+i)^t} $$

Y verás algo bonito: cuando $n$ es muy grande, el resultado se acerca al valor de la **renta perpetua** del Tema 3. Recuperamos el caso del tema anterior como **caso límite** del nuevo.

#### Empleando Python:

👉 Notebook explicado paso a paso: [finanzas_exp_py.ipynb](./finanzas_exp_py.ipynb).
👉 Script `.py` listo para ejecutar con una solución general: [finanzas.py](./finanzas.py). 

#### Empleando C:

👉 Notebook explicado paso a paso:[finanzas_exp_c.ipynb](./finanzas_exp_c.ipynb).
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [finanzas.c](./finanzas.c). 

### Ejemplo 3. Validación robusta de entrada con `try-except`

En todos los programas anteriores (los del Tema 3 y los primeros del Tema 4), **asumimos que el usuario teclea bien**. Pero, ¿qué pasa si en el ejemplo de la farmacología teclea `'doscientos'` en lugar de `200`? El programa **se rompe** con un `ValueError`.

Un programa profesional **no confía** en la entrada: la valida y, si no es válida, vuelve a pedirla. Para hacerlo necesitamos combinar:

* Un bucle `while` que se repite hasta que la entrada sea válida.
* Un bloque `try-except` que **captura** el error de conversión sin que el programa se caiga.

**Lo que aporta el Tema 4**: por primera vez podemos escribir programas que **se recuperan** de los errores en lugar de morir abruptamente. Es una de las marcas de la programación profesional.

#### Empleando Python:

👉 Notebook explicado paso a paso: [validacion_entrada_exp_py.ipynb](./validacion_entrada_exp_py.ipynb).
👉 Script `.py` listo para ejecutar con una solución general: [validacion_entrada.py](./validacion_entrada.py).

#### Empleando C:

👉 Notebook explicado paso a paso: [validacion_entrada_exp_c.ipynb](./validacion_entrada_exp_c.ipynb).
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [validacion_entrada.c](./validacion_entrada.c). 

> [!TIP]
> Una vez entendido este patrón, **vuelve a los ejemplos 1, 2 y 3** y aplícalo: protege todas las llamadas a `int(input(...))` y `float(input(...))` con un bucle de validación. Verás cómo tus programas dejan de romperse cuando alguien teclea algo raro.

### Ejemplo 4. Algoritmo de Euclides para el MCD

Hasta ahora, todos los algoritmos que has implementado tenían un **número fijo de pasos**: leer datos, hacer un cálculo, mostrar el resultado. Pero hay problemas matemáticos donde el número de pasos **no se conoce de antemano** y depende de los datos de entrada. El ejemplo más clásico es el **algoritmo de Euclides** (siglo III a.C., uno de los algoritmos más antiguos de la historia).

* El problema: dados dos enteros positivos $a$ y $b$ (con $a>=b$), calcular su **máximo común divisor** $(mcd)$.
* El método: usar repetidamente la identidad $mcd(a, b) = mcd(b, a mod b)$ hasta que el segundo argumento valga $0$.

**Lo que aporta el Tema 4**: el algoritmo no encaja en ninguna fórmula cerrada — necesita **iterar mientras se cumpla una condición**. Ese es exactamente el patrón del bucle `while`, que también vamos a usar para **validar la entrada** del usuario con `try-except`.

#### Empleando Python:

👉 Notebook explicado paso a paso: [euclides_exp_py.ipynb](./euclides_exp_py.ipynb).
👉 Script `.py` listo para ejecutar con una solución general: [euclides.py](./euclides.py).

#### Empleando C:

👉 Notebook explicado paso a paso:[euclides_exp_c.ipynb](./euclides_exp_c.ipynb).
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [euclides.c](./euclides.c). 

### Ejemplo 5. Reparto de carga en camiones — versión iterativa

En el Tema 3 resolviste un problema de logística muy interesante: una empresa quiere repartir una **carga de 31 toneladas** en camiones de **7 t** y **5 t** sin desperdiciar espacio. Esto se modeliza como una **ecuación diofántica**:

$$7x + 5y = 31$$

cuya resolución se apoya en la **Identidad de Bézout** y en el cálculo del **inverso modular**. En el Tema 3, el programa hacía las cuentas finales, pero **el gestor tenía que calcular a mano** dos cosas:

* Verificar que mcd($a$, $b$) divide a $r$ (condición de Bézout).
* Calcular el **inverso modular** de $a$ módulo $b$ y proporcionarlo como entrada extra.

**Lo que aporta el Tema 4**: con un **bucle `while`** podemos implementar el [algoritmo de Euclides](euclides.py) y calcular el mcd automáticamente. Con un **bucle `for`** podemos buscar el inverso modular probando candidatos del $1$ al $b-1$. Y con **condicionales `if`** podemos comprobar que las soluciones sean números **naturales** (porque, recuerda, $-3$ camiones no tiene sentido físico). En definitiva: el ordenador se encarga de todo y el gestor solo introduce los datos del enunciado.

#### Empleando Python:

👉 Notebook explicado paso a paso: [camiones_exp_py.ipynb](./camiones_exp_py.ipynb).
👉 Script `.py` listo para ejecutar con una solución general: [camiones.py](./camiones.py).

#### Empleando C:

👉 Notebook explicado paso a paso: [camiones_exp_c.ipynb](./camiones_exp_c.ipynb).
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [camiones.c](./camiones.c). 


> [!TIP]
> Prueba con los mismos casos de la tabla del Tema 3 (7-5-31, 9-7-44, 9-7-41, 13-5-41, 5-3-37, 4-3-37). Verás que **el resultado es idéntico** pero ya no tienes que introducir el inverso modular: lo calcula el programa 🎯. Prueba también algún caso que **falle** (p.ej. 6-4-31, donde mcd(6,4)=2 no divide a 31, o 7-5-3, donde la solución no es natural).

### Ejemplo 6. Cómo depurar un programa con bucles

Cuando un programa con bucles y condicionales **no funciona como esperabas**, el método "leer el código fijamente con cara de concentración" 😅 rara vez sirve. Lo que necesitas es **depurar**: una técnica sistemática para encontrar errores.

Este ejemplo no es un problema matemático: es un **tutorial práctico** que te enseña tres técnicas de depuración:

1. 🐛 **`print()` debugging** — la técnica universal: insertar `print()` para ver qué está pasando.
2. 🔬 **El módulo `pdb`** — el depurador integrado de Python: te permite **pausar** la ejecución, **inspeccionar** variables y **avanzar paso a paso**.
3. 💻 **El depurador visual de VS Code** — el más cómodo de todos.

Como ejemplo guía partimos de un programa con un **bug deliberado** (una suma que da un resultado incorrecto) y vemos cómo cada técnica nos ayuda a encontrarlo y corregirlo.

> [!IMPORTANT]
> Aprender a depurar es **tan importante como aprender a programar**. Un programador profesional dedica más tiempo a depurar que a escribir código nuevo. Cuanto antes te familiarices con el depurador, mejores programas escribirás 🚀.

#### Empleando Python:

👉 Notebook explicado paso a paso: [depuracion_tutorial_exp_py.ipynb](./depuracion_tutorial_exp_py.ipynb).
👉 Script `.py` con el bug para prácticar: [programa_con_bugs.py](./programa_con_bugs.py).
👉 Script `.py` con el bug corregido (no mires hasta haberlo intentado tú 😉) [programa_corregido.py](./programa_corregido.py). 

#### Empleando C:

👉 Notebook explicado paso a paso: [depuracion_tutorial_exp_py.ipynb](./depuracion_tutorial_exp_c.ipynb).
👉 Programa `.c` con el bug para prácticar: [programa_con_bugs.py](./programa_con_bugs.c).
👉 Programa `.c` con el bug corregido (no mires hasta haberlo intentado tú 😉): [programa_corregido.py](./programa_corregido.c). 


---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T4_ICC.md)              |      8       |
| 2      | [Recursos](../recursos/T4_RE_ICC.md)       |      5       |
| 3      | **Ejemplos**                               |      -       |
| 4      | [Ejercicios](../ejercicios/T4_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
