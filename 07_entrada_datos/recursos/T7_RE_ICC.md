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


# 🔗 Recursos - Tema 7: Entrada de Datos 💾

Este tema abre la puerta a un mundo enorme: ficheros, APIs, bases de datos. Aquí tienes las mejores referencias oficiales, herramientas gráficas para inspeccionar los datos, y algunos servicios de APIs gratuitas con los que practicar sin coste.

---

## 📚 Documentación oficial de Python

### 📁 Ficheros y sistema de archivos

- 📍 **[`open()` — tutorial oficial](https://docs.python.org/es/3/tutorial/inputoutput.html#reading-and-writing-files)** — introducción muy clara con ejemplos. El punto de partida.
- 📍 **[Métodos de objetos file](https://docs.python.org/es/3/library/io.html)** — la referencia completa: `read`, `write`, `readline`, `seek`, `tell`, `flush`...
- 📍 **[Módulo `os.path`](https://docs.python.org/es/3/library/os.path.html)** — para construir rutas de fichero portables (Windows/Linux).
- 📍 **[Módulo `pathlib`](https://docs.python.org/es/3/library/pathlib.html)** — la forma **moderna** de manejar rutas y ficheros (objetos `Path` con métodos). Muy recomendable.

### 📄 CSV, JSON y formatos de datos

- 📍 **[Módulo `csv`](https://docs.python.org/es/3/library/csv.html)** — la referencia completa: `reader`, `writer`, `DictReader`, `DictWriter`, dialectos.
- 📍 **[Módulo `json`](https://docs.python.org/es/3/library/json.html)** — las cuatro funciones `load`, `dump`, `loads`, `dumps` y sus parámetros.
- 📍 **[Especificación oficial de JSON](https://www.json.org/json-es.html)** — para saber qué es JSON estándar (útil para depurar formatos ajenos).

### 🌐 APIs HTTP

- 📍 **[Biblioteca `requests`](https://requests.readthedocs.io/en/latest/)** — documentación oficial, muy legible, con muchos ejemplos.
- 📍 **[Módulo `urllib`](https://docs.python.org/es/3/library/urllib.html)** — la alternativa que viene de serie en Python (más verbosa que `requests`).
- 📍 **[Códigos de estado HTTP en MDN](https://developer.mozilla.org/es/docs/Web/HTTP/Status)** — referencia clara de todos los códigos (200, 404, 500...) con explicaciones.

### 🗃️ Bases de datos

- 📍 **[Módulo `sqlite3`](https://docs.python.org/es/3/library/sqlite3.html)** — la referencia oficial en español. Incluye tutorial paso a paso.
- 📍 **[Documentación de SQLite](https://sqlite.org/docs.html)** — la BBDD en sí (independiente de Python). Muy completa.
- 📍 **[PEP 249 — Python Database API v2.0](https://peps.python.org/pep-0249/)** — la especificación estándar que siguen `sqlite3`, `psycopg2` (PostgreSQL), `mysql-connector`... Al aprender uno, los aprendes todos.

---

## 🛠️ Herramientas visuales imprescindibles

### 🗃️ Para inspeccionar bases de datos

- 📍 **[DB Browser for SQLite](https://sqlitebrowser.org/)** — herramienta **gratuita y multiplataforma** que te permite abrir tu fichero `.db`, ver las tablas, ejecutar consultas SQL, editar registros... Cuando desarrolles con SQLite, tenerla al lado ahorra muchísimo tiempo.
- 📍 **[DBeaver Community](https://dbeaver.io/)** — para cuando trabajes con bases de datos más allá de SQLite (PostgreSQL, MySQL, Oracle...). Herramienta profesional gratuita.

### 📄 Para inspeccionar CSV y JSON

- 📍 **[JSONLint](https://jsonlint.com/)** — validador online de JSON: pegas tu JSON y te dice si es válido o dónde está el error.
- 📍 **[CSV Lint](https://csvlint.io/)** — equivalente para ficheros CSV.
- 📍 **[Modelica CSV Viewer (VS Code)](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv)** — extensión de VS Code para editar CSV cómodamente.

### 🌐 Para explorar APIs

- 📍 **[Postman](https://www.postman.com/)** — herramienta profesional para explorar APIs. Puedes hacer llamadas GET/POST/PUT/DELETE sin escribir código.
- 📍 **[Insomnia](https://insomnia.rest/)** — alternativa libre y minimalista de Postman.
- 📍 **[HTTPie](https://httpie.io/)** — cliente de línea de comandos elegante para APIs. Ideal cuando ya prefieres una terminal.

---

## 🎁 APIs públicas gratuitas para practicar

Cuando estés aprendiendo a llamar a APIs, no compres nada de entrada. Estas son **gratis** (algunas requieren registro para obtener una API Key, todas tienen plan gratuito):

### 🌤️ Meteorología

- 📍 **[OpenWeatherMap](https://openweathermap.org/api)** — la del ejemplo del tema. Necesita registro. 1.000 llamadas al día gratis.
- 📍 **[Open-Meteo](https://open-meteo.com/)** — meteorología **sin API Key**. Ideal para pruebas rápidas.

### 🎮 Datos temáticos (sin API Key)

- 📍 **[PokéAPI](https://pokeapi.co/)** — todo sobre Pokémon, sin API Key.
- 📍 **[Star Wars API](https://swapi.py4e.com/)** — personajes, planetas y naves del universo Star Wars.
- 📍 **[REST Countries](https://restcountries.com/)** — información de todos los países del mundo (población, capital, idiomas, monedas...). **Ideal para prácticas** y ejercicios.

### 📈 Datos serios (para trabajos)

- 📍 **[INE — API de datos abiertos de España](https://www.ine.es/dyngs/DAB/index.htm?cid=1099)** — el Instituto Nacional de Estadística de España, gratis.
- 📍 **[Eurostat API](https://ec.europa.eu/eurostat/web/main/data/web-services)** — datos oficiales de la Unión Europea.
- 📍 **[World Bank API](https://data.worldbank.org/)** — indicadores económicos y sociales de todo el mundo.
> [!TIP]
> **Consejo para prácticas**: empieza con **PokéAPI** o **REST Countries** porque no necesitan API Key y ofrecen respuestas JSON muy claras. Ideales para tus primeros ejercicios.

---

## 📊 Referencia rápida de SQL

Los comandos SQL más útiles para tener a mano al principio:

```sql
-- Crear tabla
CREATE TABLE IF NOT EXISTS nombre_tabla (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER,
    nota REAL
);

-- Insertar
INSERT INTO nombre_tabla VALUES (?, ?, ?, ?);
INSERT INTO nombre_tabla (nombre, edad) VALUES (?, ?);   -- solo algunas columnas

-- Consultar
SELECT * FROM nombre_tabla;
SELECT nombre, nota FROM nombre_tabla WHERE edad > 18;
SELECT * FROM nombre_tabla WHERE nombre LIKE 'A%';       -- empieza por A
SELECT * FROM nombre_tabla ORDER BY nota DESC LIMIT 10;

-- Agregar
SELECT AVG(nota) FROM nombre_tabla;
SELECT COUNT(*) FROM nombre_tabla WHERE edad >= 18;
SELECT edad, COUNT(*), AVG(nota) FROM nombre_tabla GROUP BY edad;

-- Modificar y eliminar
UPDATE nombre_tabla SET nota = 10 WHERE id = 1;
DELETE FROM nombre_tabla WHERE edad < 18;

-- Borrar tabla
DROP TABLE nombre_tabla;
```

### 📖 Tutoriales de SQL

- 📍 **[SQLBolt](https://sqlbolt.com/)** — lecciones interactivas paso a paso. **Muy recomendable** para empezar.
- 📍 **[W3Schools SQL](https://www.w3schools.com/sql/)** — tutorial clásico, muy útil como referencia.
- 📍 **[SQLite Tutorial](https://www.sqlitetutorial.net/)** — enfocado específicamente a SQLite.

---

## 🐛 Errores más frecuentes y cómo diagnosticarlos

| Error | Causa habitual | Solución |
|:---|:---|:---|
| `FileNotFoundError: [Errno 2]` | El fichero no existe o la ruta es incorrecta | Comprueba con `os.path.exists()` antes; usa rutas absolutas si dudas |
| `PermissionError: [Errno 13]` | No tienes permisos de lectura/escritura | Revisa los permisos con `ls -la` (Linux/Mac) o `icacls` (Windows) |
| `UnicodeDecodeError` | El fichero no está en UTF-8 (típico en CSV de Excel español) | Añade `encoding="latin-1"` o `encoding="cp1252"` al `open` |
| Fichero queda vacío tras `w` | Abriste en modo `"w"` sin querer y borraste el contenido | Antes de sobreescribir, **haz backup** o abre con `"r+"` con cuidado |
| `json.JSONDecodeError` | El JSON está mal formado o vacío | Valida con [JSONLint](https://jsonlint.com/) |
| `sqlite3.OperationalError: table X already exists` | Intentaste crear una tabla que ya existe | Usa `CREATE TABLE IF NOT EXISTS X` |
| `sqlite3.IntegrityError: UNIQUE constraint failed` | Insertaste dos veces la misma clave primaria | Comprueba antes con `SELECT` o usa `INSERT OR REPLACE` |
| Los cambios en la BBDD "desaparecen" | Olvidaste el `conexion.commit()` | Añádelo antes del `close()` |
| Respuesta HTTP con `.text` vacío | Estás llamando bien pero la API espera parámetros distintos | Comprueba `respuesta.status_code` y `respuesta.text` |

---

## 🃏 Chuletas rápidas

### `open` y ficheros de texto

```python
# Leer completo
with open("archivo.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Leer línea a línea
with open("archivo.txt") as f:
    for linea in f:
        print(linea.rstrip())    # rstrip quita el \n final

# Escribir
with open("salida.txt", "w") as f:
    f.write("Hola\n")
    f.write("Adiós\n")

# Añadir al final
with open("log.txt", "a") as f:
    f.write("Nuevo evento\n")
```

### CSV con `DictReader` / `DictWriter`

```python
# Leer
with open("datos.csv") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"], fila["nota"])

# Escribir
with open("salida.csv", "w", newline="") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "nota"])
    escritor.writeheader()
    escritor.writerow({"nombre": "Ana", "nota": 8.5})
```

### JSON

```python
# Leer
with open("datos.json") as f:
    datos = json.load(f)

# Escribir
with open("salida.json", "w") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)
```

### API GET con `requests`

```python
respuesta = requests.get(url, params={"q": "Madrid"})
if respuesta.status_code == 200:
    datos = respuesta.json()
```

### SQLite básico

```python
conexion = sqlite3.connect("mi.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS T (id INTEGER PRIMARY KEY, x REAL)")
cursor.execute("INSERT INTO T VALUES (?, ?)", (1, 3.14))
conexion.commit()

cursor.execute("SELECT * FROM T WHERE x > ?", (0,))
for fila in cursor.fetchall():
    print(fila)

conexion.close()
```

---

## 🧭 Menú de Navegación

| Orden | Material | Tiempo |
|:-----:|:---------|:------:|
| 1     | [Teoría](../teoria/T7_ICC.md)             |  14   |
| 2     | **Recursos**                              |   8   |
| 3     | [Ejemplos](../ejemplos/T7_Ejem_ICC.md)    |   –   |
| 4     | [Ejercicios](../ejercicios/T7_Ejer_ICC.md)|   –   |
|       | [Menú del Tema actual](../README.md)      |   -   |
