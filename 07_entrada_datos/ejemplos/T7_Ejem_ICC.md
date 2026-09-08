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

# 🧐 Ejemplos - Tema 7: Entrada de Datos 💾

En esta sección, la idea es que, una vez ya has trabajado con los casos y ejemplos de clase, tengas aquí **problemas nuevos** que ilustran los mismos conceptos desde ángulos distintos, para que puedas afianzar los patrones y ver cómo se aplican a situaciones diferentes.

> [!TIP]
> Muchos ejemplos leen o escriben ficheros. Para que funcionen, ejecútalos desde la **misma carpeta** donde están los datos (`.csv`, `.json`, `.txt`).

---

## Contenido

En los temas anteriores has aprendido a **procesar datos** que estaban en variables ([Tema 3](../../03_variables_tipos_simples/README.md)), a **estructurar** el flujo ([Tema 4](../../04_control_flujo_ejecucion/README.md)), a **crear tus propias funciones y módulos** ([Tema 5](../../05_programacion_modular/README.md)) y a **modelar información** con tipos complejos ([Tema 6](../../06_tipos_compuestos/README.md)). Ahora vas a aprender a **liberar tus programas de la necesidad de tener a alguien delante**: los datos vendrán de ficheros, de APIs remotas o de bases de datos.

Los ejemplos que verás a continuación te enseñarán a:

* **Leer y escribir** ficheros de texto plano.
* **Procesar** ficheros CSV con datos tabulares.
* **Manejar** ficheros JSON con estructura anidada.
* **Consultar** APIs REST para obtener datos externos en tiempo real.
* **Crear y usar** bases de datos SQLite con SQL.
* **Combinar** varias fuentes en un flujo integrado.

---

### 📁 Bloque 1. Ficheros de texto

Los ejemplos de este bloque muestran dos usos muy típicos que **no aparecen** en las transparencias: un **fichero de log** que ilustra el modo `"a"` (append), y un **análisis léxico** de un texto que combina ficheros con diccionarios ([Tema 6](../../06_tipos_compuestos/README.md)).

#### 📝 Ejemplo 1 — Registro de eventos en un fichero de log

Un patrón esencial en programación: cada vez que ocurre algo relevante (arranque, error, aviso...), el programa **añade una línea al final** de un fichero de log, con marca de tiempo. La clave está en usar el modo `"a"` de `open()`, que **añade** en vez de sobrescribir. Este ejemplo genera entradas de log de distintos niveles (INFO, WARN, ERROR) con la fecha actual, y muestra las últimas líneas al final.

Conceptos que refuerza:

* La diferencia crítica entre **`"w"` (borra)** y **`"a"` (añade)**.
* Uso del módulo `datetime` para marcas de tiempo.
* Separación en funciones (`registrar`, `mostrar_log`) — patrón del [Tema 5](../../05_programacion_modular/README.md).

👉 [log_eventos.py](./log_eventos.py) — Prueba a ejecutarlo **varias veces seguidas**: verás cómo las entradas se acumulan sin perder las anteriores.

#### 🔍 Ejemplo 2 — Análisis léxico de un fichero

Dado un fichero de texto, cuenta el número total de palabras, las palabras distintas, encuentra la más larga, calcula la longitud media, y muestra el ranking de las 5 más frecuentes y las 5 letras más comunes. Un ejercicio muy natural para estudiantes de matemáticas: la lingüística cuantitativa.

Conceptos que refuerza:

* Lectura completa con `f.read()`.
* Uso de **diccionarios** ([Tema 6](../../06_tipos_compuestos/README.md)) como contadores de frecuencia.
* Combinación con `sorted()` y `max()` para rankings.

👉 [analizar_texto.py](./analizar_texto.py) · [texto.txt](./texto.txt)

#### 📖 Notebook explicado paso a paso

Además de los scripts, hay un notebook que introduce **todas las operaciones básicas** con ficheros de texto (`open`, `read`, `write`, `readline`, `readlines`, `with`, `seek`), con ejemplos ejecutables celda a celda:

👉 [ficheros_texto_exp_py.ipynb](./ficheros_texto_exp_py.ipynb) — usa `mensaje.txt` como ejemplo.

---

### 📄 Bloque 2. Ficheros CSV

Aquí verás dos casos que enriquecen lo visto en clase: **fusionar dos CSV** por una clave común (una idea clave que anticipa el concepto de JOIN de SQL) y **analizar una serie temporal** de temperaturas con estadísticas por semana.

#### 🔗 Ejemplo 3 — Fusionar dos CSV por clave común

En la vida real, los datos suelen venir **repartidos en varios ficheros**. Este ejemplo tiene un CSV con datos personales de estudiantes (`estudiantes.csv`) y otro con sus calificaciones en tres asignaturas (`calificaciones.csv`), ambos ligados por el DNI. El programa los combina en un único fichero `expediente.csv` que además añade una columna calculada `media`.

Conceptos que refuerza:

* Uso de `DictReader` y `DictWriter`.
* Cargar un CSV entero en un **diccionario indexado por clave**, para hacer la fusión eficientemente.
* Manejo del caso en que un estudiante no tenga registro en el otro fichero.
* Cálculo de columnas derivadas.

👉 [fusionar_csvs.py](./fusionar_csvs.py) · [estudiantes.csv](./estudiantes.csv) · [calificaciones.csv](./calificaciones.csv)

#### 🌡️ Ejemplo 4 — Serie temporal de temperaturas de Ciudad Real

Un CSV con las temperaturas mínima y máxima de cada día de un mes en Ciudad Real. El programa calcula el día más caluroso y el más frío, los promedios mensuales, la **media semanal** de la máxima (agrupando por semana ISO usando un `dict`), y cuenta los días con temperaturas de "ola de calor" (≥ 35 °C). Un patrón que se repite en toda la programación científica.

Conceptos que refuerza:

* Conversión de fechas con `datetime.date.fromisoformat()`.
* Uso de `max`/`min` con `key=lambda ...` (recurso del [Tema 6](../../06_tipos_compuestos/README.md)).
* Agrupaciones por período usando diccionarios como acumuladores.
* Filtrado con condiciones.

👉 [temperaturas_serie.py](./temperaturas_serie.py) · [temperaturas_ciudad_real.csv](./temperaturas_ciudad_real.csv)

#### 📖 Notebook explicado paso a paso

Recorre en detalle las variantes de `csv.reader`, `csv.writer`, `DictReader`, `DictWriter`, más el detalle del `newline=""` y el problema del delimitador en español:

👉 [csv_exp_py.ipynb](./csv_exp_py.ipynb)

---

### 🔧 Bloque 3. Ficheros JSON

Un caso realista muy útil de conocer: separar la **configuración de un experimento científico** de su código, para poder cambiar los parámetros sin tocar el programa.

#### 🧪 Ejemplo 5 — Configuración y resultados de un experimento numérico

En investigación es muy común **separar el código del experimento de sus parámetros**: los parámetros van en un JSON (o YAML), y el código los carga al arrancar. Ventaja: cambiar el fichero → cambiar el experimento, sin tocar el código. Este ejemplo lo aplica a un caso clásico: la **estimación por Monte Carlo** de la integral de sen(x) entre 0 y π (que vale 2). Los parámetros (número de muestras, semilla, límites) están en `config.json`; el resultado se guarda en `resultado.json` para poder analizarlo luego.

Conceptos que refuerza:

* Uso de `json.load()` para cargar configuración.
* Uso de `json.dump()` con `indent=2` y `ensure_ascii=False` para guardar resultados legibles.
* Estructura profesional: **cargar → ejecutar → guardar**, todo separado en funciones (T5).
* Un método numérico clásico aplicado a un problema real.

👉 [experimento_config.py](./experimento_config.py) · [config.json](./config.json)

**Ejercicio para experimentar**: edita `config.json` y cambia `n_muestras` a 1.000.000. Vuelve a ejecutar y observa cómo baja el error. Esa es la idea completa.

#### 📖 Notebook explicado paso a paso

Explora las cuatro funciones esenciales de `json` (`load`, `dump`, `loads`, `dumps`), la regla mnemotécnica "con `s` = con string", y datos anidados:

👉 [json_exp_py.ipynb](./json_exp_py.ipynb)

---

### 🌐 Bloque 4. APIs REST

Dos APIs **completamente gratuitas y sin API Key**, para que puedas practicar sin ninguna barrera:

#### 🛰️ Ejemplo 6 — Posición actual de la Estación Espacial Internacional

Este ejemplo tiene un buen componente matemático: consulta la API de [wheretheiss.at](https://wheretheiss.at/) para obtener la posición **en tiempo real** de la ISS (latitud, longitud, altitud, velocidad), y calcula la distancia geodésica a Ciudad Real usando la **fórmula del haversine**:

$$d = 2R \cdot \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\varphi}{2}\right) + \cos(\varphi_1)\cos(\varphi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$

Conceptos que refuerza:

* Llamadas GET simples con `requests.get()`.
* Manejo defensivo de errores de red con `try/except`.
* Interpretación del JSON de respuesta.
* Un cálculo matemático aplicado.

👉 [iss_ubicacion.py](./iss_ubicacion.py) — cada vez que ejecutes verás una posición distinta, porque la ISS se mueve a ~28.000 km/h.

#### 🎓 Ejemplo 7 — Universidades del mundo

La API de [Hipolabs](http://universities.hipolabs.com/) es gratuita y sin API Key. El programa pide un país al usuario, muestra las 10 primeras universidades encontradas, presenta un **ranking de dominios web** (`.es`, `.edu`, `.uk`...), y guarda la lista completa en un JSON.

Conceptos que refuerza:

* Uso de `params` para pasar argumentos a la API.
* Extracción de datos de una lista de dicts.
* Combinación de API + JSON: lo que recibes por HTTP lo guardas para consultarlo después.
* Uso de dicts como contadores (T6).

👉 [universidades_pais.py](./universidades_pais.py)

#### 📖 Notebook explicado paso a paso

Introduce paso a paso `requests.get()`, códigos HTTP, `params`, `.json()`, timeouts, y trabaja con REST Countries y Open-Meteo:

👉 [api_exp_py.ipynb](./api_exp_py.ipynb)

---

### 🗃️ Bloque 5. Bases de datos con SQLite

Aquí introducimos un caso más ambicioso que los de clase: una BBDD con **dos tablas relacionadas**, lo que abre la puerta a consultas más ricas.

#### 📚 Ejemplo 8 — Base de datos de una biblioteca

Una BBDD real con dos tablas relacionadas:

* **`Libros`**: `isbn` (clave primaria), `titulo`, `autor`, `ejemplares_totales`.
* **`Prestamos`**: `id` (autoincremento), `isbn`, `dni_usuario`, `fecha`.

Ambas se ligan por el `isbn`. Sin llegar a hacer JOIN formal, el programa muestra tres consultas prácticas:

1. Los **3 libros más prestados** (uso de `GROUP BY`, `ORDER BY`, `LIMIT`).
2. Los **ejemplares disponibles** de cada libro (totales − préstamos).
3. La **actividad de un usuario** concreto: qué libros ha prestado y cuándo.

Conceptos que refuerza:

* Modelado con **más de una tabla** relacionadas por una clave.
* Uso de `AUTOINCREMENT` para claves generadas automáticamente.
* Consultas cruzadas hechas "a mano" (obtener el `isbn` de una tabla, buscar detalles en la otra).
* `executemany()` para insertar varios registros de golpe.

👉 [biblioteca.py](./biblioteca.py) — crea `biblioteca.db` con datos de ejemplo y ejecuta las tres consultas.

#### 📖 Notebook explicado paso a paso

Recorre el patrón de 5 pasos (conectar → cursor → SQL → commit → cerrar), la inyección SQL y su solución con placeholders `?`, las funciones de agregación y `GROUP BY`, sobre una tabla `Estudiantes`:

👉 [sqlite_exp_py.ipynb](./sqlite_exp_py.ipynb)

---

## 🛠️ Herramientas recomendadas

* [**DB Browser for SQLite**](https://sqlitebrowser.org/) — abre `biblioteca.db` o `universidad.db` y navega visualmente. Muy útil mientras aprendes.
* [**JSONLint**](https://jsonlint.com/) — validar `config.json` o cualquier JSON que produzcas.
* [**Postman**](https://www.postman.com/) o [**HTTPie**](https://httpie.io/) — probar APIs sin escribir código.

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo (min) |
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T7_ICC.md)              |     14       |
| 2      | [Recursos](../recursos/T7_RE_ICC.md)       |      8       |
| 3      | **Ejemplos**                               |      -       |
| 4      | [Ejercicios](../ejercicios/T7_Ejer_ICC.md) |      -       |
|        | [Menú del Tema actual](../README.md)       |      -       |
