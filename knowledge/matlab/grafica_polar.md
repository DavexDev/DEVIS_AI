# MATLAB — Gráfica Polar

## Problema

Graficar la función polar r = 5cos(4θ).

## Código MATLAB

```matlab
theta = 0:0.01*pi:2*pi;
r = 5*cos(4*theta);

figure
polarplot(theta, r)
title('Grafica Polar: r = 5cos(4θ)')
```

## Variantes

```matlab
% Rosa polar de 12 pétalos
r = 4*cos(6*theta);
figure
polarplot(theta, r)
title('r = 4cos(6\theta)')
```

## Concepto

Uso de `polarplot` para representar funciones en coordenadas polares.

- `theta` es el ángulo en radianes (de 0 a 2π)
- `r` es el radio en función de `theta`
- `r = A·cos(n·θ)` genera una rosa polar de `2n` pétalos (n par) o `n` pétalos (n impar)
- `polarplot` es la función moderna (versiones ≥ R2016a); `polar` es la versión legada

## Tags

`matlab` `graficas` `polar` `trigonometria`
