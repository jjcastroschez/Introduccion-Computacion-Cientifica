
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

Cuando programamos es habitual utilizar la **interfaz de línea de comandos (CLI)** del sistema operativo, con el objetivo de aumentar la productividad, automatizar tareas repetitivas y gestionar el sistema con mayor precisión y rapidez que con una interfaz gráfica (GUI).

Para trabajar con la CLI es interesante que conozcas los comandos de la terminal de Windows ([Listado A-Z de Comandos Windows](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/windows-commands)) y Unix ([Listado Comandos macOS](https://ss64.com/mac/)), por lo menos los más usados.

### 📋 Chuleta de Comandos Básicos (CLI)

Durante tu trabajo práctico en la asignatura, utilizarás en la terminal los siguientes comandos habituales:

| Comando | Acción | Uso |
| :--- | :--- | :--- |
| `pwd`/ `cd`| Informar de la ruta actual en la terminal. | [Info. comando cd (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/cd) |
| `cd` | Cambiar de carpeta / moverse por el sistema. | [Info. comando cd (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/cd) |
| `ls` / `dir` | Listar archivos y carpetas. | [Info. comando dir (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/dir)  |
| `mkdir` | Crear carpetas nuevas. | [Info. comando mkdir (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/mkdir) | 
| `rmdir` | Eliminar carpetas. | [Info. comando rmdir (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/rmdir) | 
| `cp` / `copy` | Copiar archivos. | [Info. comando copy (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/copy) | 
| `rm` / `del` | Eliminar archivos. | [Info. comando del (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/del) | 
| `clear` / `cls` | Limpiar terminal. | [Info. comando cls (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/cls) |
| `mv` / `move` | Mover/Renombrar. | [Info. comando move (Windows)](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/move) |

> [!NOTE]
> En aquellos casos en los que se muestran dos comandos, el primero corresponde a sistemas UNIX (macOS) y el segundo a sistemas MS-DOS (Windows). Si aparece un único comando es aplicable en ambos sistemas. 

> [!TIP]
> Para acceder a las ayudas sobre los comandos UNIX (macOS) puedes usar desde la línea de comandos el comando `man` seguido del nombre del comando sobre el que deseas obtener información. Por ejemplo, la ejecución del comando `man cp` te mostrará una página de ayuda sobre el comando `cp`.  

### 📂 Chuleta de Navegación: Comando `cd` (Change Directory)
El trabajo con directorios (referenciándolos o accediendo a ellos) y el cambio entre ellos, será una tarea habitual, es por esto por lo que es interesante que te familiarices con la navegación empleando el comando `cd`:

| Acción | Unix (Linux / macOS) | Windows (PowerShell / CMD) | Concepto |
| :--- | :--- | :--- | :--- |
| **Entrar en carpeta** | `cd carpeta` | `cd carpeta` | Entra en un directorio dentro del actual. |
| **Subir un nivel** | `cd ..` | `cd ..` | Sube a la carpeta "padre". |
| **Subir varios niveles** | `cd ../..` | `cd ..\..` | Sube dos o más niveles de golpe. |
| **Ir a la raíz** | `cd /` | `cd \` | Va al inicio del disco/partición actual. |
| **Carpeta de usuario** | `cd ~` | `cd ~` (PS) / `cd %USERPROFILE%` (CMD) | Va a tu carpeta personal (Documentos, Escritorio, etc.). |
| **Cambiar de disco** | *(No aplica)* | `D:` (Solo la letra y dos puntos) | Cambia la unidad de almacenamiento. |
| **Ruta con espacios** | `cd "Carpeta A"` | `cd "Carpeta A"` | Las comillas son obligatorias si hay espacios. |
| **Volver atrás** | `cd -` | `cd -` (Solo en PowerShell) | Regresa al último directorio donde estuviste. |
| **Directorio actual** | `.` | `.` | Representa el lugar donde estás ahora mismo. |
| **Directorio superior** | `..`| `..` | Representa una carpeta superior. |

### 💡 Tips de Productividad para trabajar con la línea de comandos
1. **Autocompletado:** Escribe las primeras letras y pulsa `Tabulador` ↹. La terminal escribirá el  resto por ti.
2. **Rutas Absolutas vs Relativas:**
   - **Absoluta:** Empieza desde la raíz (`/` o `C:\`). Ej: `cd /home/usuario/descargas` (Unix) o `cd documentos\proyectos` (Windows).
   - **Relativa:** Empieza desde donde estás. Ej: `cd descargas`.

---

## 📖 Compiladores e Intérpretes Online

Los compiladores e intérpretes son esenciales en programación para comunicar a la máquina qué es lo que queremos que ejecute. Para programar tendremos que tener instalado en nuestro computador un entorno de ejecución o intérprete/compilador del lenguaje en el que programemos. No obstante, en algunos momentos podemos usar compiladores e intérpretes en línea que nos van a permitir escribir, probar, depurar y ejecutar código directamente desde un navegador web, eliminando la necesidad de instalar software pesado en nuestros computadores. Son especialmente útiles para programar desde cualquier lugar, practicar con diferentes lenguajes, compartir código rápidamente y optimizar el rendimiento sin consumir recursos del equipo local.

Existen muchos compiladores e intérpretes en línea, es decir no requieren de instalación en nuestros computadores para usarlos, con lo que esto implica: no hay generación. Algunos de ellos son:

* [myCompiler](https://www.mycompiler.io/es/)
* [OneCompiler](https://onecompiler.com)
* [CodeChef](https://www.codechef.com/ide)
* [paiza.IO](https://paiza.io/es/projects/new)
* [OnlineGDB](https://www.onlinegdb.com)

---

## 🐍 Python

En este curso se empleará el lenguaje Python para la enseñanza y aprendizaje de los fundamentos de los lenguajes de programación, bajo el paradigma imperativo, pero prestando también atención a los paradigmas orientado a objetos y funcional. Al adquirir fundamentos generales de programación se espera que estés preparado para, en un futuro, profundizar en características avanzadas de Python, así como aprender más fácilmente otros lenguajes de programación que pudieras necesitar en tu desempeño profesional. 

Para poder programar en Python, ya sabes… lo primero que necesitas es tener acceso a un intérprete de Python, lo ideal para hacer tu trabajo más eficiente es tenerlo instalado en tu computador. Comprueba si lo tienes instalado, para ello abre la terminal y a través de la línea de comandos ejecuta lo siguiente:

```shell
python --version
```

> [!NOTE]
> Puedes probar también con ``python3``.

Si no lo tienes instalado, visita la página oficial de [Python](https://python.org) y busca la zona de descarga (Downloads). Si la página no detecta tu SO automáticamente, vete a la zona de tu SO para descargarte la versión apropiada. 

Una vez descargado el archivo, ejecútalo… es el instalador. Cuando te de opciones asegúrate de seleccionar la opción "Add Python.exe to PATH", que hará más fácil su uso en el futuro.

---

## 🔠 Otros lenguajes, otros procesadores

A lo largo del curso, en clase, también haremos referencia a otros lenguajes de programación. Para practicar con ellos podrás hacer uso de algún compilador/intérprete disponible online (ver sección [Compiladores e Intérpretes Online](#-compiladores-e-intérpretes-online)) o instalar en tu máquina un compilador o intérprete del lenguaje que vayas a usar. 

Puesto que en el curso vamos a usar un lenguaje interpretado, i.e. Python, te recomiendo que te instales en tu ordenador también un lenguaje compilado, por ejemplo C, para hacer prácticas con él. 

Puesto que Windows no trae un compilador de C de fábrica (macOS sí lo trae, es `gcc`), hay que instalarlo. Instalar un compilador de C en Windows es un proceso sencillo. Vamos a instalar una versión ligera del compilador de C, que funcione desde la terminal (como `gcc`) y que luego más adelante se pueda integrar con Visual Studio Code. 

La forma más fácil de instalar un compilador de C en Windows hoy en día es a través de un gestor como **MSYS2**:

1. Descarga e instala [MSYS2](https://www.msys2.org/).
2. Abre la terminal de MSYS2 (UCRT64) y escribe el siguiente comando para instalar el compilador:
`pacman -S mingw-w64-ucrt-x86_64-gcc`
3. Configura las variables de entorno:
   * Busca en Windows "Editar las variables de entorno del sistema".
   * En "Variables del sistema", busca la que dice **Path**, selecciónala y pulsa "Editar".
   * Añade la ruta de la carpeta bin donde se instaló (si no la cambias, normalmente es `C:\msys64\ucrt64\bin`).

### ¿Cómo saber si lo has instalado bien?

Abre una terminal (CMD o PowerShell) y escribe:

```shell
gcc --version
```

O si has instalado VSC:

```shell
cl --version
```

Si te aparece información sobre la versión y no un error de "comando no reconocido", ¡ya estás listo para probar los ejemplos en C vistos en clase!

---

## 🛂 Software de Control de Versiones 

El **Software de Control de Versiones** (**VCS**, *Version Control System*) es una herramienta esencial en el desarrollo de software. Su misión es rastrear y gestionar cambios en el código fuente a lo largo del tiempo, tomando "fotos instantáneas" (snapshots) de los archivos. Permite a múltiples desarrolladores colaborar simultáneamente, revertir errores, gestionar distintas ramas de desarrollo y mantener un historial seguro del proyecto. A un único programador, le permite  experimentar sin miedo, ya que siempre podrá volver a una versión anterior funcional. Sin un VCS tendríamos archivos como ``ejercicio_final.py``, ``ejercicio_final_v2.py``o incluso ``ejercicio_final_este_es_el_bueno.py``. Mientras que con un VCS tendremos todo en un solo archivo y una línea de tiempo invisible, en la que se puede ver quién hizo qué, cuándo lo hizo y revertir cambios específicos sin perder el resto del trabajo.

[Git](https://git-scm.com) es un **Sistema de Control de Versiones Distribuido** (**DVCS**, *Distributed Version Control System*), en el que cada usuario que trabaje en el proyecto tiene una copia completa del historial en su propia máquina. Como alternativa, existen **Sistemas de control de Versiones Centralizados** (**CVCS**, *Centralized Version Control System*), donde el historial está en una única máquina (un servidor central).    

Conceptos clave que escucharás siempre cuando trabajas con DVCS:

1. **Repositorio (Repo)**: La carpeta de tu proyecto que Git está vigilando.
2. **Commit**: Una "foto" de tus archivos en un momento dado. Es el punto de guardado.
3. **Rama (Branch)**: Una línea de tiempo paralela. Útil para probar funciones nuevas sin romper la versión principal. Son fundamentales en el control de versiones. 
4. **Merge:** Unir los cambios de una rama a otra.

### 📥 Instalación de Git 
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

### 📋 Chuleta de Git: Comandos Esenciales para el Día a Día

| Acción | Comando | Concepto / Uso |
| :--- | :--- | :--- | 
Iniciar repositorio |	``git init``	| Crea un nuevo repositorio de Git local en la carpeta actual. |
Clonar proyecto	 | ``git clone <url>``|	Descarga una copia completa de un repositorio remoto a tu PC. |
Ver estado	| ``git status``	| Muestra qué archivos han cambiado y cuáles están listos para enviarse. | 
Añadir archivo	| ``git add <archivo>``	| Prepara un archivo específico para el siguiente "commit" (Stage). |
Añadir todo	| ``git add .``|	Prepara todos los archivos modificados y nuevos de golpe. |
Confirmar cambios	| ``git commit -m "mensaje"`` |	Guarda tus cambios en el historial con un mensaje descriptivo. |
Deshacer cambios locales | ``git restore <archivo>``| Descarta cambios que no se han guardado con un commit. 
Ver historial	| ``git log`` |	Muestra la lista de todos los commits realizados anteriormente. |
Crear rama	| ``git branch <nombre>``| Crea una nueva línea de tiempo (rama) para trabajar en una función. Con la opción *-d* se borra una rama ``git branch -d <nombre>``|
Cambiar de rama	| ``git switch <nombre>`` |	Salta de una rama a otra (en versiones anteriores se usaba git checkout). Con la opción *-c* se crea la rama ``git switch -c <nombre>``|
Fusionar ramas	| ``git merge <nombre>`` |	Une los cambios de la rama indicada con la rama actual. |
Descargar cambios |	``git pull``| Trae las últimas actualizaciones del servidor y las une a tu código. |
Descargar sin mezclar | ``git fetch``| Descarga el historial del servidor remoto pero no cambia nada en tus archivos de trabajo. |
Subir cambios |	``git push``|	Sube tus commits locales de la rama activa a la rama del repositorio remoto (GitHub, GitLab, etc.) del mismo nombre. |
Deshacer un commit público | ``git revert <id_del_commit>``| Crea un nuevo commit para añadir una corrección a un commit anterior. 

¡Ojo! Si la rama ha sido creada recientemente, en local, la primera vez que se suben cambios al repositorio hay que subirlos con el siguiente comando:

``git push --set-upstream <nombre-remoto> <nombre-de-tu-rama>``

o

``git push -u origin <nombre-de-tu-rama>``

Si alguien ha creado una nueva rama en el repositorio remoto, para traerla a tu local y trabajar con ella debes hacer primero un ``git fetch``y luego cambiar a la rama nueva para trabajar sobre ella ``git switch <nombre-de-la-rama>``.
En resumen, ``git pull`` es para actualizar tu trabajo actual, mientras que ``git fetch`` es para ver todo lo que hay en el servidor. 

### 🚀 Ecosistema de Colaboración: GitHub
Para llevar tus proyectos al siguiente nivel y colaborar con otros, necesitas: una plataforma de alojamiento, donde "colgar" el código para que sea accesible por todos (tu ordenador no lo es); y, si no eres un usuario avanzado, una herramienta con interfaz gráfica para gestionar Git.

* [Github](https://github.com/). Es la plataforma principal donde se guardan los repositorios en la nube. Permite gestionar proyectos, realizar Pull Requests y colaborar con programadores de todo el mundo. Otras alternativas profesionales muy potentes son [GitLab](https://gitlab.com/) (muy utilizado en entornos profesionales) y [Bitbucket](https://bitbucket.org/) (opción muy popular con buena integración con otras herramientas, como Jira, una herramienta de gestión de proyectos).

* [Github Desktop](https://github.com/apps/desktop). Es una aplicación oficial que ofrece una interfaz gráfica (GUI) para gestionar Git. Es ideal si prefieres visualizar tus cambios, ramas y commits de forma intuitiva mediante botones en lugar de comandos de texto. Otras alternativas son [GitKraken](https://www.gitkraken.com) (multiplataforma, muy visual), 
[Sourcetree](https://www.sourcetreeapp.com) (gratuito, popular en Mac/Windows) y [Sublime Merge](https://www.sublimemerge.com) (muy rápido).

#### ✅ Te recomiendo varias lecturas para empezar tu trabajo con Git y GitHub:

- [ ] [Hoja de comandos de Git](https://git-scm.com/cheat-sheet)
- [ ] [Creación de una cuenta en GiHub](https://docs.github.com/es/get-started/start-your-journey/creating-an-account-on-github)
- [ ] [Inicio rápido para repositorios en GitHub](https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories)
- [ ] [Comenzar con GitHub Desktop](https://docs.github.com/es/desktop/overview/getting-started-with-github-desktop)


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
4. **Publicar (`git push`)**: Subes tu rama a **GitHub** para que el historial esté seguro en la nube y otros puedan verla. Recuerda que si es la **primera vez** que haces `push` después de crear la rama debes usar el comando ``git push -u origin <nombre-de-tu-rama>``.
5. **Integrar (Pull Request)**: En la web de GitHub, solicitas permiso para unir (merge) tu rama al tronco principal (`main`).

### 🎨 Diagrama Simplificado del Flujo "Día a Día"

| Orden | Comando | Analogía |
| :--- | :--- | :--- |
| **1** | `git pull` | Mirar si alguien dejó notas nuevas en la pizarra común. |
| **2** | `git switch -c rama` | Sacar una hoja en sucio para no manchar el libro principal. |
| **3** | `git add` + `commit` | Escribir y guardar el progreso en tu propia hoja de trabajo. |
| **4** | `git push` | Mandar una foto de tu hoja terminada al grupo. |
| **5** | **Pull Request** | Preguntar al responsable: "¿Puedo pegar mi hoja en el libro oficial?". |

### ⏪ Cómo retroceder a un commit anterior en Git

En el desarrollo de software y la computación científica, es común cometer errores o querer volver a una versión previa que sabemos que funcionaba correctamente. Git nos ofrece distintas herramientas para "viajar en el tiempo" según nuestra necesidad.

#### 1. Identificar el punto de retorno
Antes de retroceder, necesitamos saber a qué momento de la historia queremos volver. Para ello, revisamos el historial:

```bash
git log --oneline
```

Esto mostrará una lista de commits con su identificador corto (hash), por ejemplo: `a1b2c3d`. Copia el ID del commit al que deseas interactuar.

#### 2. Opciones para regresar a un commit

Dependiendo de si queremos mantener el historial intacto, borrar cambios permanentemente o solo explorar, elegiremos una de estas tres rutas:

##### Opción 1: `git revert` (Recomendada y segura)
Esta opción **no borra el historial**. En su lugar, crea un **nuevo commit** que deshace exactamente los cambios del commit indicado.

* **Comando:** `git revert <ID_del_commit>`
* **¿Qué hace?**: Crea un parche inverso. El historial sigue creciendo hacia adelante, pero el código vuelve al estado anterior.
* **Ideal para:** Proyectos colaborativos en GitHub. Es la forma más limpia de corregir errores sin causar conflictos a tus compañeros.

##### Opción 2: `git reset --hard` (Volver completamente atrás)
Esta opción "mueve" el estado del proyecto al commit elegido y **elimina permanentemente** todos los cambios y commits que se hicieron después de ese punto.

* **Comando:** `git reset --hard <ID_del_commit>`
* **¿Qué hace?**: Borra el rastro de los commits posteriores. El proyecto queda exactamente como estaba en ese punto del pasado.
* **⚠️ Cuidado:** Úsalo solo en local. No se puede deshacer fácilmente y perderás cualquier trabajo no guardado tras ese commit.

##### Opción 3: `git switch` (Modo exploración moderno)
Esta es la forma actual y más clara de navegar a un commit antiguo para revisar el código sin crear ramas nuevas ni borrar nada.

* **Comando:** `git switch --detach <ID_del_commit>`
* **¿Qué hace?**: Mueve temporalmente tu estado de trabajo a ese commit específico. Git te avisará que estás en "detached HEAD", lo que significa que puedes ver y probar todo, pero los cambios que hagas no se guardarán en ninguna rama a menos que crees una nueva.
* **Ideal para**: Inspeccionar cómo funcionaba un algoritmo en el pasado o recuperar un dato que borraste sin querer.
* **Para volver:** Cuando termines de explorar, simplemente regresa a tu rama principal con `git switch main` (o el nombre de tu rama).

>[!NOTE]
> Es necesario usar la opción `--detach`, con `git switch --detach <ID>` le decimos a Git: "No busques una rama, llévame directamente a este punto ciego del historial solo para mirar".


#### 💡 Conclusión: ¿Cuál elegir?

| Si tu objetivo es... | Usa el comando... | ¿Es seguro en equipo? |
| :--- | :--- | :--- |
| **Deshacer un error** manteniendo el registro | `git revert` | ✅ Sí |
| **Borrar todo** y resetear el historial | `git reset --hard` | ❌ No (solo local) |
| **Explorar o revisar** sin romper nada | `git switch` | ✅ Sí |

Saber cuándo usar cada uno te ahorrará muchos problemas en tus proyectos de computación científica, permitiéndote experimentar con el código con la seguridad de que siempre puedes volver a una versión estable.

> [!TIP]
> Algunos Tips adicionales:
> 1. **Visualización:**  Visualmente el `revert` crea un nodo nuevo y el `reset` mueve la flecha hacia atrás.
> 2. **Diferenciación:** Recuerda que el `ID_del_commit` en el caso de `revert` es el commit que quieres **anular**, mientras que en `reset` y `checkout` es el commit al que quieres **llegar**.

> [!TIP]
> Si ya subiste tus cambios a un servidor remoto (como GitHub), usa siempre revert Si los cambios solo están en tu computadora y quieres "limpiar" el desorden, puedes usar reset.

---

## ⚙️ Entorno de Desarrollo Integrado (IDE)

Un **IDE** (*Integrated Development Environment*) es una aplicación software que ayuda a los programadores a desarrollar código de manera eficiente. A diferencia de un simple editor de texto, un IDE combina herramientas de escritura, depuración (corrección de errores) y ejecución en una sola interfaz.

### 🛠️ Herramientas recomendadas para este curso

Comenzaremos usando el **[IDLE](https://docs.python.org/es/3/library/idle.html)**, entorno de desarrollo integrado de Python, ese será tu primer IDE. Más adelante, y dependiendo de tu experiencia previa, puedes elegir entre estas opciones:

#### 🟢 Nivel Principiante (Simplicidad total)
* **[Mu](https://codewith.mu/es/)**: Un editor extremadamente sencillo diseñado para quienes nunca han programado. Su interfaz es limpia y evita distracciones.
* **[Thonny](https://thonny.org/)**: El IDE estándar para aprender Python. Incluye un depurador visual que te permite ver, paso a paso, cómo cambian las variables mientras se ejecuta tu programa.

#### 🔵 Nivel Recomendado / Profesional
* **[VS Code (Visual Studio Code)](https://code.visualstudio.com)**: Es el editor más popular en la industria actual. No es un IDE "puro" de serie para Python, pero mediante **extensiones** se convierte en la herramienta más potente para este lenguaje. Como **ventaja** destacar que se integra perfectamente con Git y GitHub, permitiéndote hacer `commit` y `push` sin salir del programa.

Otros IDEs multilenguaje son: 

* [Eclipse](https://www.eclipse.org) muy usado en el mundo del software libre.
* [Microsoft Visual Studio](https://visualstudio.microsoft.com/es/) diferente a VS Code, este es un IDE "pesado" diseñado para soluciones de nivel empresarial, especialmente en entornos Windows.
* [IntelliJ IDEA (y la suite de JetBrains)](https://www.jetbrains.com/es-es/) solución muy potente. 
* [Apache NetBeans](https://netbeans.apache.org/) un clásico para lenguajes como Java y C pero poco apropiado para Python. 



#### ‼️ Otros Lenguajes

Para otros lenguajes de programación existen otros IDEs. Por ejemplo, si vas a usar C o C++ en este curso para hacer pruebas, deberías tener también instalado en tu computador un compilador de C/C++ y un IDE. Existen muchos en el mercado, incluso puedes usar alguno multilenguaje (p.e. VSC), un ejemplo de IDE para C/C++ es [CLion](https://www.jetbrains.com/clion/) o [Dev-C++ (Embarcadero Edition)](https://www.dev-cpp.com). 

#### Tendencias actuales

La tendencia actual es usar una nueva generación de herramientas de programación impulsadas por Inteligencia Artificial y con un rendimiento extremo. ¡Ojo! No son para ti actualmente, estás aprendiendo...

* [Antigravity](https://antigravity.google), lanzado por Google, es una propuesta muy ambiciosa que busca cambiar la forma en que se programa.
* [Zed](https://zed.dev), una herramienta minimalista pero extremadamente eficiente.
* [Cursor](https://cursor.com/), con la familiaridad de Visual Studio Code saca provecho a la IA.

### 💡 ¿Por qué usar un IDE en lugar de un editor de texto simple?

Como ya se ha comentado un IDE facilita la tarea de programar, ya que tiene:

1.  **Resaltado de sintaxis.** Colorea el código para que identifiques visualmente funciones, variables y errores.
2.  **Autocompletado.** Te sugiere comandos mientras escribes, ahorrando tiempo y evitando erratas.
3.  **Terminal integrada.** Te permite ejecutar tu código y usar comandos de Git en la misma ventana.
4.  **Depuración (Debugging).** Te proporciona multiples ayudas para examinar el funcionamiento del programa con el propósito de detectar y corregir/solucionar fallos.

### 🐍 Comprobación de Python en el IDE

Independientemente del IDE que elijas, asegúrate de que reconozca tu instalación de Python. Puedes verificarlo abriendo la terminal integrada del IDE y escribiendo:

```shell
python --version
```

--- 

## Sumario de enlaces interesantes

### Python

* [Python](https://python.org)

### Plataforma de distribución de software y desarrollo para Windows

* [MSYS2](https://www.msys2.org/)

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
* [Python para todos](https://es.py4e.com)

---

## 🧭 Menú de Navegación

| Orden  | Material                                                                  | Tiempo       | 
|:------:|:--------------------------------------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T1_ICC.md)                                             |      8       |
| 2      | **Recursos**                                                              |      7       |
| 3      | [Ejemplos](../ejemplos/T1_Ejem_ICC.md)                                    |      -       |
| 4      | [Ejercicios](../ejercicios/T1_Ejer_ICC.md)                                |      -       |
|        | [Menu del Tema actual](../README.md#-menú-de-navegación-en-el-tema)       |      -       | 