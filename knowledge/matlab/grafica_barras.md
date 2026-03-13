# MATLAB — Gráfica de Barras

## Problema

Visualizar datos en un diagrama de barras.

## Código MATLAB

```matlab
x = [1 2 4 5 8];

figure
bar(x)
title('Grafica de barras')
```

## Variantes

```matlab
% Barras horizontales
barh(x)

% Barras agrupadas (varias series)
datos = [3 5; 4 2; 6 8; 5 4];
figure
bar(datos)
legend('Serie 1', 'Serie 2')
title('Barras agrupadas')

% Barras apiladas
bar(datos, 'stacked')

% Con etiquetas en el eje X
categorias = {'Lun', 'Mar', 'Mie', 'Jue', 'Vie'};
valores = [4 7 3 8 5];
bar(valores)
xticklabels(categorias)
title('Ventas por día')
ylabel('Unidades')

% Cambiar color
bar(x, 'FaceColor', [0.2 0.6 0.8])

% En subplot
figure
subplot(2, 2, 1)
bar(x)
title('Grafica de barras')
```

## Tags

`matlab` `graficas` `barras` `visualizacion`
