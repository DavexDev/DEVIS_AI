# MATLAB — Guardar y Cargar Variables (.mat)

## Problema

Guardar variables del workspace en un archivo `.mat` para reutilizarlas después.

## Código MATLAB

```matlab
% Crear variables
theta = 2;
g = 1/theta * 0.5/2;
h = [1 2 3 4 5 6];

% Guardar variables específicas
save("PrimerEjercicio.mat", "g", "h")

% Guardar con números aleatorios
p = rand(1, 10);
q = ones(10);
save("pqfile.mat", "p", "q")
```

## Cargar variables guardadas

```matlab
% Cargar todo el archivo
load("PrimerEjercicio.mat")

% Cargar solo una variable específica
load("PrimerEjercicio.mat", "g")

% Verificar contenido del archivo
whos('-file', 'PrimerEjercicio.mat')
```

## Opciones de save

```matlab
% Guardar todo el workspace
save("workspace_completo.mat")

% Guardar en formato ASCII (texto plano, solo matrices 2D)
save("datos.txt", "h", "-ascii")

% Guardar en versión específica de MATLAB
save("datos.mat", "h", "-v7.3")   % para archivos grandes (>2 GB)
```

## Concepto

- Los archivos `.mat` son el formato nativo de MATLAB para persistir datos
- Preservan el tipo, tamaño y nombre de cada variable
- Son independientes del sistema operativo
- `rand(1,10)` genera 10 números aleatorios en U(0,1)
- `ones(10)` genera una matriz 10×10 de unos

## Tags

`matlab` `archivos` `save` `load` `workspace`
