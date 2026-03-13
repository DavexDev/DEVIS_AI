# MATLAB — Superficie 3D

## Problema

Graficar una superficie tridimensional z = sin(√(x² + y²)).

## Código MATLAB

```matlab
[X, Y] = meshgrid(-5:0.5:5);

Z = sin(sqrt(X.^2 + Y.^2));

figure
surf(X, Y, Z)

title('Superficie 3D')
xlabel('X')
ylabel('Y')
zlabel('Z')
```

## Concepto

- `meshgrid` crea una cuadrícula 2D de coordenadas X e Y
- Las operaciones sobre `X` e `Y` se aplican **elemento a elemento** (usar `.^`, `.*`)
- `surf` dibuja la superficie coloreada según la altura Z
- `0.5` es el paso de la cuadrícula: mayor paso = más rápido pero menos detalle

## Variantes de visualización

```matlab
% Malla sin relleno
mesh(X, Y, Z)

% Superficie con transparencia
surf(X, Y, Z, 'FaceAlpha', 0.5)

% Mapa de colores
colormap hot
surf(X, Y, Z)
colorbar

% Curvas de nivel 2D
contour(X, Y, Z, 20)

% Curvas de nivel sobre la superficie
surfc(X, Y, Z)
```

## Tags

`matlab` `graficas` `3D` `superficie` `meshgrid`
