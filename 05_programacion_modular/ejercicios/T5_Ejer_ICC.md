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

# 📝 Ejercicios - Tema 5: Programación Modular 🧩

A continuación encontrarás ejercicios que te ayudarán a consolidar los conceptos del Tema 5: **definición y uso de funciones**, **paso de parámetros**, **devolución de múltiples valores**, **recursividad**, **módulos**, **paquetes**, **funciones como ciudadanos de primera clase** y **expresiones `lambda`**.

> [!NOTE]
> En estos ejercicios **sí usamos** las construcciones de los Temas 1-4 (variables y tipos simples, condicionales, bucles, `try-except`) junto con las **nuevas del Tema 5**. Aún **no usamos** listas, tuplas, diccionarios ni ficheros: eso vendrá en los Temas 6 y 7.

> [!TIP]
> Cada ejercicio incluye:
> * 📋 **Enunciado** con un objetivo claro.
> * 🧮 **Pseudocódigo orientativo** que te guía sin darte la solución.
> * 🛠️ **Tareas** concretas.
> * 🫣 **Una solución plegable** para que la consultes **solo después** de intentarlo.
>
> ¡El esfuerzo de pensarlo tú es lo que te hace mejor matemático-programador!

---

## 🟢 Bloque 1: Funciones básicas

### Ejercicio 1. Área de un triángulo 🔺

Define una función `area_triangulo(base, altura)` que reciba la base y la altura de un triángulo y devuelva su área. Recuerda la fórmula:

$$\text{área} = \frac{\text{base} \times \text{altura}}{2}$$

#### 🧮 Pseudocódigo orientativo

```text
función area_triangulo(base, altura):
    devolver base * altura / 2
```

#### 🛠️ Tareas

1. Escribe la función con type hints (`base: float, altura: float -> float`).
2. Añade un docstring breve.
3. En el bloque `if __name__ == "__main__":`, prueba la función con al menos 3 pares de valores.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def area_triangulo(base: float, altura: float) -> float:
    """Devuelve el área de un triángulo dado base y altura."""
    return base * altura / 2
```

📄 [Solución completa: area_triangulo.py](./area_triangulo.py)
</details>

---

### Ejercicio 2. Clasificador de raíces (revisita del Tema 4) 🔍

En el [Tema 4](../../04_control_flujo_ejecucion/ejercicios/T4_Ejer_ICC.md) escribiste un script que clasifica las raíces de una ecuación cuadrática $ax^2 + bx + c = 0$ según el signo del discriminante. Aquel script tomaba los datos del usuario y mostraba el resultado todo seguido.

**Ahora vamos a refactorizarlo** convirtiendo el cálculo en una función `clasificar_raices(a, b, c)` que **devuelva una cadena** descriptiva con el resultado, **sin imprimir nada**. La separación de "calcular" y "mostrar" es una buena práctica fundamental.

#### 🧮 Pseudocódigo orientativo

```text
función clasificar_raices(a, b, c):
    si a == 0:
        ... # tratar el caso degenerado: ecuación lineal o sin solución
    calcular discriminante = b² - 4ac
    si discriminante > 0:
        devolver cadena con las dos raíces reales distintas
    si discriminante == 0:
        devolver cadena con la raíz doble
    sino:
        devolver cadena con las raíces complejas conjugadas
```

#### 🛠️ Tareas

1. Implementa la función con type hints: recibe tres `float` y devuelve un `str`.
2. Trata el caso degenerado `a == 0` (¿tiene sentido la fórmula del discriminante? ¿qué pasa?).
3. Trata por separado los tres casos del discriminante.
4. **No uses `print` dentro de la función**: limítate a devolver una cadena con la descripción del resultado. El `print` debe estar en el `main()`.

> 💡 **Pista**: el caso `a == 0` se divide a su vez en subcasos: `b ≠ 0` da una ecuación lineal con solución única; `b == 0, c ≠ 0` no tiene solución; `b == 0, c == 0` tiene infinitas. Es un buen sitio para anidar `if/else`.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

📄 [Solución completa: clasificar_raices.py](./clasificar_raices.py)

La función trata los seis subcasos (a≠0 con discriminante >0, =0, <0; y a=0 con b≠0, b=c=0, b=0 c≠0) y devuelve una cadena descriptiva.
</details>

---

## 🟡 Bloque 2: Funciones que devuelven varios valores

### Ejercicio 3. División entera con resto ➗

Implementa tu propia función `divmod_entero(a, b)` que reciba dos enteros y devuelva la **pareja** `(cociente, resto)`. No uses el `divmod` integrado de Python.

#### 🧮 Pseudocódigo orientativo

```text
función divmod_entero(a, b):
    si b == 0:
        elevar excepción ZeroDivisionError
    cociente = a // b
    resto = a % b
    devolver cociente, resto    # devolver dos valores a la vez
```

#### 🛠️ Tareas

1. Implementa la función. **Tira una `ZeroDivisionError`** con un mensaje claro si `b` es cero.
2. Comprueba con `divmod_entero(17, 5)` que devuelve `(3, 2)`.
3. Demuestra el **desempaquetado** en la llamada:
   ```python
   q, r = divmod_entero(100, 7)
   ```
4. Demuestra el manejo del error con un `try-except`.

> 💡 **Recuerda**: cuando una función hace `return a, b`, devuelve **una tupla** `(a, b)`. Al asignar a `q, r = ...` Python la desempaqueta automáticamente. Si la asignas a una sola variable, recibes la tupla completa.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def divmod_entero(a: int, b: int) -> tuple:
    """División entera. Devuelve (cociente, resto)."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0.")
    return a // b, a % b
```

📄 [Solución completa: divmod_entero.py](./divmod_entero.py)
</details>

---

### Ejercicio 4. Coordenadas polares 📍

Escribe una función `coordenadas_polares(x, y)` que reciba las coordenadas cartesianas de un punto y devuelva sus coordenadas polares $(r, \theta)$ donde:

$$r = \sqrt{x^2 + y^2}, \qquad \theta = \mathrm{atan2}(y, x)$$

Usa `math.atan2(y, x)` (¡el orden es y, x!) para que el ángulo salga en el cuadrante correcto.

#### 🧮 Pseudocódigo orientativo

```text
función coordenadas_polares(x, y):
    r = sqrt(x² + y²)
    θ = atan2(y, x)
    devolver r, θ
```

#### 🛠️ Tareas

1. Implementa la función con type hints (`x: float, y: float -> tuple`).
2. Prueba con los siguientes pares:

| (x, y) | (r esperado, θ esperado) |
|:------:|:------------------------:|
| (1, 0) | (1, 0) |
| (0, 1) | (1, π/2 ≈ 1.5708) |
| (-1, 0) | (1, π ≈ 3.1416) |
| (1, 1) | (√2 ≈ 1.4142, π/4 ≈ 0.7854) |
| (-1, -1) | (√2, -3π/4 ≈ -2.3562) |

> 💡 **Por qué `atan2` y no `atan(y/x)`**: `atan` no sabe en qué cuadrante estás. `atan2(y, x)` recibe los dos argumentos por separado y devuelve el ángulo en el cuadrante correcto, en el rango $(-\pi, \pi]$.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import math

def coordenadas_polares(x: float, y: float) -> tuple:
    """Devuelve (r, theta) en coordenadas polares."""
    return math.sqrt(x**2 + y**2), math.atan2(y, x)
```

📄 [Solución completa: coordenadas_polares.py](./coordenadas_polares.py)
</details>

---

## 🟠 Bloque 3: Recursividad

### Ejercicio 5. Potencia recursiva 🪞

Implementa una función `potencia(base, n)` que calcule $\text{base}^n$ **recursivamente**, sin usar el operador `**` ni `math.pow`. Usa esta recurrencia:

$$\text{base}^n = \begin{cases} 1 & \text{si } n = 0 \\ \text{base} \cdot \text{base}^{n-1} & \text{si } n > 0 \end{cases}$$

#### 🧮 Pseudocódigo orientativo

```text
función potencia(base, n):
    si n < 0: elevar ValueError
    si n == 0: devolver 1
    devolver base * potencia(base, n - 1)
```

#### 🛠️ Tareas

1. Implementa la función. **Lanza una `ValueError`** si `n` es negativo.
2. Verifica que funciona con `potencia(2, 10) == 1024`, `potencia(3, 4) == 81` y `potencia(5, 0) == 1`.
3. **Reflexión**: ¿cuántas llamadas recursivas hace `potencia(2, 100)`? ¿Y `potencia(2, 1000)`? Recuerda el límite de pila de Python (≈ 1000). ¿Qué pasa si lo superamos?

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def potencia(base: float, n: int) -> float:
    """Devuelve base elevado a n por recursión."""
    if n < 0:
        raise ValueError("El exponente debe ser >= 0.")
    if n == 0:
        return 1.0
    return base * potencia(base, n - 1)
```

📄 [Solución completa: potencia.py](./potencia.py)
</details>

---

### Ejercicio 6. Algoritmo de Euclides recursivo (revisita del Tema 4) 🔄

En el [Tema 4](../../04_control_flujo_ejecucion/ejercicios/T4_Ejer_ICC.md) implementaste el algoritmo de Euclides con un bucle `while`. **Ahora reescríbelo recursivamente**.

La identidad de Euclides es **intrínsecamente recursiva**:

$$\gcd(a, b) = \begin{cases} a & \text{si } b = 0 \\ \gcd(b, a \bmod b) & \text{si } b \neq 0 \end{cases}$$

#### 🧮 Pseudocódigo orientativo

```text
función mcd_recursivo(a, b):
    si b == 0:
        devolver a                       # caso base
    devolver mcd_recursivo(b, a mod b)   # caso recursivo
```

#### 🛠️ Tareas

1. Implementa la función recursiva.
2. Conserva también la versión iterativa del Tema 4 con el nombre `mcd_iterativo` y compara los resultados con varios pares.
3. **Reflexión**: en este caso, ¿la versión recursiva es **realmente más clara** que la iterativa? ¿Cuál preferirías escribir en un módulo de producción?

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def mcd_recursivo(a: int, b: int) -> int:
    """MCD por recursión, usando la identidad de Euclides."""
    if b == 0:
        return a
    return mcd_recursivo(b, a % b)
```

📄 [Solución completa: mcd_recursivo.py](./mcd_recursivo.py)
</details>

---

## 🔵 Bloque 4: Módulos y paquetes

### Ejercicio 7. Tu primer módulo: `geometria.py` 📐

Vas a crear tu propio módulo Python con funciones de geometría plana. La idea es que, una vez creado, **puedas importarlo desde cualquier programa** con `import geometria`.

#### 🛠️ Tareas

1. Crea un archivo `geometria.py` y, dentro, define al menos estas funciones:
   - `area_circulo(radio)`
   - `perimetro_circulo(radio)`
   - `area_triangulo(base, altura)` (puedes reutilizar la del ejercicio 1)
   - `area_rectangulo(base, altura)`
   - `hipotenusa(cateto1, cateto2)`
2. Añade docstrings a cada función.
3. **Al final** del archivo, añade un bloque `if __name__ == "__main__":` con tests rápidos (`print` de cada función con valores que verifiquen el resultado).
4. Crea otro archivo `usa_geometria.py` que:
   - importe el módulo con `import geometria as g`,
   - lo utilice para calcular varios resultados,
   - muestre los resultados con `print`.

#### 🧪 Comprobaciones

* Ejecuta `python geometria.py` y deberían salir los tests rápidos.
* Ejecuta `python usa_geometria.py` y los tests **NO** deberían salir (porque al importar, el bloque `if __name__` no se ejecuta).

> 💡 **Truco extra**: añade también una función `area_triangulo_heron(a, b, c)` que use la fórmula de Herón:
> $s = (a+b+c)/2,\quad A = \sqrt{s(s-a)(s-b)(s-c)}$
> Es una pequeña joya matemática que merece tener en tu biblioteca.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

📄 [Solución completa: geometria.py](./geometria.py)  
📄 [Programa que lo usa: usa_geometria.py](./usa_geometria.py)
</details>

---

### Ejercicio 8. Tu primer paquete: `mi_paquete/` 🗂️

Ahora vamos un paso más allá: organizamos varias áreas matemáticas en un **paquete con submódulos**.

#### 🛠️ Tareas

1. Crea la siguiente estructura de directorios:

   ```text
   mi_paquete/
       __init__.py
       analisis/
           __init__.py
           sucesiones.py
       algebra/
           __init__.py
           polinomios.py
   ```

2. En `sucesiones.py`, implementa al menos:
   - `suma_armonica(n)` → $H_n = 1 + 1/2 + \ldots + 1/n$
   - `suma_aritmetica(primero, diferencia, n)` → suma de los $n$ primeros términos de una progresión aritmética.
   - `suma_geometrica(primero, razon, n)` → ídem para geométrica.

3. En `polinomios.py`, implementa al menos:
   - `evaluar_polinomio_simple(a, b, c, x)` → calcula $a x^2 + b x + c$ en el punto $x$.
   - `discriminante(a, b, c)` → $b^2 - 4ac$.

4. Crea un programa `usa_mi_paquete.py` que importe los submódulos y los use:

   ```python
   import mi_paquete.analisis.sucesiones as suc
   import mi_paquete.algebra.polinomios as pol
   ```

#### 🧪 Comprobaciones

* `suc.suma_armonica(100) ≈ 5.187`
* `suc.suma_aritmetica(1, 2, 10) == 100`  (1 + 3 + 5 + ... + 19)
* `suc.suma_geometrica(1, 2, 5) == 31`    (1 + 2 + 4 + 8 + 16)
* `pol.evaluar_polinomio_simple(1, -3, 2, 2) == 0`   (p(x) = x² - 3x + 2 tiene raíz x=2)

> 💡 **Conexión con bibliotecas reales**: lo que acabas de hacer es la misma estructura que tiene NumPy. Cuando escribes `numpy.linalg.solve(...)`, estás llamando a la función `solve` del submódulo `linalg` del paquete `numpy`. **Exactamente lo mismo.**

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

📂 Estructura completa del paquete:

- [`mi_paquete/__init__.py`](./mi_paquete/__init__.py)
- [`mi_paquete/analisis/__init__.py`](./mi_paquete/analisis/__init__.py)
- [`mi_paquete/analisis/sucesiones.py`](./mi_paquete/analisis/sucesiones.py)
- [`mi_paquete/algebra/__init__.py`](./mi_paquete/algebra/__init__.py)
- [`mi_paquete/algebra/polinomios.py`](./mi_paquete/algebra/polinomios.py)

📄 Programa que lo usa: [`usa_mi_paquete.py`](./usa_mi_paquete.py)
</details>

---

## 🟣 Bloque 5: Funciones de primera clase y lambdas

### Ejercicio 9. Aplicar una función varias veces 🔁

Define una función de orden superior `aplicar_n_veces(f, x, n)` que aplique `f` al valor `x` un total de `n` veces. Es decir:

$$\mathrm{aplicar\_n\_veces}(f, x, n) = \underbrace{f(f(\ldots f(x) \ldots))}_{n \text{ veces}}$$

Casos particulares:
- `aplicar_n_veces(f, x, 0) = x` (no se aplica nada)
- `aplicar_n_veces(f, x, 1) = f(x)`
- `aplicar_n_veces(f, x, 2) = f(f(x))`

#### 🧮 Pseudocódigo orientativo

```text
función aplicar_n_veces(f, x, n):
    resultado = x
    repetir n veces:
        resultado = f(resultado)
    devolver resultado
```

#### 🛠️ Tareas

1. Implementa la función con un bucle `for` simple.
2. Prueba con `aplicar_n_veces(cuadrado, 2, 3)` → debe devolver $((2^2)^2)^2 = 256$.
3. **Aplicación matemática preciosa**: itera el coseno desde 0:

   ```python
   import math
   for n in (5, 10, 50, 100):
       print(f"  tras {n:3d} iteraciones: {aplicar_n_veces(math.cos, 0, n):.10f}")
   ```

   Observarás que el valor converge a $\approx 0.7390851332$. Ese es el **punto fijo** de la función coseno (el único $x$ tal que $\cos(x) = x$). ¡Lo has encontrado iterando!

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def aplicar_n_veces(f, x: float, n: int) -> float:
    """Aplica f a x un total de n veces."""
    resultado = x
    for _ in range(n):
        resultado = f(resultado)
    return resultado
```

📄 [Solución completa: aplicar_n_veces.py](./aplicar_n_veces.py)
</details>

---

### Ejercicio 10. Lambdas — funciones de una sola línea λ

#### 🛠️ Tareas

**Parte A — Equivalencia entre `def` y `lambda`.** Reescribe estas funciones como expresiones `lambda`:

```python
def doble(x):
    return x * 2

def es_par(n):
    return n % 2 == 0

def suma(a, b):
    return a + b
```

**Parte B — Lambdas pasadas como argumento.** Reutiliza la función `aplicar` (o `aplicar_n_veces` del ejercicio 9) y úsala con **lambdas** en lugar de funciones definidas con `def`:

```python
print(aplicar_n_veces(lambda x: x + 1, 0, 100))     # ¿qué debe dar?
print(aplicar_n_veces(lambda x: x / 2, 1024, 10))   # ¿y esto?
```

**Parte C — Lambdas con integración numérica.** Reusa la función `integral_trapecio(f, a, b, n)` que viste en el ejemplo de [funciones de primera clase](../ejemplos/primera_clase_exp_py.ipynb). Calcula las siguientes integrales **pasando una lambda** en cada caso:

| Integral | Valor exacto |
|:--------|:------------:|
| $\int_0^1 x^2\,dx$ | $1/3$ |
| $\int_0^1 (x^3 + 1)\,dx$ | $5/4$ |
| $\int_0^{\pi} \sin(x)\,dx$ | $2$ |
| $\int_0^1 e^x\,dx$ | $e - 1$ |

**Parte D — Cuándo NO usar lambda.** Reflexiona: ¿qué te parece esto?

```python
clasificar = lambda x: ('positivo' if x > 0 else 'negativo' if x < 0 else 'cero')
```

Aunque es sintácticamente correcto, **viola el espíritu de `lambda`**. ¿Por qué? Reescríbelo como un `def` y compara la legibilidad.

> 💡 **Regla de oro**: usa `lambda` para expresiones simples (una operación, una comparación, una llamada a otra función). Cuando la lógica empiece a tener `if/else`, condiciones encadenadas o múltiples ramas, **vuelve a `def`** con un nombre descriptivo.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
# Parte A
doble = lambda x: x * 2
es_par = lambda n: n % 2 == 0
suma = lambda a, b: a + b

# Parte B
print(aplicar_n_veces(lambda x: x + 1, 0, 100))     # 100
print(aplicar_n_veces(lambda x: x / 2, 1024, 10))   # 1.0

# Parte C (integrales numéricas)
print(integral_trapecio(lambda x: x**2, 0, 1, 1000))         # ≈ 1/3
print(integral_trapecio(lambda x: x**3 + 1, 0, 1, 1000))     # ≈ 5/4
print(integral_trapecio(lambda x: math.sin(x), 0, math.pi, 1000))   # ≈ 2
print(integral_trapecio(lambda x: math.exp(x), 0, 1, 1000))  # ≈ e - 1
```

📄 [Solución completa: usar_lambdas.py](./usar_lambdas.py)
</details>

---

## 🎯 Reto final — Derivada numérica por diferencias finitas

Este reto **combina varios conceptos** del tema: parámetros con valor por defecto, función pasada como argumento, opcionalmente lambdas y reflexión sobre la aritmética en coma flotante.

> [!IMPORTANT]
> Este reto **no tiene solución publicada** en el repositorio. Es tu oportunidad de aplicar todo lo aprendido sin red. El esqueleto está en [`reto_derivada.py`](./reto_derivada.py) — **complétalo tú**.

### 📋 Enunciado

Implementa una función

```python
def derivada(f, x, h=1e-5):
    ...
```

que reciba:

* `f`: una función real de una variable (un objeto función).
* `x`: el punto donde queremos calcular la derivada.
* `h`: el paso de las diferencias finitas (con valor por defecto $10^{-5}$).

y devuelva una **aproximación numérica de $f'(x)$** mediante la fórmula de **diferencias centradas**:

$$ f'(x) \approx \frac{f(x+h) - f(x-h)}{2h} $$

### 🛠️ Tareas

1. Implementa la función. **Es muy corta** (una sola línea aparte del docstring).
2. Escribe un `main()` que pruebe los siguientes casos. Como conoces las derivadas exactas, podrás comprobar el error:

   | $f(x)$ | $f'(x)$ exacta | Punto $x$ a evaluar | Resultado esperado |
   |:------|:------|:-----:|:------:|
   | $x^2$ | $2x$ | 3 | 6 |
   | $\sin(x)$ | $\cos(x)$ | 0 | 1 |
   | $e^x$ | $e^x$ | 1 | $e \approx 2.71828$ |
   | $\ln(x)$ | $1/x$ | 2 | 0.5 |

3. Puedes pasar las funciones de dos maneras: **referenciando** `math.sin`, `math.exp`, etc., o **usando lambdas** `lambda x: x**2`.

### ★ Puntos extra (opcional)

#### ★ Investiga el error según $h$

Repite las pruebas con $h = 10^{-3}, 10^{-5}, 10^{-7}, 10^{-9}, 10^{-11}$ y observa qué le pasa al error. Verás que el error **primero disminuye** (porque $h$ pequeño = mejor aproximación) y **después empieza a crecer** (porque $h$ demasiado pequeño = ¡errores de redondeo en coma flotante!). Es uno de los efectos más interesantes del cálculo numérico, y descubrirlo tú mismo es una experiencia memorable.

#### ★★ Implementa la segunda derivada

Crea una función `derivada_segunda(f, x, h)` que **use tu propia `derivada`** dos veces. Es decir, una función que recibe una función y devuelve la derivada de su derivada. Necesitarás una **lambda intermedia** para envolver `derivada(f, _, h)` como una función de una variable. ¡Te toca pensarlo!

### 🧐 Para reflexionar

* ¿Por qué la **fórmula centrada** $\frac{f(x+h) - f(x-h)}{2h}$ es más precisa que la fórmula clásica $\frac{f(x+h) - f(x)}{h}$? (Pista: Taylor.)
* ¿Cómo de pequeño puedes hacer $h$ antes de que el resultado se vuelva inestable? Esto te enseñará algo importante sobre los **límites del cálculo en coma flotante**.

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T5_ICC.md)              |     10       |
| 2      | [Recursos](../recursos/T5_RE_ICC.md)       |      6       |
| 3      | [Ejemplos](../ejemplos/T5_Ejem_ICC.md)     |      -       |
| 4      | **Ejercicios**                             |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
