# MATLAB — Lectura de Archivos CSV

## Problema

Leer datos desde un archivo CSV y trabajar con ellos como matriz o tabla.

## Código MATLAB

```matlab
% Leer como matriz numérica
datos = readmatrix('vuelos.csv');

disp('Contenido del archivo CSV:')
disp(datos)

% Leer como tabla (con encabezados)
T = readtable('vuelos.csv');
disp(T)

% Seleccionar columnas específicas
T(1:2, 1:3)         % filas 1-2, columnas 1-3
```

## Selección de columnas por índice

```matlab
M = readmatrix('pesos.csv');

M(:, 1:2)    % todas las filas, columnas 1 y 2
M(:, 5:6)    % todas las filas, columnas 5 y 6
```

## Diferencia entre readmatrix y readtable

| Función      | Retorna               | Uso recomendado                |
| ------------ | --------------------- | ------------------------------ |
| `readmatrix` | Array numérico        | Datos totalmente numéricos     |
| `readtable`  | Tabla con encabezados | Datos mixtos (texto + números) |
| `readcell`   | Cell array            | Datos heterogéneos             |

## Opciones avanzadas

```matlab
% Especificar delimitador
M = readmatrix('datos.csv', 'Delimiter', ';');

% Saltar filas de encabezado
M = readmatrix('datos.csv', 'NumHeaderLines', 2);

% Especificar rango de celdas (como Excel)
M = readmatrix('datos.xlsx', 'Range', 'B2:E10');
```

## Tags

`matlab` `csv` `lectura` `datos` `readmatrix` `readtable`
