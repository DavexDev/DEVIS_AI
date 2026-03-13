"""
modules/command_router.py
Enrutador central de comandos de DEVIS CLI.
"""

import os
from modules.math_engine import derivada, integral, simplificar, det_matriz, inv_matriz
from executor.ollama_connector import OllamaConnector

# Ruta base de la base de conocimiento
_KNOWLEDGE_DIR = os.path.join(os.path.dirname(__file__), "..", "knowledge")

_ai = OllamaConnector()


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _ask(prompt: str) -> str:
    """Solicita input al usuario con un prefijo formateado."""
    return input(f"  {prompt}: ").strip()


def _load_knowledge(category: str, topic: str) -> str:
    """
    Carga un archivo Markdown de la base de conocimiento.

    Args:
        category: 'matlab' o 'flutter'
        topic:    nombre del archivo sin extensión (ej: 'graficas')

    Returns:
        Contenido del archivo o mensaje de error.
    """
    path = os.path.join(_KNOWLEDGE_DIR, category, f"{topic}.md")
    if not os.path.isfile(path):
        available = _list_knowledge(category)
        return (
            f"  No se encontró '{topic}' en la categoría '{category}'.\n"
            f"  Temas disponibles: {available}"
        )
    with open(path, encoding="utf-8") as f:
        return f.read()


def _list_knowledge(category: str) -> str:
    """Lista los temas disponibles en una categoría."""
    path = os.path.join(_KNOWLEDGE_DIR, category)
    if not os.path.isdir(path):
        return "(ninguno)"
    topics = [
        os.path.splitext(f)[0]
        for f in os.listdir(path)
        if f.endswith(".md")
    ]
    return ", ".join(topics) if topics else "(ninguno)"


# ──────────────────────────────────────────────────────────────────────────────
# Router principal
# ──────────────────────────────────────────────────────────────────────────────

HELP_TEXT = """
  Comandos disponibles:
  ─────────────────────────────────────────────────────
  derivada          Calcula d/dx de una función
  integral          Calcula la integral indefinida
  simplificar       Simplifica una expresión algebraica
  det               Determinante de una matriz cuadrada
  inv               Inversa de una matriz cuadrada
  ejemplo matlab    Muestra ejemplo de código MATLAB
  ejemplo flutter   Muestra ejemplo de código Flutter
  ejemplo python    Muestra ejemplo de código Python
  ia                Consulta a la IA local (TinyLlama/Ollama)
  help              Muestra esta ayuda
  exit              Cerrar DEVIS
  ─────────────────────────────────────────────────────
  Expresiones aceptadas: x^2 + 3x, sin(x), e^x, etc.
  Matrices: [[1,2],[3,4]]
  Temas MATLAB:   graficas, matrices, ode, estadistica
  Temas Flutter:  login, widgets, navegacion, estado
  Temas Python:   numpy, pandas
"""


class CommandRouter:
    """Enruta comandos del usuario al módulo correspondiente."""

    def route(self, user_input: str) -> str | None:
        """
        Procesa el comando del usuario y retorna la respuesta.

        Args:
            user_input: Texto ingresado por el usuario.

        Returns:
            Respuesta como string, o None si el comando es 'exit'.
        """
        cmd = user_input.lower().strip()

        # ── Salida ────────────────────────────────────────────────────────────
        if cmd in ("exit", "quit", "salir"):
            return None

        # ── Ayuda ─────────────────────────────────────────────────────────────
        if cmd in ("help", "ayuda", "?"):
            return HELP_TEXT

        # ── Derivada ──────────────────────────────────────────────────────────
        if cmd.startswith("derivada"):
            expr = self._extract_arg(user_input, "derivada") or _ask("f(x)")
            return self._run("Derivada", derivada, expr)

        # ── Integral ──────────────────────────────────────────────────────────
        if cmd.startswith("integral"):
            expr = self._extract_arg(user_input, "integral") or _ask("f(x)")
            return self._run("Integral", integral, expr)

        # ── Simplificar ───────────────────────────────────────────────────────
        if cmd.startswith("simplif"):
            expr = self._extract_arg(user_input, "simplificar") or _ask("f(x)")
            return self._run("Simplificación", simplificar, expr)

        # ── Determinante ──────────────────────────────────────────────────────
        if cmd.startswith("det"):
            mat = self._extract_arg(user_input, "det") or _ask("Matriz [[a,b],[c,d]]")
            return self._run("Determinante", det_matriz, mat)

        # ── Inversa ───────────────────────────────────────────────────────────
        if cmd.startswith("inv"):
            mat = self._extract_arg(user_input, "inv") or _ask("Matriz [[a,b],[c,d]]")
            return self._run("Inversa", inv_matriz, mat)

        # ── Ejemplo MATLAB ────────────────────────────────────────────────────
        if "matlab" in cmd and "ejemplo" in cmd:
            topic = self._extract_topic(user_input, ("matlab",)) or _ask(
                f"Tema ({_list_knowledge('matlab')})"
            )
            return _load_knowledge("matlab", topic)

        # ── Ejemplo Flutter ───────────────────────────────────────────────────
        if "flutter" in cmd and "ejemplo" in cmd:
            topic = self._extract_topic(user_input, ("flutter",)) or _ask(
                f"Tema ({_list_knowledge('flutter')})"
            )
            return _load_knowledge("flutter", topic)

        # ── Ejemplo Python ────────────────────────────────────────────────────
        if "python" in cmd and "ejemplo" in cmd:
            topic = self._extract_topic(user_input, ("python",)) or _ask(
                f"Tema ({_list_knowledge('python')})"
            )
            return _load_knowledge("python", topic)

        # ── Listar ejemplos ───────────────────────────────────────────────────
        if cmd.startswith("ejemplos"):
            return (
                f"  MATLAB   : {_list_knowledge('matlab')}\n"
                f"  Flutter  : {_list_knowledge('flutter')}\n"
                f"  Python   : {_list_knowledge('python')}"
            )

        # ── IA local ──────────────────────────────────────────────────────────
        if cmd.startswith("ia"):
            prompt = self._extract_arg(user_input, "ia") or _ask("Consulta")
            return _ai.query(prompt)

        # ── Comando no reconocido ─────────────────────────────────────────────
        return (
            f"  Comando no reconocido: '{user_input}'\n"
            "  Escribe 'help' para ver los comandos disponibles."
        )

    # ── Helpers ───────────────────────────────────────────────────────────────

    @staticmethod
    def _run(label: str, fn, arg: str) -> str:
        """Ejecuta una función del motor y formatea el resultado."""
        try:
            result = fn(arg)
            return f"\n  {label}:\n  {result}\n"
        except ValueError as exc:
            return f"\n  Error: {exc}\n"
        except Exception as exc:  # noqa: BLE001
            return f"\n  Error inesperado: {exc}\n"

    @staticmethod
    def _extract_arg(text: str, keyword: str) -> str:
        """Extrae el argumento que sigue a la palabra clave en el mismo comando."""
        lower = text.lower()
        idx = lower.find(keyword)
        if idx == -1:
            return ""
        rest = text[idx + len(keyword):].strip()
        return rest

    @staticmethod
    def _extract_topic(text: str, skip_words: tuple) -> str:
        """
        Extrae el tema de un comando tipo 'ejemplo matlab graficas'.
        Descarta palabras reservadas como 'ejemplo', 'matlab', 'flutter'.
        """
        reserved = {"ejemplo", "ejemplos"} | set(skip_words)
        words = [w for w in text.lower().split() if w not in reserved]
        return words[0] if words else ""
