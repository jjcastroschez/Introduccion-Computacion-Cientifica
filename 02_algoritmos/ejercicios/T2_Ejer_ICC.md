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

# 🧩 Ejercicios - Tema 2: Algoritmia 📝

El objetivo de estos ejercicios es que aprendas a **diseñar algoritmos** y a **expresarlos** de forma clara (pseudocódigo / diagrama de flujo), antes de “pensar en Python”.

---

## 1) Conceptos: ¿es realmente un algoritmo?

### ✅ Ejercicio 1 — “¿Algoritmo o descripción vaga?”
Indica si las siguientes instrucciones describen un algoritmo *válido*. Si no lo es, explica por qué (ambigüedad, no finito, no definido, etc.) y reescríbelo para que sí lo sea.

1. “Ordena los números y ya está”.
2. “Suma todos los valores hasta que te parezca suficiente”.
3. “Calcula la media de tres notas”.

<details>
  <summary><h4>💡 Pistas</h4></summary>
  <p>Piensa en las propiedades: preciso, finito, definido, legible. Si faltan datos de entrada o la condición de parada no es clara, no es un algoritmo “completo”.</p>
</details>

---

## 2) Del enunciado a entrada/salida

### ✅ Ejercicio 2 — Especificación mínima
Para cada problema, identifica **Entrada**, **Intermedias** y **Salida**:

a) Calcular el área de un triángulo.  
b) Convertir grados Celsius a Fahrenheit.  
c) Determinar si un número entero es par.

<details>
  <summary><h4>🧪 Ejemplo de formato de respuesta</h4></summary>
  <p><strong>Entrada:</strong> base, altura (reales). <strong>Intermedias:</strong> - <strong>Salida:</strong> area (real).</p>
</details>

---

## 3) Pseudocódigo (sin programar)

### ✅ Ejercicio 3 — Área y perímetro de un rectángulo
Escribe el pseudocódigo que calcule el **área** y el **perímetro** de un rectángulo.

- Entrada: base, altura  
- Salida: area, perimetro

<details>
  <summary><h4>✅ Solución propuesta</h4></summary>
  <pre><code>Algoritmo RectanguloAreaPerimetro
Entrada: base (real), altura (real)
Intermedias: -
Salida: area (real), perimetro (real)
Inicio
  1: Leer(base)
  2: Leer(altura)
  3: area &lt;- base * altura
  4: perimetro &lt;- 2 * (base + altura)
  5: Escribir(area, perimetro)
Fin</code></pre>
</details>

---

### ✅ Ejercicio 4 — Valor absoluto
Diseña un algoritmo que calcule \(|x|\) para un número real \(x\).

> [!NOTE]
> No uses funciones “mágicas” tipo `abs`. Resuélvelo con **selección**.

---

### ✅ Ejercicio 5 — Máximo de tres números
Diseña un algoritmo que reciba tres números reales y devuelva el mayor.

- Debe ser **definido** (si hay empates, tu algoritmo debe seguir funcionando).
- Presenta dos versiones:
  1) con comparaciones directas,
  2) usando una variable auxiliar `maximo`.

---

## 4) Eficiencia (muy introductorio)

### ✅ Ejercicio 6 — Dos formas de sumar 1..n
Considera dos algoritmos para calcular \(S = 1 + 2 + ... + n\).

- A) sumar con un bucle  
- B) usar \(S = \frac{n(n+1)}{2}\)

1) ¿Ambos son correctos?  
2) ¿Cuál es más eficiente en tiempo?  
3) ¿Cuál es más legible para alguien que empieza?

<details>
  <summary><h4>💡 Comentario orientativo</h4></summary>
  <p>Los dos pueden ser correctos. El de la fórmula es más eficiente en tiempo (constante). El del bucle puede ser más “explicativo” al principio, pero es más costoso cuando n es grande.</p>
</details>

---

## 5) Diagramas de flujo

> [!IMPORTANT]
> Respeta las restricciones: un inicio y un fin, top-down, líneas rectas, y símbolos estándar.

### ✅ Ejercicio 7 — Diagrama de flujo: par o impar
Diseña el diagrama de flujo que determine si un número entero es **par** o **impar**.

- Entrada: \(n\) (entero)
- Salida: “PAR” o “IMPAR”

---

### ✅ Ejercicio 8 — Diagrama de flujo: factorial
Diseña el diagrama de flujo del factorial \(n!\), suponiendo \(n \ge 0\).

> [!TIP]
> Este ejercicio obliga a usar **iteración** (bucle). Aún no estamos programando: solo diseñando el algoritmo.

---

## 6) Reto (opcional)

### ⭐ Ejercicio 9 — Algoritmo de Euclides (MCD)
Diseña en pseudocódigo el algoritmo para calcular el **máximo común divisor** (MCD) de dos enteros positivos \(a\) y \(b\) usando el algoritmo de Euclides.

<details>
  <summary><h4>💡 Pista</h4></summary>
  <p>Mientras b ≠ 0, sustituye (a, b) por (b, a mod b). Al final, a es el MCD.</p>
</details>

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo       | 
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T2_ICC.md)              |      6       |
| 2      | [Recursos](../recursos/T2_RE_ICC.md)       |      5       |
| 3      | [Ejemplos](../ejemplos/)                   |      -       |
| 4      | **Ejercicios**                             |      -       |
|        | [Menu del Tema actual](../README.md)       |      -       |
