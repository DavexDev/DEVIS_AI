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
│   └── command_router.py          ← enrutador de comandos CLI
├── knowledge/
│   ├── matlab/
│   │   ├── graficas.md            ← ejemplo fplot, grid, title
│   │   ├── matrices.md            ← ejemplo det, inv, rank
│   │   ├── ode.md                 ← ecuaciones diferenciales (ode45, dsolve)
│   │   └── estadistica.md        ← mean, std, histfit, corrcoef
│   ├── flutter/
│   │   ├── login.md               ← pantalla login completa (Dart)
│   │   ├── widgets.md             ← Scaffold, Card, Dialog, BottomNav
│   │   ├── navegacion.md          ← Navigator, go_router, rutas nombradas
│   │   └── estado.md              ← setState, Provider, Riverpod
│   └── python/
│       ├── numpy.md               ← arrays, operaciones vectoriales
│       └── pandas.md              ← DataFrame, read_csv, groupby
├── executor/
│   ├── __init__.py
│   └── ollama_connector.py        ← cliente TinyLlama activo (v0.2)
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
ejemplo matlab graficas     → código fplot
ejemplo matlab matrices     → código det/inv
ejemplo matlab ode          → ecuaciones diferenciales
ejemplo matlab estadistica  → estadística descriptiva
ejemplo flutter login       → pantalla login Dart
ejemplo flutter widgets     → referencia widgets
ejemplo flutter navegacion  → rutas y navegación
ejemplo flutter estado      → manejo de estado
ejemplo python numpy        → arrays NumPy
ejemplo python pandas       → DataFrames Pandas
ejemplos          → lista temas disponibles
ia <consulta>     → IA local TinyLlama (Ollama)
help              → ayuda
exit              → salir
```

---

## Decisiones de diseño tomadas

| Decisión              | Elección                                | Razón                                                |
| --------------------- | --------------------------------------- | ---------------------------------------------------- |
| Parser de expresiones | `sympy.parsing` con transformaciones    | Más robusto que regex; soporta `sin(x)`, `e^x`, etc. |
| Sintaxis de entrada   | Natural (`x^2 + 3x`)                    | Más cómodo para el usuario                           |
| Matrices              | `ast.literal_eval`                      | Seguro, sin `eval()`                                 |
| Modelo IA             | TinyLlama vía Ollama                    | ~637 MB, corre en laptop sin GPU                     |
| Versión IA            | Stub en v0.1, activo en v0.2            | Interfaz definida sin romper el router               |
| Dependencias v0.1     | Solo `sympy`                            | Sin peso extra                                       |
| Dependencias v0.2     | `sympy` + `requests`                    | Mínimas para HTTP a Ollama                           |
| Knowledge v0.3        | 3 categorías: matlab / flutter / python | Cobertura ampliada sin cambiar el router             |

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

| Versión  | Estado             | Contenido                                                   |
| -------- | ------------------ | ----------------------------------------------------------- |
| **v0.1** | ✅ **Completo**    | CLI + motor matemático + base de conocimiento               |
| **v0.2** | ✅ **Completo**    | IA local TinyLlama vía Ollama (health-check + POST real)    |
| **v0.3** | 🔄 **En progreso** | Base de conocimiento expandida (+python, +flutter, +matlab) |
| v0.4     | 🔜 Pendiente       | Ejecución de código MATLAB/Octave                           |
| v0.5     | 🔜 Pendiente       | Generador de código Flutter                                 |

---

## Próximos pasos sugeridos (v0.4)

```bash
# Instalar GNU Octave (compatible con MATLAB)
sudo apt install octave -y

# Plan: módulo executor/octave_runner.py
# - Recibe código MATLAB/Octave como string
# - Lo ejecuta con subprocess + octave --no-gui
# - Devuelve stdout/stderr al CLI
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
