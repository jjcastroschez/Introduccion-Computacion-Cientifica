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


# 🖥️ Ejercicios Autocomprobación - Tema 1: Introducción a la Computación Científica 📝

¡Es hora de practicar lo aprendido! De esta forma acabarás de aprender y adquirir los conocimientos y habilidades de este tema. Te animo a que realices los siguientes ejercicios para acabar de asimilar los contenidos del tema.

---

## ⚙️ Sistema Operativo (SO) y la Terminal

Veamos si has aprendido a moverte por el árbol de directorios y a interactuar con el Sistema Operativo (SO) de una manera rápida y eficiente 😜. Recuerda hacer este ejercicio sin usar la interfaz gráfica del SO, abre la terminal y a por ello...

### 🏗️ Ejercicio: "Construyendo tu espacio de trabajo"

Haz lo que te indico aquí 👇

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

Es el momento de comprobar si eres consciente de la utilidad/necesidad de los compiladores e intérpretes y eres capaz de entender lo que hacen.

### ⚙️ Ejercicio: "Ejecutando programas"

Ejecuta el siguiente programa escrito en el lenguaje de programación C, y responde a las preguntas que te hago antes de ver la solución... 😜

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
    printf("Resultado (%d x %d) = %d\n",multiplicador,multiplicando,res);
    return 0;
}
```
<!-- Defino un estilo para poner preguntas Desplegables con formnato 😜 -->

#### Responde a las siguientes consultas 👇
  <details>
  <summary><h4>¿Qué necesitas para poder ejecutar el programa en C?<h4></summary>
  <p>¡Muy bien! C es un lenguaje compilado, por lo que te tendrías que descargar un compilador de C en tu ordenador. Ya lo harás, no es el momento... Empleemos para este ejercicio un <a href="../recursos/T1_RE_ICC.md#-compiladores-e-intérpretes-online">compilador online</a>.</p>
</details>

<details>
  <summary><h4>¿Qué ha ocurrido?¿Se genera código máquina?</h4></summary>
  <p>Al usar un compilador online no hay, no puede haber, generación de código máquina. La herramienta que has usado, lee tu programa y simula el trabajo del compilador, analizando y ejecutando las instrucciones, pero no hay generación.</p>
</details>
  
  <details>
  <summary><h4>Si sustituyes en el código en C el contenido de la línea 8, por:  <em>multiplica = 1000;</em> ¿qué tipo de error ocurrirá?<h4></summary>
  <p>No es un error de vocabulario, ni es un error de sintaxis. Está ocurriendo un error semántico, estás intentando asignar un valor a una variable que no está declarada. Ya aprenderás más sobre esto... 😜</p>
</details>
  
  <details>
  <summary><h4>Y si ahora el contenido de esa misma línea es <em>multiplicador = 1000</em> ¿qué tipo de error ocurre?</h4></summary>
  <p>Efectivamente, es un error de sintaxis. Se espera el símbolo ';' para que tenga una estructura correcta, al no estar se produce un error.</p>
</details>
  
  <details>
  <summary><h4>Una última pregunta, y si en el original cambias la línea 5 por <em>int 1numero;</em> ¿qué ocurre ahora?<h4></summary>
  <p>¡Puf! Parece el fin, ¿eh?. Y eso que solo has tocado una cosa. Tranquilidad, efectivamente solo hay un error que luego provoca otros, que realmente no existen. El primer error se produce por el uso de <em>1numero</em>, ahí se está produciendo un error en el léxico. Ya hablaremos de lo que ocurre más adelante.</p>
</details>
  

---

## Python

De este lenguaje de programación ya hemos hablado algo en clase y [en este mismo espacio](../teoria/T1_ICC.md#-tu-primer-programa-en-python), así que deberías responder correctamente a las cuestiones que te planteo a continuación.

### 🐍 Ejercicio: "Ejecutando scripts de Python"

Ejecuta el siguiente script escrito en el lenguaje de programación Python, y responde a las preguntas que te hago. Recuerda que es conveniente no mirar la solución... 😜

```python

print("Script en Python\n")
multiplicador = 1000 
multiplicando=2
res=multiplicador*multiplicando
print(f"Resultado ({multiplicador} * {multiplicando}) = {res}\n") 

```

#### Responde a las siguientes consultas 👇
  <details>
  <summary><h4>¿Qué necesitas para poder ejecutar el programa en Python?<h4></summary>
  <p>¡Muy bien! Python es un lenguaje interpretado, por lo que te tendrías que descargar un intérprete de Python en tu ordenador. ¡Ya lo has hecho! Así que empléalo para este ejecutar este script.</p>
</details>

<details>
  <summary><h4>¿Qué ha ocurrido ahora?¿Se genera código máquina?</h4></summary>
  <p>Al usar un intérprete no hay generación de código máquina. El intérprete ha ido recibiendo instrucción a instrucción, cada una de ellas ha sido analizada y ejecutada, pero no hay generación.</p>
</details>
  
  <details>
  <summary><h4>Si sustituyes en el código en Python el contenido de la línea 2, por:  <em>multiplica = 1000;</em> ¿qué tipo de error ocurrirá?<h4></summary>
  <p>¿Qué has hecho? Si has ejecutado este script desde la línea de comandos de Python, e inmediatamente después de ejecutar el anterior, ¡no ha pasado nada! 😜. Si lo has ejecutado por primera vez, tampoco ocurre nada después de ejecutarlo. Pero si inicias Python o lo cierras, y vuelves a ejecutarlo línea a línea, al introducir la línea 4 se producirá un error semántico. Esto se debe a que no está definida la variable <em>multiplicador</em>.</p>
</details>
  
  <details>
  <summary><h4>Y si cambiamos la línea 5 por <em>res=multiplicador x multiplicando</em> ¿qué ocurre?</h4></summary>
  <p>Efectivamente, es un error de sintaxis. El intérprete cuando analiza la instrucción no entiende la presencia del carácter <em>x</em>.</p>
</details>
  
  <details>
  <summary><h4>Una última pregunta, y si en el original cambiamos la línea 2 por <em><em>1numero=1000</em></em> ¿qué ocurre ahora?<h4></summary>
  <p>El intérprete encuentra un error al analizarla, es un error léxico, aunque lo está reportando como un error sintáctico, al construir un elemento de vocabulario, en concreto un número.</p>
</details>
  

---

## Software de Control de Versiones 

Como sabes el software de control de versiones te ayuda a registrar cambios en archivos a lo largo del tiempo, permitiendo recuperar estados anteriores de esos archivos y gestionar modificaciones simultáneas por varios usuarios. Vamos a ver si eres capaz de poner en marcha este software sobre tus proyectos.

### 📋 Ejercicio: "Tomando precauciones para evitar daños"

1. Crea un repositorio sobre la raíz de la estructura que has construido <strong>Introduccion_Computacion_Cientifica</strong>. 
2. Sube tu repositorio a tu cuenta de GitHub.
3. Comparte tu repositorio en GitHub con el profesor.

---

## ⚙️ Entorno de Desarrollo Integrado (IDE)

Guarda el script anterior de Python en un archivo nombrado ``multiplicacion.py`` y sitúalo en una nueva carpeta de nombre ``Pruebas`` que cuelgue de la raíz. Ahora es tiempo de ejecutarlo en el IDLE de Python.

Sube ahora los cambios a tu repositorio en GitHub.

---

## 🧭 Menú de Navegación

| Orden  | Material                                                                  | Tiempo       | 
|:------:|:--------------------------------------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T1_ICC.md)                                             |      8       |
| 2      | [Recursos](../recursos/T1_RE_ICC.md)                                      |      7       |
| 3      | [Ejemplos](../ejemplos/T1_Ejem_ICC.md)                                    |      -       |
| 4      | **Ejercicios**                                                            |      -       |
|        | [Menu del Tema actual](../README.md#-menú-de-navegación-en-el-tema)       |      -       |  