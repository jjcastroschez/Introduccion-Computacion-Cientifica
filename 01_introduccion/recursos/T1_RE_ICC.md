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


# 🎓 Recursos - Tema 1: Introducción 🚀

A continuación se relacionan varios recursos y enlaces a sitios que son de interés y utilidad para comprender, instalar y configurar el ecosistema con el que trabajarás a lo largo del curso.

---

## ⚙️ Sistema Operativo (SO) y la Terminal

Cuando programamos es habitual utilizar la interfaz de línea de comandos (CLI) del sistema operativo con el objetivo de aumentar la productividad, automatizar tareas repetitivas y gestionar el sistema con mayor precisión y rapidez que con una interfaz gráfica (GUI).

En el siguiente enlace tienes acceso a una referencia en línea de los comandos A-Z de la terminal de Windows ([Listado de Comandos Windows](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/windows-commands)). Para acceder a las ayudas sobre los comandos UNIX (macOS) puedes usar desde la línea de comandos el comando `man` seguido del nombre del comando sobre el que deseas obtener información. Por ejemplo, la ejecución del comando `man cp` te mostrará una página de ayuda sobre el comando `cp`.  

### 📋 Chuleta de Comandos Básicos (CLI)

Durante tu trabajo práctico en la asignatura, utilizarás en la terminal los siguientes comandos habituales:

| Comando | Acción | Uso |
| :--- | :--- | :--- |
| `cd` | Cambiar de carpeta / moverse por el sistema. | [Info. comando cd (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/cd) |
| `ls` / `dir` | Listar archivos y carpetas. | [Info. comando dir (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/dir)  |
| `mkdir` | Crear carpetas nuevas. | [Info. comando mkdir (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/mkdir) | 
| `rmdir` | Eliminar carpetas. | [Info. comando rmdir (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/rmdir) | 
| `cp` / `copy` | Copiar archivos. | [Info. comando copy (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/copy) | 
| `rm` / `del` | Eliminar archivos. | [Info. comando del (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/del) | 
| `clear` / `cls` | Limpiar terminal. | [Info. comando cls (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/cls) |
| `mv` / `move` | Mover/Renombrar. | [Info. comando move (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/move) |

---

## 📖 Compiladores e Intérpretes Online

Los compiladores e intérpretes son esenciales en programación para comunicar a la máquina qué es lo que queremos que ejecute. Para programar tendremos que tener instalado en nuestro computador un entorno de ejecución o intérprete/compilador del lenguaje en el que programemos. No obstante, en algunos momentos podemos usar compiladores e intérpretes en línea que nos van a permitir escribir, probar, depurar y ejecutar código directamente desde un navegador web, eliminando la necesidad de instalar software pesado en nuestros computadores. Son especialmente útiles para programar desde cualquier lugar, practicar con diferentes lenguajes, compartir código rápidamente y optimizar el rendimiento sin consumir recursos del equipo local.

Existen muchos compiladores e intérpretes en línea, algunos de ellos son:

* [myCompiler](https://www.mycompiler.io/es/)
* [OneCompiler](https://onecompiler.com)
* [CodeChef](https://www.codechef.com/ide)
* [paiza.IO](https://paiza.io/es/projects/new)
* [OnlineGDB](https://www.onlinegdb.com)

---

## Python

En este curso se empleará el lenguaje Python para la enseñanza y aprendizaje de los fundamentos de los lenguajes de programación, bajo el paradigma imperativo, pero prestando también atención a los paradigmas orientado a objetos y funcional. Al adquirir fundamentos generales de programación se espera que estés preparado para en un futuro profundizar en características avanzadas de Python, así como aprender más fácilmente otros lenguajes de programación que pudieras necesitar en tu desempeño  profesional. 

Para poder programar en Python, ya sabes… lo primero que necesitas es tener acceso a un intérprete de Python, lo ideal para hacer tu trabajo más eficiente es tenerlo instalado en tu computador. Comprueba si lo tienes instalado, para ello abre la terminal y a través de la línea de comandos ejecuta lo siguiente:

```shell
python --version
```

> [!NOTE]
> #Nota
> Puedes probar también con ``python3``.

Si no lo tienes instalado, visita la página oficial de [Python](https://python.org) y busca la zona de descarga (Downloads). Si la página no detecta tu SO automáticamente, vete a la zona de tu SO para descargarte la versión apropiada. 

Una vez descargado el archivo, ejecútalo… es el instalador. Cuando te de opciones asegúrate de seleccionar la opción Add Python.exe to PATH, que hará más fácil configurar bien el sistema.

---

## Software de Control de Versiones 

El **Software de Control de Versiones** (**VCS**, *Version Control System*) es una herramienta esencial en el desarrollo de software. Su misión es rastrear y gestionar cambios en el código fuente a lo largo del tiempo, tomando "fotos instantáneas" (snapshots) de los archivos. Permite a múltiples desarrolladores colaborar simultáneamente, revertir errores, gestionar distintas ramas de desarrollo y mantener un historial seguro del proyecto. A un único programador, le permite evitar experimentar sin miedo, ya que siempre podrá volver al una versión anterior funcional. Sin un VCS tendríamos archivos como ``libro_final.txt``, ``libro_final_v2.txt``o incluso ``libro_final_este_es_el_bueno``. Mientras que con un VCS tendremos en un solo archivo y una línea de tiempo invisible donde se puede ver quién hizo qué, cuándo lo hizo y revertir cambios específicos sin perder el resto del trabajo.

[Git](https://git-scm.com) es un **Sistema de Control de Versiones Distribuido** (**DVCS**, *Distributed Version Control System*), en el que cada usuario que trabaje en el proyecto tiene una copia completa del historial en su propia máquina. Como alternativa, existen **Sistemas de control de Versiones Centralizados** (**CVCS**, *Centralized Version Control System*), donde el historial está en una única máquina (un servidor central).    

Conceptos clave que escucharás siempre cuando trabajas con VCS:

1. **Repositorio (Repo)**: La carpeta de tu proyecto que Git está vigilando.
2. **Commit**: Una "foto" de tus archivos en un momento dado. Es el punto de guardado.
3. **Rama (Branch)**: Una línea de tiempo paralela. Útil para probar funciones nuevas sin romper la versión principal.
4. **Merge:** Unir los cambios de una rama a otra.

### Instalación de Git 📥
Para poder usar el control de versiones, necesitas el "motor" de Git corriendo en tu sistema operativo.

1. **Descarga**. Debes ir a la página oficial de [Git](git-scm.com) y descargar el instalador correspondiente a tu sistema (Windows, macOS o Linux).

2. **Instalación**. Sigue los pasos del asistente. En Windows, se recomienda dejar las opciones por defecto si es tu primera vez.

3. **Verificación**. Para comprobar que se instaló correctamente, abre la terminal y ejecuta el siguiente comando:

```shell
git --version
```

Git se maneja principalmente por comandos, pero si la terminal te intimida, existen opciones más visuales que veremos más adelante. 

**🛠️ Configuración Inicial (Solo una vez)**
Antes de empezar, debes identificarte ante Git para que tus "puntos de guardado" tengan autoría:

```shell
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### 🚀 Ecosistema de Colaboración: GitHub
Para llevar tus proyectos al siguiente nivel y colaborar con otros, necesitas: una plataforma de alojamiento, donde "colgar" el código que sea accesible por todos (tu ordenador no lo es); y, si no eres un usuario avanzado, una herramienta con interfaz gráfica para gestionar Git. 

[Github](https://github.com/). Es la plataforma principal donde se guardan los repositorios en la nube. Permite gestionar proyectos, realizar Pull Requests y colaborar con programadores de todo el mundo. Otras alternativas profesionales muy potentes son [GitLab](https://gitlab.com/) (muy utilizado en entornos profesionales) y [Bitbucket](https://bitbucket.org/) (opción muy popular con buena integración con otras herramientas, como Jira, una herramienta de gestión de proyectos).

[Github Desktop](https://github.com/apps/desktop). Es una aplicación oficial que ofrece una interfaz gráfica (GUI) para gestionar Git. Es ideal si prefieres visualizar tus cambios, ramas y commits de forma intuitiva mediante botones en lugar de comandos de texto. Otras alternativas son [GitKraken](https://www.gitkraken.com) (multiplataforma, muy visual), 
[Sourcetree](https://www.sourcetreeapp.com) (gratuito, popular en Mac/Windows) y [Sublime Merge](https://www.sublimemerge.com) (muy rápido). 

### 🔄 El Ciclo de Vida Completo del Código

El flujo de trabajo se divide en dos entornos: **Local** (tu ordenador) y **Remoto** (GitHub).

Para que comprendas cómo se trabaja profesionalmente, imagina que este es el "paso a paso" que seguirás cuando lo emplees:

#### 1. Preparación (Una sola vez por proyecto)
* **`git init`**: Inicia el control de versiones en tu carpeta local para que Git empiece a vigilar los cambios.
* **Conexión Remota**: Conecta tu carpeta local con un repositorio en **GitHub** (usualmente mediante el comando `git remote add origin URL`).

#### 2. El Ciclo Diario (Las 5 etapas)

1. **Sincronizar (`git pull`)**: Antes de tocar nada, te traes lo que haya de nuevo en la nube. Así evitas trabajar sobre código viejo y reduces errores de compatibilidad.
2. **Ramificar (`git switch -c nombre-tarea`)**: Nunca trabajas directamente en el "tronco" (`main`). Creas una **Rama** (línea de tiempo paralela) específica para tu trabajo.
3. **Trabajar y Guardar (`add` + `commit`)**:
    * Modificas tus archivos en el editor.
    * **`git add`**: Preparas los archivos modificados (los metes en la "maleta").
    * **`git commit -m "..."`**: Creas el punto de guardado oficial con un mensaje descriptivo.
4. **Publicar (`git push`)**: Subes tu rama a **GitHub** para que el historial esté seguro en la nube y otros puedan verla.
5. **Integrar (Pull Request)**: En la web de GitHub, solicitas permiso para unir (merge) tu rama al tronco principal (`main`).

### 🎨 Diagrama del Flujo "Día a Día"

| Orden | Comando | Analogía |
| :--- | :--- | :--- |
| **1** | `git pull` | Mirar si alguien dejó notas nuevas en la pizarra común. |
| **2** | `git switch -c rama` | Sacar una hoja en sucio para no manchar el libro principal. |
| **3** | `git add` + `commit` | Escribir y guardar el progreso en tu propia hoja de trabajo. |
| **4** | `git push` | Mandar una foto de tu hoja terminada al grupo. |
| **5** | **Pull Request** | Preguntar al responsable: "¿Puedo pegar mi hoja en el libro oficial?". |

---

## ⚙️ Entorno de Desarrollo Integrado (IDE)

Un **IDE** (*Integrated Development Environment*) es una aplicación de software que ayuda a los programadores a desarrollar código de manera eficiente. A diferencia de un simple editor de texto, un IDE combina herramientas de escritura, depuración (corrección de errores) y ejecución en una sola interfaz.

### 🛠️ Herramientas recomendadas para este curso

El **[IDLE](https://docs.python.org/es/3/library/idle.html)**, entorno de desarrollo integrado de Python, será tu primer IDE. 

Más adelante, y dependiendo de tu experiencia previa, puedes elegir entre estas opciones:

#### 🟢 Nivel Principiante (Simplicidad total)
* **[Mu](https://codewith.mu/es/)**: Un editor extremadamente sencillo diseñado para quienes nunca han programado. Su interfaz es limpia y evita distracciones.
* **[Thonny](https://thonny.org/)**: El IDE estándar para aprender Python. Incluye un depurador visual que te permite ver, paso a paso, cómo cambian las variables mientras se ejecuta tu programa.

#### 🔵 Nivel Recomendado / Profesional
* **[VS Code (Visual Studio Code)](https://code.visualstudio.com)**: Es el editor más popular en la industria actual. No es un IDE "puro" de serie, pero mediante **extensiones** se convierte en la herramienta más potente para Python.
    * **Ventaja:** Se integra perfectamente con Git y GitHub, permitiéndote hacer `commit` y `push` sin salir del programa.

### 💡 ¿Por qué usar un IDE en lugar de un editor de texto simple?

1.  **Resaltado de sintaxis:** Colorea el código para que identifiques visualmente funciones, variables y errores.
2.  **Autocompletado:** Te sugiere comandos mientras escribes, ahorrando tiempo y evitando erratas.
3.  **Terminal integrada:** Puedes ejecutar tu código de Python y usar comandos de Git en la misma ventana.
4.  **Depuración (Debugging):** Te permite detener el programa en una línea específica para entender por qué no funciona como esperas.

### 🐍 Comprobación de Python en el IDE

Independientemente del IDE que elijas, asegúrate de que reconozca tu instalación de Python. Puedes verificarlo abriendo la terminal integrada del IDE y escribiendo:

```shell
python --version
```

--- 

## Sumario de enlaces interesantes

### Python

* [Python](https://python.org)

### Control de Versiones

* [Git](git-scm.com)
* [Github](https://github.com/)
* [Github Desktop](https://github.com/apps/desktop)

### IDE 

* [VS Code (Visual Studio Code)](https://code.visualstudio.com)

### Documentación

* [Python España](https://es.python.org/)
* [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
* [30-Dias-de-Python](https://github.com/jjcastroschez/30-Dias-de-Python/blob/master/readme.md)




