# DEVIS AI — Manual de Usuario

> **Versión:** v0.5 | **Fecha:** 12 de marzo de 2026
> **Plataforma:** Kali Linux · Python 3.13+ · CLI

---

## Índice

1. [¿Qué es DEVIS?](#1-qué-es-devis)
2. [Instalación y requisitos](#2-instalación-y-requisitos)
3. [Iniciar DEVIS](#3-iniciar-devis)
4. [Matemáticas](#4-matemáticas)
5. [Base de conocimiento](#5-base-de-conocimiento)
6. [Ejecutar código MATLAB](#6-ejecutar-código-matlab)
7. [Generador de código Flutter](#7-generador-de-código-flutter)
8. [IA local (TinyLlama)](#8-ia-local-tinyllama)
9. [Comandos de referencia rápida](#9-comandos-de-referencia-rápida)
10. [Solución de problemas](#10-solución-de-problemas)

---

## 1. ¿Qué es DEVIS?

**DEVIS** (Development Intelligent System) es un asistente de desarrollo que corre
completamente en tu equipo, sin conexión a la nube. Desde una terminal puedes:

- Calcular derivadas, integrales, determinantes e inversas simbólicamente
- Consultar ejemplos listos de MATLAB, Flutter, Python y Dart
- Ejecutar bloques de código MATLAB usando GNU Octave
- Generar código Flutter a partir de una descripción en español
- Hacer preguntas a un modelo de lenguaje local (TinyLlama vía Ollama)

---

## 2. Instalación y requisitos

### Requisitos mínimos

| Componente         | Versión mínima | Notas                       |
| ------------------ | -------------- | --------------------------- |
| Python             | 3.10+          | Se recomienda 3.13          |
| sympy              | 1.12+          | Motor matemático            |
| requests           | 2.28+          | Necesario para IA (Ollama)  |
| GNU Octave         | 8.x            | Solo para `ejecutar matlab` |
| Ollama + TinyLlama | cualquiera     | Solo para comando `ia`      |

### Instalar dependencias Python

```bash
pip install sympy requests
# En Kali/Debian con Python del sistema:
pip install sympy requests --break-system-packages
```

### Instalar GNU Octave (para ejecutar MATLAB)

```bash
sudo apt update
sudo apt install octave -y
```

### Instalar Ollama + TinyLlama (para IA local)

```bash
# Instalar Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Descargar modelo TinyLlama (~637 MB, sin GPU)
ollama run tinyllama

# Iniciar servidor (necesario al usar DEVIS)
ollama serve
```

---

## 3. Iniciar DEVIS

```bash
cd ~/DEVIS_AI
python3 devis_cli.py
```

Verás el banner:

```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║    ██████╗ ███████╗██╗   ██╗██╗███████╗             ║
║    ...                                               ║
║    Development Intelligent System  v0.5              ║
║    Matemáticas · MATLAB · Flutter · Octave · IA      ║
╚══════════════════════════════════════════════════════╝
  Escribe 'help' para ver los comandos disponibles.
```

Para cerrar: escribe `exit` o presiona `Ctrl+C`.

---

## 4. Matemáticas

DEVIS usa SymPy para cálculo simbólico. Las expresiones se escriben en notación
natural: `x^2`, `sin(x)`, `e^x`, `2x` (sin `*`).

### 4.1 Derivada

```
DEVIS> derivada x^3 + 2x
```

También puedes escribirlo solo y DEVIS te pedirá la expresión:

```
DEVIS> derivada
  f(x): sin(x) * e^x
```

**Ejemplos:**

| Entrada                 | Resultado       |
| ----------------------- | --------------- |
| `derivada x^3 + 2x`     | `3x² + 2`       |
| `derivada sin(x)`       | `cos(x)`        |
| `derivada e^x`          | `eˣ`            |
| `derivada x^2 * log(x)` | `x + 2x·log(x)` |

### 4.2 Integral indefinida

```
DEVIS> integral x^2 + 3x
```

**Ejemplos:**

| Entrada           | Resultado     |
| ----------------- | ------------- |
| `integral x^2`    | `x³/3 + C`    |
| `integral sin(x)` | `-cos(x) + C` |
| `integral 1/x`    | `log(x) + C`  |

### 4.3 Simplificar

```
DEVIS> simplificar (x^2 - 1) / (x - 1)
```

**Ejemplos:**

| Entrada                           | Resultado     |
| --------------------------------- | ------------- |
| `simplificar (x^2-1)/(x-1)`       | `x + 1`       |
| `simplificar sin(x)^2 + cos(x)^2` | `1`           |
| `simplificar (x+1)^2`             | `x² + 2x + 1` |

### 4.4 Determinante

```
DEVIS> det [[1,2],[3,4]]
```

Formato de matrices: `[[fila1],[fila2],...]`, sin espacios obligatorios.

**Ejemplos:**

| Entrada                         | Resultado |
| ------------------------------- | --------- |
| `det [[1,2],[3,4]]`             | `-2`      |
| `det [[1,0,0],[0,2,0],[0,0,3]]` | `6`       |

### 4.5 Inversa

```
DEVIS> inv [[1,2],[3,4]]
```

**Ejemplo:**

```
DEVIS> inv [[1,2],[3,4]]

  Inversa:
  ⎡-2    1  ⎤
  ⎢         ⎥
  ⎣3/2  -1/2⎦
```

---

## 5. Base de conocimiento

DEVIS incluye más de 40 archivos Markdown con código listo para copiar y usar.

### Listar categorías y temas

```
DEVIS> ejemplos
  MATLAB   : graficas, matrices, ode, estadistica, ...
  Flutter  : login, widgets, navegacion, estado, ...
  Python   : numpy, pandas
  Dart     : listas_enlazadas, pilas, colas, ...
```

### Ver un ejemplo

```
DEVIS> ejemplo matlab graficas
DEVIS> ejemplo flutter login
DEVIS> ejemplo python numpy
DEVIS> ejemplo dart pilas
```

### Categorías disponibles

#### MATLAB (22 temas)

| Tema                       | Descripción                         |
| -------------------------- | ----------------------------------- |
| `graficas`                 | fplot, hold on, legend              |
| `matrices`                 | operaciones básicas                 |
| `ode`                      | ecuaciones diferenciales ordinarias |
| `estadistica`              | media, std, histograma              |
| `multiplicacion_matrices`  | producto matricial                  |
| `suma_matrices`            | suma y resta                        |
| `transpuesta_matrices`     | A'                                  |
| `matrices_automaticas`     | zeros, ones, eye, linspace          |
| `graficas_trigonometricas` | sin, cos, tan en fplot              |
| `grafica_polar`            | polar plot                          |
| `cardioide_polar`          | curva cardioide                     |
| `grafica_3d_resorte`       | plot3 helicoidal                    |
| `subplots`                 | múltiples gráficas en una figura    |
| `superficie_3d`            | mesh, surf                          |
| `formatos_numericos`       | fprintf, format                     |
| `reshape_matriz`           | reshape, size, numel                |
| `vector_incremento`        | a:paso:b                            |
| `matriz_rangos`            | indexado y slicing                  |
| `lectura_csv`              | readtable, csvread                  |
| `grafica_barras`           | bar, barh                           |
| `guardar_variables`        | save, load                          |
| `numeros_aleatorios`       | rand, randn, randi, rng             |

#### Flutter (8 temas)

| Tema                   | Descripción                           |
| ---------------------- | ------------------------------------- |
| `login`                | Formulario con validación             |
| `widgets`              | Scaffold, AppBar, FAB de referencia   |
| `navegacion`           | Navigator push/pop + go_router        |
| `estado`               | setState, Provider, Riverpod          |
| `contador_basico`      | StatefulWidget completo               |
| `lista_notas`          | ListView + AlertDialog + FilledButton |
| `widget_personalizado` | StatelessWidget con parámetros        |
| `web`                  | Guía completa Flutter Web             |

#### Python (2 temas)

`numpy`, `pandas`

#### Dart (8 temas)

`listas_enlazadas`, `pilas`, `colas`, `arbol_binario`, `recorridos_arbol`,
`arbol_avl`, `propiedades_arbol`, `equilibrio_arbol`

---

## 6. Ejecutar código MATLAB

DEVIS puede ejecutar bloques de código MATLAB usando GNU Octave.

> **Requisito:** `sudo apt install octave -y`

### Uso

```
DEVIS> ejecutar matlab

  Ingresa código MATLAB línea a línea.
  Escribe 'fin' para ejecutar, 'cancelar' para salir.

  >> x = 1:5;
  >> disp(sum(x))
  >> fin

15
```

### Más ejemplos

**Calcular determinante:**

```
  >> A = [1 2; 3 4];
  >> disp(det(A))
  >> fin
-2
```

**Graficar seno:** _(abre ventana gráfica)_

```
  >> x = 0:0.01:2*pi;
  >> plot(x, sin(x))
  >> title('Seno')
  >> fin
```

**Cancelar sin ejecutar:**

```
  >> x = 1:10;
  >> cancelar
```

### Notas

- El código se ejecuta en un archivo `.m` temporal que se borra al finalizar.
- Tiempo máximo de ejecución: **15 segundos** (protección ante bucles infinitos).
- Si Octave no está instalado, DEVIS muestra las instrucciones de instalación y
  sigue funcionando con normalidad.

---

## 7. Generador de código Flutter

DEVIS genera código Flutter listo para usar a partir de una descripción
en lenguaje natural.

```
DEVIS> generar flutter pantalla de login con validación
```

O sin descripción inline (DEVIS la pide):

```
DEVIS> generar flutter
  Describe la pantalla/componente (ej: 'pantalla de login con validación'): lista de tareas con eliminar
```

### Plantillas disponibles

| Palabras clave detectadas              | Plantilla generada                     |
| -------------------------------------- | -------------------------------------- |
| login, formulario, contraseña, usuario | Pantalla de Login                      |
| lista, notas, items, crud, agregar     | Lista de Items                         |
| contador, incrementar, decrementar     | Contador con StatefulWidget            |
| navegacion, rutas, paginas, go_router  | Navegación con go_router               |
| estado, provider, riverpod, setstate   | Manejo de Estado con Provider          |
| widget, componente, personalizado      | Widget Personalizado (StatelessWidget) |
| _(cualquier otra cosa)_                | Página básica (Scaffold + AppBar)      |

### Ejemplo de salida

```
DEVIS> generar flutter pantalla de login

  ── Flutter Generator ───────────────────────────────────
  Descripción : pantalla de login
  Plantilla   : Pantalla de Login
  ─────────────────────────────────────────────────────────

import 'package:flutter/material.dart';

void main() => runApp(const MyApp());
...

  ── Para correr en web ──────────────────────────────────
  flutter run -d chrome
```

### Con IA (cuando Ollama está activo)

Si `ollama serve` está corriendo con TinyLlama, el generador usa la IA para
personalizar el código según tu descripción específica.

---

## 8. IA local (TinyLlama)

```
DEVIS> ia cómo funciona un árbol AVL?
DEVIS> ia explica qué es Provider en Flutter
DEVIS> ia dame un ejemplo de función recursiva en Dart
```

O sin argumento:

```
DEVIS> ia
  Consulta: ¿cuál es la diferencia entre StatelessWidget y StatefulWidget?
```

### Configurar Ollama

```bash
# Terminal 1: iniciar servidor
ollama serve

# Terminal 2: verificar modelo disponible
ollama list

# Si TinyLlama no aparece, descargarlo:
ollama pull tinyllama
```

> **Si Ollama no está corriendo:** DEVIS muestra instrucciones de instalación
> y todos los demás comandos siguen funcionando normalmente.

---

## 9. Comandos de referencia rápida

```
derivada  [expr]         →  d/dx de expr
integral  [expr]         →  ∫expr dx
simplificar [expr]       →  simplificación algebraica
det [matriz]             →  determinante
inv [matriz]             →  inversa
ejemplo matlab  [tema]   →  código MATLAB
ejemplo flutter [tema]   →  código Flutter
ejemplo python  [tema]   →  código Python
ejemplo dart    [tema]   →  código Dart
ejemplos                 →  listar todos los temas
ejecutar matlab          →  modo multi-línea para correr MATLAB
generar flutter [desc]   →  generar código Flutter desde descripción
ia [consulta]            →  pregunta a TinyLlama
help                     →  esta ayuda
exit                     →  cerrar DEVIS
```

**Atajos de teclado:**

| Tecla     | Acción                                        |
| --------- | --------------------------------------------- |
| `Ctrl+C`  | Cerrar DEVIS (o cancelar entrada multi-línea) |
| `Ctrl+D`  | Cerrar DEVIS (EOF)                            |
| `↑` / `↓` | Historial de comandos (readline)              |

---

## 10. Solución de problemas

### `ModuleNotFoundError: No module named 'sympy'`

```bash
pip install sympy --break-system-packages
```

### `ModuleNotFoundError: No module named 'requests'`

```bash
pip install requests --break-system-packages
```

### `GNU Octave no está instalado`

```bash
sudo apt update && sudo apt install octave -y
```

### Ollama no responde / tiempo de espera

```bash
# Verificar que el servidor esté corriendo
ollama serve

# En otro terminal, verificar modelo
ollama list
# Si TinyLlama no aparece:
ollama pull tinyllama
```

### El `.venv/` no funciona en Kali

El entorno virtual local puede quedar incompleto en Kali. Usa siempre Python
del sistema:

```bash
/usr/bin/python3 devis_cli.py
```

### Smoke test rápido

```bash
cd ~/DEVIS_AI
python3 test_smoke.py
```

Resultado esperado:

```
OK  derivada   x^3 + 2x  =>  3⋅x² + 2
OK  integral   x^2       =>  x³/3 + C
OK  simplificar (x^2-1)/(x-1)  =>  x + 1
OK  det [[1,2],[3,4]]  =>  -2
OK  inv [[1,2],[3,4]]  =>  [[-2, 1], [3/2, -1/2]]
```

---

## Historial de versiones

| Versión | Fecha    | Cambios                                                 |
| ------- | -------- | ------------------------------------------------------- |
| v0.1    | Mar 2026 | CLI + motor SymPy + base de conocimiento inicial        |
| v0.2    | Mar 2026 | IA local TinyLlama vía Ollama                           |
| v0.3    | Mar 2026 | Expansión masiva: 40 archivos, categorías python y dart |
| v0.4    | Mar 2026 | Ejecución MATLAB/Octave con modo multi-línea            |
| v0.5    | Mar 2026 | Generador de código Flutter con plantillas + IA         |

---

_DEVIS AI — Desarrollado para entornos sin conexión en Kali Linux._
