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

# 🎓 Recursos - Tema 2: Algoritmia 🧩

A continuación se listan herramientas y recursos útiles para practicar el **diseño y representación de algoritmos** (pseudocódigo y diagramas de flujo).

---

## 🧾 Pseudocódigo

Para el pseudocódigo no existen un conjunto de reglas léxicas ni sintácticas estrictas o formales como las de cualquier otro lenguaje. El pseudocódigo es una herramienta flexible diseñada para ser leída por humanos. Existen muchas "variantes", pero lo importante es que cualquiera de la usada, represente de manera clara, estructurada y lógica el algoritmo. Para elllo es conveniente seguir una serie de recomendaciones prácticas:

### ✅ Reglas prácticas (muy recomendadas)

#### Convenciones estructurales
1. Usa **palabras clave claras** para definir el inicio y fin de algoritmos o bloques o estructuras, como INICIO/FIN, SI/FINSI, MIENTRAS/FINMIENTRAS, PARA/FINPARA...
2. Usa el idioma requerido por el equipo de trabajo, el uso del inglés es común (IF, ENDIF, WHILE, ENDWHILE) y de utilidad en equipos internacionales, pero el español también es válido y útil en entornos individuales o nacionales. 
3. Usa el **sangrado (Indentation)** para mostrar la jerarquía y bloques de código anidados (por ejemplo, dentro de un bloque SI o MIENTRAS).
4. Escribe una **instrucción por línea** para facilitar la lectura. Pueden numerarse para facilitar referirnos a puntos en concreto del algoritmo.

#### Convenciones léxicas
1. Usa **mayúsculas** y **minúsculas**. Se acostumbra a usar palabras en mayúsculas para las estructuras de control principales y en minúsculas para las variables. Esto no es estrictamente necesario.
2. Usa **palabras con semántica** y relación con las construcciones usadas:
* Entrada/Salida: LEER, OBTENER, MOSTRAR, IMPRIMIR, ESCRIBIR.
* Decisión: SI...ENTONCES...SINO...FINSI.
* Bucles: MIENTRAS, HACER...HASTA QUE, PARA...HASTA...FINPARA.
3. Usa símbolos y operadores habituales (aritméticos y relacionales), y estándar donde se requiera, por ejemplo la asignación con ← (p.e. media ← (a+b) / 2 ).
4. Usa para las variables **nombres claros y que describan su propósito**, por ejemplo `radio`, `area`, `suma`, `contador` o `calculaArea`. 

#### Generales

1. Indica claramente variables de **entrada / intermedias / salida** (siempre que el problema lo permita).
2. **Mantén el pseudocódigo sintácticamdente independiente del lenguaje** (no uses `print()`, `input()`, o incluso '`{`/`}`, etc.), a menos que sea una convención acordada por el equipo de trabajo. 
3. **Evita ambigüedades**, si faltan cosas o casos, el algoritmo no está completo.

> [!NOTE]
> Todas estas "reglas" del pseudocódigo son más pautas de legibilidad que normas obligatorias.

Existen herramientas para programar en pseudocódigo y generar diagramas de flujo a partir de ellos (p.e. [PSeInt](https://pseint.sourceforge.net)). También te pueden ayudar los LLMs a hacer la transformación 😜. 

---

## 📊 Diagramas de flujo

Otro de los mecanismos que existen para representar de forma gráfica un algoritmo o proceso son los diagramas de flujo. Este mecanismo permite ver más fácilmente cuál es el orden de las acciones. 

Aunque los símbolos gráficos utilizados en los diagramas de flujo han sido estandarizados por el American National Standards Institute (ANSI) ([ISO 5807:1985](https://www.iso.org/standard/11955.html)), no existe un "estandar" ampliamente usado. Cada herramienta emplea sus propias convenciones. Nosotros usaremos los vistos en clase, que los permiten la mayoría de herramientas, siendo los principales los siguientes: 

* *Óvalo*: Representa los puntos de inicio y finalización dentro de una secuencia.
* *Paralelogramo*: Indica una entrada o salida.
* *Rectángulo*: Indica una acción.
* *Rombo*: Indica decisiones que tienen que tomarse, suelen dar lugar a dos caminos aunque también suelen usarse para la selección múltiples caminos (más de dos) según el resultado de la decisión o comparación realizada.
* *Flecha*: Indica las direcciones que toma la secuencia.  

A continuación se referencian una serie de herramientas de utilidad para la creación de diagramas de flujo.

### Herramientas online (sin instalar nada)
- **[draw.io](https://www.drawio.com)**: editor gratuito, exporta a PNG/SVG/PDF.
- **[Lucidchart](https://lucid.app/)**: muy potente.
- **[Canva](https://www.canva.com/es_es/)**: tiene plantillas de diagramas, útil si quieres un estilo visual cuidado.
- **[Miro](https://miro.com/)**: pizarra colaborativa (ideal para trabajar en grupo).
- **[Mermaid](https://www.mermaidonline.live/es/flowchart)**: permite escribir diagramas en texto y renderizarlos (GitHub soporta Mermaid).

Todas ellas tienen un plan gratuito limitado que os permite hacer las cosas básicas necesarias. 

### Herramientas “ligeras” para apuntes y GitHub

- **[PlantUML](https://plantuml.com/es/)**: diagramas a partir de texto, muy usado en entornos técnicos.

> [!TIP]
> Si te interesa documentar algoritmos dentro del repositorio GitHub, **Mermaid** suele ser la opción más cómoda porque el diagrama se “versiona” como texto.

---

## 📚 Lecturas y referencias recomendadas

- [Cambridge International Pseudocode Guide](https://www.cambridgeinternational.org/Images/697401-2026-pseudocode-guide-for-teachers.pdf). Ejemplo de Guía "más formal" para escritura de pseudocódigo.
- Conceptos básicos de algoritmos (entrada/salida, pasos, finitud): cualquier texto introductorio de programación.
- Diagramas de flujo (símbolos y convenciones): busca “flowchart symbols” y revisa tablas comparativas.

---

## 🧭 Menú de Navegación

| Orden  | Material                                   | Tiempo       | 
|:------:|:-------------------------------------------|:------------:|
| 1      | [Teoría](../teoria/T2_ICC.md)              |      6       |
| 2      | **Recursos**                               |      5       |
| 3      | [Ejemplos](../ejemplos/T2_Ejem_ICC.md)     |      -       |
| 4      | [Ejercicios](../ejercicios/T2_Ejer_ICC.md) |      -       |
|        | [Menu del Tema actual](../README.md)       |      -       |
