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

# 🔗 Recursos - Tema 5: Programación Modular 🧩

Aquí encontrarás los **enlaces y herramientas** que te permitirán dar el salto desde escribir pequeños scripts a usar el **ecosistema profesional** de Python para matemáticas y ciencia.

El tema se divide en dos grandes bloques:

1. 📚 **Documentación oficial** y referencias para los conceptos del tema.
2. 📦 **Instalación de módulos externos** con `pip`, entornos virtuales y **los paquetes imprescindibles** para un graduado en Matemáticas.

> [!TIP]
> No intentes memorizar las direcciones URL ni todas las opciones de `pip`. Marca este documento como referencia y vuelve a él cada vez que necesites instalar algo nuevo o consultar la documentación oficial de un módulo.

---

## 📚 Documentación oficial y referencias

### 🐍 Python: biblioteca estándar

Python viene con una **biblioteca estándar** enorme y muy bien documentada. Antes de buscar módulos externos en [PyPI](#-los-dos-sitios-que-debes-conocer), **consulta siempre** si lo que necesitas ya está en la biblioteca estándar:

- 📍 [Documentación oficial de la biblioteca estándar](https://docs.python.org/3/library/) — el índice completo de todos los módulos que vienen con Python.
- 📍 [Módulos numéricos y matemáticos](https://docs.python.org/3/library/numeric.html) — `math`, `cmath`, `decimal`, `fractions`, `random`, `statistics`...
- 📍 [Funciones integradas](https://docs.python.org/3/library/functions.html) — `abs`, `len`, `range`, `sum`, `min`, `max`, `sorted`, `map`, `filter`, `zip`, `enumerate`, `any`, `all`...
- 📍 [Tutorial oficial — módulos y paquetes](https://docs.python.org/3/tutorial/modules.html) — el capítulo del tutorial oficial que cubre exactamente la materia de este tema.

> 💡 **Truco**: desde dentro de Python puedes consultar la documentación de cualquier módulo sin abrir el navegador:
>
> ```python
> import math
> help(math)              # documentación completa
> help(math.sqrt)         # documentación de una función concreta
> print(dir(math))        # lista de todo lo que hay en el módulo
> ```

### 🇪🇸 Recursos (alguno en español 😜)

- 📍 [Tutorial de Python en español](https://docs.python.org/es/3/tutorial/) — la documentación oficial traducida.
- 📍 [Real Python (en inglés, pero con búsqueda muy potente)](https://realpython.com/) — la mejor web de tutoriales prácticos de Python.

---

## 📦 Instalación de módulos externos con `pip`

`pip` es el **gestor de paquetes oficial** de Python. Te permite descargar, instalar, actualizar y desinstalar paquetes del repositorio público **PyPI** (Python Package Index).

### 🌐 Los dos sitios que debes conocer

- 📍 **[PyPI — Python Package Index](https://pypi.org)** — el repositorio oficial. **Aquí buscarás** todos los paquetes que vayas a instalar. Cada paquete tiene su ficha con descripción, licencia, número de descargas y enlaces a la documentación.
- 📍 **[pip — documentación oficial](https://pip.pypa.io/)** — referencia completa del comando `pip`.

### 📊 Para evaluar la calidad de un paquete

- 📍 **[PePy — estadísticas de descargas](https://pepy.tech/)** — te dice cuántas veces se ha descargado un paquete (un buen indicador de popularidad y madurez).
- 📍 **[Snyk Advisor](https://snyk.io/advisor/)** — analiza la salud del paquete (mantenimiento, seguridad, comunidad).

### ✅ Antes de instalar nada: verifica tu instalación

Lo primero que debes saber es **qué versión de Python estás usando** y **dónde está instalado**:

```python
import sys
print(sys.version)        # versión de Python
print(sys.executable)     # ruta al ejecutable
```

Y comprueba que `pip` funciona:

```bash
pip --version
```

Si te da error, intenta una de estas:

```bash
python -m pip --version
python3 -m pip --version
```

> ⚠️ **Atención usuarios de Mac**: en algunos macOS hay varias versiones de Python coexistiendo, y `pip` a secas puede no apuntar a la versión de Python que usa tu IDLE. **Usa siempre la ruta completa que te haya devuelto `sys.executable`** seguida de `-m pip`:
>
> ```bash
> /Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -m pip install matplotlib
> ```
>
> Es feo, pero es **infalible**. Si lo haces así, te aseguras de que instalas el paquete en la misma versión de Python que estás usando.

### 🖥️ Instalación de paquetes en IDEs

Para instalar paquetes de Python, por ejemplo, en VS Code, abre la **Terminal integrada** y utiliza el gestor `pip`. Asegúrate de tener seleccionado el entorno de Python correcto en la esquina inferior derecha antes de instalar.

> ⚠️ Si instalas el paquete pero tu código sigue arrojando un error de tipo `ModuleNotFoundError`, es probable que VS Code esté usando un entorno de Python distinto al que utilizaste para instalar la librería.

### 🔧 Los comandos básicos de `pip`

```bash
pip install nombre_paquete                    # instalar la última versión
pip install nombre_paquete==1.2.3             # instalar una versión específica
pip install nombre_paquete --upgrade          # actualizar a la última versión
pip uninstall nombre_paquete                  # desinstalar
pip list                                      # listar paquetes instalados
pip show nombre_paquete                       # información detallada de un paquete
pip search nombre_paquete                     # buscar (puede estar desactivado)
```

> 💡 **Truco**: para guardar la lista de paquetes que usa tu proyecto y poder reinstalarla en otro ordenador:
>
> ```bash
> pip freeze > requirements.txt          # guardar
> pip install -r requirements.txt        # restaurar
> ```
>
> Esto es lo que verás en cualquier proyecto Python serio.

---

## 🏗️ Entornos virtuales: una buena costumbre desde el primer día

Imagina que para un trabajo necesitas `numpy 1.25` y para otro `numpy 2.0`. Si los instalas todos al sistema, **se pisan entre sí**. La solución son los **entornos virtuales**: pequeñas carpetas que contienen una instalación independiente de Python y sus paquetes.

### 🛠️ Crear y usar un entorno virtual

```bash
# 1) Crear el entorno (en la carpeta del proyecto)
python3 -m venv mi_entorno

# 2) Activarlo
source mi_entorno/bin/activate     # Linux / macOS
mi_entorno\Scripts\activate        # Windows

# 3) Ya puedes instalar paquetes; quedan solo dentro del entorno
pip install numpy matplotlib

# 4) Cuando termines, desactiva
deactivate
```

Cuando hayas terminado con un proyecto, **simplemente borra la carpeta `mi_entorno`** y desaparece todo lo que instalaste para él. Limpio y sin residuos.

> 🎓 **Aprender esto ahora te ahorra disgustos futuros**. En todos los proyectos profesionales se trabaja con entornos virtuales. Acostúmbrate desde ya.

### 🛠️ Alternativas modernas a `venv`

- 📍 **[Conda / Miniconda](https://docs.conda.io/projects/miniconda/)** — sistema de entornos virtuales más potente, muy usado en ciencia de datos. Maneja también dependencias no-Python (compiladores, bibliotecas C, etc.). Si vas a usar mucho NumPy/SciPy/Pandas, vale la pena considerarlo.
- 📍 **[uv](https://docs.astral.sh/uv/)** — gestor moderno y muchísimo más rápido que `pip`. Aún reciente, pero ganando popularidad rápido.

Para empezar, `venv` + `pip` es perfectamente suficiente.

---

## 🧮 Paquetes esenciales para un graduado en Matemáticas

Esta es **la lista corta** de paquetes que debes conocer. No hace falta dominarlos todos ya: lo importante es saber **qué hace cada uno** para saber a cuál acudir cuando te encuentres con un problema concreto.

### 🔢 Cálculo numérico

#### [NumPy](https://numpy.org/) — `pip install numpy`

**La base** de todo el ecosistema científico de Python. Te permite trabajar con **arrays multidimensionales** (vectores, matrices, tensores) de forma eficiente, gracias a que internamente está escrito en C.

```python
import numpy as np

v = np.array([1, 2, 3])
A = np.array([[1, 2], [3, 4]])
print(A @ v[:2])           # producto matriz-vector
print(np.linalg.det(A))    # determinante
print(np.linalg.inv(A))    # inversa
```

📍 [Documentación oficial](https://numpy.org/doc/stable/) · [Tutorial para principiantes](https://numpy.org/doc/stable/user/absolute_beginners.html) · [NumPy User Guide](https://numpy.org/doc/stable/numpy-user.pdf)

> 💡 **Por qué importa**: si vas a estudiar álgebra lineal, métodos numéricos, estadística o análisis de datos, **NumPy será tu pan diario**.

#### [SciPy](https://scipy.org/) — `pip install scipy`

Construido sobre NumPy, **amplía sus capacidades** con módulos para optimización, integración, interpolación, ecuaciones diferenciales, álgebra lineal avanzada, transformadas de Fourier, estadística, procesamiento de señales...

```python
from scipy.optimize import minimize, fsolve
from scipy.integrate import quad         # integración numérica
from scipy.linalg import eig             # autovalores
```

📍 [Documentación oficial](https://docs.scipy.org/doc/scipy/) · [Lecture notes (gratuitas, en inglés)](https://scipy-lectures.org/)

> 💡 **Por qué importa**: en cuanto necesites cualquier algoritmo numérico clásico, antes de programarlo tú, **busca en SciPy**. Probablemente esté implementado, optimizado y bien testeado.

### 🔣 Matemáticas simbólicas

#### [SymPy](https://www.sympy.org/) — `pip install sympy`

Mientras que NumPy y SciPy trabajan **numéricamente** (con aproximaciones de coma flotante), SymPy trabaja **simbólicamente**: deriva, integra, factoriza, resuelve ecuaciones... exactamente, como lo haría un humano con lápiz y papel (o como Mathematica/Maple).

```python
from sympy import symbols, diff, integrate, solve, sin, cos, pi

x = symbols('x')
print(diff(sin(x)**2, x))        # derivada simbólica → 2*sin(x)*cos(x)
print(integrate(x**2, (x, 0, 1)))  # ∫x²dx desde 0 a 1 → 1/3
print(solve(x**2 - 2, x))         # raíces → [-√2, √2]
```

📍 [Documentación oficial](https://docs.sympy.org/latest/index.html) · [Tutorial interactivo](https://live.sympy.org/)

> 💡 **Por qué importa**: ideal para Análisis Matemático, Álgebra y Ecuaciones Diferenciales. Cuando necesites el **resultado exacto** y no una aproximación.

### 📊 Análisis y manipulación de datos

#### [Pandas](https://pandas.pydata.org/) — `pip install pandas`

La herramienta estándar de Python para **trabajar con datos tabulares** (estilo hoja de cálculo): leer CSV/Excel, filtrar filas, agrupar por columnas, calcular estadísticas, hacer joins... Imprescindible para Estadística e Inferencia, Minería de Datos o cualquier asignatura aplicada.

```python
import pandas as pd

df = pd.read_csv("ventas.csv")
print(df.describe())                          # estadísticas básicas
print(df.groupby("region")["ventas"].mean())  # ventas medias por región
```

📍 [Documentación oficial](https://pandas.pydata.org/docs/) · [10-minute intro a Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

### 📈 Visualización

#### [Matplotlib](https://matplotlib.org/) — `pip install matplotlib`

La biblioteca de gráficos **clásica y universal** de Python. Aprenderás a usarla en las prácticas. Inspirada en MATLAB.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.xlabel("x");  plt.ylabel("y")
plt.legend();  plt.show()
```

📍 [Documentación oficial](https://matplotlib.org/stable/) · [Galería de ejemplos](https://matplotlib.org/stable/gallery/) — un recurso oro: encuentra un gráfico parecido al que quieres y copia el código.

#### [Seaborn](https://seaborn.pydata.org/) — `pip install seaborn`

Construido sobre Matplotlib, ofrece **gráficos estadísticos preciosos** con muy poco código. Especialmente útil cuando trabajes con Pandas.

📍 [Documentación oficial](https://seaborn.pydata.org/) · [Tutorial](https://seaborn.pydata.org/tutorial.html)

#### [Plotly](https://plotly.com/python/) — `pip install plotly`

Para **gráficos interactivos** (3D, dashboards, gráficas que se pueden manipular con el ratón). Especialmente útil para presentaciones y trabajos finales.

📍 [Documentación oficial](https://plotly.com/python/)

### 🤖 Aprendizaje automático

#### [scikit-learn](https://scikit-learn.org/) — `pip install scikit-learn`

La biblioteca de **machine learning clásico** más utilizada del mundo. Regresión, clasificación, clustering, validación cruzada, métricas... todo con una API muy coherente.

📍 [Documentación oficial](https://scikit-learn.org/stable/) · [Tutorial introductorio](https://scikit-learn.org/stable/tutorial/index.html)

> 💡 **Por qué importa**: si te interesa la rama aplicada de las Matemáticas (Inteligencia Artificial, Ciencia de Datos, Estadística aplicada), `scikit-learn` será tu primera puerta de entrada al machine learning.

### 📓 Entornos de trabajo

#### [Jupyter](https://jupyter.org/) — `pip install jupyter`

Ya debes conocer los notebooks de Jupyter (`.ipynb`) hablamos de ellos en el [Tema 3](../../03_variables_tipos_simples/recursos/). Si quieres ejecutarlos localmente sin depender de la web:

```bash
pip install jupyter
jupyter notebook        # arranca el servidor local
```

📍 [Documentación oficial](https://docs.jupyter.org/)

#### [JupyterLab](https://jupyter.org/) — `pip install jupyterlab`

La evolución moderna de Jupyter Notebook. Misma idea pero con interfaz más potente (pestañas, terminal integrada, vista en paralelo de varios notebooks).

---

## 📋 Tabla resumen — paquetes recomendados por asignatura

| Asignatura típica del Grado | Paquetes que te van a interesar |
|:----------------------------|:--------------------------------|
| Álgebra Lineal              | NumPy (vectores, matrices, sistemas lineales) |
| Análisis Matemático         | SymPy (derivadas, integrales simbólicas) |
| Ecuaciones Diferenciales    | SciPy (`scipy.integrate.solve_ivp`), SymPy |
| Análisis Numérico           | NumPy + SciPy (optimización, raíces, interpolación) |
| Estadística e Inferencia    | NumPy, SciPy (`scipy.stats`), Pandas, Seaborn |
| Modelos Matemáticos         | NumPy + SciPy + Matplotlib |
| Investigación Operativa     | SciPy (`scipy.optimize.linprog`), [PuLP](https://coin-or.github.io/pulp/) |
| Aprendizaje Automático      | scikit-learn, NumPy, Pandas, Matplotlib |
| Trabajo Fin de Grado        | Lo que el TFG requiera + Jupyter para escribir tu memoria reproducible |

---

## 🃏 Cheatsheets útiles

- 📍 [**NumPy cheatsheet**](https://numpy.org/devdocs/user/cheatsheet.html) — referencia rápida oficial.
- 📍 [**Pandas cheatsheet**](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) — PDF oficial.
- 📍 [**Matplotlib cheatsheets**](https://matplotlib.org/cheatsheets/) — varios cheatsheets visuales muy útiles.
- 📍 [**Python cheatsheet** (no oficial)](https://www.pythoncheatsheet.org/) — recopilatorio en español/inglés con sintaxis básica, funciones, módulos.

---

## 🆘 Cuando algo no funciona

Algunos problemas habituales y cómo solucionarlos:

| Síntoma | Probable causa | Solución |
|:--------|:--------------|:---------|
| `ModuleNotFoundError: No module named 'X'` al importar | El paquete no está instalado en la versión de Python que usa el IDE | `pip install X` o, en Mac, usar la ruta completa |
| `pip install` instala, pero el `import` sigue fallando | Tienes varias instalaciones de Python | Comprobar `sys.executable` y usar `python -m pip install ...` |
| `pip install` muy lento | Conexión o caché corrupta | Probar `pip install --no-cache-dir X` |
| Conflictos entre versiones de paquetes | Instalación compartida | Crear un entorno virtual (`python -m venv`) |

> 🤝 **Cómo buscar ayuda eficazmente**:
> 1. Copia y pega el mensaje de error **completo** en Google.
> 2. Filtra por **Stack Overflow** o por la documentación oficial.
> 3. Si pides ayuda a un compañero o profesor, **incluye siempre**: comando exacto que has ejecutado, mensaje de error completo, versión de Python (`python --version`) y sistema operativo.

---

## 🧭 Menú de Navegación

| Orden | Material | Tiempo |
|:-----:|:---------|:------:|
| 1     | [Teoría](../teoria/T5_ICC.md)             |  10   |
| 2     | **Recursos**                              |   6   |
| 3     | [Ejemplos](../ejemplos/T5_Ejem_ICC.md)    |   –   |
| 4     | [Ejercicios](../ejercicios/T5_Ejer_ICC.md)|   –   |
|       | [Menú del Tema actual](../README.md)      |   -   |
