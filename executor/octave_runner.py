"""
executor/octave_runner.py
Ejecutor de código MATLAB/Octave usando GNU Octave — activo en v0.4.

Requisitos previos:
  sudo apt install octave -y
"""

import shutil
import subprocess
import tempfile
import os


class OctaveRunner:
    """
    Ejecuta código MATLAB/Octave a través de GNU Octave instalado localmente.

    Al instanciarse, detecta si Octave está disponible en el sistema.
    Si no lo está, self.available queda en False y run() devuelve
    un mensaje de ayuda en lugar de fallar con excepción.
    """

    # Tiempo máximo de ejecución por bloque de código (segundos)
    TIMEOUT = 15

    def __init__(self):
        # Detectar Octave con shutil.which (mismo enfoque que 'which' en bash)
        self._octave_bin = shutil.which("octave")
        self.available = self._octave_bin is not None

    # ──────────────────────────────────────────────────────────────────────────
    # Métodos públicos
    # ──────────────────────────────────────────────────────────────────────────

    def run(self, code: str) -> str:
        """
        Ejecuta un bloque de código MATLAB/Octave y devuelve su salida.

        El código se escribe en un archivo temporal .m, se ejecuta con
        octave --no-gui y se captura stdout + stderr.

        Args:
            code: Código MATLAB/Octave como string (puede ser multi-línea).

        Returns:
            Salida de la ejecución, o mensaje de error si algo falla.
        """
        if not self.available:
            return self._unavailable_msg()

        if not code.strip():
            return "  No se proporcionó código para ejecutar."

        # Crear archivo temporal .m para pasar el código a Octave
        tmp_file = None
        try:
            # delete=False para poder pasar la ruta a subprocess
            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".m",
                delete=False,
                encoding="utf-8"
            ) as f:
                f.write(code)
                tmp_file = f.name

            # Ejecutar Octave en modo no interactivo
            result = subprocess.run(
                [self._octave_bin, "--no-gui", "--norc", tmp_file],
                capture_output=True,
                text=True,
                timeout=self.TIMEOUT,
            )

            # Combinar stdout y stderr (Octave mezcla ambos canales)
            output = result.stdout.strip()
            errors = result.stderr.strip()

            if output and errors:
                return f"{output}\n\n⚠  Warnings/Errors:\n{errors}"
            elif output:
                return output
            elif errors:
                return f"⚠  {errors}"
            else:
                return "  (sin salida)"

        except subprocess.TimeoutExpired:
            return (
                f"  Error: El código tardó más de {self.TIMEOUT} segundos.\n"
                "  Revisa si hay bucles infinitos o cálculos muy costosos."
            )
        except Exception as exc:  # noqa: BLE001
            return f"  Error inesperado al ejecutar Octave: {exc}"
        finally:
            # Siempre limpiar el archivo temporal
            if tmp_file and os.path.exists(tmp_file):
                os.remove(tmp_file)

    # ──────────────────────────────────────────────────────────────────────────
    # Métodos privados
    # ──────────────────────────────────────────────────────────────────────────

    @staticmethod
    def _unavailable_msg() -> str:
        """Mensaje de ayuda cuando Octave no está instalado."""
        return (
            "\n  GNU Octave no está instalado o no se encuentra en el PATH.\n"
            "\n"
            "  Para instalarlo en Kali/Debian/Ubuntu:\n"
            "    sudo apt install octave -y\n"
            "\n"
            "  Luego reinicia DEVIS y vuelve a intentarlo.\n"
        )
