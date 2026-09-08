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

# 📘 Teoría - Tema 7: Entrada de Datos 💾

> [!NOTE]
> Este documento **no sustituye** a las transparencias de clase: las **complementa**. Aquí encontrarás analogías, buenos hábitos, advertencias sobre errores frecuentes y matices que ayudan a fijar los conceptos.

---

## 📚 Una analogía para empezar: la biblioteca

Imagina que tus programas son estudiantes en una biblioteca. Hasta ahora, cuando un estudiante necesitaba leer un libro, se lo tenías que **dictar** tú al oído (con `input()`). Un método útil, pero limitado: si el estudiante quiere estudiar por la noche o los libros son largos y muchos, no puedes estar ahí. Se necesita que el estudiante tenga capacidad para no requerir de la intervención del bibliotecario, es decir pueda tomar los datos de otra fuente.

Los tipos de "fuente de datos" que verás en este tema son las distintas formas en que un programa puede **conseguir** información por sí mismo:

- Un **fichero** es como un **cuaderno de apuntes**: los datos están escritos y pueden consultarse cuando haga falta. Es sencillo, portable, y funciona sin más.
- Un **CSV** es como una **tabla de doble entrada** en el cuaderno: filas y columnas ordenadas.
- Un **JSON** es como una **ficha con etiquetas**: no una tabla, sino datos con nombre.
- Una **API** es como **preguntar a un experto por teléfono**: alguien externo mantiene los datos y te los sirve cuando llamas.
- Una **base de datos** es como una **biblioteca entera con un bibliotecario**: puedes hacer preguntas complejas y las responde en un instante, incluso con millones de libros.

Cada fuente tiene su momento. Elegir bien es parte del arte del programador.

---

## 🗄️ El modelo mental de un fichero

Un fichero es una **secuencia de bytes** guardada en un dispositivo (disco, SSD, USB). Da igual si contiene texto, una foto o un vídeo: para el sistema operativo son todos **bytes en fila**. Lo que cambia es **cómo los interpreta el programa** que los lee.

### 📖 El cursor

Cuando abres un fichero, Python crea un objeto con un **cursor** interno: la posición actual dentro del fichero. Es como el dedo con el que sigues la lectura de un libro.

- Cada vez que lees (`.read()`, `.readline()`), el cursor **avanza**.
- Cuando llegas al final, futuras lecturas devuelven **cadena vacía**, no error.
- Puedes **mover el cursor** con `.seek(posición)`: `f.seek(0)` te devuelve al principio.

Este modelo mental explica muchas rarezas:

```python
with open("datos.txt") as f:
    contenido = f.read()   # cursor al final
    otra_vez = f.read()    # devuelve '' — ya no queda nada
    f.seek(0)              # rebobinamos
    de_nuevo = f.read()    # ahora sí, contenido completo
```

---

## 🎯 Los modos de apertura, sin sorpresas

La función `open("archivo", "modo")` admite un segundo argumento que determina qué se puede hacer con el fichero. Los tres modos que verás en el 95% de los casos son:

| Modo | Nombre | Qué hace | Trampa oculta |
|:---:|:---:|:---|:---|
| `"r"` | read | Lee. **Falla si no existe.** | Es el modo por defecto |
| `"w"` | write | Escribe. **Crea el fichero o BORRA si existe.** | ⚠️ Cuidado, borra silenciosamente |
| `"a"` | append | Añade al final. Crea si no existe. | Es el modo más seguro para añadir |

Existen variantes: `"r+"` (leer y escribir), `"rb"`/`"wb"` (binario)... pero para el 99% del trabajo con datos, los tres de arriba son suficientes.

> [!WARNING]
> **La trampa clásica de `"w"`**: abrir un fichero existente con modo `"w"` **borra su contenido sin preguntar**. Si te equivocas de modo, adiós a los datos. Cuando no estés seguro de si quieres sobreescribir o añadir, piensa dos veces antes de teclear la `w`.

---

## 🔒 La regla de oro: siempre `with`

Para acceder a un fichero podríamos escribir algo así:

```python
f = open("archivo.txt")
contenido = f.read()
f.close()                  # ← si olvidas esto, el fichero queda "colgado"
```

Es correcto, pero **frágil**: si entre el `open` y el `close` ocurre una excepción, el `close` **no se ejecuta** y el sistema puede quedar en un estado extraño. Además, es fácil olvidar el `close` a secas.

La solución **profesional** es la construcción `with`:

```python
with open("archivo.txt") as f:
    contenido = f.read()
# Aquí fuera del bloque, el fichero YA está cerrado
```

Aunque haya una excepción dentro del bloque, Python **garantiza** que el fichero se cierra al salir. Este patrón se llama **gestor de contexto** y verás la misma idea en muchas otras librerías (bases de datos, red, cerrojos...).

> [!IMPORTANT]
> **Regla que no debes romper nunca**: siempre que abras un fichero, hazlo con `with`. Las excepciones a esta regla son tan raras que probablemente no las verás en toda la asignatura.

---

## 🧾 CSV vs. JSON: cuándo usar cada uno

Ambos son formatos de **texto plano** (los abres con un editor cualquiera). Pero **su estructura y su uso son distintos**:

| Aspecto | CSV | JSON |
|:---|:---|:---|
| **Estructura** | Tabular (filas y columnas) | Anidada (dicts y listas) |
| **Tipos de datos** | Solo cadenas | Cadenas, números, booleanos, listas, dicts, `null` |
| **Legibilidad** | Fácil para tablas simples | Más rica pero más ruidosa |
| **Interoperabilidad** | Excel, hojas de cálculo | APIs web, config de aplicaciones |
| **Volumen** | Muy compacto para tablas grandes | Más "hinchado" por sintaxis |

### 💡 Cuándo elegir CSV

- Los datos **son una tabla**: siempre las mismas columnas para cada fila.
- Quieres que **Excel** o LibreOffice puedan abrirlos directamente.
- Los datos son **homogéneos**: notas, temperaturas, medidas.

### 💡 Cuándo elegir JSON

- Los datos son **heterogéneos** o **jerárquicos** (un libro tiene una lista de autores, un pedido tiene productos con precios...).
- Vas a intercambiarlos con una **API web** o una aplicación moderna.
- Quieres representar **tipos distintos** (números, booleanos, listas) sin ambigüedad.

### 🚨 El error del `,` en CSV en español

Un problema clásico: en español, los decimales se escriben con **coma** (`3,14`), pero en un CSV la coma también es el **separador de columnas**. Al abrir el CSV en Excel en español, `3,14` se puede interpretar como **dos columnas**.

**Solución habitual**: usar `;` como separador en países hispanohablantes:

```python
lector = csv.reader(f, delimiter=";")
```

O bien fijar el punto como decimal en Python (`str(3.14)` da `"3.14"`), que es lo que hace Python por defecto.

---

## 🔒 Permisos: la seguridad empieza aquí

Un fichero no es solo su contenido: también lleva asociados unos **permisos** que dicen quién puede leerlo, escribirlo o ejecutarlo. En sistemas UNIX (Linux, macOS), esto se ve al ejecutar `ls -la`:

```text
-rw-r--r--   john.smith  staff   datos.csv
```

Los 10 caracteres iniciales tienen un significado muy concreto:

1. **`-`**: tipo del elemento (`-` fichero, `d` directorio, `l` enlace).
2. **`rw-`**: permisos del **propietario** (Juan puede leer y escribir).
3. **`r--`**: permisos del **grupo** (`staff` solo puede leer).
4. **`r--`**: permisos de **los demás** (todos los demás solo pueden leer).

Y cada trío tiene tres letras:

- **`r`** — read (leer)
- **`w`** — write (escribir)
- **`x`** — execute (ejecutar, o entrar en el directorio)

### 🔢 Notación octal: los números mágicos

La misma información se puede expresar con **tres dígitos entre 0 y 7**. Cada trío binario se codifica así:

$$r=4, \quad w=2, \quad x=1$$

Y se **suman**. Por ejemplo, `rw-` es $4+2+0 = 6$, así que `-rw-r--r--` equivale a `644`.

Los valores más habituales que verás son:

| Octal | Simbólico | Uso típico |
|:---:|:---:|:---|
| `644` | `rw-r--r--` | Ficheros de datos comunes |
| `600` | `rw-------` | Ficheros privados (contraseñas, claves) |
| `755` | `rwxr-xr-x` | Directorios, scripts públicos |
| `700` | `rwx------` | Directorios privados |
| `777` | `rwxrwxrwx` | ⚠️ Todo el mundo puede todo (evítalo salvo desarrollo local) |

### 💡 Regla mental para no equivocarse

Si te preguntan **"¿qué permisos debe tener mi script de Python para que lo puedan ejecutar otros?"**, la respuesta es casi siempre `755`: el dueño puede modificarlo, todos los demás pueden leerlo y ejecutarlo.

Si te preguntan por **claves privadas** o **datos sensibles**, la respuesta es `600`: solo el dueño accede.

---

## 🌐 APIs REST: la puerta a datos externos

Una **API REST** es un servicio remoto al que llamas por **URL**, especificando qué acción quieres realizar mediante un **método HTTP**:

- **GET**: pedir información (leer).
- **POST**: enviar información nueva (crear).
- **PUT/PATCH**: modificar información existente.
- **DELETE**: eliminar información.

En Python usamos la biblioteca `requests` (externa, se instala con `pip install requests`):

```python
import requests

respuesta = requests.get("https://api.openweathermap.org/data/2.5/weather",
                          params={"q": "Ciudad Real", "appid": "TU_KEY"})

if respuesta.status_code == 200:      # 200 = OK
    datos = respuesta.json()           # convierte la respuesta JSON en dict
```

### 🚦 Los códigos HTTP que hay que conocer

Cuando llamas a una API, la respuesta viene con un **código numérico**. Los más importantes:

| Código | Significado | Qué hacer |
|:---:|:---|:---|
| **200** | OK | Todo bien, procesa los datos |
| **400** | Bad Request | Falta un parámetro o está mal formado |
| **401** | Unauthorized | Falta tu clave o es inválida |
| **403** | Forbidden | Tienes clave pero no permisos suficientes |
| **404** | Not Found | La URL o el recurso no existe |
| **429** | Too Many Requests | Has llamado muchas veces, espera |
| **500** | Internal Server Error | Problema en el servidor, no en ti |

### 🔑 Sobre las API Keys

Muchas APIs (como OpenWeatherMap) requieren una **clave** para saber quién eres y controlar los abusos. La consigues **registrándote** en el servicio (gratis en muchos casos). La clave es **secreta**: **nunca la publiques** en un repositorio de código, y **nunca la envíes en el URL** — pásala como parámetro o en las cabeceras.

> [!TIP]
> **Un consejo de oro:** Cuando empieces con APIs que requieren clave (como OpenWeatherMap), nunca dejes tu API Key escrita directamente en el código de forma pública si vas a subir tus prácticas a sitios como GitHub. Acostúmbrate desde temprano a usar **variables de entorno** (con la librería `python-dotenv`) para mantener tus contraseñas seguras.

#### Variables de entorno

Cuando programas con APIs, es habitual encontrarse con API Keys, contraseñas de bases de datos o tokens de acceso. Si escribes estas claves directamente en el código (lo que se conoce como hardcoding), te arriesgas a que cualquiera que vea tu archivo de Python te las robe, especialmente si subes tus proyectos a plataformas públicas como GitHub.

Para solucionar esto se utilizan las variables de entorno. En lugar de escribir la clave en el archivo `.py`, la guardas en el sistema operativo o en un archivo oculto, y Python la lee desde ahí en "tiempo de ejecución". La librería `python-dotenv` es el estándar en Python para gestionar esto de forma ultra sencilla mediante un archivo local llamado `.env`.

Aquí tienes el paso a paso de cómo se configura y cómo funciona.

* **Paso 1: Instalación**

Lo primero que necesitas es instalar la librería en tu entorno de desarrollo mediante tu terminal:

```bash
pip install python-dotenv
```
* **Paso 2: Crear el archivo `.env`**

En la misma carpeta donde tienes tu script de Python, crea un archivo nuevo y nómbralo exactamente `.env` (sí, empieza con un punto y no tiene extensión).
Dentro de este archivo, vas a guardar tus credenciales en un formato de CLAVE=VALOR, una por línea y sin espacios alrededor del signo igual:

```bash
# Archivo .env
WEATHER_API_KEY=tu_clave_secreta_de_openweathermap_12345
DB_PASSWORD=mi_contraseña_secreta
```
* **Paso 3: Leer el archivo desde Python**

Ahora, en tu archivo de Python (por ejemplo, `main.py`), vas a utilizar `python-dotenv` para cargar esas variables en la memoria de tu programa y la librería nativa os para leerlas.

```python
import os
import requests
from dotenv import load_dotenv

# 1. Cargamos las variables que están escritas en el archivo .env
load_dotenv()

# 2. Leemos la variable específica usando os.environ.get
api_key = os.environ.get("WEATHER_API_KEY")

# Ahora puedes usar 'api_key' en tu petición sin haber revelado su valor en el código
url = f"https://api.openweathermap.org/data/2.5/weather?q=Madrid&appid={api_key}"

print(f"Clave cargada con éxito: {api_key[:5]}... (ocultando el resto)")
# respuesta = requests.get(url)
```

**El secreto final: ¿Cómo mantengo esto seguro en GitHub?**
El archivo `.env` solo vive en tu ordenador. Para evitar que se suba por error a internet, debes usar un archivo especial llamado .gitignore.

1. **Crear un archivo `.gitignore`**
En la raíz de tu proyecto, crea un archivo de texto llamado .gitignore (con un punto al inicio).

2. **Añadir el archivo `.env` a la lista de exclusión**
Abre .gitignore y escribe adentro .env en una línea. Esto le dice a Git que ignore por completo ese archivo y nunca lo rastree.

3. **Crear una plantilla pública (.env.example)**
Crea un archivo llamado `.env.example` que sí subirás a GitHub. En él, pon las mismas variables pero sin tus datos reales. Esto sirve como guía para que otras personas sepan qué configuración necesita tu programa para funcionar.

Tu archivo `.env.example` se vería simplemente así:

```bash
# Archivo .env.example (Este sí se sube a GitHub)
WEATHER_API_KEY=coloca_aqui_tu_clave_de_openweathermap
DB_PASSWORD=coloca_aqui_tu_password
```

Cuando otra persona descargue tu proyecto, solo tendrá que duplicar el archivo `.env.example`, renombrarlo a `.env` y rellenarlo con sus propias claves.

---

## 🗃️ Bases de datos: cuando el fichero se queda corto

Las bases de datos entran en juego cuando los ficheros dejan de ser prácticos:

- **Volumen**: 50.000 estudiantes en un CSV se vuelven lentos a cada consulta.
- **Complejidad**: "nota media por curso de los aprobados en 2024" es un cálculo tedioso con ficheros.
- **Concurrencia**: si dos programas escriben a la vez en un CSV, corrompen el fichero.
- **Integridad**: no puedes obligar por sí solo a que una nota esté entre 0 y 10.

Una **base de datos relacional** organiza la información en **tablas** con **filas** y **columnas**, define restricciones de integridad (claves primarias, tipos, rangos) y ofrece un lenguaje de consulta (**SQL**) que hace todo el trabajo pesado.

### 🎯 SQLite: la BBDD que viene con Python

Python trae de serie el módulo **`sqlite3`**, que permite tener una base de datos completa **sin instalar nada**. Toda la BBDD vive en un **único fichero** (por ejemplo `universidad.db`), muy fácil de compartir, respaldar y llevar.

### 🔄 El patrón de trabajo con `sqlite3`

Trabajar con una BBDD en SQLite sigue **siempre el mismo patrón de cinco pasos**:

```python
import sqlite3

conexion = sqlite3.connect("universidad.db")   # 1) conectar
cursor = conexion.cursor()                     # 2) obtener un cursor
cursor.execute("INSERT INTO ...")              # 3) ejecutar SQL
conexion.commit()                              # 4) confirmar
conexion.close()                               # 5) cerrar
```

- Si solo **consultas** datos (no modificas), puedes omitir el paso 4 (`commit`).
- Si te olvidas de `commit` tras insertar o modificar, **tus cambios se pierden**.
- Si te olvidas de `close`, el fichero puede quedar bloqueado para otros programas.

### 🚨 El error clásico: la inyección SQL

Esta es una de las **vulnerabilidades más famosas** de la historia de la informática. Un ejemplo malo:

```python
# ❌ TERRIBLE
nombre = input("Nombre: ")
cursor.execute(f"SELECT * FROM Users WHERE nombre = '{nombre}'")
```

Si el usuario teclea `'Ana' OR '1'='1'`, la consulta se convierte en `SELECT * FROM Users WHERE nombre = 'Ana' OR '1'='1'`, que **devuelve todos los usuarios**. Peor aún: puede escribir `'Ana'; DROP TABLE Users;--` y **destruir la tabla**.

La versión correcta usa **parámetros** con `?`:

```python
# ✅ SEGURO
cursor.execute("SELECT * FROM Users WHERE nombre = ?", (nombre,))
```

Y si en vez de un campo, son dos o cualesquiera, ya sabes usa el AND:

```python
# Los valores que quieres buscar
nombre_buscado = "Ana"
apellido buscado = "García"

# La consulta con ambos campos
cursor.execute(
    "SELECT * FROM Users WHERE nombre = ? AND apellidos = ?", 
    (nombre_buscado, apellido_buscado)
)
```

Ahora SQLite trata el valor como **dato**, no como código SQL, y no hay manera de romperlo. Este patrón (`execute` con `?`) **es la regla que debes seguir siempre**.

### 🎓 Un poco de SQL básico

Para consultar en SQLite se usa **SQL**, que verás en muchos otros contextos. Los cuatro pilares:

```sql
CREATE TABLE Estudiantes (              -- crear tabla
    dni TEXT PRIMARY KEY,
    nombre TEXT,
    curso INTEGER,
    nota REAL
);

INSERT INTO Estudiantes VALUES (?, ?, ?, ?);   -- insertar

SELECT nombre, nota FROM Estudiantes          -- consultar
WHERE curso = 1;

UPDATE Estudiantes SET nota = 10               -- modificar
WHERE dni = '50123456A';

DELETE FROM Estudiantes WHERE nota < 5;        -- eliminar
```

Y las **funciones de agregación** que hacen el trabajo pesado por ti:

```sql
SELECT AVG(nota), MAX(nota), MIN(nota), COUNT(*)
FROM Estudiantes
WHERE curso = 1;
```

En una línea, obtienes la media, el máximo, el mínimo y el número total. Compara con el trabajo que costaría hacerlo a mano con un fichero.

---

## 🏆 Un pipeline de datos: la práctica profesional

Como colofón, este tema te da las piezas necesarias para construir un **pipeline de datos completo**:

1. **Leer** un CSV con datos históricos.
2. **Llamar** a una API para enriquecer los datos (por ejemplo, geolocalizar).
3. **Guardar** el resultado combinado en una base de datos SQLite.
4. Luego, **consultar** la BBDD para producir informes.

Esta cadena, en el Tema 7, la puedes construir con las herramientas que aquí has aprendido. Es lo que hacen los pipelines de datos de las empresas modernas, solo que con volúmenes mayores y herramientas más especializadas (`pandas`, `Airflow`, `Spark`...). Pero **la lógica es la misma**.

> [!NOTE]
> **Para llevar a casa**: Este tema te permite aprender a **conectar tu programa con el mundo**. A partir de aquí, tus programas ya no dependen de que alguien esté delante tecleando: pueden alimentarse solos.

---

## 🧭 Menú de Navegación

| Orden | Material | Tiempo |
|:-----:|:---------|:------:|
| 1     | **Teoría**                                |   14   |
| 2     | [Recursos](../recursos/T7_RE_ICC.md)      |    8   |
| 3     | [Ejemplos](../ejemplos/T7_Ejem_ICC.md)    |    –   |
| 4     | [Ejercicios](../ejercicios/T7_Ejer_ICC.md)|    –   |
|       | [Menú del Tema actual](../README.md)      |    -   |
