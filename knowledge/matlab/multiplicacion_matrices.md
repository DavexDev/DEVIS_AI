# MATLAB — Multiplicación de Matrices

## Problema

Multiplicar dos matrices A y B.

## Datos

```
A = [1  2 ]   (3×2)
    [-1  0 ]
    [-3 -1 ]

B = [2  0  1]   (2×3)
    [-5  2  3]
```

## Código MATLAB

```matlab
A = [1 2;
    -1 0;
    -3 -1];

B = [2 0 1;
    -5 2 3];

AB = A * B
BA = B * A
```

## Concepto

Multiplicación de matrices. El número de columnas de A debe ser igual al número de filas de B.

- `A` es 3×2 y `B` es 2×3 → `AB` resulta en 3×3
- `B` es 2×3 y `A` es 3×2 → `BA` resulta en 2×2
- En general: A×B ≠ B×A (no es conmutativa)

## Tags

`matlab` `matrices` `algebra`
