# MATLAB — Cardioide Polar

## Problema

Graficar la cardioide r = 5 − 5sin(θ).

## Código MATLAB

```matlab
theta = 0:0.01*pi:2*pi;
r = 5 - 5*sin(theta);

figure
polar(theta, r)
title('Grafica Polar: r = 5 - 5sin(θ)')
```

## Versión moderna (polarplot)

```matlab
figure
polarplot(theta, r)
title('Cardioide: r = 5 - 5sin(\theta)')
```

## Concepto

Las cardioides son curvas polares generadas por funciones trigonométricas.

- La forma general es `r = a ± a·sin(θ)` o `r = a ± a·cos(θ)`
- La curva tiene forma de corazón y pasa por el origen
- `polar()` es la función legada; usar `polarplot()` en versiones modernas de MATLAB

## Tags

`matlab` `graficas` `polar` `cardioide`
