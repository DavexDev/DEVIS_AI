# MATLAB — Números Aleatorios

## Problema

Generar vectores y matrices con números aleatorios.

## Código MATLAB

```matlab
p = rand(1, 10);    % vector fila con 10 números aleatorios U(0,1)
q = ones(10);       % matriz 10×10 de unos

save("pqfile.mat", "p", "q")
```

## Funciones principales

```matlab
% Distribución uniforme [0, 1]
rand(3)          % matriz 3×3
rand(1, 5)       % vector fila de 5 elementos
rand(4, 2)       % matriz 4×2

% Distribución normal N(0,1)
randn(3)
randn(1, 100)

% Enteros aleatorios entre 1 y 10
randi(10, 3, 3)         % matriz 3×3 de enteros en [1,10]
randi([5, 20], 1, 6)    % vector de 6 enteros en [5,20]
```

## Reproducibilidad (semilla)

```matlab
rng(42)          % fijar semilla
r1 = rand(1, 5)  % siempre da el mismo resultado con esta semilla

rng('shuffle')   % semilla basada en el reloj (comportamiento aleatorio real)
```

## Estadísticas de valores generados

```matlab
datos = randn(1, 10000);

fprintf('Media:  %.4f\n', mean(datos))   % debe ser ~0
fprintf('Std:    %.4f\n', std(datos))    % debe ser ~1

figure
histogram(datos, 50)
title('Distribución N(0,1)')
```

## Tags

`matlab` `aleatorios` `rand` `randn` `estadistica`
