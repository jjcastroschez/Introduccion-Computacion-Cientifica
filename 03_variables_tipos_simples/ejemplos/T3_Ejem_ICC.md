
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

En esta carpeta encontrarás enlaces a algunos documentos Notebooks de Jupyter preparados para mostrarte problemas solucionados simplemente usando variables de tipos simples, operaciones y expresiones de asignación.

> [!NOTE]
> Aún no se emplean estructuras más complejas (p.e. `if`, `while`, `for`) que se estudiarán en clase con detalle en el **Tema 4**.  
> En este tema el objetivo es que hagas tus primeros programas simples, hay muchas cosas que puedes hacer tan solo con lo que has visto en clase. Aquí tienes varios ejemplos. Espero que sean de utilidad para coger ideas para tus trabajos.

## Contenido

Existe un problema que se repite en muchos campos (medicina y farmacología, finanzas,...) y para el que desde el campo de las matemáticas le han dado solución ofreciéndole una fórmula, ahora desde el campo de la computación científica le vas a dar un programa para que puedan usarlo y hacer los cálculos pertinentes.

###  Ejemplo 1. Medicina y Farmacología: Acumulación de fármacos

Cuando un paciente toma un medicamento, su cuerpo elimina un porcentaje constante (por ejemplo, el 20%) cada día.

El problema: Si toma una dosis diaria **a**, ¿cuánta medicina habrá en su cuerpo a largo plazo máximo?

La serie: Cada dosis nueva se suma a lo que queda de las anteriores (que se han multiplicado por r=0.8).

Aplicación: La convergencia de esta serie le dice al médico cuál es el "nivel de estado estacionario", es decir, el punto donde dejas de acumular fármaco y el nivel se estabiliza para no ser tóxico.

👉 Aquí tienes la solución explicada en un Notebook de Jupyter [farmacologia.ipynb](./farmacologia.ipynb). 
👉 Aquí tienes la explicación de la solución con detalles de la implementación. [farmacologia_icc.ipynb](./farmacologia_icc.ipynb). 
👉 Aquí tienes el script con la implementación de la solución empleando el lenguaje de programación Python [farmacologia_icc.py](./farmacologia_icc.py). 

> [!TIP]
> Descárga los archivos anteriores, examínalos y ejecútalos. Decide para cada uno de ellos cuál es la herramienta que necesitas 😜.  


###  Ejemplo 2. Finanzas: El valor del dinero en el tiempo

Un banco te ha prometido pagar 100€ cada año para siempre, ese dinero del futuro vale menos hoy debido a la inflación y al coste de oportunidad.

El problema: Calcular el valor presente de una anualidad o una renta perpetua.

La serie: El "primer término" a es el pago inicial, y la "razón" r es el factor de descuento (basado en el tipo de interés).

Aplicación: Saber cuánto vale hoy un fondo de pensiones o un préstamo.

👉 Aquí tienes la solución explicada en un Notebook de Jupyter 😜. 

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo       | 
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T2_ICC.md)              |      6       |
| 2      | [Recursos](../recursos/T2_RE_ICC.md)       |      5       |
| 3      | **Ejemplos**                               |      -       |
| 4      | [Ejercicios](../ejercicios/T2_Ejer_ICC.md) |      -       |
|        | [Menu del Tema actual](../README.md)       |      -       |