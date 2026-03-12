# MATLAB — Matrices: det e inv

## Descripción
Calcula el determinante e inversa de matrices cuadradas.

## Código

```matlab
% Definir una matriz 3x3
A = [1, 2, 3;
     4, 5, 6;
     7, 8, 10];

% Determinante
d = det(A);
fprintf('Determinante: %g\n', d);

% Inversa
if d ~= 0
    A_inv = inv(A);
    disp('Inversa:')
    disp(A_inv)
else
    disp('La matriz es singular, no tiene inversa.')
end

% Verificar: A * inv(A) ≈ I
I_check = A * A_inv;
disp('Verificacion A * inv(A):')
disp(round(I_check))
```

## Funciones relacionadas
- `det(A)`     — determinante
- `inv(A)`     — inversa (usa LU internamente)
- `rank(A)`    — rango de la matriz
- `eig(A)`     — valores y vectores propios
- `rref(A)`    — forma escalonada reducida
- `linsolve`   — resolver sistema Ax = b

## Resultado esperado
```
Determinante: -3
Inversa:
  -0.6667    0.6667   -0.3333
  -0.6667   -3.6667    2.0000
   1.0000    2.0000   -1.0000
```
