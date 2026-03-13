# MATLAB — Formatos Numéricos

## Problema

Controlar la forma en que MATLAB muestra los números en consola.

## Código MATLAB

```matlab
format short      % 4 decimales (por defecto)
pi

format long       % 15 decimales
pi

format short e    % notación científica corta
pi

format long e     % notación científica larga
pi
```

## Resultado esperado

```
format short  →  3.1416
format long   →  3.141592653589793
format short e→  3.1416e+00
format long e →  3.141592653589793e+00
```

## Formatos disponibles

| Formato          | Descripción                 | Ejemplo                |
| ---------------- | --------------------------- | ---------------------- |
| `format short`   | 4 decimales (default)       | `3.1416`               |
| `format long`    | 15 decimales                | `3.14159265358979`     |
| `format short e` | Notación científica 4 dec.  | `3.1416e+00`           |
| `format long e`  | Notación científica 15 dec. | `3.14159265358979e+00` |
| `format rat`     | Fracción racional           | `355/113`              |
| `format bank`    | 2 decimales (moneda)        | `3.14`                 |
| `format hex`     | Hexadecimal                 | `400921fb54442d18`     |

## Nota

`format` solo cambia la **visualización**, no la precisión interna del cálculo (siempre doble precisión).

## Tags

`matlab` `formato` `numeros` `consola`
