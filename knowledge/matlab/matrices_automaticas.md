# MATLAB — Matrices Automáticas

## Problema

Generar matrices especiales de forma automática sin introducir los valores manualmente.

## Código MATLAB

```matlab
M1 = eye(3)      % Matriz identidad 3×3
M2 = magic(3)    % Cuadrado mágico 3×3
M3 = ones(3)     % Matriz de unos 3×3
M4 = zeros(3)    % Matriz de ceros 3×3
M5 = pascal(4)   % Triángulo de Pascal 4×4
```

## Resultados esperados

```
M1 =              M2 =              M3 =
  1 0 0             8 1 6             1 1 1
  0 1 0             3 5 7             1 1 1
  0 0 1             4 9 2             1 1 1

M4 =              M5 =
  0 0 0              1  1  1  1
  0 0 0              1  2  3  4
  0 0 0              1  3  6 10
                     1  4 10 20
```

## Concepto

MATLAB incluye funciones para generar matrices con propiedades especiales:

| Función     | Descripción                                                |
| ----------- | ---------------------------------------------------------- |
| `eye(n)`    | Identidad n×n                                              |
| `zeros(n)`  | Todos ceros n×n                                            |
| `ones(n)`   | Todos unos n×n                                             |
| `magic(n)`  | Cuadrado mágico (filas, columnas y diagonales suman igual) |
| `pascal(n)` | Coeficientes binomiales del triángulo de Pascal            |
| `rand(n)`   | Aleatorios U(0,1)                                          |
| `randn(n)`  | Aleatorios N(0,1)                                          |
| `diag(v)`   | Diagonal con vector `v`                                    |

## Tags

`matlab` `matrices` `funciones`
