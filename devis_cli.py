#!/usr/bin/env python3
"""
devis_cli.py
Punto de entrada principal de DEVIS — Development Intelligent System.
"""

import sys
import os

# Asegura que el directorio raíz del proyecto esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.command_router import CommandRouter  # noqa: E402

BANNER = r"""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║    ██████╗ ███████╗██╗   ██╗██╗███████╗             ║
║    ██╔══██╗██╔════╝██║   ██║██║██╔════╝             ║
║    ██║  ██║█████╗  ██║   ██║██║███████╗             ║
║    ██║  ██║██╔══╝  ╚██╗ ██╔╝██║╚════██║             ║
║    ██████╔╝███████╗ ╚████╔╝ ██║███████║             ║
║    ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝             ║
║                                                      ║
║    Development Intelligent System  v0.2              ║
║    Matemáticas · MATLAB · Flutter                    ║
╚══════════════════════════════════════════════════════╝
  Escribe 'help' para ver los comandos disponibles.
  Escribe 'exit' para salir.
"""


def main() -> None:
    router = CommandRouter()
    print(BANNER)

    while True:
        try:
            user_input = input("DEVIS> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nDEVIS shutting down...")
            break

        if not user_input:
            continue

        response = router.route(user_input)

        if response is None:
            # El router señala salida explícita (comando 'exit')
            print("DEVIS shutting down...")
            break

        print(response)


if __name__ == "__main__":
    main()
