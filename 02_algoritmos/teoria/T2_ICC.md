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

# Teoría - Tema 2: Algoritmia 🧠

En este tema nos centramos en el *diseño de la solución* (el algoritmo), antes de preocuparnos por cómo escribirla en un lenguaje de programación.

> [!IMPORTANT]
> **No corras.** Antes de programar, diseña la solución. Es más barato corregir un algoritmo mal planteado que depurar un programa caótico.

---

## 🧩 Sección 1: ¿Qué es un algoritmo?

Un **algoritmo** es una secuencia **clara y ordenada** de pasos o instrucciones que se siguen para resolver un problema o realizar una tarea específica.

### 📥 Entradas, intermedios y salidas
Un algoritmo:
- parte de **cero o más datos de entrada** (información proporcionada),
- puede construir **datos intermedios** (variables auxiliares),
- y produce **al menos una salida** (resultado).

Cada paso del algoritmo debe ser un paso *hacia la solución*.

### 🍳 Analogía rápida: receta de cocina
Si quieres explicar una receta, el algoritmo sería la lista de instrucciones:

1. Lavar ingredientes  
2. Cortar verduras  
3. Calentar sartén  
4. Cocinar durante X minutos  
5. Servir  

Los datos de entrada serían los ingredientes que vamos a usar para elaborar la receta (p.e. 2 tomates, 1 cebolla, 1 pimiento rojo), los datos intermedios serían los productos intermedios que se producen (p.e. el sofrito), y los datos de salida serían el plato ya elaborado. 

> [!NOTE]
> El orden importa. Si “calientas la sartén” después de “cocinar”, algo no encaja.

---

## ✅ Sección 2: Características de un buen algoritmo

Un buen algoritmo debe ser:

- **Preciso**: sin ambigüedades, se interpreta siempre igual.  
- **Robusto**: no contiene errores lógicos evidentes (y contempla casos razonables).  
- **Definido**: para la misma entrada, produce la misma salida (determinismo).  
- **Ordenado**: deja claro el orden de ejecución de los pasos.  
- **Finito**: termina en algún momento (no se queda en un bucle “eterno”).  
- **Independiente**: no depende de un lenguaje concreto (no uses `print`, `scanf`, etc. en el algoritmo).  
- **Legible**: comprensible para otra persona (o para tu “yo” del futuro, puede que tengas que mantenerlo 😜).

> [!TIP]
> Si un algoritmo no es legible, es *difícil de validar* y *difícil de mantener*.

---

## 🎸 Sección 3: No hay una única solución

Distintos algoritmos pueden resolver el mismo problema.

La pregunta entonces es: **¿cuál elegir?**  
Normalmente, buscamos el más eficiente (en **tiempo** y **memoria**) *sin perder claridad*.

### Ejemplo rápido: suma 1..n
- Algoritmo A: sumar valor a valor hasta alcanzar n (tiempo dependiente de n, se realizan n sumas).
- Algoritmo B: usar la fórmula de Gauss $\frac{n(n+1)}{2}$ (tiempo constante).

> [!NOTE]
> En este curso introduciremos la eficiencia de forma gradual. Lo importante aquí es interiorizar que *dos soluciones correctas* pueden tener costes muy distintos.

---

## 🧩 Sección 4: Elementos de un algoritmo (programación estructurada)

Según el **teorema de la programación estructurada**, cualquier programa puede escribirse utilizando solo tres estructuras de control:

1. **Secuencia**: instrucciones que se ejecutan una vez, en orden.
2. **Selección**: ejecutar o no ejecutar instrucciones en función de una condición.
3. **Iteración**: repetir instrucciones un número variable de veces.

> [!IMPORTANT]
> Simplemente combinando estas tres estructuras, es posible expresar cualquier función computable.

---

## 🧾 Sección 5: ¿Cómo se expresan los algoritmos?

Un algoritmo se puede expresar de muchas formas:

- **Lenguaje natural** (útil, pero puede ser ambiguo).
- **Pseudocódigo** (muy usado en docencia y diseño).
- **Diagramas de flujo** (gráficos y muy intuitivos).
- Otras: diagramas Nassi–Shneiderman, notaciones formales, UML (diagramas de actividad), etc.

La elección depende del **contexto**, el **público objetivo** y el **propósito**.

---

## 🔠 Sección 6: Pseudocódigo

El pseudocódigo busca un equilibrio: estructura parecida a un programa, pero **sin depender** de un lenguaje.

### 📌 Plantilla recomendada
```text
Algoritmo NOMBRE_ALGORITMO
Entrada: ...
Intermedias: ...
Salida: ...
Inicio
  1: ...
  2: ...
  ...
  n: ...
Fin
```

Ahora veamos dos ejemplos:

### 🧮 Ejemplo: área de un círculo
```text
Algoritmo CalculoAreaCirculo
Entrada: radio (número real), pi (número real)
Intermedias: -
Salida: area (número real)
Inicio
  1: Escribir "Introduce el valor del radio del círculo:"
  2: Leer(radio)
  3: Escribir "Introduce el valor de pi:"
  4: Leer(pi)
  5: area ← pi * radio * radio
  6: Escribir "El área del círculo es:", area
Fin
```
### 🧮 Ejemplo: media aritmética de dos números
```text
Algoritmo CalculoMediaDosNumeros
Entrada: a (número real), b (número real)
Intermedias: suma (número real)
Salida: media (número real)
Inicio
  1: Escribir "Introduce el primer número:"
  2: Leer(a)
  3: Escribir "Introduce el segundo número:"
  4: Leer(b)
  5: suma ← a + b
  6: media ← suma / 2
  7: Escribir "La media de los dos números es:", media
Fin
```

> [!TIP]
> Aunque el pseudocódigo incluya “Leer/Escribir”, piensa en ello como *abstracciones* de entrada/salida, no como funciones concretas de un lenguaje.

---

## 📊 Sección 7: Diagramas de flujo

Los **diagramas de flujo** representan un algoritmo gráficamente mediante **símbolos** estándar y flechas de flujo.

Son populares para:
- representar algoritmos,
- documentar procesos,
- visualizar decisiones y ramificaciones,
- mejorar sistemas (procesos administrativos, industriales, etc.).

### 🔷 Símbolos habituales
- **Terminal**: inicio/fin.
- **Entrada/Salida**: leer o mostrar información.
- **Proceso**: operación/cálculo/asignación.
- **Decisión**: bifurcación (sí/no).
- **Conectores**: unión dentro/fuera de página.
- **Operación manual**: intervención humana.
- **Flechas**: dirección del flujo.

### ✅ Restricciones recomendadas (para diagramas claros)
- Un solo **inicio** y un solo **fin**.
- Construcción **top-down** (arriba→abajo) y **left-to-right** (izquierda→derecha).
- Usar líneas rectas.
- A cada símbolo le llega solo una línea de flujo (salvo excepciones bien justificadas).
- Notación **independiente** del lenguaje final.

Veamos dos ejemplos simples, para representar los algoritmos anteriores:

### 🧮 Ejemplo: área de un círculo
```mermaid
flowchart TD    
    A([Inicio]) --> B[/Escribir: "Introduce el valor del radio del círculo:"/]
    B --> C[/"Leer(radio)"/]    
    C --> D[/Escribir: "Introduce el valor de pi:"/]    
    D --> E[/"Leer(pi)"/]    
    E --> F[area ← pi * radio * radio]    
    F --> G[/Escribir: "El área del círculo es:", area/]    
    G --> H([Fin])
```
### 🧮 Ejemplo: media aritmética de dos números
```mermaid
flowchart TD
    A([Inicio]) --> B[/Escribir: "Introduce el primer número:"/]
    B --> C[/"Leer(a)"/]
    C --> D[/Escribir: "Introduce el segundo número:"/]
    D --> E[/"Leer(b)"/]
    E --> F[suma ← a + b]
    F --> G[media ← suma / 2]
    G --> H[/Escribir: "La media de los dos números es:", media/]
    H --> I([Fin])
```
---

## 🧭 Sección 8: Recordatorio importante: del problema al programa

El fujo de trabajo habitual será:

1. **Análisis del problema**: datos de entrada, salida esperada, casos especiales, restricciones.
2. **Diseño del algoritmo**: redacta el algoritmo y verifica sus propiedades.
3. **Selección del lenguaje**: elige el lenguaje y herramientas más apropiados.
4. **Implementación**: traduce el algoritmo al lenguaje elegido.

---

## ✅ Mini-checklist de autoevaluación

Antes de dar por bueno tu algoritmo, comprueba:

- [ ] ¿Has identificado claramente **entrada**, **intermedios** y **salida**?
- [ ] ¿Los pasos están en orden y **sin ambigüedad**?
- [ ] ¿Hay un punto de entrada y otro de salida?
- [ ] ¿El algoritmo **termina** siempre?
- [ ] ¿La representación es **independiente** del lenguaje?
- [ ] ¿Otra persona podría entenderlo sin preguntarme?

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo       | 
|:------:|:-------------------------------------------|:------------:|
| 1      | **Teoría**                                 |      6       |
| 2      | [Recursos](../recursos/T2_RE_ICC.md)       |      5       |
| 3      | [Ejemplos](../ejemplos/T2_Ejem_ICC.md)     |      -       |
| 4      | [Ejercicios](../ejercicios/T2_Ejer_ICC.md) |      -       |
|        | [Menu del Tema actual](../README.md)       |      -       |
