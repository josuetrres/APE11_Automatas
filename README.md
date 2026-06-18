# Informe de Proyecto: Analizadores Léxicos y Sintácticos de Ecuaciones Algebraicas

## 1. Introducción
El objetivo de este proyecto es construir un analizador léxico y sintáctico capaz de procesar y validar un sistema de ecuaciones algebraicas (por ejemplo, `x+y=30`). 

Para demostrar la equivalencia teórica y práctica en la construcción de compiladores, el sistema ha sido desarrollado desde cero utilizando dos tecnologías diferentes:
1. **Java**, empleando las herramientas **JFlex** y **Java CUP**.
2. **Python**, empleando la biblioteca **PLY (Python Lex-Yacc)**.

Ambos programas leen un mismo archivo de entrada (`entrada.txt`) y validan línea por línea si la ecuación escrita cumple con las reglas matemáticas predefinidas.

---

## 2. Análisis Léxico (Tokens)
El analizador léxico es el encargado de leer los caracteres del archivo de texto y agruparlos en unidades con significado llamadas **Tokens**. Se definieron los siguientes:

* **ID (Identificador):** Empieza con una letra, seguida de letras o números (Ej: `x`, `y10`, `resultado`).
* **NUM (Número):** Secuencia de uno o más dígitos (Ej: `30`, `1000`).
* **Operadores Aritméticos:** `SUMA (+)`, `RESTA (-)`, `MULT (*)`, `DIV (/)`.
* **Asignación:** `IGUAL (=)`.
* **Separador:** `EOL` (Salto de línea, indica el fin de una ecuación).

Los espacios y tabulaciones son ignorados por el lexer.

---

## 3. Análisis Sintáctico (Gramática)
El analizador sintáctico recibe los tokens y comprueba que estén en un orden válido utilizando una gramática libre de contexto LALR(1).

### Reglas Gramaticales (BNF)
El lenguaje se define formalmente de la siguiente manera:

1. **sistema** $\rightarrow$ **lista_ecuaciones**
2. **lista_ecuaciones** $\rightarrow$ **ecuacion** | **lista_ecuaciones** **EOL** **ecuacion**
3. **ecuacion** $\rightarrow$ **expresion** **IGUAL** **expresion**
4. **expresion** $\rightarrow$ **ID** | **NUM** 
5. **expresion** $\rightarrow$ **expresion** **OPERADOR** **expresion**

*(Donde OPERADOR puede ser SUMA, RESTA, MULT o DIV).*

### Precedencia y Asociatividad
Para evitar la ambigüedad en operaciones matemáticas (por ejemplo, saber que la multiplicación se resuelve antes que la suma), el parser implementa reglas de precedencia:
- La multiplicación (`*`) y división (`/`) tienen **mayor precedencia**.
- La suma (`+`) y resta (`-`) tienen **menor precedencia**.
- Todos los operadores tienen asociatividad por la izquierda.

### Recuperación de Errores (Modo Pánico)
Si el usuario escribe una ecuación mal formada (ej. `x+y1000` sin el signo `=` ni el resultado), los analizadores no abortan la ejecución del programa. En su lugar, reportan en qué línea y columna ocurrió el error, descartan esa ecuación (ignorando los tokens hasta llegar al final de la línea), y continúan analizando las siguientes ecuaciones matemáticas de manera transparente.

---

## 4. Arquitectura de las Implementaciones

### Implementación en Java (JFlex y Java CUP)
Ubicación: Carpeta `Java/`
* **JFlex (`lexer.flex`)**: Contiene las expresiones regulares y retorna los objetos `Symbol` de CUP.
* **CUP (`parser.cup`)**: Define la gramática y el código Java embebido para reportar errores e imprimir los resultados en consola.
* **Maven**: Se estructuró el proyecto utilizando Maven para automatizar la construcción. Los plugins generan los archivos de Java a partir de los `.flex` y `.cup` en tiempo de compilación.

**Ejecución:**
```bash
cd Java
mvn clean compile
mvn exec:java
```

### Implementación en Python (PLY)
Ubicación: Carpeta `Python/`
Para Python se utilizó **PLY**, que es la adaptación directa de Lex y Yacc. Para mantener el principio de código limpio y modular, el sistema se dividió en tres archivos:
* **`lexer_rules.py`**: Contiene las expresiones regulares (mediante convenciones de prefijos `t_`) y genera el lexer.
* **`parser_rules.py`**: Importa los tokens e implementa la gramática mediante funciones de Python y *docstrings*.
* **`main.py`**: El punto de entrada principal que inicializa ambos módulos y mide el tiempo de ejecución.

**Ejecución:**
Requiere la instalación del módulo `ply`.
```bash
cd Python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 5. Conclusión
El proyecto comprueba exitosamente que, independientemente del lenguaje o de la herramienta subyacente (JFlex/CUP vs PLY), los conceptos teóricos de compiladores y teoría de autómatas se mantienen consistentes. Ambas soluciones logran procesar el mismo conjunto de datos con gramáticas idénticas, ofreciendo robustez mediante un manejo avanzado de errores.
