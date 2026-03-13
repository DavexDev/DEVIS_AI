# MATLAB — Suma de Matrices

## Problema

Sumar dos matrices A y B del mismo tamaño.

## Código MATLAB

```matlab
A = [1 2;
     3 4];

B = [5 6;
     7 8];

C = A + B
```

## Resultado esperado

```
C =
    6    8
   10   12
```

## Concepto

La suma de matrices se realiza **elemento a elemento**. Ambas matrices deben tener las mismas dimensiones.

- `C(i,j) = A(i,j) + B(i,j)` para cada posición
- También se puede restar: `D = A - B`
- Se puede sumar un escalar: `E = A + 10` (suma 10 a todos los elementos)

## Operaciones relacionadas

```matlab
% Resta
D = A - B

% Suma con escalar
E = A + 10

% Multiplicación elemento a elemento (no matricial)
F = A .* B
```

## Tags

`matlab` `matrices` `algebra`
