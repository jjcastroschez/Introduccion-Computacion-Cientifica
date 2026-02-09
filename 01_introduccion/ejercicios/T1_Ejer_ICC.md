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

<style>
.faq-container {    
  max-width: 800px;
  margin: 50px auto 0 auto;
  padding: 2rem;
}
.faq-container h2 {
  margin-bottom: 50px;
  font-size: 2.5rem;
  font-weight: 600;
  text-align: center;
  color: #364f6b;
}
details { 
  background-color: #f6f8fa;
  width: 100%;
  margin-bottom: 1rem;   
  border-radius: 8px;  
  border: 1px solid #d8e0e9;
  color: #364f6b;
  position: relative;  
}
details summary {  
  font-weight: 400;
  font-size: 1.25rem;
  padding: 1rem;
  cursor: pointer;
  list-style: none;
}
details p {
  padding: 1rem;
  margin: 0 1rem 1rem 1rem;
  background: #f6f8fa;
  border-left: 2px solid #364f6b;
}

details:hover,
details[open] {
  box-shadow: 5px 5px 15px #d9d9d9;
}

details[open] {
  background: #ffffff;
}

details[open] summary {
  font-weight: 600;
}

details summary::before {
  position: absolute;
    content: "👇";    
    font-size: 1.75rem;
    top: 10px;
    right: 16px;  
}

details[open] summary::before {
  -webkit-animation: rotate 0.6s ease-in-out both;
          animation: rotate-emoji 0.6s ease-in-out both;
}

@-webkit-keyframes rotate-emoji {
  0% {
    -webkit-transform: rotate(0);
            transform: rotate(0);
  }
  100% {
    -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
  }
}

</style>

<!-- Código HTML para usar el estido previamente definido -->

<div class="faq-container">
  <h2>Responde a las siguientes consultas</h2>
  <details open>
  <summary>¿Qué necesitas para poder ejecutar el programa en C?</summary>
  <p>¡Muy bien! C es un lenguaje compilado, por lo que te tendrías que descargar un compilador de C en tu ordenador. Ya lo harás, no es el momento... Empleemos para este ejercicio un <a href="../recursos/T1_RE_ICC.md#-compiladores-e-intérpretes-online">compilador online</a>.</p>
</details>

<details>
  <summary>¿Qué ha ocurrido?¿Se genera código máquina?</summary>
  <p>Al usar un compilador online no hay, no puede haber, generación de código máquina. La herramienta que has usado, analiza tu programa y simula el trabajo del compilador, analiza y ejecuta, pero no hay generación.</p>
</details>
  
  <details>
  <summary>Si sustituyes en el código en C el contenido de la línea 8, por:  <span style="font-family: monospace;">multiplica = 1000;</span> ¿qué tipo de error ocurrirá?</summary>
  <p>No es un error de vocabulario, ni es un error de sintaxis. Está ocurriendo un error semántico, estás intentando asignar un valor a una variable que no está declarada. Ya aprenderás más sobre esto... 😜</p>
</details>
  
  <details>
  <summary>Y si sustituyes en el código C original el contenido de esa misma línea ahora con <span style="font-family: monospace;">multiplicador = 1000</span> ¿qué tipo de error ocurre ahora?</summary>
  <p>Efectivamente, es un error de sintaxis, ya que se ahora se espera el símbolo ';' para que tenga una estructura correcta.</p>
</details>
  
  <details>
  <summary>Una última pregunta, y si en el original cambias la línea 5 por <span style="font-family: monospace;">int 1numero;</span> ¿qué ocurre ahora?</summary>
  <p>¡Puf! Parece el fin... ¿eh? Y eso que solo has tocado una cosa. Tranquilidad, hay un error que luego provoca otros, que realmente no existen. El primer error se produce por el uso de 1numero, ahí se está produciendo un error en el vocabulario. Ya hablaremos de esto más adelante.</p>
</details>
  
</div>

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




