# MATLAB — Subplots

## Problema

Mostrar múltiples gráficas en una misma figura usando `subplot`.

## Código MATLAB

```matlab
x = linspace(-2*pi, 2*pi, 100);

figure

subplot(2, 2, 1)
plot(x, sin(x), 'r')
title('sin(x)')
grid on

subplot(2, 2, 2)
plot(x, cos(x), 'b')
title('cos(x)')
grid on

subplot(2, 2, 3)
plot(x, tan(x), 'g')
title('tan(x)')
grid on

subplot(2, 2, 4)
plot(x, x.^2, 'k')
title('x^2')
grid on
```

## Concepto

`subplot(m, n, p)` divide la figura en una cuadrícula de `m` filas × `n` columnas y activa el panel número `p` (numerados de izquierda a derecha, arriba a abajo).

```
subplot(2,2,1) | subplot(2,2,2)
───────────────────────────────
subplot(2,2,3) | subplot(2,2,4)
```

- Cada `subplot` es independiente: tiene sus propios ejes, título y etiquetas
- `x.^2` usa el operador elemento a elemento (`.^`) para elevar al cuadrado cada punto

## Layouts comunes

```matlab
subplot(1, 2, p)   % 2 paneles lado a lado
subplot(3, 1, p)   % 3 paneles apilados verticalmente
subplot(2, 3, p)   % 6 paneles en 2 filas
```

## Tags

`matlab` `graficas` `subplot` `visualizacion`
