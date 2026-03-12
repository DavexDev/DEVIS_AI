# DEVIS AI — Contexto del Proyecto

> Archivo de contexto generado el 11 de marzo de 2026.
> Úsalo para retomar la conversación o el desarrollo en cualquier momento.

---

## Identidad del asistente

**DEVIS** (Development Intelligent System) — asistente CLI especializado en:
- Matemáticas computacionales (derivadas, integrales, matrices, simplificación)
- MATLAB — ejemplos de fplot, det, inv
- Flutter/Dart — widgets, pantallas, lógica
- IA local con TinyLlama vía Ollama (planeado para v0.2)

---

## Repositorio

```
https://github.com/DavexDev/DEVIS_AI.git
rama: main
commit inicial: 98b2341
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
│   │   └── matrices.md            ← ejemplo det, inv, rank
│   └── flutter/
│       ├── login.md               ← pantalla login completa (Dart)
│       └── widgets.md             ← Scaffold, Card, Dialog, BottomNav
├── executor/
│   ├── __init__.py
│   └── ollama_connector.py        ← stub TinyLlama (activo en v0.2)
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
- En v0.1: retorna mensaje informativo con instrucciones de instalación
- En v0.2: hará POST a `http://localhost:11434/api/generate` con modelo `tinyllama`
- Cambiar `self.available = True` para activar

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
ejemplo matlab graficas   → código fplot
ejemplo matlab matrices   → código det/inv
ejemplo flutter login     → pantalla login Dart
ejemplo flutter widgets   → referencia widgets
ejemplos          → lista temas disponibles
ia <consulta>     → IA local (v0.2)
help              → ayuda
exit              → salir
```

---

## Decisiones de diseño tomadas

| Decisión | Elección | Razón |
|---|---|---|
| Parser de expresiones | `sympy.parsing` con transformaciones | Más robusto que regex; soporta `sin(x)`, `e^x`, etc. |
| Sintaxis de entrada | Natural (`x^2 + 3x`) | Más cómodo para el usuario |
| Matrices | `ast.literal_eval` | Seguro, sin `eval()` |
| Modelo IA | TinyLlama vía Ollama | ~637 MB, corre en laptop sin GPU |
| Versión IA | Stub en v0.1, activo en v0.2 | Interfaz definida sin romper el router |
| Dependencias v0.1 | Solo `sympy` | Sin peso extra |

---

## Entorno de desarrollo

- **OS**: Kali Linux
- **Python**: 3.13.11 (`/usr/bin/python3`)
- **SymPy**: 1.14.0 (instalado con `--break-system-packages`)
- **Ejecutar**: `python3 devis_cli.py` desde `/home/mrrobot/DEVIS_AI/`

---

## Hoja de ruta

| Versión | Estado | Contenido |
|---|---|---|
| **v0.1** | ✅ **Completo** | CLI + motor matemático + base de conocimiento |
| v0.2 | 🔜 Pendiente | IA local TinyLlama vía Ollama |
| v0.3 | 🔜 Pendiente | Base de conocimiento expandida |
| v0.4 | 🔜 Pendiente | Ejecución de código MATLAB/Octave |
| v0.5 | 🔜 Pendiente | Generador de código Flutter |

---

## Próximos pasos sugeridos (v0.2)

```bash
# 1. Instalar Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. Descargar TinyLlama
ollama run tinyllama

# 3. En executor/ollama_connector.py:
#    Cambiar self.available = False → True
#    Descomentar el bloque de requests
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
