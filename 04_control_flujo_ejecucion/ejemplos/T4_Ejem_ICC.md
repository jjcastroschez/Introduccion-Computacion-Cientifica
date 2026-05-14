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

En esta carpeta encontrarás **problemas reales** resueltos paso a paso usando los conceptos del Tema 4: condicionales (`if`, `match-case`), bucles (`for`, `while`), bucles anidados, manejo de excepciones (`try-except`) y rupturas del flujo (`break`, `continue`).

> [!NOTE]
> A diferencia del Tema 3, donde solo podías hacer programas "lineales" (ejecutar instrucciones una tras otra), ahora tus programas serán **dinámicos**: tomarán decisiones, repetirán cálculos cuantas veces haga falta y se recuperarán cuando algo vaya mal. Esta es la materia de la que están hechos los programas reales 💪.

Cada ejemplo se presenta en **tres formatos** complementarios -tal y como se hizo en el **Tema 3**- que son:

1. 📓 Un **Notebook básico** (`.ipynb`) con la solución directa.
2. 📔 Un **Notebook explicado** (`_icc.ipynb`) con el razonamiento, los matices y los detalles de implementación.
3. 🐍 Un **script** (`.py`) con la implementación lista para ejecutar desde la terminal.

> [!TIP]
> Descárgate los archivos, examínalos y ejecútalos. Ya conoces las herramientas que tienes que usar para trabajar con cada uno de ellos 😜.

---

## Contenido

| # | Ámbito | Problema | Estructura clave |
| :-: | :--- | :--- | :--- |
| 1 | Salud y deporte | Frecuencia cardíaca máxima por zonas de entrenamiento | `if-elif-else` |
| 2 | Climatología | Detección de olas de calor | `for` con `if` interno |
| 3 | Métodos numéricos | Cálculo de la raíz cuadrada por el método babilónico | `while` con convergencia |
| 4 | Software robusto | Validación de entradas con `try-except` | Manejo de excepciones |
| 5 | Depuración | Cómo encontrar bugs en bucles y condicionales | (transversal) |

---

### Ejemplo 1. Salud y deporte: Zonas de entrenamiento por frecuencia cardíaca

Cuando haces deporte, tu corazón late a distintas velocidades según la intensidad del ejercicio. Los entrenadores y médicos deportivos clasifican las **pulsaciones por minuto (ppm)** en **cinco zonas de entrenamiento**, cada una con efectos fisiológicos distintos: quema de grasa, mejora aeróbica, umbral anaeróbico, etc.

**El problema:** Dada la edad del usuario y sus pulsaciones actuales, queremos clasificar el esfuerzo en una de las cinco zonas y darle una recomendación.

**La fórmula:** La **Frecuencia Cardíaca Máxima** (FCM) se estima con la fórmula clásica de Tanaka *et al.* (2001):

$$\text{FCM} = 208 - 0.7 \cdot \text{edad}$$

Y a partir de ahí se definen los porcentajes que delimitan cada zona (50–60%, 60–70%, 70–80%, 80–90%, 90–100%).

**Por qué este ejemplo:** Es perfecto para un `if-elif-else` con varias ramas mutuamente excluyentes. Y como bonus, introduce un caso "fuera de rango" (pulsaciones absurdamente altas o bajas) que conviene tratar con cuidado.

👉 Solución directa en Notebook: [zonas_cardiacas.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/zonas_cardiacas.ipynb).  
👉 Notebook explicado paso a paso: [zonas_cardiacas_icc.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/zonas_cardiacas_icc.ipynb).  
👉 Script `.py` listo para ejecutar: [zonas_cardiacas_icc.py](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/zonas_cardiacas_icc.py).

---

### Ejemplo 2. Climatología: Detección de olas de calor

Una **ola de calor** se define oficialmente como un periodo de al menos **3 días consecutivos** en que la temperatura máxima diaria supera el umbral del percentil 95 de la serie histórica (en Castilla-La Mancha, en torno a los 36 ºC en verano).

**El problema:** Dada una lista con las temperaturas máximas diarias de un mes, contar cuántas olas de calor ha habido y cuántos días en total las componen.

**Por qué este ejemplo:** Combina un bucle `for` recorriendo la lista de temperaturas con un `if` que comprueba el umbral, y requiere mantener un **contador de días consecutivos** y otro de **olas detectadas**. Es un patrón de programación llamado *runs detection* (detección de rachas) que aparece en muchísimos campos: control de calidad, análisis de series temporales, biología, etc.

**Bonus pedagógico:** El ejemplo ilustra perfectamente cómo una decisión dentro de un bucle puede generar lógica compleja a partir de instrucciones muy simples. También muestra la importancia de **inicializar correctamente las variables contadoras** antes del bucle.

👉 Solución directa en Notebook: [olas_calor.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/olas_calor.ipynb).  
👉 Notebook explicado paso a paso: [olas_calor_icc.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/olas_calor_icc.ipynb).  
👉 Script `.py` listo para ejecutar: [olas_calor_icc.py](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/olas_calor_icc.py).

---

### Ejemplo 3. Métodos numéricos: Raíz cuadrada por el método babilónico

¿Cómo calcula tu calculadora una raíz cuadrada? No usa una fórmula mágica: aplica un **algoritmo iterativo** que se va aproximando al valor real. El más conocido (e increíblemente eficiente) es el **método babilónico** (también llamado método de Herón), que se usa desde hace más de 2 000 años:

$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)$$

Cada iteración duplica el número de cifras correctas. En menos de 10 vueltas, tienes la raíz cuadrada con precisión de 15 decimales.

**El problema:** Implementar este método para calcular $\sqrt{a}$ con una **tolerancia** dada (por ejemplo, $10^{-10}$), sin usar la función `math.sqrt()`.

**Por qué este ejemplo:** Es el ejemplo *paradigmático* del bucle `while` en computación científica:

* No sabes a priori cuántas iteraciones harán falta → necesitas `while`, no `for`.
* La condición de salida es la **convergencia** ($|x_{n+1} - x_n| < \text{tolerancia}$).
* Hay que protegerse contra **bucles infinitos** con un límite máximo de iteraciones.
* Ilustra un patrón fundamental que aparece en cientos de algoritmos científicos: bisección, Newton-Raphson, gradiente descendente...

👉 Solución directa en Notebook: [raiz_babilonica.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/raiz_babilonica.ipynb).  
👉 Notebook explicado paso a paso: [raiz_babilonica_icc.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/raiz_babilonica_icc.ipynb).  
👉 Script `.py` listo para ejecutar: [raiz_babilonica_icc.py](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/raiz_babilonica_icc.py).

---

### Ejemplo 4. Software robusto: Validación de entradas con `try-except`

Un programa "de juguete" asume que todo va bien: confía en que el usuario teclee lo que se le pide. Un programa **profesional** no asume nada: comprueba, valida y se recupera de los errores.

**El problema:** Crear una pequeña utilidad que pida al usuario un número entero positivo entre 1 y 100, y siga pidiéndolo (mostrando un mensaje de error claro) hasta que la entrada sea correcta.

**Por qué este ejemplo:** Combina **dos estructuras esenciales** de este tema:

* Un bucle `while` que se ejecuta hasta que la entrada es válida.
* Un bloque `try-except` que captura los distintos tipos de error (`ValueError` cuando se teclea texto en lugar de número, condición lógica para el rango).

Aprenderás también a **diferenciar tipos de excepción** (no es lo mismo que el usuario escriba `"hola"` que `"-5"`), y verás un patrón llamado **"validación robusta"** que se utiliza en cualquier programa que reciba datos del usuario.

👉 Solución directa en Notebook: [validacion_entrada.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/validacion_entrada.ipynb).  
👉 Notebook explicado paso a paso: [validacion_entrada_icc.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/validacion_entrada_icc.ipynb).  
👉 Script `.py` listo para ejecutar: [validacion_entrada_icc.py](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/validacion_entrada_icc.py).

---

### Ejemplo 5. Depuración: Cómo encontrar bugs en bucles y condicionales

Cuando un programa con bucles y condicionales **no funciona como esperabas**, el método "leer el código fijamente con cara de concentración" 😅 rara vez sirve. Lo que necesitas es un **depurador**.

Este ejemplo no es un problema de cálculo: es un **tutorial práctico** que te enseña tres técnicas para encontrar errores:

1. **🐛 *Print debugging***: la técnica universal. Insertar `print()` estratégicos para ver qué está pasando. Funciona siempre, no necesita herramientas, pero es lenta y poco escalable.
2. **🔬 El módulo `pdb`**: el depurador integrado de Python. Te permite **pausar** la ejecución, **inspeccionar** variables y **avanzar paso a paso** sin instalar nada extra.
3. **💻 El depurador visual de VS Code**: el más cómodo de todos. Marcas un *breakpoint* con un click, pulsas F5 y avanzas con los botones de control.

Como ejemplo guía partimos de un **programa con bugs deliberados** (un sumatorio que da resultados raros) y vemos cómo cada técnica nos ayuda a encontrar y corregir el error.

> [!IMPORTANT]
> Aprender a depurar es **tan importante como aprender a programar**. Un programador profesional dedica más tiempo a depurar que a escribir código nuevo. Cuanto antes te familiarices con el depurador, mejores programas escribirás 🚀.

👉 Notebook tutorial completo: [depuracion_tutorial_icc.ipynb](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/depuracion_tutorial_icc.ipynb).  
👉 Script con bugs para practicar: [programa_con_bugs.py](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/programa_con_bugs.py).  
👉 Script ya corregido (no mires hasta haber intentado depurarlo tú 😉): [programa_corregido.py](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejemplos/programa_corregido.py).

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T4_ICC.md)              |      8       |
| 2      | [Recursos](../recursos/T4_RE_ICC.md)       |      5       |
| 3      | **Ejemplos**                               |      -       |
| 4      | [Ejercicios](../ejercicios/T4_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
