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

# 🏋️ Ejercicios - Tema 7: Entrada de Datos 💾

Con el Tema 7 tus programas dejan de depender de un usuario tecleando: los datos ahora vienen de **ficheros**, **APIs** y **bases de datos**. En estos ejercicios vas a practicar cada una de esas fuentes, empezando por operaciones básicas con ficheros de texto, pasando por CSV y JSON, y terminando con SQL en SQLite y con una API pública. El reto final integra todo en un pipeline realista.

> [!TIP]
> Como en temas anteriores: **intenta primero**, sin mirar la solución. Cuando estés atascado, o cuando termines y quieras contrastar tu enfoque, despliega la sección "Mira cómo quedaría la implementación...". El objetivo no es "copiar el código correcto", sino construir tu propia intuición sobre cómo se atacan estos problemas.
>
> Los ejercicios usan los mismos ficheros de datos que hay en la carpeta [ejemplos](../ejemplos/): `mensaje.txt`, `notas_clase.csv`, `libro.json`, etc. Cópialos a tu carpeta de trabajo antes de empezar.

---

## 🟢 Nivel básico — Ficheros de texto

### Ejercicio 1 — Copiar un fichero línea a línea

Escribe una función `copiar_fichero(origen, destino)` que copie el contenido de un fichero de texto a otro. Pruébala copiando `mensaje.txt` a `copia.txt`. Devuelve el número de líneas copiadas.

**Pistas**:

- Se puede abrir dos ficheros en el mismo `with`: `with open(...) as fin, open(...) as fout:`.
- Iterar directamente sobre el fichero (`for linea in fin:`) es la forma más elegante.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def copiar_fichero(origen: str, destino: str) -> int:
    n = 0
    with open(origen, "r") as fin, open(destino, "w") as fout:
        for linea in fin:
            fout.write(linea)
            n = n + 1
    return n

def main():
    lineas = copiar_fichero("mensaje.txt", "copia.txt")
    print(f"✅ Copiadas {lineas} líneas")

if __name__ == "__main__":
    main()
```

**Comentarios**:

- Fíjate en el patrón `for linea in fin:` — Python itera línea a línea sin necesidad de llamar a `readline` explícitamente.
- Al iterar así, `linea` **incluye el `\n`** final, por eso lo escribimos directamente sin añadirlo.
- Ejemplo completo: [copiar_fichero.py](./copiar_fichero.py).
</details>

---

### Ejercicio 2 — Contar líneas, palabras y caracteres

Implementa una versión Python del clásico comando UNIX **`wc`**. Escribe una función `contar(fichero)` que devuelva una tupla `(líneas, palabras, caracteres)`. Pruébala con `mensaje.txt`.

**Pista**: `linea.split()` sin argumentos divide por cualquier espacio en blanco. La longitud de la lista resultante es el número de palabras.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
def contar(fichero: str) -> tuple:
    lineas = 0
    palabras = 0
    caracteres = 0

    with open(fichero, "r") as f:
        for linea in f:
            lineas = lineas + 1
            palabras = palabras + len(linea.split())
            caracteres = caracteres + len(linea)

    return lineas, palabras, caracteres

def main():
    l, p, c = contar("mensaje.txt")
    print(f"Líneas:     {l}")
    print(f"Palabras:   {p}")
    print(f"Caracteres: {c}")

if __name__ == "__main__":
    main()
```

**Comentarios**:

- Reutilizamos el patrón de iteración del ejercicio 1: recorrer línea a línea en un solo pase.
- `split()` sin argumentos es más robusto que `split(" ")` porque agrupa espacios múltiples y también saltos de línea.
- Ejemplo completo: [contar_wc.py](./contar_wc.py).
</details>

---

## 🟡 Nivel intermedio — CSV

### Ejercicio 3 — Añadir una columna calculada

Dado el fichero `notas_clase.csv` (columnas: `nombre`, `curso`, `nota`), genera un CSV nuevo `notas_con_estado.csv` que tenga una columna adicional `estado` con valor `"Aprobado"` (si la nota es ≥ 5) o `"Suspenso"` (si es < 5). Las columnas originales se mantienen.

**Pistas**:

- Al escribir, indica `fieldnames = list(lector.fieldnames) + ["estado"]`.
- Puedes modificar cada `fila` (que es un dict) directamente antes de escribirla.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import csv

def anadir_estado(csv_origen: str, csv_destino: str) -> None:
    with open(csv_origen, "r") as fin:
        lector = csv.DictReader(fin)
        campos = list(lector.fieldnames) + ["estado"]

        with open(csv_destino, "w", newline="") as fout:
            escritor = csv.DictWriter(fout, fieldnames=campos)
            escritor.writeheader()

            for fila in lector:
                nota = float(fila["nota"])
                fila["estado"] = "Aprobado" if nota >= 5 else "Suspenso"
                escritor.writerow(fila)
```

**Comentarios**:

- El patrón "abrir ambos ficheros en el mismo `with`" evita variables intermedias (una lista de todo el CSV en memoria), lo que sería ineficiente con ficheros grandes.
- `float(fila["nota"])` es obligatorio: si comparas directamente con `>=`, la cadena `"4.5"` como texto se comparará **alfabéticamente** con `5`, dando resultados absurdos.
- Ejemplo completo: [anadir_columna.py](./anadir_columna.py).
</details>

---

### Ejercicio 4 — Filtrar un CSV

Escribe una función `filtrar_csv(origen, destino, umbral=7.0)` que copie a `destino` solo las filas de `origen` cuya `nota` sea ≥ `umbral`. Manteniendo las mismas columnas. Devuelve el número de filas escritas.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import csv

def filtrar_csv(origen: str, destino: str, umbral: float = 7.0) -> int:
    n = 0
    with open(origen, "r") as fin:
        lector = csv.DictReader(fin)
        with open(destino, "w", newline="") as fout:
            escritor = csv.DictWriter(fout, fieldnames=lector.fieldnames)
            escritor.writeheader()
            for fila in lector:
                if float(fila["nota"]) >= umbral:
                    escritor.writerow(fila)
                    n = n + 1
    return n
```

**Comentarios**:

- `lector.fieldnames` te da directamente los nombres de columna del CSV origen, lo que evita tener que declararlos a mano.
- Cambia el `umbral` desde el `main` para reutilizar la función en distintos casos (5.0 para aprobados, 9.0 para sobresalientes...).
- Ejemplo completo: [filtrar_csv.py](./filtrar_csv.py).
</details>

---

## 🟠 Nivel intermedio — JSON

### Ejercicio 5 — Modificar un JSON

Carga `libro.json`, incrementa el campo `paginas` en 10, añade el tema `"edición ampliada"` a la lista `temas`, y guarda el resultado en `libro_modificado.json` (con `indent=2` y `ensure_ascii=False`).

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import json

def main():
    with open("libro.json", "r") as f:
        datos = json.load(f)

    datos["paginas"] = datos["paginas"] + 10
    datos["temas"].append("edición ampliada")

    with open("libro_modificado.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

    print("✅ Guardado.")

if __name__ == "__main__":
    main()
```

**Comentarios**:

- Fíjate en la elegancia del patrón: **leer → modificar como un dict normal → guardar**. Como JSON se convierte directamente a estructuras Python, trabajas con los datos como si fueran cualquier `dict`.
- `datos["temas"].append(...)` es directo porque `temas` ya es una lista Python (no un string).
- Ejemplo completo: [modificar_json.py](./modificar_json.py).
</details>

---

### Ejercicio 6 — Convertir CSV a JSON

Escribe una función `csv_a_json(csv_origen, json_destino)` que lea un CSV y produzca un JSON con una **lista de diccionarios**, uno por cada fila. Convierte los tipos: `curso` a int, `nota` a float.

Pruébala con `notas_clase.csv`.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import csv
import json

def csv_a_json(csv_origen: str, json_destino: str) -> int:
    estudiantes = []
    with open(csv_origen, "r") as f:
        for fila in csv.DictReader(f):
            estudiantes.append({
                "nombre": fila["nombre"],
                "curso":  int(fila["curso"]),
                "nota":   float(fila["nota"]),
            })

    with open(json_destino, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, indent=2, ensure_ascii=False)

    return len(estudiantes)
```

**Comentarios**:

- Este ejercicio muestra la ventaja de JSON sobre CSV: mientras que en CSV `curso` y `nota` son cadenas, en JSON los guardas ya como int y float. Al volver a leerlo, no hará falta convertir de nuevo.
- Podrías hacer directamente `estudiantes.append(dict(fila))`, pero perderías las conversiones de tipo. Lo mejor es construir explícitamente el dict con los tipos correctos.
- Ejemplo completo: [csv_a_json.py](./csv_a_json.py).
</details>

---

## 🔵 Nivel avanzado — SQLite

### Ejercicio 7 — Estadísticas por grupos

Crea una BBDD `empresa.db` con una tabla `Ventas(id, vendedor, mes, importe)`, inserta al menos 9 registros con al menos 3 vendedores y 3 meses distintos, y responde con SQL:

- **a)** Total vendido por vendedor (ordenado descendente).
- **b)** Total vendido por mes (ordenado descendente).
- **c)** ¿Cuál es el mes con más ventas totales?
- **d)** ¿Cuál es el vendedor con mayor venta promedio?

**Pista**: El poder aquí está en `GROUP BY vendedor` y `GROUP BY mes`, combinados con `SUM(importe)`, `AVG(importe)` y `ORDER BY`.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import sqlite3

conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendedor TEXT,
        mes TEXT,
        importe REAL
    )
""")
cursor.execute("DELETE FROM Ventas")

ventas = [
    ("Ana", "enero", 1200.0), ("Ana", "febrero", 1500.0), ("Ana", "marzo", 1100.0),
    ("Luis", "enero", 1800.0), ("Luis", "febrero", 2100.0), ("Luis", "marzo", 1600.0),
    ("Marta", "enero", 900.0), ("Marta", "febrero", 1300.0), ("Marta", "marzo", 1400.0),
]
for v in ventas:
    cursor.execute("INSERT INTO Ventas (vendedor, mes, importe) VALUES (?, ?, ?)", v)
conexion.commit()

# a) Total por vendedor
cursor.execute("""
    SELECT vendedor, SUM(importe) FROM Ventas
    GROUP BY vendedor
    ORDER BY SUM(importe) DESC
""")
for vendedor, total in cursor.fetchall():
    print(f"{vendedor}: {total:.2f} €")

# b) Total por mes
cursor.execute("SELECT mes, SUM(importe) FROM Ventas GROUP BY mes ORDER BY SUM(importe) DESC")
# ... etc

# c) Mejor mes: la primera fila del apartado b)
cursor.execute("SELECT mes, SUM(importe) FROM Ventas GROUP BY mes ORDER BY SUM(importe) DESC LIMIT 1")
mejor_mes, total = cursor.fetchone()
print(f"Mejor mes: {mejor_mes} con {total:.2f} €")

# d) Vendedor con mejor promedio
cursor.execute("SELECT vendedor, AVG(importe) FROM Ventas GROUP BY vendedor ORDER BY AVG(importe) DESC LIMIT 1")
mejor_vendedor, media = cursor.fetchone()
print(f"Mejor vendedor: {mejor_vendedor} con {media:.2f} € de media")

conexion.close()
```

**Comentarios**:

- El truco de este ejercicio es que **casi todo el trabajo lo hace SQL**, no Python. Sin `GROUP BY`, tendrías que acumular manualmente los totales en un diccionario por vendedor y por mes.
- El `LIMIT 1` combinado con `ORDER BY ... DESC` es un patrón muy útil para "obtener el mayor/el menor de algo".
- Ejemplo completo: [estadisticas_sqlite.py](./estadisticas_sqlite.py).
</details>

---

### Ejercicio 8 — Cargar un CSV en SQLite

Escribe una función `cargar_csv_a_bbdd(csv_origen, bbdd)` que:

1. Cree una tabla `Alumnos(id AUTOINCREMENT, nombre, curso, nota)` en la BBDD `bbdd`.
2. Recorra el CSV origen y por cada fila haga un `INSERT` en la tabla (con placeholders `?`).
3. Devuelva el número de registros insertados.

Pruébala con `notas_clase.csv` → `clase.db`, y luego consulta la tabla con un `SELECT` ordenado por nota descendente.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import csv
import sqlite3

def cargar_csv_a_bbdd(csv_origen: str, bbdd: str) -> int:
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            curso INTEGER,
            nota REAL
        )
    """)
    cursor.execute("DELETE FROM Alumnos")

    n = 0
    with open(csv_origen, "r") as f:
        for fila in csv.DictReader(f):
            cursor.execute(
                "INSERT INTO Alumnos (nombre, curso, nota) VALUES (?, ?, ?)",
                (fila["nombre"], int(fila["curso"]), float(fila["nota"]))
            )
            n = n + 1

    conexion.commit()
    conexion.close()
    return n
```

**Comentarios**:

- Este patrón (importar un CSV a una BBDD) es **omnipresente** en el mundo profesional. Casi todos los ETL (Extract, Transform, Load) empiezan así.
- Fíjate en el uso de `id AUTOINCREMENT`: SQLite genera un identificador único para cada fila automáticamente, así que no tenemos que preocuparnos por eso.
- Ejemplo completo: [csv_a_sqlite.py](./csv_a_sqlite.py).
</details>

---

### Ejercicio 9 — Exportar SQLite a JSON

Escribe una función `exportar_tabla_a_json(bbdd, tabla, fichero_json)` que:

1. Se conecte a la BBDD.
2. Ejecute `SELECT * FROM tabla`.
3. Convierta cada fila en un dict `{columna1: valor1, columna2: valor2, ...}` usando los nombres de columna (accesibles con `cursor.description`).
4. Guarde todo como una **lista de dicts** en formato JSON.

Es el ejercicio inverso al anterior: BBDD → JSON. Muy útil para publicar datos abiertos.

**Pista**: `cursor.description` devuelve una lista de tuplas, y el nombre de la columna es el **primer elemento** de cada tupla.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import json
import sqlite3

def exportar_tabla_a_json(bbdd: str, tabla: str, fichero_json: str) -> int:
    conexion = sqlite3.connect(bbdd)
    cursor = conexion.cursor()

    cursor.execute(f"SELECT * FROM {tabla}")
    columnas = [descripcion[0] for descripcion in cursor.description]

    registros = []
    for fila in cursor.fetchall():
        registro = {}
        for i, columna in enumerate(columnas):
            registro[columna] = fila[i]
        registros.append(registro)

    conexion.close()

    with open(fichero_json, "w", encoding="utf-8") as f:
        json.dump(registros, f, indent=2, ensure_ascii=False)

    return len(registros)
```

**Comentarios**:

- Este ejercicio combina las tres piezas del tema: SQL, dicts (T6) y JSON.
- Un detalle sutil: en el `f"SELECT * FROM {tabla}"` estamos poniendo un nombre de tabla directamente en el SQL, **no un valor de datos**. Los placeholders `?` son para datos, no para nombres de tabla ni de columna. Si la función la usa **solo tu código** (nunca un valor introducido por un usuario), es aceptable.
- Ejemplo completo: [sqlite_a_json.py](./sqlite_a_json.py).
</details>

---

## 🟣 Nivel avanzado — APIs

### Ejercicio 10 — Consultar la PokéAPI

La **[PokéAPI](https://pokeapi.co/)** es una API pública, gratuita, y **no requiere API Key**. La URL para consultar un Pokémon es:

```text
https://pokeapi.co/api/v2/pokemon/{nombre}
```

Escribe un programa que pida al usuario el nombre de un Pokémon, consulte la API, y muestre:

- Número (`id`).
- Altura (`height`, en decímetros — divide entre 10 para obtener metros).
- Peso (`weight`, en hectogramos — divide entre 10 para obtener kg).
- Los **tipos** (agua, fuego, etc.).
- Las **habilidades**.
- Las estadísticas base.

Debes manejar el caso de que la API responda con **404** (Pokémon no encontrado).

**Pistas**:

- Los tipos vienen como lista de dicts: `datos["types"]` es una lista donde cada elemento es como `{"slot": 1, "type": {"name": "electric", ...}}`. Para extraer solo los nombres: recórrela y toma `t["type"]["name"]`.
- Igual con habilidades y estadísticas.

<details>
<summary>🫣 Mira cómo quedaría la implementación...</summary>

```python
import requests

def obtener_pokemon(nombre: str) -> dict:
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower().strip()}"
    try:
        respuesta = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None

    if respuesta.status_code == 200:
        return respuesta.json()
    elif respuesta.status_code == 404:
        print(f"❌ Pokémon '{nombre}' no encontrado.")
    else:
        print(f"❌ Error {respuesta.status_code}")
    return None

def mostrar_pokemon(datos: dict) -> None:
    print(f"📋 {datos['name'].upper()}   Nº {datos['id']}")
    print(f"Altura:  {datos['height'] / 10:.1f} m")
    print(f"Peso:    {datos['weight'] / 10:.1f} kg")

    tipos = [t["type"]["name"] for t in datos["types"]]
    print(f"Tipos:   {', '.join(tipos)}")

    habilidades = [h["ability"]["name"] for h in datos["abilities"]]
    print(f"Habilidades: {', '.join(habilidades)}")

    for stat in datos["stats"]:
        print(f"  {stat['stat']['name']:15} {stat['base_stat']:>3}")

def main():
    nombre = input("Introduce el nombre de un Pokémon: ")
    datos = obtener_pokemon(nombre)
    if datos is not None:
        mostrar_pokemon(datos)

if __name__ == "__main__":
    main()
```

**Comentarios**:

- El detalle más delicado es **navegar por el JSON anidado**. Cuando trabajas con una API que no conoces, imprime primero `datos` en bruto y estúdiala.
- El `try/except` sobre `requests.exceptions.RequestException` cubre los casos más frecuentes: no hay Internet, la máquina remota no responde, timeout... En un programa real es imprescindible.
- Ejemplo completo: [consultar_pokeapi.py](./consultar_pokeapi.py).
</details>

---

## 🎯 Reto final — Pipeline de datos completo

Un **pipeline de datos** es un flujo que combina varias fuentes y transformaciones para producir un resultado útil. Vamos a construir uno pequeño que integra **todo** lo que has aprendido en el tema.

### Enunciado

Escribe un programa que haga lo siguiente:

1. **Lee** un CSV `paises.csv` con una única columna `pais` que contiene los nombres (en inglés) de varios países. Puedes crearlo tú con unos 5-10 países. Por ejemplo:

   ```csv
   pais
   spain
   portugal
   france
   germany
   japan
   ```

2. Para cada país del CSV, **consulta la [REST Countries API](https://restcountries.com/)** en la URL:

   ```text
   https://restcountries.com/v3.1/name/{pais}
   ```

   Y extrae:
   - Nombre común (`name.common`).
   - Capital (`capital[0]`).
   - Región (`region`).
   - Población (`population`).
   - Superficie (`area`).

3. **Guarda** los resultados en una BBDD SQLite `mundo.db` con una tabla `Paises` con esas 5 columnas más un `id`.

4. **Genera un informe** que muestre:
   - El listado de países guardados en la BBDD, ordenados por población descendente.
   - La **población total** de todos los países del CSV.
   - La región con **más países** en el CSV (uno o varios países pueden compartir región).

5. **Exporta** todos los datos de la tabla como un fichero `mundo.json`.

### Objetivos pedagógicos del reto

Este reto combina:

- **Ficheros CSV** (leer una lista de entrada).
- **APIs REST** (obtener datos externos, uno por país).
- **JSON** (procesar las respuestas y exportar al final).
- **SQLite** (almacenar y consultar los datos).
- **Manejo de errores** (¿qué haces si un país no existe en la API?).
- **Estructura del programa** (funciones separadas para cada etapa: Tema 5).

### Sugerencia de estructura

```python
def leer_paises_csv(fichero):        # devuelve una lista de nombres
    ...

def consultar_pais(nombre):           # devuelve dict con datos, o None si falla
    ...

def crear_bbdd(bbdd):                 # crea/limpia la tabla Paises
    ...

def guardar_pais(bbdd, datos):        # inserta un país en la BBDD
    ...

def generar_informe(bbdd):            # consulta la BBDD y muestra resultados
    ...

def exportar_bbdd_a_json(bbdd, salida):
    ...

def main():
    paises = leer_paises_csv("paises.csv")
    crear_bbdd("mundo.db")
    for nombre in paises:
        datos = consultar_pais(nombre)
        if datos:
            guardar_pais("mundo.db", datos)
    generar_informe("mundo.db")
    exportar_bbdd_a_json("mundo.db", "mundo.json")
```

### 💡 Consejos

- Empieza probando **una sola llamada a la API** con un país conocido. Imprime la respuesta y estúdiala antes de escribir el código que la procesa.
- **No** almacenes en la BBDD países que la API no ha devuelto (usa un `if datos is not None:`).
- Añade `time.sleep(0.5)` entre llamadas para no saturar la API si el CSV tiene muchos países. Es una cortesía profesional.
- Este reto **no tiene solución publicada**: es el momento de que apliques todo lo que has aprendido y encuentres tu propio camino. Cuando lo consigas, tendrás una idea muy clara de qué es un pipeline de datos.

---

## 🎓 ¿Qué has aprendido en estos ejercicios?

Al completar estos 10 ejercicios y el reto, sabrás:

- **Manipular ficheros de texto** con las operaciones esenciales de I/O.
- **Procesar CSV** para leer, filtrar, transformar y escribir datos tabulares.
- **Manejar JSON** para representar datos estructurados y comunicarte con APIs.
- **Combinar** CSV, JSON y SQLite en flujos completos (el patrón profesional).
- **Consultar APIs REST** con manejo defensivo de errores y códigos HTTP.
- **Consultar BBDD** con SQL, incluyendo `WHERE`, `GROUP BY`, `AVG`, `SUM`, `MAX`.
- **Escribir código robusto** que anticipa errores en los datos y en la red.

Estas son las herramientas básicas con las que se construyen los **pipelines de datos** en la vida profesional. En temas posteriores verás cómo `numpy` y `pandas` te ofrecen versiones más potentes de muchas de estas operaciones, pero la lógica que has aprendido aquí sigue siendo la misma.

---

## 🧭 Menú de Navegación

| Orden  | Material                                | Tiempo (min) |
|:------:|:----------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T7_ICC.md)           |     14       |
| 2      | [Recursos](../recursos/T7_RE_ICC.md)    |      8       |
| 3      | [Ejemplos](../ejemplos/T7_Ejem_ICC.md)  |      -       |
| 4      | **Ejercicios**                          |      -       |
|        | [Menú del Tema actual](../README.md)    |      -       |
