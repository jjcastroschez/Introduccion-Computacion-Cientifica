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

# 🔨 Ejercicios Autocomprobación — Tema 4: Control del Flujo de Ejecución 🔀

En esta sección encontrarás ejercicios diseñados para que **interiorices las construcciones del Tema 4** (condicionales, bucles, anidamientos, excepciones) aplicándolas a problemas matemáticos clásicos y a la mejora de algunos de los programas que ya implementaste en el Tema 3.

En el [Tema 3](../../03_variables_tipos_simples/ejercicios/T3_Ejer_ICC.md) ya implementaste algoritmos **lineales** —donde las instrucciones se ejecutaban una tras otra, sin condiciones ni repeticiones—. Ahora ya has dado un salto cualitativo: tus programas **toman decisiones** y **repiten cálculos** las veces que haga falta, justo como hacen los algoritmos matemáticos clásicos (Euclides, criba de Eratóstenes, métodos iterativos…).

> [!WARNING]
> 👉 **Recuerda:** antes de programar **hay que pensar**. Para cada ejercicio te recomiendo seguir esta secuencia:
>
> 1. **Comprende el problema** matemáticamente. Asegúrate de entender la fórmula o el procedimiento.
> 2. **Diseña el algoritmo** en pseudocódigo, decidiendo qué condicionales y bucles necesitas.
> 3. **Dibuja el diagrama de flujo** (en papel basta).
> 4. **Implementa** la solución en Python o el lenguaje que decidas.
> 5. **Prueba** con varios casos, incluyendo los extremos (entrada cero, negativa, muy grande...).

> [!TIP]
> Las soluciones están **plegadas** dentro de bloques desplegables. Antes de mirarlas, **inténtalo tú**. Si te atascas, despliega solo lo necesario para desbloquearte. La programación se aprende programando 💪.

> [!NOTE]
> En este tema todavía **no se utilizan listas, tuplas, diccionarios ni se definen funciones propias** (esos contenidos se ven en los Temas 5 y 6). Todos los ejercicios se resuelven únicamente con **tipos simples** (`int`, `float`, `bool`) y las **construcciones del Tema 4**.

---

## 🟢 Bloque 1 — Condicionales (`if`, `if-elif-else`)

### 📝 Ejercicio 1: "Clasificando las raíces de una ecuación de segundo grado"

Dados los coeficientes $a$, $b$, $c$ de la ecuación $ax^2 + bx + c = 0$, queremos un programa que clasifique las raíces según el **discriminante** $\Delta = b^2 - 4ac$:

* Si $\Delta > 0$ → **dos raíces reales distintas**. Calcular ambas.
* Si $\Delta = 0$ → **una raíz real doble**. Calcular su valor.
* Si $\Delta < 0$ → **dos raíces complejas conjugadas**. Mostrar la parte real e imaginaria.

**Pseudocódigo orientativo:**

```text
ALGORITMO clasificar_raices_cuadratica
  Entrada: a, b, c (real)
  Salida: (texto descriptivo de las raíces)
INICIO
  1. ESCRIBIR "Dame los valores a, b, c de la ecuación:" 
  2. LEER(a, b, c)
  3. SI a == 0 ENTONCES
        (tratar como ecuación lineal)
     SINO
  4.    discriminante ← b² - 4·a·c
        SI discriminante > 0 ENTONCES
            ESCRIBIR "Dos raíces reales distintas..."
        SINO SI discriminante == 0 ENTONCES
            ESCRIBIR "Raíz real doble..."
        SINO
            ESCRIBIR "Raíces complejas conjugadas..."
        FINSI
     FINSI
FIN
```

#### ✔️ Tareas

1. Implementa la solución en Python (necesitarás `import math` para la raíz cuadrada).
2. Pruébala con: $x^2 - 5x + 6 = 0$ (raíces $2$ y $3$), $x^2 - 4x + 4 = 0$ (raíz doble $2$), $x^2 + x + 1 = 0$ (complejas).
3. **Bonus**: ¿qué pasa si el usuario introduce $a = 0$? La ecuación deja de ser de segundo grado: se convierte en una lineal $bx + c = 0$. Trata también este caso (y el caso aún más degenerado en que también $b = 0$).

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinitas soluciones (0 = 0).")
        else:
            print("Sin solución.")
    else:
        print(f"Ecuación lineal. Raíz única: x = {-c / b}")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante > 0:
        sqrt_d = math.sqrt(discriminante)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        print(f"Dos raíces reales distintas: x1 = {x1}, x2 = {x2}")
    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"Raíz real doble: x = {x}")
    else:
        parte_real = -b / (2 * a)
        parte_imag = math.sqrt(-discriminante) / (2 * a)
        print(f"Raíces complejas conjugadas: {parte_real} ± {parte_imag}i")
```

📁 [Solución completa en Python](./raices_cuadratica.py)

</details>

---

### 📝 Ejercicio 2: "Mejorando el cálculo de la nota con clasificación"

En el [Tema 3](../../03_variables_tipos_simples/ejercicios/T3_Ejer_ICC.md) ya implementaste un programa que calculaba la nota final del estudiante como media ponderada de tres pruebas. Pero el programa **solo decía el número** — no clasificaba al estudiante. Vamos a corregirlo.

Diseña un programa que:

1. Pida las tres calificaciones (cada una sobre 10).
2. Calcule la **nota final** como $\,0.30 \cdot c_1 + 0.40 \cdot c_2 + 0.30 \cdot c_3$.
3. Clasifique al estudiante según los **criterios académicos estándar**:

| Nota | Clasificación |
| :---: | :--- |
| $< 5$ | Suspenso |
| $[5, 7)$ | Aprobado |
| $[7, 9)$ | Notable |
| $[9, 9.5)$ | Sobresaliente |
| $\geq 9.5$ | Matrícula de honor |

#### ✔️ Tareas

1. Implementa la solución usando `if-elif-else`.
2. Pruébala con $(5, 8, 9)$ → debe dar Notable (7.40), $(3, 4, 4)$ → Suspenso (3.70), $(10, 10, 10)$ → Matrícula (10.00).
3. **Reflexión**: ¿qué pasaría si el orden de los `elif` fuera el opuesto (empezando por la matrícula)? ¿Funcionaría igual? Pruébalo y razónalo.
4. **Sentencia match-case**: ¿puedes emplear esta construcción en este problema? 

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
calif1 = float(input("Calificación de la primera prueba (sobre 10): "))
calif2 = float(input("Calificación de la segunda prueba (sobre 10): "))
calif3 = float(input("Calificación de la tercera prueba (sobre 10): "))

nota = calif1 * 0.30 + calif2 * 0.40 + calif3 * 0.30

print(f"Nota obtenida: {nota:.2f}")

if nota < 5:
    clasificacion = "Suspenso"
elif nota < 7:
    clasificacion = "Aprobado"
elif nota < 9:
    clasificacion = "Notable"
elif nota < 9.5:
    clasificacion = "Sobresaliente"
else:
    clasificacion = "Matrícula de honor"

print(f"Clasificación: {clasificacion}")
```

📁 [Solución completa en Python](./calculo_nota.py)

Veamos ahora como quedaría con la sentencia `match-case`:

```python
calif1 = float(input("Calificación de la primera prueba (sobre 10): "))
calif2 = float(input("Calificación de la segunda prueba (sobre 10): "))
calif3 = float(input("Calificación de la tercera prueba (sobre 10): "))

nota = calif1 * 0.30 + calif2 * 0.40 + calif3 * 0.30

print(f"Nota obtenida: {nota:.2f}")

match nota:
    case _ if nota < 5:
        clasificacion = "Suspenso"
    case _ if nota < 7:
        clasificacion = "Aprobado"
    case _ if nota < 9:
        clasificacion = "Notable"
    case _ if nota < 9.5:
        clasificacion = "Sobresaliente"
    case _:
        clasificacion = "Matrícula de honor"

print(f"Clasificación: {clasificacion}")
```

> [!WARNING]
> La sentencia `case` no evalúa condiciones booleanas (verdadero/falso) directamente, sino que hace coincidencia de patrones (pattern matching). Es decir, no podemos hacer `case nota < 5`. Con **guardas** (if dentro del case), si podemos hacerlo. 
> 🤯 **¿Qué está pasando aquí?**
>    * El guión bajo (case _): En el mundo del pattern matching, el guión bajo es un comodín. Significa "coincide con cualquier cosa que venga de match nota".
>    * La guarda (if ...): Al añadir el if, le dices a Python: "Vale, coincide con cualquier nota, pero solo si se cumple esta condición extra".
>    * El case _ final: Es el caso por defecto; si ninguna de las condiciones anteriores se cumple, entrará ahí.

📁 [Solución completa en Python](./calculo_nota_match.py)

</details>



---

## 🟡 Bloque 2 — Bucle `for`

### 📝 Ejercicio 3: "Aproximando $\pi$ por la serie de Leibniz"

Una de las series infinitas más famosas de la historia de las matemáticas es la **fórmula de Leibniz** (1676):

$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}$$

Diseña un programa que, dado un entero $N$, calcule la **aproximación de $\pi$** que se obtiene sumando los $N$ primeros términos de la serie y la compare con el valor real (`math.pi`).

> 💡 **Pista**: el signo $(-1)^k$ va alternando $+1, -1, +1, -1, \ldots$ Puedes calcularlo con `(-1) ** k`, o más eficientemente usando una variable `signo` que multipliques por $-1$ en cada vuelta del bucle.

#### ✔️ Tareas

1. Implementa la solución usando un bucle `for` y una variable acumuladora.
2. Pruébala con $N = 10, 100, 1000, 10000$. Observa cómo el error decrece, pero **muy lentamente**.
3. ¿Cuántos términos hacen falta para que el error sea menor que $10^{-2}$? Esta lenta convergencia es un resultado conocido en Análisis Numérico.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

n = int(input("Número de términos a sumar: "))

suma = 0.0
signo = 1   # alternará +1, -1, +1, -1...
for k in range(n):
    denominador = 2 * k + 1
    suma = suma + signo / denominador
    signo = -signo

pi_aprox = suma * 4
error = abs(pi_aprox - math.pi)

print(f"π aproximado con {n} términos: {pi_aprox:.10f}")
print(f"π real:                       {math.pi:.10f}")
print(f"Error absoluto:               {error:.2e}")
```

📁 [Solución completa en Python](./pi_leibniz.py)

</details>

---

### 📝 Ejercicio 4: "Factorial y fórmula de Stirling"

El **factorial** de un entero positivo se define como $n! = 1 \cdot 2 \cdot 3 \cdots n$. Para valores grandes de $n$, $n!$ crece tan rápido que en muchas aplicaciones se sustituye por la **fórmula de Stirling**, una aproximación asintótica:

$$n! \approx \sqrt{2 \pi n} \cdot \left(\frac{n}{e}\right)^n$$

Diseña un programa que:

1. Calcule $n!$ usando un bucle `for` (acumulador multiplicativo).
2. Calcule la aproximación de Stirling.
3. Muestre el **error relativo** entre ambos: $\dfrac{|n! - \text{Stirling}|}{n!} \cdot 100$ (%).

#### ✔️ Tareas

1. Implementa la solución.
2. Pruébala con $n = 5, 10, 20, 50$. Verás que el error relativo decrece a medida que $n$ aumenta.
3. **Reflexión**: con $n = 5$ el error es ~2%; con $n = 50$ es ~0.2%. Es decir, la fórmula es mejor cuando $n$ es grande. ¿Por qué es importante esto desde el punto de vista práctico?

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

n = int(input("Calcular n! para n = "))

# Cálculo exacto con bucle for (acumulador multiplicativo)
factorial = 1
for i in range(2, n + 1):
    factorial = factorial * i

# Aproximación de Stirling
stirling = math.sqrt(2 * math.pi * n) * (n / math.e) ** n

# Error relativo
error_relativo = abs(factorial - stirling) / factorial * 100

print(f"{n}! exacto:               {factorial}")
print(f"Aproximación de Stirling: {stirling:.4e}")
print(f"Error relativo:           {error_relativo:.4f} %")
```

📁 [Solución completa en Python](./factorial_stirling.py)

</details>

---

## 🟠 Bloque 3 — Bucle `while`

### 📝 Ejercicio 5: "Raíz cuadrada por el método babilónico"

Implementaremos uno de los **algoritmos iterativos más antiguos** que se conocen (más de 2 000 años). Dada una estimación inicial $x_0$, refinamos sucesivamente:

$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)$$

En menos de 10 iteraciones tendrás precisión de 15 decimales. Es el patrón fundamental de los métodos numéricos: **iterar hasta converger**.

#### ✔️ Tareas

1. Implementa el método con un bucle `while` cuya condición de parada sea $|x_{n+1} - x_n| < \varepsilon$ (tolerancia, por ejemplo $10^{-12}$).
2. Añade un **límite máximo de iteraciones** como red de seguridad (por ejemplo, 100).
3. Trata el caso $a < 0$ con un `if` previo (no existe raíz real).
4. **Bonus**: ¿en cuántas iteraciones converge para $a = 2$? ¿Y para $a = 1\,000\,000$? ¿Cuánto influye el valor inicial?

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

a = float(input("Calcular la raíz cuadrada de: "))

if a < 0:
    print("⚠️ No existe raíz real de un número negativo.")
elif a == 0:
    print("√0 = 0")
else:
    TOLERANCIA = 1e-12
    MAX_ITER = 100

    x = a / 2
    iteracion = 0
    diferencia = TOLERANCIA + 1   # para entrar al bucle al menos una vez

    while diferencia > TOLERANCIA and iteracion < MAX_ITER:
        x_nuevo = 0.5 * (x + a / x)
        diferencia = abs(x_nuevo - x)
        x = x_nuevo
        iteracion = iteracion + 1

    print(f"√{a} ≈ {x:.15f}")
    print(f"Resultado de math.sqrt:  {math.sqrt(a):.15f}")
    print(f"Iteraciones empleadas: {iteracion}")
```

📁 [Solución completa en Python](./raiz_babilonica.py)

</details>

---

### 📝 Ejercicio 6: "Conjetura de Collatz (3n+1)"

La **conjetura de Collatz** afirma que la siguiente sucesión, partiendo de cualquier entero positivo, **siempre acaba llegando a 1**:

$$a_{n+1} = \begin{cases} a_n / 2 & \text{si } a_n \text{ es par} \\ 3 a_n + 1 & \text{si } a_n \text{ es impar} \end{cases}$$

Por ejemplo, partiendo de 6: $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$ (8 pasos).

**Nadie ha demostrado todavía** si la conjetura es cierta para todos los números, aunque se ha verificado computacionalmente para los primeros $10^{20}$ valores.

#### ✔️ Tareas

1. Implementa un programa que, dado un entero positivo $n$, vaya **mostrando la sucesión por pantalla** (usa `print(..., end="")` para mantenerlo en una sola línea con flechas) y cuente cuántos pasos tarda en llegar a 1.
2. Protege la entrada con `try-except` para que el programa no se rompa si el usuario teclea algo raro.
3. Prueba con $n = 6, 27, 100$. Verás que $27$ tarda **111 pasos** (¡es famosamente largo para su tamaño!).

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
while True:
    try:
        n = int(input("Entero positivo: "))
        if n <= 0:
            print("⚠️ Debe ser positivo.")
            continue
        break
    except ValueError:
        print("⚠️ Eso no es un entero válido.")

n_original = n
pasos = 0

print(f"Sucesión partiendo de {n}: ", end="")
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    pasos = pasos + 1
    print(f" → {n}", end="")

print(f"\n\nPartiendo de {n_original}, llegamos a 1 en {pasos} pasos.")
```

📁 [Solución completa en Python](./collatz.py)

</details>

---

## 🔵 Bloque 4 — Bucles anidados

### 📝 Ejercicio 7: "Récord de Collatz en el rango [1, N]"

Amplía el ejercicio 6: queremos encontrar, dentro del rango $[1, N]$, **cuál es el entero que tarda más pasos** en llegar a 1. Llamaremos a este número el **récord de Collatz** de $[1, N]$.

> 💡 **Pista pedagógica**: aquí necesitas combinar **dos bucles anidados**:
>
> * Un bucle externo `for` que recorra cada $\text{inicio}$ entre 1 y $N$.
> * Un bucle interno `while` que aplique la sucesión a $\text{inicio}$ hasta llegar a 1, contando los pasos.
>
> Y necesitas **dos variables simples** para guardar el mejor encontrado hasta el momento (`mejor_numero` y `max_pasos`), que vas actualizando dentro del `for` externo cuando encuentres uno mejor. **¡Sin listas, no las necesitas!**

#### ✔️ Tareas

1. Implementa el algoritmo.
2. Pruébalo con $N = 10, 100, 1000$. Para $N = 100$ el récord es $97$ (118 pasos); para $N = 1000$ es $871$ (178 pasos).
3. **Reflexión sobre el coste**: cada $\text{inicio}$ requiere ejecutar el bucle de Collatz hasta llegar a 1. ¿Por qué tarda tanto el programa para $N = 100\,000$? Esto te dará una primera intuición sobre la **complejidad computacional** de los algoritmos anidados.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
n_max = int(input("Buscar el récord entre 1 y N. Introduce N: "))

# Variables simples para guardar el mejor (sin usar listas)
mejor_numero = 1
max_pasos = 0

for inicio in range(1, n_max + 1):
    # Bucle interno: aplicamos Collatz al número 'inicio'
    n = inicio
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos = pasos + 1

    # ¿Es este el nuevo récord?
    if pasos > max_pasos:
        max_pasos = pasos
        mejor_numero = inicio

print(f"Del 1 al {n_max}, el número con más pasos es {mejor_numero} ({max_pasos} pasos).")
```

📁 [Solución completa en Python](./collatz_record.py)

</details>

---

### 📝 Ejercicio 8: "Imprimir la tabla pitagórica"

Diseña un programa que imprima la **tabla pitagórica** de $N \times N$, es decir, la tabla con todos los productos $i \cdot j$ para $i, j \in [1, N]$. La salida debe parecerse a esto (para $N = 5$):

```text
    |   1   2   3   4   5
-------------------------
  1 |   1   2   3   4   5
  2 |   2   4   6   8  10
  3 |   3   6   9  12  15
  4 |   4   8  12  16  20
  5 |   5  10  15  20  25
```

> 💡 **Pista**: usa `print(..., end="")` para imprimir varios valores **en la misma línea** y un `print()` vacío para saltar de línea al acabar cada fila. Y usa los formateadores de cadena (`f"{x:4}"` reserva 4 espacios) para alinearlo bonito.

#### ✔️ Tareas

1. Implementa la solución con dos bucles `for` anidados.
2. Añade la cabecera (los números de columna) y la línea separadora.
3. **Bonus**: modifica el programa para que solo imprima los productos del **triángulo superior** (es decir, los del tipo $i \cdot j$ con $j \geq i$). ¿Cómo logras que se vean bien alineados?

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
n = int(input("Tamaño de la tabla pitagórica: "))

# Cabecera
print("    |", end="")
for j in range(1, n + 1):
    print(f"{j:4}", end="")
print()
print("-" * (5 + 4 * n))

# Cuerpo
for i in range(1, n + 1):
    print(f"{i:3} |", end="")
    for j in range(1, n + 1):
        print(f"{i*j:4}", end="")
    print()
```

📁 [Solución completa en Python](./tabla_pitagorica.py)

</details>

---

## 🔴 Bloque 5 — Manejo de excepciones

### 📝 Ejercicio 9: "Validación robusta del cambio de moneda"

En el [Tema 3](../../03_variables_tipos_simples/ejercicios/T3_Ejer_ICC.md) implementaste el cálculo de cambio de moneda. Si te fijaste, ese programa **se rompe** si el usuario teclea cualquier cosa que no sea un número. También daría resultados absurdos si el porcentaje del banco fuera negativo o mayor que 100.

Vamos a aplicar lo aprendido sobre **validación robusta** (Ejemplo 4 de este tema): cada llamada a `input()` debe ir envuelta en un bucle `while True` con `try-except` que vuelva a pedir el dato hasta que sea correcto.

#### ✔️ Tareas

1. Recupera tu programa del Tema 3 (o vuelve a empezar).
2. Para cada dato de entrada, asegúrate de que:
   - La conversión a número es correcta (captura `ValueError`).
   - El valor cumple las restricciones lógicas (positivo, en rango...).
3. Cuando todo sea válido, calcula y muestra el resultado **como en el Tema 3**.
4. **Reflexión**: ¿cuántas líneas extra has tenido que añadir? ¿Te parece que vale la pena? Cuando trabajes en proyectos reales, verás que este código de validación es habitual y, una vez aprendido el patrón, se escribe casi automáticamente.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
# --- Conversión de la moneda extranjera a dólares ---
while True:
    try:
        conv_moneda_dolares = float(input(
            "Valor de conversión de la moneda extranjera a dólares: "
        ))
        if conv_moneda_dolares <= 0:
            print("  ⚠️ Debe ser un valor positivo.")
            continue
        break
    except ValueError:
        print("  ⚠️ Debe ser un número.")

# --- Conversión del euro a dólares ---
while True:
    try:
        conv_euros_dolares = float(input("Valor de conversión del euro a dólares: "))
        if conv_euros_dolares <= 0:
            print("  ⚠️ Debe ser un valor positivo.")
            continue
        break
    except ValueError:
        print("  ⚠️ Debe ser un número.")

# --- Cantidad de moneda extranjera ---
while True:
    try:
        cantidad_moneda_extranj = int(input("Cantidad de moneda extranjera a cambiar: "))
        if cantidad_moneda_extranj <= 0:
            print("  ⚠️ Debe ser un entero positivo.")
            continue
        break
    except ValueError:
        print("  ⚠️ Debe ser un entero.")

# --- Porcentaje de ganancia del banco ---
while True:
    try:
        porc_ganancia_banco = float(input("Porcentaje de ganancia del banco (0-100): "))
        if porc_ganancia_banco < 0 or porc_ganancia_banco > 100:
            print("  ⚠️ Debe estar entre 0 y 100.")
            continue
        break
    except ValueError:
        print("  ⚠️ Debe ser un número.")

# --- Cálculos (igual que en el Tema 3) ---
cantidad_en_dolares = cantidad_moneda_extranj * conv_moneda_dolares
cantidad_en_euros = cantidad_en_dolares / conv_euros_dolares
cantidad_por_comision = cantidad_en_euros * porc_ganancia_banco / 100
cantidad_cambio_entrega = cantidad_en_euros - cantidad_por_comision

print(f"\nLa cantidad a entregar al cliente es: {cantidad_cambio_entrega:.2f} €")
```

📁 [Solución completa en Python](./cambio_moneda.py)

</details>

---

## 🎯 Reto final (sin solución publicada)

### 📝 Ejercicio reto: "Aproximación del número $e$ por la serie de Taylor"

La constante de Euler $e$ se puede definir como la suma de la serie:

$$e = \sum_{n=0}^{\infty} \frac{1}{n!} = 1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \cdots$$

Diseña un programa que aproxime $e$ sumando términos **hasta que el último término sumado sea menor que una tolerancia $\varepsilon$ dada por el usuario** (por ejemplo, $\varepsilon = 10^{-10}$).

> 💡 **Pista de implementación**: no calcules cada factorial desde cero — sería terriblemente ineficiente. Aprovecha la relación recurrente entre dos términos consecutivos:
>
> $$ \text{termino}_{n+1} = \text{termino}_n \cdot \frac{1}{n+1} $$
>
> Es decir, **multiplica el término anterior por $1/(n+1)$** para obtener el siguiente. Con una sola variable acumuladora, sin definir funciones, sin listas.

#### ✔️ Tareas

1. Implementa el método con un bucle `while` cuyo criterio de parada sea **que el último término sea menor que $\varepsilon$**.
2. Añade un máximo de iteraciones como red de seguridad.
3. Muestra cuántos términos han hecho falta para alcanzar la tolerancia.
4. **Compara** tu resultado con `math.e` y calcula el error.
5. ¿Cuántos términos hacen falta para tener precisión de $10^{-10}$? Pista: con la serie de Taylor de $e$, **muchos menos** que con la serie de Leibniz para $\pi$. ¿Por qué?

> [!IMPORTANT]
> Este ejercicio **no tiene solución publicada**. Es un buen ejercicio de fin de tema para autoevaluarte: si lo resuelves sin mirar nada, has interiorizado bien los conceptos. Si te atascas, vuelve a los ejercicios 3 (Leibniz, también es una serie infinita) y 5 (criterio de convergencia con tolerancia).

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T4_ICC.md)              |      8       |
| 2      | [Recursos](../recursos/T4_RE_ICC.md)       |      5       |
| 3      | [Ejemplos](../ejemplos/T4_Ejem_ICC.md)     |      -       |
| 4      | **Ejercicios**                             |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
