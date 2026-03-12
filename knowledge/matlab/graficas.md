# MATLAB — Gráficas con fplot

## Descripción
Genera gráficas de funciones simbólicas usando `fplot` en MATLAB/Octave.

## Código

```matlab
% Grafica de una función simbólica
syms x

f = x^2 + 3*x;

figure;
fplot(f, [-10, 10])
grid on
title('Gráfica de f(x) = x^2 + 3x')
xlabel('x')
ylabel('f(x)')
legend('x^2 + 3x')
```

## Variantes

```matlab
% Múltiples funciones en la misma figura
syms x
f1 = sin(x);
f2 = cos(x);

fplot(f1, [-2*pi, 2*pi], 'b-', 'LineWidth', 1.5)
hold on
fplot(f2, [-2*pi, 2*pi], 'r--', 'LineWidth', 1.5)
grid on
legend('sin(x)', 'cos(x)')
title('Funciones trigonométricas')
```

## Resultado esperado
Se genera una ventana con la gráfica de la función en el rango especificado,
con cuadrícula, título y etiquetas de ejes.

## Funciones relacionadas
- `plot(x, y)`  — para vectores numéricos
- `ezplot(f)`   — alternativa legacy (MATLAB antiguo)
- `fplot3`      — para curvas en 3D
- `surf`, `mesh` — superficies 3D
