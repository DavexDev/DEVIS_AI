# DEVIS AI — Development Intelligent System

> Asistente de inteligencia artificial especializado en desarrollo de software
> y resolución de problemas matemáticos.

```
██████╗ ███████╗██╗   ██╗██╗███████╗
██╔══██╗██╔════╝██║   ██║██║██╔════╝
██║  ██║█████╗  ██║   ██║██║███████╗
██║  ██║██╔══╝  ╚██╗ ██╔╝██║╚════██║
██████╔╝███████╗ ╚████╔╝ ██║███████║
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝
```

## Áreas principales

- **Matemáticas** — derivadas, integrales, simplificación, matrices
- **MATLAB** — ejemplos de fplot, det, inv y más
- **Flutter/Dart** — widgets, pantallas y lógica básica
- **IA local** — TinyLlama vía Ollama _(v0.2)_

---

## Estructura del proyecto

```
DEVIS_AI/
├── core/
│   └── parser.py              # Parser de expresiones matemáticas naturales
├── modules/
│   ├── math_engine.py         # Motor: derivada, integral, simplificar, det, inv
│   └── command_router.py      # Enrutador de comandos CLI
├── knowledge/
│   ├── matlab/
│   │   ├── graficas.md        # Ejemplos con fplot
│   │   └── matrices.md        # Ejemplos con det, inv
│   └── flutter/
│       ├── login.md           # Pantalla de login completa
│       └── widgets.md         # Widgets comunes (Scaffold, Card, etc.)
├── executor/
│   └── ollama_connector.py    # Conector TinyLlama (stub v0.1 → activo v0.2)
├── devis_cli.py               # Punto de entrada principal
├── requirements.txt
└── README.md
```

---

## Requisitos

- Python 3.9 o superior
- pip

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/DavexDev/DEVIS_AI.git
cd DEVIS_AI

# 2. (Opcional) Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## Uso

```bash
python3 devis_cli.py
```

Verás el banner de DEVIS y el prompt `DEVIS>`.

---

## Comandos disponibles

| Comando                   | Descripción                                       |
|---------------------------|---------------------------------------------------|
| `derivada`                | Calcula d/dx de una función                       |
| `integral`                | Calcula la integral indefinida                    |
| `simplificar`             | Simplifica una expresión algebraica               |
| `det`                     | Determinante de una matriz cuadrada               |
| `inv`                     | Inversa de una matriz cuadrada                    |
| `ejemplo matlab graficas` | Muestra ejemplo de código MATLAB (fplot)          |
| `ejemplo matlab matrices` | Muestra ejemplo de matrices en MATLAB             |
| `ejemplo flutter login`   | Muestra pantalla de login en Flutter/Dart         |
| `ejemplo flutter widgets` | Muestra referencia de widgets comunes             |
| `ejemplos`                | Lista todos los temas disponibles                 |
| `ia <consulta>`           | Consulta a IA local (activo en v0.2)              |
| `help`                    | Muestra la ayuda                                  |
| `exit`                    | Cierra DEVIS                                      |

### Formato de expresiones

Las expresiones matemáticas se ingresan en sintaxis natural:

```
x^2 + 3x          →  x² + 3x
sin(x)cos(x)      →  sin(x)·cos(x)
e^x               →  eˣ
(x^2 - 1)/(x-1)  →  (x²-1)/(x-1)
```

### Matrices

```
[[1, 2], [3, 4]]   →  matriz 2×2
[[1,0,0],[0,1,0],[0,0,1]]  →  identidad 3×3
```

---

## Ejemplos de sesión

```
DEVIS> derivada
  f(x): x^3 + 2x

  Derivada:
     2
  3·x  + 2

DEVIS> integral x^2
  Integral:
   3
  x
  ── + C
  3

DEVIS> simplificar (x^2 - 1)/(x - 1)

  Simplificación:
  x + 1

DEVIS> det [[1,2],[3,4]]

  Determinante:
  -2

DEVIS> ejemplo flutter login
  # Flutter — Pantalla de Login
  ...

DEVIS> exit
DEVIS shutting down...
```

---

## Hoja de ruta

| Versión | Estado | Contenido                                    |
|---------|--------|----------------------------------------------|
| v0.1    | ✅ Listo | CLI + motor matemático + base de conocimiento |
| v0.2    | 🔜     | IA local con TinyLlama vía Ollama             |
| v0.3    | 🔜     | Base de conocimiento expandida                |
| v0.4    | 🔜     | Ejecución de código MATLAB/Octave             |
| v0.5    | 🔜     | Generador de proyectos Flutter                |

---

## Activar IA local (v0.2)

```bash
# Instalar Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Descargar TinyLlama (~637 MB)
ollama run tinyllama
```

Luego actualiza `executor/ollama_connector.py` y cambia `self.available = True`.

---

## Contribuir

1. Fork del repositorio
2. Crea una rama: `git checkout -b feature/mi-feature`
3. Commit: `git commit -m "feat: descripción"`
4. Push: `git push origin feature/mi-feature`
5. Abre un Pull Request

---

## Licencia

MIT — ver [LICENSE](LICENSE)
