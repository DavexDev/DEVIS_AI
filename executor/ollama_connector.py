"""
executor/ollama_connector.py
Conector para IA local (TinyLlama vía Ollama) — activo en v0.2.

Requisitos previos:
  1. Instalar Ollama:  curl -fsSL https://ollama.com/install.sh | sh
  2. Descargar modelo: ollama run tinyllama
  3. Asegurarse de que el servidor esté corriendo en localhost:11434
"""

import json
import requests


class OllamaConnector:
    """
    Cliente HTTP para el servidor Ollama local.

    Al instanciarse, realiza un health-check automático para determinar
    si el servidor está disponible. Si no lo está, self.available queda
    en False y query() devuelve un mensaje de ayuda en lugar de fallar.
    """

    # Modelo a utilizar — TinyLlama (~637 MB, sin GPU requerida)
    MODEL = "tinyllama"

    # Endpoints del servidor Ollama
    BASE_URL   = "http://localhost:11434/api/generate"  # generación de texto
    HEALTH_URL = "http://localhost:11434/api/tags"       # lista de modelos (health-check)

    # Tiempo máximo de espera por respuesta del modelo (segundos)
    TIMEOUT = 60

    def __init__(self):
        # Intentamos conectarnos al servidor; si falla, desactivamos la IA
        self.available = self._health_check()

    # ──────────────────────────────────────────────────────────────────────────
    # Métodos públicos
    # ──────────────────────────────────────────────────────────────────────────

    def query(self, prompt: str) -> str:
        """
        Envía un prompt al modelo de lenguaje local y devuelve su respuesta.

        Si el servidor no está disponible, devuelve instrucciones de instalación
        en lugar de lanzar una excepción.

        Args:
            prompt: Texto de entrada para el modelo.

        Returns:
            Respuesta generada por el modelo, o mensaje de error/ayuda.
        """
        # Si el health-check falló al iniciar, informamos al usuario
        if not self.available:
            return self._unavailable_msg()

        try:
            # Construimos el payload para la API de Ollama
            payload = {
                "model": self.MODEL,
                "prompt": prompt,
                "stream": False,   # recibir respuesta completa, no en chunks
            }

            # POST al endpoint de generación
            response = requests.post(
                self.BASE_URL,
                json=payload,
                timeout=self.TIMEOUT,
            )
            response.raise_for_status()   # lanza HTTPError si status >= 400

            # La API devuelve JSON con el campo "response"
            data = json.loads(response.text)
            return data.get("response", "(sin respuesta del modelo)")

        except requests.exceptions.ConnectionError:
            # El servidor se cayó después del health-check inicial
            self.available = False
            return (
                "  [IA] El servidor Ollama dejó de responder.\n"
                "  Ejecuta: ollama serve"
            )
        except requests.exceptions.Timeout:
            return (
                f"  [IA] El modelo tardó más de {self.TIMEOUT}s en responder.\n"
                "  Intenta con una consulta más corta."
            )
        except requests.exceptions.HTTPError as exc:
            return f"  [IA] Error HTTP {exc.response.status_code}: {exc}"
        except (json.JSONDecodeError, KeyError) as exc:
            return f"  [IA] Respuesta inesperada del servidor: {exc}"

    # ──────────────────────────────────────────────────────────────────────────
    # Métodos privados
    # ──────────────────────────────────────────────────────────────────────────

    def _health_check(self) -> bool:
        """
        Comprueba si el servidor Ollama está activo y el modelo está disponible.

        Hace GET a /api/tags (lista de modelos descargados) con un timeout
        corto para no bloquear el arranque de la CLI.

        Returns:
            True  — servidor activo y modelo 'tinyllama' presente.
            False — servidor inaccesible o modelo no descargado.
        """
        try:
            resp = requests.get(self.HEALTH_URL, timeout=3)
            resp.raise_for_status()

            # Verificar que el modelo esté descargado localmente
            data = resp.json()
            modelos = [m.get("name", "") for m in data.get("models", [])]

            # El nombre puede venir como "tinyllama" o "tinyllama:latest"
            modelo_disponible = any(self.MODEL in nombre for nombre in modelos)

            if not modelo_disponible:
                print(
                    f"  [IA] Ollama activo, pero el modelo '{self.MODEL}' no está descargado.\n"
                    f"  Ejecuta: ollama run {self.MODEL}"
                )
                return False

            print(f"  [IA] Modelo '{self.MODEL}' listo.")
            return True

        except requests.exceptions.ConnectionError:
            # Ollama no está corriendo — silencioso en el arranque
            return False
        except Exception:
            # Cualquier otro error: no bloquear la CLI
            return False

    @staticmethod
    def _unavailable_msg() -> str:
        """Mensaje de ayuda cuando Ollama no está disponible."""
        return (
            "  [IA no disponible]\n"
            "  Para activarla:\n"
            "    1. Instalar Ollama:  curl -fsSL https://ollama.com/install.sh | sh\n"
            "    2. Iniciar servidor: ollama serve\n"
            "    3. Descargar modelo: ollama run tinyllama\n"
            "    4. Volver a ejecutar DEVIS."
        )
