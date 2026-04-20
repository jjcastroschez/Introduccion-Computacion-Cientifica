
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

## Jupyter

[Jupyter](https://jupyter.org) es un proyecto de código abierto y sin fines de lucro. Tras el proyecto hay un estándar y una comunidad, no solo un programa. Nace con un propósito principal: **La Ciencia Abierta y Reproducible**. 

Antes, si un científico descubría algo usando código, te enviaba un documento (generalmente un documento PDF) con el resultado. Tú veías la gráfica, pero no sabías qué código la había generado ni podías probarlo tú mismo. Era como leer la receta de un pastel sin poder entrar en la cocina.

Jupyter pretenden facilitar que el código no sea algo "oculto" que solo ejecutan los ingenieros, sino que sea parte del documento. Como ya hemos dicho el propósito es que que cualquier persona pueda ver el razonamiento, el código y el resultado en un solo lugar.

Su misión es crear herramientas gratuitas para que científicos, estudiantes y programadores puedan compartir sus descubrimientos de forma transparente. Cuando alguien dice "esto es Jupyter", se refiere a esta filosofía de "computación abierta e interactiva".

Jupyter es "políglota" (ya sabes a qué nos referimos... *Multilenguaje* 😜). El nombre Ju-Py-teR viene de Julia, Python y R, que fueron los tres primeros lenguajes que soportó. Hoy puedes usar Jupyter para programar en casi cualquier lenguaje (C++, Java, Scala, etc.) simplemente cambiando el "Kernel" (el motor que procesa el código).

Jupyter creó un estándar de archivos llamado **Notebooks**, un archivo `.ipynb` que puede contener:

* Tu código.

* Los resultados (tablas, fotos, mapas).

* Tus comentarios y notas.

### 🧪 Jupyter Notebook y Jupyter Lab: Tu Laboratorio de Código

Las dos herramientas generadas en el proyecto son: **Jupyter Notebook** y **Jupyter Lab**, con las que es posible crear y editar **Notebooks** (recuerda archivos con extensión `.ipynb`). La difencia entre ellas está en la "experiencia de usuario" y el flujo de trabajo que cambian radicalmente.

#### Comparativa: Jupyter Notebook vs. Jupyter Lab

| Característica | Jupyter Notebook (El Clásico) | Jupyter Lab (El Moderno) |
| :--- | :--- | :--- |
| **Interfaz de usuario** | Basada en documentos individuales. Simple y lineal. | Basada en un entorno de trabajo integrado (IDE). |
| **Gestión de archivos** | Cada cuaderno se abre en una pestaña diferente del navegador. | Pestañas internas que permiten trabajar con varios archivos en una sola ventana. |
| **Explorador de archivos** | Se encuentra en una página de inicio separada del editor. | Barra lateral integrada para navegar por carpetas mientras programas. |
| **Flexibilidad de diseño** | Diseño fijo. No permite ver dos celdas o archivos en paralelo fácilmente. | Diseño modular. Permite arrastrar y soltar ventanas para dividir la pantalla. |
| **Herramientas integradas** | Enfocado exclusivamente en archivos `.ipynb`. | Soporta terminales, editores de texto (`.py`, `.md`), consolas y visores de datos. |
| **Extensiones** | Sistema de extensiones antiguo y más difícil de gestionar. | Sistema de extensiones moderno y potente para añadir funcionalidades. |

### 📓 ¿Qué es un Notebook?

Aunque ya sabes de manera general que es un Notebook, vamos a verlo en más detalle. Un Notebook es un documento interactivo que se organiza en celdas. Existen principalmente dos tipos de celdas:

* **Celdas de Markdown**: Para escribir texto, fórmulas matemáticas, insertar imágenes o tablas.

* **Celdas de Código**: Donde escribes código (en nuestro caso Python). Al ejecutar una celda, el resultado (la salida) aparece justo debajo.

Una ventaja clave de Notebook es que el "estado" se mantiene. Si defines una variable en una celda, esta la podrás usar en cualquier celda posterior. Esto permite construir programas paso a paso.

### 🚀 Ejemplo práctico (Contenido del Notebook)

Imagina que tenemos un archivo llamado `Ejemplo_Tipos_T3.ipynb`. Su contenido en 4 celdas podría ser el siguiente:

#### Celda 1 (Markdown)
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

Descárgate el [ejem1_tipos_T3.ipynb](/03_variables_tipos_simples/recursos/Ejemplo_Tipos_T3.ipynb) y ejecútalo tú 😜.

### ⚙️ ¿Cómo ejecutarlos?

Existen herramientas que permiten ejecutarlos de manera:

- **Local**: Si tienes instalado **VS Code** (recomendado en el [Tema 1]()), solo tienes que instalar la extensión de Jupyter y abrir un archivo el archivo con extensión `.ipynb`.
- **Nube**: Existen herramientas para poderlas usar sin necesidad de instalación, por ejemplo puedes usar [Google Colab](https://colab.research.google.com/) para crear y ejecutar Notebooks sin instalar nada en tu ordenador.

Más adelante, en el [Sumario de enlaces interesantes](#sumario-de-enlaces-interesantes), te dejo otras alternativas.


### 🚀 ¿Por qué usar Notebooks en este tema?
1. **Interactividad**: Puedes probar qué pasa si sumas un `int` y un `float` y ver el resultado al instante.
2. **Visualización**: Ideales para ver cómo cambian los valores de las variables paso a paso.
3. **Documentación**: Tus ejercicios quedan documentados con tus propias notas al lado del código.

### 🔗 Para profundizar en Jupyter Notebook

- **[Guía oficial de Jupyter](https://docs.jupyter.org/en/latest/)**. La referencia más completa para y actualizada.

---

## Markdown

**Markdown** es un lenguaje de marcado ligero que permite añadir formato a un texto (negritas, listas, títulos, imágenes) utilizando caracteres sencillos del teclado, sin necesidad de usar botones o menús complejos.

A diferencia de un procesador de textos como Microsoft Word, donde aplicas el formato visualmente, en Markdown escribes el formato directamente en el texto. Es el estándar utilizado en GitHub, en los Notebooks de Jupyter, en la documentación técnica profesional y recientemente se considera el "idioma" de la inteligencia artificial moderna, ya que Funciona como un formato puente entre el lenguaje humano y la estructura de datos. Los modelos lingüísticos (LLM), como ChatGPT, Claude o Gemini, procesan estos datos de manera eficiente.

Para escribir las explicaciones en los Notebooks o crear documentos en GitHub (como este mismo archivo), utilizamos **Markdown**.

### 📊 Tabla de Referencia Rápida

| Resultado | Sintaxis Markdown |
| :--- | :--- |
| **Título Principal** | `# Título` |
| **Subtítulo 2º nivel** | `## Subtítulo` |
| **Subtítulo 3er nivel** | `### Subtítulo` |  
| **Negrita** | `**texto**` |
| **Cursiva** | `*texto*` |
| **Lista punteada** | `- Elemento` |
| **Lista numerada** | `1. Elemento` |
| **Enlace** | `[Texto](URL)` |
| **Código en línea** | `` `variable_x` `` |
| **Bloque de código** | ` ```python ` (en la línea anterior) finalizando con ` ``` ` |
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

## Sumario de enlaces interesantes

### Jupyter

* [Jupyter](https://jupyter.org)

### Editores de Notebook para escritorio

* Visual Studio Code [con extensión para Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter). 
* [Jupyter Notebook](https://jupyter.org/install) o [Jupyter Lab](https://jupyter.org/install).

### Editores de Notebook online

* [Google Colab](https://colab.research.google.com/).
* [Jupyter](https://jupyter.org/try)

### Markdown

* [Guía de Markdown](https://www.markdownguide.org)

### Editores de Markdown para escritorio

* [Ghostwriter](https://kde.github.io/ghostwriter/). Un editor de texto de código abierto especializado en Markdown, diseñado para ofrecer una experiencia de escritura libre de distracciones.
* [MarkText](https://marktext.me). Una alternativa de código abierto, muy personalizable y compatible con diversos temas visuales.
* Visual Studio Code [con extensión para Markdown](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced). Es la opción preferida por desarrolladores. Mediante extensiones, ofrece una previsualización en tiempo real y soporte avanzado para archivos `.md`.

### Editores de Markdown online

* [StackEdit](https://stackedit.io). Es uno de los editores web más populares; se sincroniza con Google Drive y Dropbox, permitiendo publicar directamente en plataformas como GitHub o Blogger.
* [Dillinger](https://dillinger.io). Un editor muy rápido y sencillo que permite exportar a formatos como PDF o HTML.
* [PenPage](https://penpage.com/). Una opción rápida y gratuita basada en el navegador que permite el almacenamiento local o en Google.

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) | 
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T3_ICC.md)              |      10      |
| 2      | **Recursos** |      5       |
| 3      | [Ejemplos](../ejemplos/T3_Ejem_ICC.md)     |      -       |
| 4      | [Ejercicios](../ejercicios/T3_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |