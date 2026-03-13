# MATLAB — Gráficas Trigonométricas

## Problema

Graficar las funciones seno y coseno en el intervalo [-2π, 2π].

## Código MATLAB

```matlab
x = linspace(-2*pi, 2*pi, 100);

y1 = sin(x);
y2 = cos(x);

figure
plot(x, y1, 'r')
hold on
plot(x, y2, 'b')

title('Seno y Coseno')
xlabel('x')
ylabel('Valor')

legend('sin(x)', 'cos(x)')
grid on
```

## Concepto

Uso de `plot` para graficar múltiples funciones en la misma figura.

- `linspace(a, b, n)` genera `n` puntos equiespaciados entre `a` y `b`
- `hold on` permite superponer varias gráficas sin borrar la anterior
- El string de color (`'r'`, `'b'`) define el color de la línea

## Tags

`matlab` `graficas` `trigonometria`
