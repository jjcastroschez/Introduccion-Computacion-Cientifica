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

En esta sección encontrarás ejercicios pensados para que **interiorices las construcciones del Tema 4** (condicionales, bucles, anidamientos, excepciones) aplicándolas a problemas que ya conoces de tus asignaturas de **Cálculo, Álgebra y Análisis Numérico**.

En el [Tema 3](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/03_variables_tipos_simples/ejercicios/T3_Ejer_ICC.md) implementaste algoritmos lineales —donde las instrucciones se ejecutaban una tras otra, sin condiciones ni repeticiones—. Ahora vas a dar un salto cualitativo: **tus programas tomarán decisiones y repetirán cálculos**, justo como hacen los algoritmos matemáticos clásicos (Euclides, criba de Eratóstenes, Newton-Raphson…).

> [!WARNING]
> 👉 **Recuerda:** antes de programar **hay que pensar**. Para cada ejercicio te recomiendo seguir esta secuencia:
>
> 1. **Comprende el problema** matemáticamente. Asegúrate de entender la fórmula o el procedimiento.
> 2. **Diseña el algoritmo** en pseudocódigo, decidiendo qué condicionales y bucles necesitas.
> 3. **Dibuja el diagrama de flujo** (en papel basta).
> 4. **Implementa** la solución en Python.
> 5. **Prueba** con varios casos, incluyendo los extremos (entrada cero, negativa, muy grande...).

> [!TIP]
> Las soluciones están **plegadas** dentro de bloques desplegables. Antes de mirar mi solución, **inténtalo tú**. Si te atascas, mira solo lo necesario para desbloquearte. La programación se aprende programando 💪.

---

## 🟢 Bloque 1 — Condicionales (`if`, `if-elif-else`)

### 📝 Ejercicio 1.1: Clasificación de un triángulo

**Enunciado.** Dados tres números reales $a$, $b$, $c$ que representan las longitudes de los lados de un triángulo, escribe un programa que:

1. Compruebe si **forman un triángulo válido** (recuerda la **desigualdad triangular**: la suma de dos lados cualesquiera ha de ser mayor que el tercero).
2. Si lo es, lo clasifique como **equilátero** (3 lados iguales), **isósceles** (2 iguales) o **escaleno** (todos distintos).

**Pseudocódigo orientativo:**

```text
ALGORITMO clasificar_triangulo
  Entrada: a, b, c (real)
  Salida: tipo_triangulo (texto)

INICIO
  1. LEER(a, b, c)
  2. SI no se cumple la desigualdad triangular ENTONCES
        ESCRIBIR "No es un triángulo válido"
     SINO
  3.    SI a == b Y b == c ENTONCES
            ESCRIBIR "Equilátero"
        SINO SI a == b O b == c O a == c ENTONCES
            ESCRIBIR "Isósceles"
        SINO
            ESCRIBIR "Escaleno"
        FINSI
     FINSI
FIN
```

#### ✔️ Tareas

1. Implementa la solución en Python.
2. Pruébala con: `(3, 3, 3)`, `(3, 4, 5)`, `(5, 5, 8)`, `(1, 2, 5)` (este último **no** es triángulo).
3. **Bonus matemático**: amplía el programa para que indique también si el triángulo es **rectángulo** (Teorema de Pitágoras: $a^2 + b^2 = c^2$, salvo permutación de los lados). ⚠️ Cuidado con la comparación de `float`: usa una tolerancia.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

# Comprobar desigualdad triangular
if a + b <= c or a + c <= b or b + c <= a:
    print("No es un triángulo válido.")
elif a == b == c:
    print("Equilátero")
elif a == b or b == c or a == c:
    print("Isósceles")
else:
    print("Escaleno")

# Bonus: ¿es rectángulo?
TOL = 1e-9
lados = sorted([a, b, c])  # los ordenamos para que c sea el mayor
if abs(lados[0]**2 + lados[1]**2 - lados[2]**2) < TOL:
    print("Además, es un triángulo rectángulo.")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/clasificar_triangulo.py)

</details>

---

### 📝 Ejercicio 1.2: Clasificación de las raíces de una ecuación de 2.º grado

**Enunciado.** Dados los coeficientes $a$, $b$, $c$ de la ecuación $ax^2 + bx + c = 0$ (con $a \neq 0$), escribe un programa que clasifique sus raíces en función del **discriminante** $\Delta = b^2 - 4ac$:

* Si $\Delta > 0$ → dos **raíces reales distintas** y calcula ambas.
* Si $\Delta = 0$ → una **raíz real doble** y calcula su valor.
* Si $\Delta < 0$ → dos **raíces complejas conjugadas** y muestra su parte real e imaginaria.

#### ✔️ Tareas

1. Implementa la solución en Python.
2. Pruébala con: $x^2 - 5x + 6 = 0$, $x^2 - 4x + 4 = 0$, $x^2 + x + 1 = 0$.
3. **Bonus**: ¿qué pasa si el usuario introduce $a = 0$? Modifica el programa para tratarlo como **ecuación de primer grado** $bx + c = 0$. Si además $b = 0$, distingue los casos $c = 0$ (infinitas soluciones) y $c \neq 0$ (sin solución).

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

if a == 0:
    # Caso degenerado: ecuación lineal
    if b == 0:
        if c == 0:
            print("Infinitas soluciones (0 = 0).")
        else:
            print("Sin solución.")
    else:
        print(f"Raíz única: x = {-c / b}")
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

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/raices_cuadratica.py)

</details>

---

## 🟡 Bloque 2 — Bucle `for`

### 📝 Ejercicio 2.1: Suma de los $N$ primeros números de Fibonacci

**Enunciado.** La sucesión de **Fibonacci** se define recursivamente como:

$$F_0 = 0,\quad F_1 = 1,\quad F_n = F_{n-1} + F_{n-2} \text{ para } n \geq 2$$

Escribe un programa que, dado un entero $N$, calcule **la suma** de los $N$ primeros términos: $\displaystyle \sum_{n=0}^{N-1} F_n$.

#### ✔️ Tareas

1. Implementa la solución en Python usando un bucle `for`.
2. Comprueba que para $N = 10$ el resultado es **88**.
3. **Curiosidad matemática**: existe una identidad que afirma $\sum_{n=0}^{N-1} F_n = F_{N+1} - 1$. Modifica el programa para verificarla numéricamente para varios valores de $N$.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
n = int(input("¿Cuántos términos de Fibonacci sumar?: "))

a, b = 0, 1
suma = 0
for _ in range(n):
    suma = suma + a
    a, b = b, a + b   # asignación múltiple: avanzamos a la siguiente pareja

print(f"La suma de los primeros {n} términos de Fibonacci es: {suma}")

# Verificación de la identidad: la suma debe coincidir con F_{N+1} - 1
print(f"F_{n+1} - 1 = {b - 1}")    # tras el bucle, b = F_{N+1}
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/fibonacci_suma.py)

</details>

---

### 📝 Ejercicio 2.2: Aproximación de $\pi$ con la serie de Leibniz

**Enunciado.** La fórmula de Leibniz nos da una serie infinita que converge a $\pi/4$:

$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}$$

Escribe un programa que, dado un número $N$ de términos, calcule la aproximación de $\pi$ que se obtiene sumando los $N$ primeros términos de la serie.

#### ✔️ Tareas

1. Implementa la solución usando un bucle `for`.
2. Calcula y muestra el **error absoluto** respecto al valor real de $\pi$ (usa `math.pi`).
3. ¿Cuántos términos hacen falta para tener un error menor que $10^{-2}$? ¿Y menor que $10^{-4}$? Te darás cuenta de que la serie de Leibniz converge **muy lentamente** — un resultado interesante en Análisis Numérico.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

n = int(input("Número de términos: "))

pi_aprox = 0
for k in range(n):
    pi_aprox = pi_aprox + ((-1) ** k) / (2 * k + 1)

pi_aprox = pi_aprox * 4
error = abs(pi_aprox - math.pi)

print(f"π aproximado con {n} términos: {pi_aprox:.10f}")
print(f"π real:                       {math.pi:.10f}")
print(f"Error absoluto:               {error:.2e}")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/pi_leibniz.py)

</details>

---

### 📝 Ejercicio 2.3: Factorial y combinatorio

**Enunciado.** Escribe un programa que, dados dos enteros no negativos $n$ y $k$ con $k \leq n$, calcule el **número combinatorio**:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

#### ✔️ Tareas

1. Define una función `factorial(n)` que use un bucle `for` para calcular $n!$.
2. Usa esa función para calcular $\binom{n}{k}$.
3. **Bonus**: para evitar el desbordamiento (los factoriales crecen muy rápido), implementa una versión que use la fórmula equivalente $\binom{n}{k} = \prod_{i=1}^{k} \frac{n-i+1}{i}$, que va dividiendo en cada paso y mantiene los números pequeños.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def factorial(n: int) -> int:
    """Devuelve n!"""
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado


def combinatorio(n: int, k: int) -> int:
    """Devuelve C(n, k) usando factoriales."""
    return factorial(n) // (factorial(k) * factorial(n - k))


def combinatorio_estable(n: int, k: int) -> int:
    """
    Versión más eficiente y estable: evita calcular factoriales gigantes.
    Calcula C(n, k) = product_{i=1..k} (n - i + 1) / i.
    """
    resultado = 1
    for i in range(1, k + 1):
        resultado = resultado * (n - i + 1) // i
    return resultado


n = int(input("n: "))
k = int(input("k: "))

print(f"C({n}, {k}) = {combinatorio(n, k)}")
print(f"C({n}, {k}) = {combinatorio_estable(n, k)}  (versión estable)")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/combinatorio.py)

</details>

---

## 🟠 Bloque 3 — Bucle `while`

### 📝 Ejercicio 3.1: Algoritmo de Euclides para el MCD

**Enunciado.** Implementa el **algoritmo de Euclides** para calcular el máximo común divisor (MCD) de dos enteros positivos. El algoritmo se basa en:

$$\gcd(a, b) = \gcd(b, a \bmod b),\qquad \gcd(a, 0) = a$$

Y termina cuando el segundo argumento es 0.

**Pseudocódigo orientativo:**

```text
ALGORITMO mcd_euclides
  Entrada: a, b (entero positivo)
  Salida: mcd (entero positivo)

INICIO
  1. MIENTRAS b != 0
       resto ← a mod b
       a ← b
       b ← resto
  2. ESCRIBIR "MCD =", a
FIN
```

#### ✔️ Tareas

1. Implementa el algoritmo en Python con un bucle `while`.
2. Pruébalo con $\gcd(48, 18) = 6$, $\gcd(1071, 462) = 21$, $\gcd(17, 5) = 1$.
3. **Bonus matemático**: extiende el programa para que también calcule el **mínimo común múltiplo** usando $\text{mcm}(a,b) = \dfrac{a \cdot b}{\gcd(a,b)}$.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
a = int(input("a: "))
b = int(input("b: "))

# Guardamos los originales para el cálculo posterior del mcm
a_orig, b_orig = a, b

while b != 0:
    a, b = b, a % b   # asignación múltiple: muy útil aquí

mcd = a
mcm = (a_orig * b_orig) // mcd

print(f"MCD({a_orig}, {b_orig}) = {mcd}")
print(f"MCM({a_orig}, {b_orig}) = {mcm}")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/euclides_mcd.py)

</details>

---

### 📝 Ejercicio 3.2: Método de la bisección

**Enunciado.** Sea $f$ una función continua en $[a, b]$ tal que $f(a) \cdot f(b) < 0$. Por el **Teorema de Bolzano**, existe al menos una raíz $\xi \in (a, b)$. El **método de la bisección** la aproxima dividiendo el intervalo a la mitad en cada paso:

1. Calcular $c = (a+b)/2$.
2. Si $|f(c)| < \varepsilon$, hemos encontrado la raíz.
3. Si $f(a) \cdot f(c) < 0$ → la raíz está en $[a, c]$ → hacer $b \leftarrow c$.
4. En otro caso → la raíz está en $[c, b]$ → hacer $a \leftarrow c$.
5. Repetir mientras $b - a > \varepsilon$.

Implementa el método para encontrar la raíz de $f(x) = x^3 - x - 2$ en el intervalo $[1, 2]$ (la raíz exacta es $\xi \approx 1.521380$).

#### ✔️ Tareas

1. Implementa el método con un bucle `while` que termine cuando se cumpla la tolerancia.
2. Añade un **límite máximo de iteraciones** como red de seguridad (por ejemplo, 100).
3. Cuenta el **número de iteraciones** que han hecho falta. ¿Cuántas iteraciones hacen falta para tolerancia $10^{-6}$? ¿Y para $10^{-12}$? Compáralo con la teoría: cada iteración reduce el intervalo a la mitad, así que el error decrece como $2^{-n}$.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def f(x):
    return x**3 - x - 2

a = 1.0
b = 2.0
TOLERANCIA = 1e-10
MAX_ITER = 100

if f(a) * f(b) >= 0:
    print("⚠️ No se garantiza la existencia de raíz en este intervalo.")
else:
    iteracion = 0
    while (b - a) > TOLERANCIA and iteracion < MAX_ITER:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteracion = iteracion + 1

    raiz = (a + b) / 2
    print(f"Raíz aproximada: {raiz:.12f}")
    print(f"Iteraciones empleadas: {iteracion}")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/biseccion.py)

</details>

---

### 📝 Ejercicio 3.3: Método de Newton-Raphson

**Enunciado.** El **método de Newton-Raphson** aproxima una raíz de $f(x) = 0$ partiendo de una estimación $x_0$ y aplicando la recurrencia:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Implementa el método para calcular $\sqrt{a}$ aplicándolo a la función $f(x) = x^2 - a$ (cuya derivada es $f'(x) = 2x$). Sustituyendo en la fórmula obtienes —¡sorpresa!— la **fórmula babilónica** que viste en el [Ejemplo 3](../ejemplos/T4_Ejem_ICC.md#ejemplo-3-métodos-numéricos-raíz-cuadrada-por-el-método-babilónico).

#### ✔️ Tareas

1. Implementa el método de **forma genérica**, recibiendo `f` y `df` como parámetros.
2. Úsalo para calcular $\sqrt{2}$ y compara el número de iteraciones con el método de la bisección del ejercicio anterior. ¿Cuál converge más rápido?
3. **Bonus**: úsalo también para encontrar una raíz de $f(x) = \cos(x) - x$ partiendo de $x_0 = 0.5$. La raíz es la famosa **constante de Dottie**, $\xi \approx 0.7390851332$.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

def newton_raphson(f, df, x0, tol=1e-12, max_iter=100):
    """
    Devuelve una raíz aproximada de f, partiendo de x0.

    Parámetros:
      f, df:       función y su derivada
      x0:          estimación inicial
      tol:         tolerancia
      max_iter:    máximo de iteraciones (red de seguridad)
    """
    x = x0
    for iteracion in range(max_iter):
        x_nuevo = x - f(x) / df(x)
        if abs(x_nuevo - x) < tol:
            return x_nuevo, iteracion + 1
        x = x_nuevo
    raise RuntimeError(f"No convergió en {max_iter} iteraciones")


# 1. √2 con Newton-Raphson
a = 2.0
raiz, iteraciones = newton_raphson(
    f=lambda x: x**2 - a,
    df=lambda x: 2 * x,
    x0=a / 2,
)
print(f"√{a} ≈ {raiz} en {iteraciones} iteraciones")

# 2. Constante de Dottie: cos(x) = x
dottie, iteraciones = newton_raphson(
    f=lambda x: math.cos(x) - x,
    df=lambda x: -math.sin(x) - 1,
    x0=0.5,
)
print(f"Constante de Dottie ≈ {dottie} en {iteraciones} iteraciones")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/newton_raphson.py)

</details>

---

## 🔵 Bloque 4 — Bucles anidados

### 📝 Ejercicio 4.1: Criba de Eratóstenes

**Enunciado.** La **criba de Eratóstenes** es un algoritmo clásico para encontrar todos los números primos hasta un cierto límite $N$. Funciona así:

1. Crea una lista `[2, 3, 4, ..., N]`.
2. Empieza con $p = 2$ (el primer primo).
3. Tacha de la lista todos los múltiplos de $p$ (excepto $p$ mismo).
4. Avanza al siguiente número no tachado y repite.
5. Cuando $p^2 > N$, los números no tachados restantes son **todos primos**.

#### ✔️ Tareas

1. Implementa el algoritmo. Pista: usa una lista de booleanos `es_primo = [True] * (N + 1)` y necesitarás dos bucles anidados.
2. Pruébalo con $N = 30$. Deberías obtener: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`.
3. **Reflexión sobre la complejidad**: ¿cuántas operaciones realiza la criba para llegar hasta $N$? ¿Por qué la condición $p^2 > N$ es suficiente para parar?

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
n = int(input("Encontrar primos hasta: "))

# Inicialmente, todos los números son candidatos a primo
es_primo = [True] * (n + 1)
es_primo[0] = es_primo[1] = False   # 0 y 1 no son primos

# Criba propiamente dicha
p = 2
while p * p <= n:
    if es_primo[p]:
        # Tachamos los múltiplos de p (empezando por p*p, que es el primer
        # múltiplo de p que no se ha tachado en pasadas anteriores)
        for multiplo in range(p * p, n + 1, p):
            es_primo[multiplo] = False
    p = p + 1

# Recogemos los primos de la lista
primos = [i for i in range(n + 1) if es_primo[i]]
print(f"Primos hasta {n}: {primos}")
print(f"Cantidad: {len(primos)}")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/eratostenes.py)

</details>

---

### 📝 Ejercicio 4.2: Multiplicación de matrices

**Enunciado.** Sean $A \in \mathbb{R}^{m \times n}$ y $B \in \mathbb{R}^{n \times p}$. Su producto $C = A \cdot B$ tiene dimensión $m \times p$ y se calcula como:

$$C_{ij} = \sum_{k=1}^{n} A_{ik} \cdot B_{kj}$$

Implementa el producto matricial usando **listas de listas** (matrices representadas como `[[1, 2], [3, 4]]`) y **tres bucles anidados**.

#### ✔️ Tareas

1. Implementa la función `multiplicar(A, B)` que devuelva la matriz producto.
2. Comprueba primero que las **dimensiones son compatibles** (columnas de $A$ = filas de $B$). Si no lo son, lanza un `ValueError`.
3. Pruébalo con:

   $$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \quad \Rightarrow \quad A \cdot B = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

4. **Análisis de coste**: ¿cuántas operaciones de multiplicación realizan los tres bucles anidados para matrices $n \times n$? Verás que es $O(n^3)$ — el coste cúbico clásico de la multiplicación de matrices.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def multiplicar(A, B):
    """Multiplica dos matrices representadas como listas de listas."""
    filas_A = len(A)
    cols_A = len(A[0])
    filas_B = len(B)
    cols_B = len(B[0])

    if cols_A != filas_B:
        raise ValueError(
            f"Dimensiones incompatibles: A es {filas_A}x{cols_A}, "
            f"B es {filas_B}x{cols_B}."
        )

    # Inicializamos C como una matriz de ceros
    C = [[0] * cols_B for _ in range(filas_A)]

    # Triple bucle anidado
    for i in range(filas_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    return C


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = multiplicar(A, B)
for fila in C:
    print(fila)
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/multiplicar_matrices.py)

</details>

---

### 📝 Ejercicio 4.3: Triángulo de Pascal

**Enunciado.** El **triángulo de Pascal** se construye colocando un `1` en los extremos de cada fila, y siendo cada elemento interno la **suma de los dos elementos que tiene encima** en la fila anterior:

```text
                1
              1   1
            1   2   1
          1   3   3   1
        1   4   6   4   1
      1   5  10  10   5   1
    1   6  15  20  15   6   1
```

Cada elemento corresponde al número combinatorio: $\text{Pascal}_{n, k} = \binom{n}{k}$.

#### ✔️ Tareas

1. Implementa un programa que pida un entero $N$ e imprima las primeras $N$ filas del triángulo de Pascal.
2. **Bonus**: usa los formateadores de cadena para que el triángulo aparezca **bien centrado** visualmente, como en el ejemplo.
3. **Conexión teórica**: comprueba que el elemento $(n, k)$ del triángulo coincide con el número combinatorio que calculaste en el [Ejercicio 2.3](#-ejercicio-23-factorial-y-combinatorio).

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
n = int(input("Número de filas del triángulo de Pascal: "))

# Lista que iremos modificando fila a fila
fila = [1]

# Calculamos el ancho máximo para centrar visualmente
ancho = len("   ".join(["1"] * n)) + 2 * (n - 1)

for i in range(n):
    # Mostrar la fila actual centrada
    cadena = "   ".join(str(x) for x in fila)
    print(cadena.center(ancho))

    # Calcular la siguiente fila usando bucles anidados
    nueva_fila = [1]
    for k in range(len(fila) - 1):
        nueva_fila.append(fila[k] + fila[k + 1])
    nueva_fila.append(1)
    fila = nueva_fila
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/triangulo_pascal.py)

</details>

---

## 🔴 Bloque 5 — Combinando todo: condicionales, bucles y excepciones

### 📝 Ejercicio 5.1: Conjetura de Collatz (3n+1)

**Enunciado.** La **conjetura de Collatz** afirma que la siguiente sucesión, partiendo de cualquier entero positivo, **siempre acaba llegando a 1**:

$$a_{n+1} = \begin{cases} a_n / 2 & \text{si } a_n \text{ es par} \\ 3 a_n + 1 & \text{si } a_n \text{ es impar} \end{cases}$$

Por ejemplo, partiendo de 6: $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$. **Nadie ha demostrado todavía** si la conjetura es cierta para todos los números, pero se ha verificado computacionalmente para los primeros $10^{20}$ valores.

#### ✔️ Tareas

1. Escribe un programa que, dado un entero positivo $n$, muestre la sucesión de Collatz hasta llegar a 1, y cuente cuántos pasos ha tardado.
2. Maneja la entrada del usuario con `try-except` para garantizar que se introduce un entero positivo.
3. **Reto**: para los enteros del 1 al 100, encuentra cuál tiene la **trayectoria más larga** (es decir, tarda más pasos en llegar a 1). ¿Cuál es ese número?

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def collatz(n: int) -> tuple[list[int], int]:
    """Devuelve la sucesión de Collatz partiendo de n y el número de pasos."""
    sucesion = [n]
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sucesion.append(n)
        pasos = pasos + 1
    return sucesion, pasos


# Pedir entrada con validación robusta
while True:
    try:
        n = int(input("Entero positivo: "))
        if n <= 0:
            print("Debe ser positivo.")
            continue
        break
    except ValueError:
        print("Eso no es un entero válido.")

sucesion, pasos = collatz(n)
print(f"Sucesión: {sucesion}")
print(f"Pasos hasta llegar a 1: {pasos}")

# Reto: el número con trayectoria más larga del 1 al 100
mas_largo = 1
max_pasos = 0
for i in range(1, 101):
    _, p = collatz(i)
    if p > max_pasos:
        max_pasos = p
        mas_largo = i

print(f"\nDel 1 al 100, el de trayectoria más larga es {mas_largo} ({max_pasos} pasos).")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/collatz.py)

</details>

---

### 📝 Ejercicio 5.2: Suma de la serie armónica truncada

**Enunciado.** La **serie armónica** $\sum_{n=1}^{\infty} \frac{1}{n}$ es divergente — no tiene suma finita —, pero crece **muy lentamente**. Vamos a estudiar dos preguntas con un programa:

1. **Sumar los $N$ primeros términos**: $H_N = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{N}$.
2. **Encontrar el $N$ tal que $H_N$ supere por primera vez un umbral** $S$ dado por el usuario.

#### ✔️ Tareas

1. Implementa la primera pregunta con un bucle `for`.
2. Implementa la segunda con un bucle `while`. Añade un límite máximo de iteraciones por seguridad.
3. ¿Cuántos términos hacen falta para que $H_N > 10$? ¿Y para que $H_N > 20$? Compáralo con la fórmula asintótica $H_N \approx \ln(N) + \gamma$, donde $\gamma \approx 0.5772$ es la **constante de Euler-Mascheroni**.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

# Pregunta 1: Sumar los N primeros términos
n = int(input("N (cuántos términos sumar): "))
suma = 0
for i in range(1, n + 1):
    suma = suma + 1 / i
print(f"H_{n} = {suma:.10f}")
print(f"Aproximación asintótica ln(N) + γ = {math.log(n) + 0.5772156649:.10f}")

# Pregunta 2: Encontrar N tal que H_N > S
s = float(input("\nUmbral S: "))
MAX = 10**8

n = 0
suma = 0.0
while suma <= s and n < MAX:
    n = n + 1
    suma = suma + 1 / n

if suma > s:
    print(f"H_{n} = {suma:.6f} > {s} (primer N que supera el umbral)")
else:
    print(f"⚠️ No se ha superado el umbral en {MAX} iteraciones.")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/serie_armonica.py)

</details>

---

### 📝 Ejercicio 5.3: Integración numérica por la regla del trapecio

**Enunciado.** La **regla del trapecio compuesta** aproxima la integral $\int_a^b f(x)\, dx$ dividiendo el intervalo en $n$ subintervalos iguales:

$$\int_a^b f(x)\, dx \approx \frac{h}{2}\left[f(a) + 2\sum_{i=1}^{n-1} f(a+ih) + f(b)\right], \quad h = \frac{b-a}{n}$$

#### ✔️ Tareas

1. Implementa una función `trapecio(f, a, b, n)` que reciba una función, los extremos del intervalo y el número de subintervalos, y devuelva la integral aproximada.
2. Pruébala calculando $\int_0^1 x^2\, dx$ (cuyo valor exacto es $1/3$) y $\int_0^\pi \sin(x)\, dx$ (cuyo valor exacto es $2$).
3. **Análisis numérico**: comprueba empíricamente que **al duplicar $n$, el error se divide por 4**. Esto se debe a que el error de la regla del trapecio es $O(h^2)$.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

def trapecio(f, a, b, n):
    """Integral aproximada de f en [a, b] por la regla del trapecio compuesta."""
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
    for i in range(1, n):
        suma = suma + f(a + i * h)
    return suma * h


# Caso 1: ∫₀¹ x² dx = 1/3
print("∫₀¹ x² dx (exacta = 0.333333...)")
for n in [10, 100, 1000, 10000]:
    aprox = trapecio(lambda x: x**2, 0, 1, n)
    error = abs(aprox - 1/3)
    print(f"  n={n:5d}: aprox = {aprox:.10f}, error = {error:.2e}")

# Caso 2: ∫₀^π sin(x) dx = 2
print("\n∫₀^π sin(x) dx (exacta = 2.0)")
for n in [10, 100, 1000, 10000]:
    aprox = trapecio(math.sin, 0, math.pi, n)
    error = abs(aprox - 2)
    print(f"  n={n:5d}: aprox = {aprox:.10f}, error = {error:.2e}")
```

📁 [Solución completa en Python](https://github.com/jjcastroschez/Introduccion-Computacion-Cientifica/blob/main/04_control_flujo_ejecucion/ejercicios/trapecio.py)

</details>

---

## 🎯 Mini-reto final

> [!IMPORTANT]
> Si has llegado aquí y has resuelto los anteriores, este es para ti. **No tiene solución publicada**: tendrás que pensarlo por completo tú mismo.

### 📝 Ejercicio reto: Aproximación de $e$ por dos métodos

La constante de Euler $e$ se puede calcular por al menos dos métodos:

* **Serie de Taylor**: $\displaystyle e = \sum_{n=0}^{\infty} \frac{1}{n!}$.
* **Límite**: $\displaystyle e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n$.

Escribe un programa que calcule $e$ por **ambos métodos**, comparando para distintos valores de $n$ (digamos $n = 10, 100, 1000, 10\,000, 100\,000$) **el error respecto a `math.e` y el número de operaciones**.

* ¿Cuál de los dos métodos converge **más rápido**?
* ¿Cuál es **numéricamente más estable**? Pista: el segundo método sufre **cancelación catastrófica** para $n$ muy grandes con `float`.

Documenta tus conclusiones en un Notebook de Jupyter. Esta es la clase de pregunta que te encontrarás en la asignatura de **Análisis Numérico**.

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T4_ICC.md)              |      8       |
| 2      | [Recursos](../recursos/T4_RE_ICC.md)       |      5       |
| 3      | [Ejemplos](../ejemplos/T4_Ejem_ICC.md)     |      -       |
| 4      | **Ejercicios**                             |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
