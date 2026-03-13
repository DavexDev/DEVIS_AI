# DEVIS AI — Contexto del Proyecto

> Archivo de contexto actualizado el 12 de marzo de 2026.
> Úsalo para retomar la conversación o el desarrollo en cualquier momento.

---

## Identidad del asistente

**DEVIS** (Development Intelligent System) — asistente CLI especializado en:

- Matemáticas computacionales (derivadas, integrales, matrices, simplificación)
- MATLAB — ejemplos de fplot, det, inv
- Flutter/Dart — widgets, pantallas, lógica
- IA local con TinyLlama vía Ollama (activo desde v0.2)

---

## Repositorio

```
https://github.com/DavexDev/DEVIS_AI.git
rama: main
commit inicial: 98b2341
commit v0.2:   dc1a1f5
```

---

## Estructura actual del proyecto

```
DEVIS_AI/
├── core/
│   ├── __init__.py
│   └── parser.py                  ← parser de expresiones naturales
├── modules/
│   ├── __init__.py
│   ├── math_engine.py             ← motor matemático (5 operaciones)
│   ├── command_router.py          ← enrutador de comandos CLI
│   └── flutter_generator.py       ← generador de código Flutter (v0.5)
├── knowledge/
│   ├── matlab/          (22 archivos)
│   │   ├── graficas.md, matrices.md, ode.md, estadistica.md
│   │   ├── multiplicacion_matrices.md, suma_matrices.md
│   │   ├── transpuesta_matrices.md, matrices_automaticas.md
│   │   ├── graficas_trigonometricas.md, grafica_polar.md
│   │   ├── cardioide_polar.md, grafica_3d_resorte.md
│   │   ├── subplots.md, superficie_3d.md, formatos_numericos.md
│   │   ├── reshape_matriz.md, vector_incremento.md, matriz_rangos.md
│   │   └── lectura_csv.md, grafica_barras.md, guardar_variables.md, numeros_aleatorios.md
│   ├── flutter/         (8 archivos)
│   │   ├── login.md, widgets.md, navegacion.md, estado.md
│   │   └── contador_basico.md, lista_notas.md, widget_personalizado.md, web.md
│   ├── python/          (2 archivos)
│   │   └── numpy.md, pandas.md
│   └── dart/            (8 archivos — estructuras de datos)
│       ├── listas_enlazadas.md, pilas.md, colas.md
│       ├── arbol_binario.md, recorridos_arbol.md
│       └── arbol_avl.md, propiedades_arbol.md, equilibrio_arbol.md
├── executor/
│   ├── __init__.py
│   ├── ollama_connector.py        ← cliente TinyLlama activo (v0.2)
│   └── octave_runner.py           ← ejecutor MATLAB/Octave (v0.4)
├── devis_cli.py                   ← entrada principal / CLI
├── requirements.txt               ← sympy>=1.12, requests>=2.28
├── .gitignore
├── README.md
└── CONTEXT.md                     ← este archivo
```

---

## Descripción de cada módulo

### `core/parser.py`

Convierte sintaxis matemática natural a objetos SymPy.

- Usa `sympy.parsing.sympy_parser` con transformaciones:
  - `standard_transformations`
  - `implicit_multiplication_application` → `2x` = `2*x`
  - `convert_xor` → `x^2` = `x**2`
- Función principal: `parse_natural(expr_str) -> Expr`
- Soporta: `x^2 + 3x`, `sin(x)cos(x)`, `e^x`, `(x^2-1)/(x-1)`

### `modules/math_engine.py`

Motor matemático. Todas las funciones reciben `str` y retornan `str` (pretty-print SymPy).
| Función | Operación |
|---|---|
| `derivada(expr_str)` | `diff(expr, x)` |
| `integral(expr_str)` | `integrate(expr, x)` + `" + C"` |
| `simplificar(expr_str)` | `simplify(expr)` |
| `det_matriz(filas_str)` | `Matrix(...).det()` |
| `inv_matriz(filas_str)` | `Matrix(...).inv()` con validación singular |

Las matrices se ingresan como `"[[1,2],[3,4]]"` y se parsean con `ast.literal_eval` (sin `eval()`).

### `modules/command_router.py`

Clase `CommandRouter` con método `route(user_input) -> str | None`.

- Retorna `None` para indicar salida (`exit`)
- Detecta comandos: `derivada`, `integral`, `simplificar`, `det`, `inv`, `ejemplo matlab`, `ejemplo flutter`, `ejemplos`, `ia`, `help`, `exit`
- Extrae argumentos en línea (`derivada x^2 + 3x`) o pide con `input()` si faltan
- Lee archivos `.md` de `knowledge/` para los ejemplos

### `executor/ollama_connector.py`

Clase `OllamaConnector` con método `query(prompt) -> str`.

- `_health_check()`: al arrancar hace GET a `/api/tags`, verifica que `tinyllama` esté listado
- `query()`: hace POST a `http://localhost:11434/api/generate` con `stream=False`
- Manejo explícito de `ConnectionError`, `Timeout` y `HTTPError`
- Si el servidor cae en sesión, `self.available` se pone en `False` automáticamente

### `devis_cli.py`

Punto de entrada. Muestra banner ASCII, instancia `CommandRouter`, loop `while True`.

- Maneja `KeyboardInterrupt` y `EOFError` con salida limpia
- Ejecutar con: `python3 devis_cli.py`

---

## Comandos disponibles en DEVIS

```
derivada          → d/dx de f(x)
integral          → integral indefinida de f(x)
simplificar       → simplificación algebraica
det               → determinante de matriz cuadrada
inv               → inversa de matriz cuadrada
ejemplo matlab <tema>    → 22 temas disponibles
ejemplo flutter <tema>   → 7 temas disponibles
ejemplo python <tema>    → numpy, pandas
ejemplo dart <tema>      → 8 temas de estructuras de datos
ejemplos          → lista todas las categorías y temas
ia <consulta>     → IA local TinyLlama (Ollama)
help              → ayuda
exit              → salir
```

---

## Decisiones de diseño tomadas

| Decisión              | Elección                                       | Razón                                                |
| --------------------- | ---------------------------------------------- | ---------------------------------------------------- |
| Parser de expresiones | `sympy.parsing` con transformaciones           | Más robusto que regex; soporta `sin(x)`, `e^x`, etc. |
| Sintaxis de entrada   | Natural (`x^2 + 3x`)                           | Más cómodo para el usuario                           |
| Matrices              | `ast.literal_eval`                             | Seguro, sin `eval()`                                 |
| Modelo IA             | TinyLlama vía Ollama                           | ~637 MB, corre en laptop sin GPU                     |
| Versión IA            | Stub en v0.1, activo en v0.2                   | Interfaz definida sin romper el router               |
| Dependencias v0.1     | Solo `sympy`                                   | Sin peso extra                                       |
| Dependencias v0.2     | `sympy` + `requests`                           | Mínimas para HTTP a Ollama                           |
| Knowledge v0.3        | 4 categorías: matlab / flutter / python / dart | Cobertura ampliada sin cambiar el router             |

---

## Entorno de desarrollo

- **OS**: Kali Linux
- **Python**: 3.13.11 (`/usr/bin/python3`)
- **SymPy**: 1.14.0 (instalado con `--break-system-packages`)
- **requests**: 2.32.5 (instalado con `--break-system-packages`)
- **Nota venv**: el `.venv/` local está incompleto (sin pip). Usar `/usr/bin/python3` directamente.
- **Ejecutar**: `/usr/bin/python3 devis_cli.py` desde `/home/mrrobot/DEVIS_AI/`

---

## Hoja de ruta

| Versión  | Estado          | Contenido                                                  |
| -------- | --------------- | ---------------------------------------------------------- |
| **v0.1** | ✅ **Completo** | CLI + motor matemático + base de conocimiento              |
| **v0.2** | ✅ **Completo** | IA local TinyLlama vía Ollama (health-check + POST real)   |
| **v0.3** | ✅ **Completo** | Base de conocimiento expandida (40 archivos, 4 categorías) |
| **v0.4** | ✅ **Completo** | Ejecución MATLAB/Octave vía subprocess (modo multi-línea)  |
| **v0.5** | ✅ **Completo** | Generador de código Flutter con plantillas + IA opcional   |

---

## Próximos pasos sugeridos (v0.5)

```
Idea: generador de código Flutter
- El usuario describe una pantalla en lenguaje natural
- DEVIS genera el código Dart/Flutter correspondiente
- Podría usar la IA local (TinyLlama) o plantillas predefinidas
```

---

## Tests smoke (verificación rápida)

```bash
cd ~/DEVIS_AI
python3 test_smoke.py
```

Resultados esperados:

```
OK  derivada   x^3 + 2x  =>  3⋅x² + 2
OK  integral   x^2       =>  x³/3  + C
OK  simplificar (x^2-1)/(x-1)  =>  x + 1
OK  det [[1,2],[3,4]]    =>  -2
OK  inv [[1,2],[3,4]]    =>  [[-2, 1], [3/2, -1/2]]
```
