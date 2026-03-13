# MATLAB — Estadística Descriptiva

## Medidas de tendencia central y dispersión

```matlab
datos = [4 7 2 9 5 1 8 3 6 10];

m   = mean(datos);      % Media aritmética
med = median(datos);    % Mediana
s   = std(datos);       % Desviación estándar (muestral, n-1)
v   = var(datos);       % Varianza
r   = range(datos);     % Rango (max - min)

fprintf('Media:    %.2f\n', m);
fprintf('Mediana:  %.2f\n', med);
fprintf('Std:      %.2f\n', s);
fprintf('Varianza: %.2f\n', v);
fprintf('Rango:    %.2f\n', r);
```

## Histograma y ajuste de distribución

```matlab
datos = randn(1, 1000);   % 1000 muestras N(0,1)

figure;
histfit(datos, 30);        % histograma + curva normal ajustada
title('Histograma con ajuste normal');
xlabel('Valor'); ylabel('Frecuencia');
grid on;
```

## Correlación entre variables

```matlab
x = 1:20;
y = 2*x + randn(1, 20)*3;   % y lineal con ruido

R = corrcoef(x, y);
fprintf('Coeficiente de correlación: %.4f\n', R(1,2));

figure;
scatter(x, y, 50, 'b', 'filled');
lsline;   % línea de mínimos cuadrados
title('Correlación x vs y'); grid on;
```

## Percentiles y cuartiles

```matlab
datos = randn(1, 500);
p25 = prctile(datos, 25);    % Cuartil 1
p50 = prctile(datos, 50);    % Mediana
p75 = prctile(datos, 75);    % Cuartil 3
iqr_val = iqr(datos);        % Rango intercuartil

figure;
boxplot(datos);
title('Diagrama de caja'); grid on;
```

## Regresión lineal simple

```matlab
x = (1:50)';
y = 3*x + 10 + randn(50,1)*5;

p = polyfit(x, y, 1);           % p(1)=pendiente, p(2)=intercepto
y_pred = polyval(p, x);

figure;
scatter(x, y, 'b'); hold on;
plot(x, y_pred, 'r-', 'LineWidth', 2);
legend('Datos', 'Regresión'); grid on;
fprintf('y = %.4fx + %.4f\n', p(1), p(2));
```

## Prueba t de Student (una muestra)

```matlab
datos = randn(1, 30) + 0.5;   % Media poblacional hipotética: 0
[h, p, ci] = ttest(datos, 0, 'Alpha', 0.05);
fprintf('Rechazar H0: %d  |  p-valor: %.4f\n', h, p);
fprintf('IC 95%%: [%.4f, %.4f]\n', ci(1), ci(2));
```
