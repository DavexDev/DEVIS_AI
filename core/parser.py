"""
core/parser.py
Convierte sintaxis matemática natural (x^2 + 3x) a expresiones SymPy.
"""

from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

TRANSFORMATIONS = standard_transformations + (
    implicit_multiplication_application,
    convert_xor,
)

# Constantes matemáticas reconocidas como símbolos SymPy
LOCAL_DICT = {
    "e": None,  # se resuelve automáticamente via SymPy
    "pi": None,
}


def parse_natural(expr_str: str):
    """
    Convierte una expresión matemática en texto al objeto SymPy equivalente.

    Ejemplos:
        "x^2 + 3x"  -> x**2 + 3*x
        "sin(x)e^x" -> sin(x)*exp(x)
        "2x + 1"    -> 2*x + 1

    Args:
        expr_str: Cadena con la expresión en sintaxis natural.

    Returns:
        Expresión SymPy.

    Raises:
        ValueError: Si la expresión no puede ser parseada.
    """
    expr_str = expr_str.strip()
    if not expr_str:
        raise ValueError("La expresión está vacía.")

    try:
        return parse_expr(expr_str, transformations=TRANSFORMATIONS)
    except Exception as exc:
        raise ValueError(
            f"No se pudo interpretar la expresión '{expr_str}'.\n"
            f"  Asegúrate de usar: x^2 + 3x, sin(x), e^x, etc.\n"
            f"  Error interno: {exc}"
        ) from exc
