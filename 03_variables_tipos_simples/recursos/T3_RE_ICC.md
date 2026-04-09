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

# 🎓 Recursos - Tema 3: Tipos de Datos y Variables 🧩

En este apartado encontrarás herramientas y documentación para profundizar en cómo los lenguajes de programación gestionan la información y cómo puedes empezar a experimentar con código vivo.

---

## 📓 Jupyter Notebooks: Tu Laboratorio de Código

Para este tema y los siguientes, utilizaremos *Jupyter Notebooks*, que son documentos interactivos que contienen código en vivo (principalmente Python, pero también R o Julia), junto a ecuaciones, visualizaciones y texto narrativo. 

Estos documentos son generados por **Jupyter Notebook**, una herramienta que permite crear y compartir documentos que combinan texto explicativo (Markdown) con bloques de código ejecutable. Es el estándar en la computación científica actual, ya que permite compartirlos fácilmente. 

### 📓 ¿Qué es un Jupyter Notebook?

Un Jupyter Notebook es un entorno interactivo basado en web (o integrado en VS Code) que se organiza en celdas. Existen principalmente dos tipos de celdas:

* **Celdas de Markdown**: Para escribir texto, fórmulas matemáticas, insertar imágenes o tablas.

* **Celdas de Código**: Donde escribes código (en nuestro caso Python). Al ejecutar una celda, el resultado (la salida) aparece justo debajo.

Una ventaja clave de Jupiter Notebook es que el "estado" se mantiene. Si defines una variable en una celda, esta la podrás usar en cualquier celda posterior. Esto permite construir programas paso a paso.

La extensión de los archivos generados con Jupyter Notebook será `.ipynb`. 

### 🚀 Ejemplo práctico (Contenido del Notebook)

Imagina que tenemos un archivo llamado `Ejemplo_Tipos_T3.ipynb`. Su contenido en 4 celdas podría ser el siguiente:

#### Celda 1 (Markdown)
```markdown
# Mi primer experimento con Variables
En este notebook vamos a probar cómo Python gestiona los tipos de datos de forma dinámica.
```
#### Celda 2 (Código Python)
```python
# Definimos una variable con un número entero
numero_alumnos = 25
print(f"Valor: {numero_alumnos} - Tipo: {type(numero_alumnos)}")

# Ahora cambiamos el tipo de la misma variable (Tipado Dinámico)
numero_alumnos = "Veinticinco"
print(f"Valor: {numero_alumnos} - Tipo: {type(numero_alumnos)}")
```

#### Celda 3 (Markdown)
```markdown
# Operaciones y Precedencia
Vamos a calcular el área de un círculo: $Area = \pi \cdot r^2$
```

#### Celda 4 (Código Python)
```python
radio = 5.0
# Usamos el operador de potencia **
area = 3.1416 * radio ** 2

print(f"El área del círculo es: {area:.2f}")
```

Descárgatelo y ejecútalo tú 😜. 

### 🚀 ¿Por qué usar Notebooks en este tema?
1. **Interactividad**: Puedes probar qué pasa si sumas un `int` y un `float` y ver el resultado al instante.
2. **Visualización**: Ideales para ver cómo cambian los valores de las variables paso a paso.
3. **Documentación**: Tus ejercicios quedan documentados con tus propias notas al lado del código.

### 🛠️ ¿Cómo ejecutarlos?
- **Local**: Si instalaste la extensión de Jupyter en **VS Code** (recomendado en el [Tema 1]()), solo tienes que abrir un archivo con extensión `.ipynb`.
- **Nube**: Puedes usar [Google Colab](https://colab.research.google.com/) para ejecutar notebooks sin instalar nada en tu ordenador.

---

## Nociones Básicas de Markdown

**Markdown** es un lenguaje de marcado ligero que permite añadir formato a un texto (negritas, listas, títulos, imágenes) utilizando caracteres sencillos del teclado, sin necesidad de usar botones o menús complejos.

A diferencia de un procesador de textos como Microsoft Word, donde aplicas el formato visualmente, en Markdown escribes el formato directamente en el texto. Es el estándar utilizado en GitHub, en los Jupyter Notebooks y en la documentación técnica profesional.

Para escribir las explicaciones en los Notebooks o crear documentos en GitHub (como este mismo archivo), utilizamos **Markdown**. 

### 📊 Tabla de Referencia Rápida

| Resultado | Sintaxis Markdown |
| :--- | :--- |
| **Título Principal** | `# Título` |
| **Subtítulo** | `## Subtítulo` |
| **Negrita** | `**texto**` |
| *Cursiva* | `*texto*` |
| **Lista punteada** | `- Elemento` |
| **Lista numerada** | `1. Elemento` |
| **Enlace** | `[Texto](URL)` |
| **Código en línea** | `` `variable_x` `` |
| **Bloque de código** | ` ```python ` (en la línea anterior) |
| **Fórmulas (LaTeX)** | `$E = m \cdot c^2$` |

### 🔗 Para profundizar en Markdown
- **[Guía oficial de GitHub](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)**: La referencia más completa para el formato que verás en este repositorio.
- **[Markdown Tutorial (Interactivo)](https://www.markdowntutorial.com/es/)**: Un tutorial de 10 minutos para practicar en el navegador.

---

## 📚 Documentación de Referencia

### Python (Tipado Dinámico)
* **[Built-in Types (Oficial)](https://docs.python.org/3/library/stdtypes.html)**: La "biblia" de los tipos de datos en Python. Imprescindible para consultar métodos de cadenas y límites de números.
* **[Python Type Hinting](https://docs.python.org/3/library/typing.html)**: Aunque Python es dinámico, existe una forma de "anotar" tipos para ayudar al programador.

### Lenguaje C (Tipado Estático)
* **[C Data Types (Programiz)](https://www.programiz.com/c-programming/c-data-types)**: Una guía visual muy clara sobre el tamaño en bytes de cada tipo en C y su rango de valores.
* **[Format Specifiers en C](https://www.geeksforgeeks.org/format-specifiers-in-c/)**: Tabla esencial para saber qué usar en `printf` y `scanf` (`%d`, `%f`, `%c`, etc.).

---

## 🔍 Herramientas de Inspección y Estilo

### Visualizadores de Memoria
* **[Python Tutor](https://pythontutor.com/)**: **Recurso Estrella**. Permite ver "dentro" de la memoria del ordenador. Verás cómo se crean las variables, qué valor tienen y cómo cambian línea a línea. Soporta Python y C.

### Guías de Estilo (Naming)
* **[PEP 8](https://peps.python.org/pep-0008/#naming-conventions)**: La guía oficial de estilo para Python. Revisa la sección de *Naming Conventions* para aprender a nombrar variables correctamente.

---

## 💡 Consejos Prácticos para el Estudiante

> [!TIP]
> **Sobre la precisión:** En computación científica, nunca compares dos números `float` usando `==`. Debido a la representación en binario, `0.1 + 0.2` no es exactamente `0.3`. Usa una pequeña tolerancia o funciones como `math.isclose()`.

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) | 
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T3_ICC.md)              |      10      |
| 2      | **Recursos** |      5       |
| 3      | [Ejemplos](../ejemplos/T3_Ejem_ICC.md)     |      -       |
| 4      | [Ejercicios](../ejercicios/T3_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |