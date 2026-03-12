"""
executor/ollama_connector.py
Conector para IA local (TinyLlama vía Ollama) — stub para v0.1.
Se activará en v0.2 con: ollama run tinyllama
"""


class OllamaConnector:
    """
    Cliente para el servidor Ollama local.

    v0.1: devuelve mensaje informativo.
    v0.2: realiza POST a http://localhost:11434/api/generate
    """

    MODEL = "tinyllama"
    BASE_URL = "http://localhost:11434/api/generate"

    def __init__(self):
        self.available = False  # se actualizará en v0.2 con health-check

    def query(self, prompt: str) -> str:
        """
        Envía un prompt al modelo de lenguaje local.

        Args:
            prompt: Texto de entrada para el modelo.

        Returns:
            Respuesta del modelo (str).
        """
        if not self.available:
            return (
                "[IA local no disponible en v0.1]\n"
                "Para activarla en v0.2:\n"
                "  1. Instalar Ollama: curl -fsSL https://ollama.com/install.sh | sh\n"
                f"  2. Descargar modelo:  ollama run {self.MODEL}\n"
                "  3. Actualizar executor/ollama_connector.py"
            )

        # ── v0.2 implementation placeholder ──────────────────────────────────
        # import requests, json
        # payload = {"model": self.MODEL, "prompt": prompt, "stream": False}
        # resp = requests.post(self.BASE_URL, json=payload, timeout=60)
        # resp.raise_for_status()
        # return json.loads(resp.text)["response"]
        # ─────────────────────────────────────────────────────────────────────
