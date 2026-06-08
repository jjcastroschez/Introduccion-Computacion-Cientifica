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

# 🧐 Ejemplos - Tema 5: Programación Modular 🧩

En esta carpeta encontrarás Notebooks de Jupyter y scripts que muestran los nuevos conceptos del Tema 5: **funciones propias**, **módulos**, **paquetes**, **recursividad** y **funciones como ciudadanos de primera clase**.

> [!NOTE]
> A diferencia de los temas anteriores, aquí ya **definimos funciones propias** y **organizamos código en módulos**. Pero todavía no usamos **estructuras de datos compuestas** (`list`, `tuple`, `dict`...) ni hacemos **entrada/salida a ficheros**: esos contenidos se ven en los **Temas 6 y 7**. Seguimos trabajando con tipos simples (`int`, `float`, `bool`, `str`).

## Contenido

En el [Tema 4](../../04_control_flujo_ejecucion/ejemplos/T4_Ejem_ICC.md) escribimos programas que **tomaban decisiones** y **repetían cálculos**, pero cada programa era un script independiente que vivía en un único archivo. Cuando necesitábamos reutilizar un algoritmo (por ejemplo, el de Euclides en el problema de los camiones), **copiábamos y pegábamos** el código.

Con las construcciones del Tema 5, esa época termina. Vas a poder:

* **Encapsular** un cálculo en una función reutilizable que se invoca con un solo nombre.
* **Reunir** funciones relacionadas en módulos importables desde cualquier programa.
* **Organizar** módulos grandes en paquetes jerárquicos (como hacen NumPy, SciPy y todas las bibliotecas profesionales).
* **Tratar las funciones como valores** que se pueden pasar a otras funciones, anticipando el estilo funcional del Tema 6.
* **Aplicar recursividad** cuando aporte claridad al problema, y reconocer cuándo no es la mejor opción.

### Ejemplo 1. Calculadora científica modular

Empezamos por lo más sencillo: **escribir nuestras propias funciones**. En lugar de calcular las cosas con expresiones inline (`math.pi * r**2`), las encapsulamos en funciones con nombre descriptivo (`area_circulo(r)`).

Aprenderás:

* La sintaxis `def nombre(parámetros) -> tipo:`.
* La diferencia entre **definir** una función y **llamarla**.
* La convención de **nombrado** (sustantivos para funciones, verbos para procedimientos, `es_` para booleanas).
* La estructura profesional con `main()` y `if __name__ == "__main__":`.

**Lo que aporta el Tema 5**: el primer paso del salto cualitativo. Tus programas dejan de ser una secuencia plana de instrucciones para convertirse en **piezas con nombre** que puedes combinar.

#### Empleando Python:

👉 Notebook explicado paso a paso: [calculadora_exp_py.ipynb](./calculadora_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar con una solución general: [calculadora.py](./calculadora.py).

#### Empleando C:

👉 Notebook explicado paso a paso: [calculadora_exp_c.ipynb](./calculadora_exp_c.ipynb).  
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [calculadora.c](./calculadora.c).

### Ejemplo 2. Mejorando la validación de entrada

En el [Tema 4](../../04_control_flujo_ejecucion/ejemplos/T4_Ejem_ICC.md) escribíamos un bucle `while` + `try-except` cada vez que necesitábamos pedir un número al usuario. **Lo copiábamos y pegábamos** para cada nueva entrada, cambiando solo el mensaje y el rango.

Ahora encapsulamos ese patrón en una función `pedir_entero(mensaje, minimo, maximo)`. Con una sola línea pedimos cualquier entero, con cualquier mensaje, en cualquier rango. Y si mañana queremos mejorar el mensaje de error, **lo cambiamos en un solo sitio**.

**Lo que aporta el Tema 5**: cuando un patrón se repite, no se duplica — **se encapsula en una función**. Es la regla número uno del programador profesional.

> [!TIP]
> Este ejemplo en C es especialmente interesante porque **C no dispone del mecanismo `try-except`**. Verás cómo encapsular la validación usando las técnicas más manuales que ya conoces del Tema 4: comprobar el valor de retorno de `scanf` y vaciar el buffer de entrada.

#### Empleando Python:

👉 Notebook explicado paso a paso: [validacion_entrada_exp_py.ipynb](./validacion_entrada_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar con una solución general: [validacion_entrada.py](./validacion_entrada.py).

#### Empleando C:

👉 Notebook explicado paso a paso: [validacion_entrada_exp_c.ipynb](./validacion_entrada_exp_c.ipynb).  
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [validacion_entrada.c](./validacion_entrada.c).

### Ejemplo 3. Tu propio módulo: `matematicas.py`

Las funciones que defines en un programa solo viven dentro de ese programa. Si en otro programa necesitas la misma función, **copias y pegas**. Otra vez la trampa de la duplicación.

La solución son los **módulos**: archivos `.py` con funciones reutilizables. Cuando otro programa hace `import matematicas`, dispone automáticamente de todas las funciones que has puesto dentro.

En este ejemplo reunimos varias funciones que escribimos como scripts independientes en el Tema 4 (Euclides, raíz babilónica, criba de Eratóstenes, inverso modular, factorial...) y las metemos juntas en un **módulo importable**.

**Lo que aporta el Tema 5**: estás construyendo **tu primera biblioteca**. Y aprendes el patrón profesional `if __name__ == "__main__":` para que el mismo archivo sirva como librería **Y** como programa ejecutable.

#### Empleando Python:

👉 Notebook explicado paso a paso: [matematicas_exp_py.ipynb](./matematicas_exp_py.ipynb).  
👉 El módulo creado: [matematicas.py](./matematicas.py).  
👉 Un programa principal que usa el módulo: [usa_matematicas.py](./usa_matematicas.py).

#### Empleando C:

👉 Notebook explicado paso a paso: [matematicas_exp_c.ipynb](./matematicas_exp_c.ipynb).  
👉 Archivo de cabecera con las declaraciones: [matematicas.h](./matematicas.h).  
👉 Archivo de implementación: [matematicas.c](./matematicas.c).  
👉 Un programa principal que usa el módulo: [usa_matematicas.c](./usa_matematicas.c).

### Ejemplo 4. Paquete con submódulos: `paq_matematicas/`

Cuando un módulo crece demasiado (80 funciones de áreas distintas), se vuelve inmanejable. La solución es **agrupar funciones temáticamente** en submódulos dentro de un paquete:

```text
paq_matematicas/
├── __init__.py
├── aritmetica/
│   ├── __init__.py
│   └── enteros.py          ← MCD, MCM, primos
└── geometria/
    ├── __init__.py
    └── plana.py            ← áreas y perímetros
```

Esta es **la estructura estándar** de todas las bibliotecas científicas que vas a usar como matemático: `numpy.linalg`, `numpy.random`, `scipy.optimize`, `scipy.integrate`... todas son **paquetes con submódulos**, igual que el que vas a construir aquí.

**Lo que aporta el Tema 5**: **organización jerárquica del código**. Es la estructura que escala a proyectos grandes.

#### Empleando Python:

👉 Notebook explicado paso a paso: [paquete_exp_py.ipynb](./paquete_exp_py.ipynb).  
👉 El paquete creado: [paq_matematicas/](./paq_matematicas.zip).  
👉 Un programa principal que usa el paquete: [usa_paquete.py](./usa_paquete.py).

### Ejemplo 5. Recursividad: cuando una función se llama a sí misma

Una función **recursiva** es una función que **se llama a sí misma**. Suena raro, pero es la forma más elegante de resolver muchos problemas matemáticos clásicos: factoriales, sucesiones definidas por recurrencia (Fibonacci), divide y vencerás...

En este ejemplo programamos el **factorial** y la **sucesión de Fibonacci** en dos versiones (recursiva e iterativa) y descubrirás algo sorprendente: para Fibonacci, la versión recursiva ingenua es **más de 100 000 veces más lenta** que la iterativa. Una lección que no se olvida.

**Lo que aporta el Tema 5**: aprendes a usar la recursión donde brilla (problemas con estructura recursiva natural) y a evitarla donde es un desastre (problemas con solapamiento masivo de subproblemas).

#### Empleando Python:

👉 Notebook explicado paso a paso: [recursividad_exp_py.ipynb](./recursividad_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar con una solución general: [recursividad.py](./recursividad.py).

#### Empleando C:

👉 Notebook explicado paso a paso: [recursividad_exp_c.ipynb](./recursividad_exp_c.ipynb).  
👉 Programa `.c` listo para compilar y ejecutar con una solución general: [recursividad.c](./recursividad.c).

### Ejemplo 6. Funciones como ciudadanos de primera clase

En Python, una función es **un valor más**: se puede asignar a una variable, pasar como argumento a otra función y devolver como resultado. Esta característica abre la puerta a un estilo de programación muy elegante.

En este ejemplo aprenderás:

* A **asignar** una función a una variable (alias).
* A **pasar una función como argumento** a otra (funciones de orden superior), construyendo una `integral_trapecio(f, a, b, n)` que integra **cualquier función** que le pases.
* A **definir funciones anónimas en una línea** con `lambda`.
* A **devolver funciones desde otras funciones** (closures).

**Lo que aporta el Tema 5**: la base para entender las **funciones de orden superior** (`map`, `filter`, `reduce`) que verás en el Tema 6, y el estilo funcional que utilizan muchas bibliotecas científicas.

> [!IMPORTANT]
> Estas características **no existen en C clásico** (sí en C++ moderno con lambdas y `std::function`, pero queda fuera de este curso). Por eso este ejemplo es **solo en Python**.

#### Empleando Python:

👉 Notebook explicado paso a paso: [primera_clase_exp_py.ipynb](./primera_clase_exp_py.ipynb).  
👉 Script `.py` listo para ejecutar con una solución general: [primera_clase.py](./primera_clase.py).

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T5_ICC.md)              |     10       |
| 2      | [Recursos](../recursos/T5_RE_ICC.md)       |      6       |
| 3      | **Ejemplos**                               |      -       |
| 4      | [Ejercicios](../ejercicios/T5_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
