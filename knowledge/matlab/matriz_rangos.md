# MATLAB — Matrices desde Rangos

## Problema

Construir matrices directamente usando la notación de rangos por filas.

## Código MATLAB

```matlab
A = [2:2:10; 12:2:20]
```

## Resultado esperado

```
A =
    2    4    6    8   10
   12   14   16   18   20
```

## Concepto

Se puede construir una matriz combinando vectores de rango como filas, separándolos con `;`.

- `2:2:10` → `[2 4 6 8 10]` (5 elementos)
- `12:2:20` → `[12 14 16 18 20]` (5 elementos)
- Ambas filas deben tener el mismo número de elementos

## Combinar con otros vectores

```matlab
x = [1 2 4 5 8];
y = [x; 1:5]     % combina el vector x con el vector 1:5 como filas
```

## Construcción de matrices por bloques

```matlab
fila1 = 1:4;
fila2 = 5:8;
fila3 = 9:12;

M = [fila1; fila2; fila3]   % Matriz 3×4
```

## Tags

`matlab` `matrices` `rangos` `vectores`
