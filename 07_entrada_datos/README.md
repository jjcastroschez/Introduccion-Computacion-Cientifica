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

# 💾 Tema 7: Entrada de Datos 🌐

Hasta ahora, los datos que necesitaban tus programas se los proporcionabas **tú** con `input()`. Es una forma perfecta cuando quien ejecuta el programa es un usuario humano dispuesto a teclear. Pero en el mundo real, la mayoría de los datos **no vienen del teclado**: vienen de **ficheros** que dejó otro programa, de **bases de datos** con millones de registros, de **APIs web** que exponen servicios remotos, o directamente de **sensores** que miden fenómenos físicos.

En este tema aprenderás a **liberar a tus programas de la necesidad de tener a alguien delante**. Vas a leer y escribir ficheros de texto, CSV y JSON; vas a llamar a APIs para obtener datos en tiempo real; y vas a manejar tu primera base de datos con SQL. Cada una de estas fuentes tiene sus fortalezas: los ficheros son sencillos y portables, los CSV y JSON son estándares universales de intercambio, las APIs abren la puerta a servicios ajenos, y las bases de datos ofrecen consultas potentes sobre grandes volúmenes.

> [!NOTE]
> Este es probablemente el tema que **más te acerca al mundo profesional**. La inmensa mayoría de los programas científicos, de análisis de datos y de aplicaciones web trabajan con las fuentes que verás aquí. Al final del tema, sabrás construir un programa que lea un CSV, consulte una API, y guarde el resultado en una base de datos: un pipeline completo de datos.

---

## 📚 Contenido del Tema

### 📁 Concepto y organización de los ficheros

Empezamos por lo fundamental: qué es un **fichero**, cómo lo clasifican los sistemas operativos (**texto vs. binario**), y qué significan las **extensiones** que ves cada día (`.txt`, `.csv`, `.json`, `.py`, `.exe`...).

### 🔒 Permisos de ficheros

Los ficheros no son públicos por defecto: cada uno lleva asociados unos **permisos** que dicen quién puede leerlo, modificarlo o ejecutarlo. Aprenderás:

- La notación clásica de UNIX (`-rw-r--r--`) y su equivalente en **notación octal** (`644`, `755`, `600`...).
- El comando **`chmod`** para modificarlos en Linux/Mac, en sus dos modos (octal y simbólico).
- El comando **`icacls`** para gestionarlos en Windows.

### 🗄️ Operaciones básicas con ficheros en Python

El núcleo del tema. Verás:

- La función **`open()`** con sus modos (`"r"` leer, `"w"` escribir, `"a"` añadir).
- Los métodos **`.read()`**, **`.write()`**, **`.readline()`**, **`.readlines()`**, **`.close()`**.
- La construcción **`with open(...) as f:`** que asegura el cierre automático.
- El **cursor** interno de los ficheros y el método **`.seek()`** para reposicionarlo.

### 📄 CSV: datos tabulares

Los ficheros CSV (*Comma-Separated Values*) son el formato universal para intercambiar datos en filas y columnas: los generan las hojas de cálculo, los aceptan las bases de datos, los procesan los programas estadísticos. Aprenderás a leerlos y escribirlos con el módulo **`csv`** de la biblioteca estándar, tanto con `reader`/`writer` como con las versiones más cómodas `DictReader`/`DictWriter`.

### 🔧 JSON: datos estructurados

JSON (*JavaScript Object Notation*) es **el formato dominante** para intercambiar datos entre programas modernos, sobre todo con APIs web. Su sintaxis es prácticamente idéntica a la de los diccionarios y listas de Python, así que el módulo **`json`** convierte entre ambos mundos en una sola línea con **`json.load()`**, **`json.dump()`**, **`json.loads()`** y **`json.dumps()`**.

### 🌐 APIs REST y el módulo `requests`

Una **API** (*Application Programming Interface*) es un servicio remoto al que llamas para pedir o enviar datos. Las APIs **REST** son las más comunes hoy: se accede a ellas por URL, con métodos HTTP (**GET**, **POST**, **PUT**, **DELETE**), y suelen devolver los datos en JSON. Aprenderás a consultarlas con la biblioteca **`requests`**, viendo un caso real con la API pública de **OpenWeatherMap**.

### 🗃️ Bases de datos con SQLite

Cuando los datos crecen o necesitas consultas complejas, los ficheros se quedan cortos. Las **bases de datos relacionales** organizan la información en **tablas** con **filas** y **columnas**, y permiten consultarlas con **SQL** (*Structured Query Language*). Usarás **`sqlite3`**, el módulo estándar de Python que trae una base de datos completa sin necesidad de instalar ningún servidor, para:

- **Crear tablas** con `CREATE TABLE`.
- **Insertar registros** con `INSERT INTO`.
- **Consultar datos** con `SELECT`, con filtros `WHERE`, agrupaciones `GROUP BY` y funciones de agregación (`AVG`, `MAX`, `MIN`, `COUNT`).

### 🌟 Panorama del ecosistema

Al final verás una visión de conjunto de otras bases de datos que encontrarás en el mundo profesional: **PostgreSQL**, **MySQL/MariaDB**, **Oracle**, **MongoDB**, **Redis**... para que sepas cuándo se usa cada una.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema serás capaz de:

### 1. Fundamentos (el "qué" y el "por qué")

- **Identificar** las distintas fuentes de entrada de datos (usuario, ficheros, APIs, BBDD, sensores).
- **Distinguir** entre ficheros de texto y binarios.
- **Interpretar** los permisos de un fichero, tanto en notación simbólica como octal.
- **Comprender** cuándo conviene usar cada formato de datos (CSV vs. JSON vs. BBDD).
- **Entender** qué es una API REST y cómo se comunica un programa con ella.

### 2. Representación (el "cómo se expresa")

- **Aplicar** los modos de apertura de ficheros (`"r"`, `"w"`, `"a"`) según el objetivo.
- **Escribir** código con `with open(...) as f:` que gestiona el cierre automáticamente.
- **Modelar** datos tabulares con CSV y datos estructurados con JSON.
- **Diseñar** una tabla simple en SQLite, con clave primaria y tipos adecuados.

### 3. Capacidad aplicada (el "cómo se usa")

- **Leer y escribir** ficheros de texto plano usando `read`, `write`, `readline`, `readlines`.
- **Procesar** un CSV completo, tanto por posiciones como por nombres de columna.
- **Cargar y guardar** ficheros JSON como diccionarios de Python.
- **Consultar** APIs REST con `requests`, manejando códigos HTTP e interpretando JSON.
- **Ejecutar** operaciones básicas en SQLite: crear tabla, insertar registros, consultar con filtros y agregaciones.
- **Combinar** todas estas fuentes en un pipeline: leer un CSV, procesarlo, llamar a una API, guardarlo en una BBDD.

---

## ✅ Resultados de Aprendizaje

Podrás marcar como completados:

- [ ] **Leer y escribir** ficheros de texto usando `open`, `read`, `write`, `close` y el bloque `with`.
- [ ] **Recorrer** un fichero línea por línea con `readline`, `readlines` o iterando directamente.
- [ ] **Reposicionar** el cursor de un fichero con `.seek()`.
- [ ] **Interpretar** una cadena de permisos como `-rwxr-xr-x` y su equivalente octal.
- [ ] **Modificar** los permisos de un fichero con `chmod` o `icacls`.
- [ ] **Leer y escribir** ficheros CSV con el módulo `csv` (`reader`/`writer` y `DictReader`/`DictWriter`).
- [ ] **Cargar y guardar** datos JSON con `json.load`, `json.dump`, `json.loads`, `json.dumps`.
- [ ] **Realizar** peticiones HTTP a una API REST con `requests.get()`.
- [ ] **Interpretar** códigos HTTP (200, 401, 404) y respuestas JSON.
- [ ] **Crear** una base de datos SQLite y una tabla con `CREATE TABLE`.
- [ ] **Insertar** registros de forma segura usando parámetros con `?`.
- [ ] **Consultar** una tabla con `SELECT`, filtrar con `WHERE`, agrupar con `GROUP BY`, agregar con `AVG`/`MAX`/`MIN`/`COUNT`.
- [ ] **Confirmar** los cambios en una base de datos con `commit` y cerrar la conexión.
- [ ] **Comprender** el problema de la inyección SQL y cómo evitarlo.

---

## 🧭 Menú de Navegación en el Tema

| Orden | Material | Tiempo |
| ----- | -------- | ------ |
| 1     | [Teoría](./teoria/T7_ICC.md)              |   14   |
| 2     | [Recursos](./recursos/T7_RE_ICC.md)       |    8   |
| 3     | [Ejemplos](./ejemplos/T7_Ejem_ICC.md)     |    –   |
| 4     | [Ejercicios](./ejercicios/T7_Ejer_ICC.md) |    –   |
|       | [Menú de Temas](../README.md)                                     |    -   |
