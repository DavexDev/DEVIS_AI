# MATLAB — Gráfica 3D: Resorte

## Problema

Generar una gráfica tridimensional que represente un resorte.

## Código MATLAB

```matlab
x = linspace(0, 10*pi, 1000);
y = cos(x);
z = sin(x);

figure
plot3(x, y, z)

grid
xlabel('angulo')
ylabel('cos(x)')
zlabel('sen(x)')

title('Un resorte')
```

## Concepto

`plot3` permite representar curvas en tres dimensiones.

- `x` representa el avance a lo largo del eje del resorte
- `y = cos(x)` y `z = sin(x)` forman la hélice circular
- `linspace(0, 10*pi, 1000)` da 1000 puntos para una curva suave
- `grid` activa la rejilla en 3D
- La hélice paramétrica `(t, cos(t), sin(t))` traza exactamente la forma de un resorte

## Tags

`matlab` `graficas` `3D` `visualizacion`
