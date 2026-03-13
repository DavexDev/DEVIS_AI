# MATLAB — Transpuesta de Matrices

## Problema

Realizar operaciones combinando matrices y su transpuesta.

## Código MATLAB

```matlab
A = [1 2 3;
     4 5 6];

B = [1 2;
     3 4;
     5 6];

C = A - 2*(B')
```

## Resultado esperado

```
C =
   -1   -4   -7
    2   -3   -8
```

## Concepto

El operador `'` calcula la **transpuesta** de una matriz (intercambia filas y columnas).

- `B` es 3×2 → `B'` es 2×3
- `2*(B')` escala cada elemento por 2
- `A - 2*(B')` realiza la resta elemento a elemento (ambas son 2×3)

## Transpuesta vs. transpuesta conjugada

```matlab
A = [1+2i, 3+4i];

A.'   % transpuesta simple (sin conjugar)
A'    % transpuesta conjugada (hermitiana) — conjuga números complejos
```

## Tags

`matlab` `matrices` `transpuesta` `algebra`
