# MATLAB — Vectores con Incremento

## Problema

Crear vectores usando la notación de rango con paso personalizado.

## Código MATLAB

```matlab
v = 2:2:20
```

## Resultado esperado

```
v =
    2    4    6    8   10   12   14   16   18   20
```

## Concepto

La notación `inicio:paso:fin` genera un vector de valores equiespaciados.

```matlab
v = 2:2:20     % de 2 a 20 con paso 2  → [2 4 6 ... 20]
w = 0:0.5:3    % de 0 a 3  con paso 0.5 → [0 0.5 1 ... 3]
z = 10:-1:1   % de 10 a 1 con paso -1  → [10 9 8 ... 1]
```

## Usos comunes

```matlab
% Índices de iteración
for i = 1:2:10
    disp(i)   % 1 3 5 7 9
end

% Eje X para gráficas
x = 0:2:20;
y = x.^2;
plot(x, y, 'o-')
grid on

% Combinado con reshape
M = reshape(2:2:24, 3, 4)
```

## linspace vs rango

|            | `a:paso:b`           | `linspace(a,b,n)`       |
| ---------- | -------------------- | ----------------------- |
| Controlas  | El **paso**          | El **número de puntos** |
| Uso típico | Índices, iteraciones | Ejes de gráficas        |

## Tags

`matlab` `vectores` `rango` `incremento`
