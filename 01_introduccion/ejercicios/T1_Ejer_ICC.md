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


# 🖥️ Ejercicios - Tema 1: Introducción a la Computación Científica 📝

¡Es hora de practicar lo aprendido! De esta forma acabarás de aprender y adquirir los conocimientos y habilidades de este tema. Te animo a que realices los siguientes ejercicios para acabar de asimilar los contenidos del tema.

---

## ⚙️ Sistema Operativo (SO) y la Terminal

Veamos si has aprendido a moverte por el árbol de directorios y a interactuar con el Sistema Operativo (SO) de una manera rápida y eficiente 😜. Recuerda hacer este ejercicio sin usar la interfaz gráfica del SO, abre la terminal y a por ello...

### 🏗️ Ejercicio: "Construyendo tu espacio de trabajo"

#### Parte Primera: Navegación

1. **Exploración:** Abre la terminal, mira en que directorio estás y sitúate en la carpeta "Documents" o "Documentos". 
2. **Creación:** Crea una carpeta llamada ``Introduccion_Computacion_Cientifica``, entra en ella.
3. **Anidación:** Crea la siguiente estructura de carpetas, que cuelga desde la recien creada ``Introduccion_Computacion_Cientifica``:

```sh
Introduccion_Computacion_Cientifica
 │ 
 ├── Guia_INTRODUCCION_A_LA_COMPUTACION_CIENTIFICA.pdf
 ├── Libros
 │    ├── pythonlearn.pdf
 │    └── Python para todos.pdf
 └── Tema 1
     ├── Transparencias
     │   ├── Teoria
     │   │    └── Tema1_ICC.pdf
     │   └── Practicas
     │        ├── Sesion1A_ICC_Practicas.pdf
     │        └── Sesion1B_ICC_Practicas.pdf
     ├── Ejemplos
     ├── Ejercicios
     ├── Otros
     └── Entregables
```

> [!NOTE]
> La guía de la asignatura (*Guia_INTRODUCCION_A_LA_COMPUTACION_CIENTIFICA.pdf*) te la puedes descargar de la web. 
> Los archivos de la carpeta `Libros` son algunos de acceso libre, como **Python para todos** escrito por Charles R. Severance (*pythonlearn.pdf*) o el del mismo título escrito por Raúl González Duque (*Python para todos.pdf*), ambos son  tutoriales de Python adecuado para todos los niveles que puedes descargar totalmente grátis de la web (mira el apartado [**Recursos**](../recursos/T1_RE_ICC.md)). Hay muchos en la web, pero no te obsesiones en tener muchos libros, lo importante es leerlos, por lo menos uno.
> El resto de documentos que aparecen en la estructura te los puedes descargar del espacio de la asignatura en Campus Virtual.

4. **Generacion:** Crea un archivo de texto dentro de la carpeta ``Ejemplos`` llamado ``opinion.txt`` que contenga una frase oculta (ej. "Encantado de conocer al SO, el boss").

5. **Copia:** Copia el archivo `opinion.txt` a la carpeta `Otros` y elimínalo de la carpeta `Ejemplos`.

6. **Limpieza:** Elimina la carpeta `Otros`. 

> [!TIP]
> Para realizar el ejercicio consulta la 📋[**Chuleta de Comandos Básicos (CLI)**](../recursos/T1_RE_ICC.md#-chuleta-de-comandos-básicos-cli) y la 📂[**Chuleta de Navegación: Comando `cd` (Change Directory)**](../recursos/T1_RE_ICC.md#-chuleta-de-navegación-comando-cd-change-directory).


---

## 📖 Compiladores e Intérpretes Online

Ejecuta el siguiente programa...

```c
#include <stdio.h>
 
 int main() {
    printf("Programa en C\n");
    int multiplicador; 
    int multiplicando;
    int res; 
    multiplicador = 1000; 
    multiplicando=2;
    res=multiplicador*multiplicando;
    printf("Resultado (%d x %d) = %d\n",multiplicador,multiplicando,res); /*se muestra el resultado */ 
    return 0;
}
```
<!-- Defino un estilo para poner preguntas Desplegables con formnato 😜 -->

### Responde a las siguientes consultas
  <details>
  <summary><h3>¿Qué necesitas para poder ejecutar el programa en C?<h3></summary>
  <p>¡Muy bien! C es un lenguaje compilado, por lo que te tendrías que descargar un compilador de C en tu ordenador. Ya lo harás, no es el momento... Empleemos para este ejercicio un <a href="../recursos/T1_RE_ICC.md#-compiladores-e-intérpretes-online">compilador online</a>.</p>
</details>

<details>
  <summary><h3>¿Qué ha ocurrido?¿Se genera código máquina?</h3></summary>
  <br>
  <p>Al usar un compilador online no hay, no puede haber, generación de código máquina. La herramienta que has usado, analiza tu programa y simula el trabajo del compilador, analiza y ejecuta, pero no hay generación.</p>
</details>
  
  <details>
  <summary><h3>Si sustituyes en el código en C el contenido de la línea 8, por:  <em>multiplica = 1000;</em> ¿qué tipo de error ocurrirá?<h3></summary>
  <br>
  <p>No es un error de vocabulario, ni es un error de sintaxis. Está ocurriendo un error semántico, estás intentando asignar un valor a una variable que no está declarada. Ya aprenderás más sobre esto... 😜</p>
</details>
  
  <details>
  <summary><h3>Y si sustituyes en el código C original el contenido de esa misma línea ahora con <em>multiplicador = 1000</em> ¿qué tipo de error ocurre ahora?</h3></summary>
  <br>
  <p>Efectivamente, es un error de sintaxis, ya que se ahora se espera el símbolo ';' para que tenga una estructura correcta.</p>
</details>
  
  <details>
  <summary><h3>Una última pregunta, y si en el original cambias la línea 5 por <em>int 1numero;</em> ¿qué ocurre ahora?<h3></summary>
  <br>
  <p>¡Puf! Parece el fin... ¿eh? Y eso que solo has tocado una cosa. Tranquilidad, hay un error que luego provoca otros, que realmente no existen. El primer error se produce por el uso de 1numero, ahí se está produciendo un error en el vocabulario. Ya hablaremos de esto más adelante.</p>
</details>
  

---

## Python

Crea y ejecuta...

---

## Software de Control de Versiones 

Crea el siguiente repositorio...

---

## ⚙️ Entorno de Desarrollo Integrado (IDE)

Guarda y ejecuta en el IDLE de Python...

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo       | 
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T1_ICC.md)              |    8         |
| 2      | [Recursos](../recursos/T1_RE_ICC.md)       |      7       |
| 3      | [Ejemplos](../ejemplos/)                   |      -       |
| 4      | [Ejercicios](../ejercicios/T1_Ejer_ICC.md) |      -       |
|        | [Menu del Tema actual](../README.md)       |      -       | 




