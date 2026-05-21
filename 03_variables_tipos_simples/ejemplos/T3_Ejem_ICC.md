
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

# 🧐 Ejemplos - Tema 3: Tipos de Datos y Variables 🔤

Vamos a ver varios **problemas reales** resueltos paso a paso usando los conceptos del Tema 3. Hay muchas cosas que puedes ya hacer con lo estudiado: selección de los tipos de datos básicos, manejo de variables para almacenar datos y la realización de operaciones con ellos. 

Comprender el concepto de variable, identificador, constantes, tipos de datos es el primer paso para escribir código comprensible, eficiente, mantenible, profesional... 

> [!NOTE]
> Serán solo programas "lineales", en los que se ejecutará una instrucción una tras otra de una secuencia proporcionada en el script. No puedes tomar decisiones ni repetir cálculos cuantas veces haga falta. Aún solo puedes hacer cosas básicas pero es el comienzo 🚀. En el Tema 4, empezarás a hacer programas más dinámicos 💪.  

Cada ejemplo se presenta en **dos formatos** complementarios:

1. 📔 Un **Notebook explicado** (`_exp.ipynb`) con el razonamiento, los matices y los detalles de implementación.
2. 🐍 Un **script** (`.py`) o **programa** (`.c`) con la implementación lista para ejecutar desde la terminal.

> [!TIP]
> Descárgate los archivos, examínalos y ejecútalos. Decide para cada uno cuál es la herramienta que mejor se ajusta a lo que quieres hacer 😜.

## Contenido

En contextos cotidianos es habitual enfrentarse a problemas que requieren la realización de cálculos sencillos que a menudo involucran operaciones básicas de suma, resta, multiplicación o división. Este tipo de problemas ya puedes solucionarlos sin problema, ya tienes todos los conocimientos necesarios (ejemplos 1 y 2).

Existe un problema que se repite en muchos campos (medicina y farmacología, finanzas,...) y para el que desde el campo de las matemáticas le han dado solución ofreciéndole una fórmula, ahora desde el campo de la computación científica le vas a dar un script para que puedan usarlo y hacer los cálculos pertinentes (ejemplos 3 y 4).

###  Ejemplo 1. Cálculo del interés simple

En algún momento de tu vida harás una inversión o solicitarás un préstamo o abrirás un depósito a plazo ficho, en el que realizando cálculos sobre los tipos de interés propuestos te va a ayudar a tomar mejores decisiones financieras.

El **interés** se define como *el precio del dinero*, es decir, lo que cuesta lo que pagas por utilizar un dinero que no es tuyo durante un tiempo determinado o lo que el banco te paga por utilizar tu dinero. 

**El problema concreto:** Vas a abrir una cuenta para meter esos ahorros que has tenido en tu primer trabajo más los ahorros de tu etapa pre-trabajador, en total tienes **6500€**. Has preguntado en varias entidades financieras y quieres saber cuál será el rendimiento en cada una de ellas. 

**La fórmula:** Trabajamos con la fórmula del cálculo del interés simple sobre el capital inicial durante el tiempo ofrecido.  

**Solución:** Hay que calcular el valor del interés simple. 

#### Empleando Python:

👉 Notebook explicado paso a paso: [interes_simple_exp_py.ipynb](./interes_simple_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar con una solución general: [interes_simple.py](./interes_simple.py). 

#### Empleando C:

👉 Notebook explicado paso a paso: [interes_simple_exp_c.ipynb](./interes_simple_exp_c.ipynb). 
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [interes_simple.c](./interes_simple.c). 

###  Ejemplo 2. Cálculo de capacidad de carga necesaria

La **identidad de Bézout** es un pilar de la *teoría de números*. Este teorema postula que el máximo común divisor (*mcd*) de dos enteros, *a* y *b*, se puede representar como la combinación lineal:

$$ax+by=mcd(a,b)$$

Es una herramienta esencial para despejar ecuaciones diofánticas, obtener inversos modulares y optimizar el manejo de fracciones.

**El problema concreto:** Una empresa de logística en España necesita enviar exactamente 31 toneladas de mercancía. Para ello, dispone únicamente de dos tipos de camiones: 
  * Camiones grandes con capacidad de 7 toneladas.
  * Camiones medianos con capacidad de 5 toneladas.

El gestor de la flota necesita saber cuántos camiones de cada tipo debe enviar para que vayan totalmente llenos, sin desperdiciar espacio ni dejar mercancía en tierra.

**La fórmula:** Definimos *x* como el número de camiones de 7 toneladas e *y* como el número de camiones de 5 toneladas. Queremos resolver la ecuación:

$$7x+5y=31$$

**La solución:** Vamos a solucionarlo con las herramientas que tenemos ahora y que implicará hacer algunas cosas a mano. Aplicaremos la aritmética modular directamente.

#### Empleando Python:

👉 Notebook explicado paso a paso: [camiones_exp_py.ipynb](./camiones_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar con una solución general: [camiones.py](./camiones.py).  

> [!WARNING]
> No es la mejor forma de solucionar este problema, porque implica hacer muchas cosas a mano, e incluso suposiciones, pero así justificamos la necesidad de hacer mejoras en siguientes temas 😜. 

###  Ejemplo 3. Medicina y Farmacología: Acumulación de fármacos

Cuando un paciente toma un medicamento en una dosis diaria, eliminando su cuerpo diariamente un porcentaje constante, llega un momento en el que la cantidad de medicamento en sangre se estabiliza y no cambia.  

**El problema concreto:** Si un paciente toma una dosis diaria de **100mg** de un medicamento, cuyo porcentaje de eliminación diaria es del **20%**, ¿cuánta medicina habrá en su cuerpo a largo plazo máximo?

**La fórmula:** Trabajamos con series geométricas convergentes. Cada dosis nueva se suma a lo que queda de las anteriores (que se ha multiplicado por r=0.8). 

**Solución:** Hay que calcular la convergencia de la serie geométrica.

La convergencia de esta serie le dice al médico cuál es el "nivel de estado estacionario", es decir, el punto donde se deja de acumular fármaco y el nivel se estabiliza para no ser tóxico.

#### Empleando Python:

👉 Notebook explicado paso a paso: [farmacologia_exp_py.ipynb](./farmacologia_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar con una solución general: [farmacologia.py](./farmacologia.py). 

#### Empleando C:

👉 Notebook explicado paso a paso: [farmacologia_exp_c.ipynb](./farmacologia_exp_c.ipynb). 
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [farmacologia.c](./farmacologia.c). 


###  Ejemplo 4. Finanzas: El valor del dinero en el tiempo

Un banco te ha prometido pagar **100€** cada año para siempre, ese dinero del futuro vale menos hoy debido a la inflación y al coste de oportunidad. El dinero está a un interés del **5%**. 

**El problema:** Calcular el valor presente de una anualidad o una renta perpetua.

**La fórmula:** Volvemos a trabajar con una serie geométrica. El "primer término" **a** es el pago inicial, y la "razón" r es el factor de descuento (basado en el tipo de interés).

**Solución:** El análisis de la convergencia nos permite saber cuánto vale hoy un fondo de pensiones.

#### Empleando Python:

👉 Notebook explicado paso a paso:[finanzas_exp_py.ipynb](./finanzas_exp_py.ipynb).
👉 Script `.py` listo para ejecutar con una solución general: [finanzas.py](./finanzas.py). 

#### Empleando C:

👉 Notebook explicado paso a paso:[finanzas_exp_c.ipynb](./finanzas_exp_c.ipynb).
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [finanzas.c](./finanzas.c). 


---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo       | 
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T3_ICC.md)              |      6       |
| 2      | [Recursos](../recursos/T3_RE_ICC.md)       |      5       |
| 3      | **Ejemplos**                               |      -       |
| 4      | [Ejercicios](../ejercicios/T3_Ejer_ICC.md) |      -       |
|        | [Menu del Tema actual](../README.md)       |      -       |