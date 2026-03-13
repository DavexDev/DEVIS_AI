# MATLAB — Reshape de Matrices

## Problema

Crear una matriz reorganizando un vector usando `reshape`.

## Código MATLAB

```matlab
M = reshape(2:2:24, 3, 4)
```

## Resultado esperado

```
M =
    2    8   14   20
    4   10   16   22
    6   12   18   24
```

## Concepto

`reshape` reorganiza los elementos de un vector o matriz en nuevas dimensiones.

- `2:2:24` genera el vector `[2 4 6 8 10 12 14 16 18 20 22 24]` (12 elementos)
- `reshape(v, 3, 4)` lo distribuye en 3 filas × 4 columnas
- MATLAB llena **por columnas** (column-major order)
- El número total de elementos debe coincidir: `3×4 = 12`

## Uso general

```matlab
% Cualquier reorganización válida
B = reshape(1:12, 2, 6)   % 2×6
C = reshape(1:12, 4, 3)   % 4×3
D = reshape(1:12, 12, 1)  % vector columna
```

## Tags

`matlab` `matrices` `reshape`
