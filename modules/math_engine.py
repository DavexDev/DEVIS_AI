"""
modules/math_engine.py
Motor matemático de DEVIS — derivadas, integrales, simplificación, det e inv.
"""

import ast

from sympy import (
    symbols,
    diff,
    integrate,
    simplify,
    Matrix,
    Symbol,
    latex,
    pretty,
)
from sympy import E, pi, oo  # noqa: F401 — disponibles para el parser

from core.parser import parse_natural

x: Symbol = symbols("x")


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _fmt(result) -> str:
    """Devuelve la representación en texto legible de un resultado SymPy."""
    return pretty(result, use_unicode=True)


def _parse(expr_str: str):
    """Wrapper local para parse_natural con símbolo x ya definido."""
    return parse_natural(expr_str)


# ──────────────────────────────────────────────────────────────────────────────
# Operaciones
# ──────────────────────────────────────────────────────────────────────────────

def derivada(expr_str: str) -> str:
    """
    Calcula la derivada de f(x) respecto a x.

    Ejemplo:
        derivada("x^3 + 2x") -> "3*x**2 + 2"
    """
    expr = _parse(expr_str)
    resultado = diff(expr, x)
    return _fmt(resultado)


def integral(expr_str: str) -> str:
    """
    Calcula la integral indefinida de f(x) respecto a x.

    Ejemplo:
        integral("x^2") -> "x**3/3 + C"
    """
    expr = _parse(expr_str)
    resultado = integrate(expr, x)
    return _fmt(resultado) + " + C"


def simplificar(expr_str: str) -> str:
    """
    Simplifica una expresión algebraica.

    Ejemplo:
        simplificar("(x^2 - 1)/(x - 1)") -> "x + 1"
    """
    expr = _parse(expr_str)
    resultado = simplify(expr)
    return _fmt(resultado)


def det_matriz(filas_str: str) -> str:
    """
    Calcula el determinante de una matriz cuadrada.

    Args:
        filas_str: Representación de la matriz como lista de listas.
                   Ejemplo: "[[1, 2], [3, 4]]"

    Returns:
        Determinante como string.
    """
    try:
        filas = ast.literal_eval(filas_str.strip())
    except (ValueError, SyntaxError) as exc:
        raise ValueError(
            f"Formato inválido. Usa: [[1,2],[3,4]]\nError: {exc}"
        ) from exc

    m = Matrix(filas)
    if m.rows != m.cols:
        raise ValueError(
            f"La matriz debe ser cuadrada. Recibida: {m.rows}x{m.cols}"
        )

    resultado = m.det()
    return _fmt(resultado)


def inv_matriz(filas_str: str) -> str:
    """
    Calcula la inversa de una matriz cuadrada.

    Args:
        filas_str: Representación de la matriz como lista de listas.
                   Ejemplo: "[[1, 2], [3, 4]]"

    Returns:
        Matriz inversa como string, o error si es singular.
    """
    try:
        filas = ast.literal_eval(filas_str.strip())
    except (ValueError, SyntaxError) as exc:
        raise ValueError(
            f"Formato inválido. Usa: [[1,2],[3,4]]\nError: {exc}"
        ) from exc

    m = Matrix(filas)
    if m.rows != m.cols:
        raise ValueError(
            f"La matriz debe ser cuadrada. Recibida: {m.rows}x{m.cols}"
        )

    if m.det() == 0:
        raise ValueError("La matriz es singular (det = 0). No tiene inversa.")

    resultado = m.inv()
    return _fmt(resultado)
