# MATLAB — Ecuaciones Diferenciales Ordinarias

## ode45 — Solver numérico (Runge-Kutta 4/5)

```matlab
% dy/dt = -2y,  y(0) = 1
f = @(t, y) -2 * y;
[t, y] = ode45(f, [0 5], 1);

figure;
plot(t, y, 'b-', 'LineWidth', 2);
xlabel('t'); ylabel('y(t)');
title('Solución numérica: dy/dt = -2y');
grid on;
```

## ode45 — Sistema de ecuaciones (2 ecuaciones)

```matlab
% y1' = y2
% y2' = -y1   (oscilador armónico)
f = @(t, y) [y(2); -y(1)];
[t, y] = ode45(f, [0 10], [1; 0]);   % y1(0)=1, y2(0)=0

figure;
plot(t, y(:,1), 'r-', t, y(:,2), 'b--', 'LineWidth', 1.5);
legend('y_1 = cos(t)', 'y_2 = -sin(t)');
title('Oscilador armónico'); grid on;
```

## dsolve — Solución simbólica

```matlab
syms y(t)

% dy/dt = -2y
eqn  = diff(y, t) == -2 * y;
cond = y(0) == 1;
sol  = dsolve(eqn, cond);
disp(sol)        % -> exp(-2*t)

% Graficar solución simbólica
fplot(sol, [0 3]);
title('Solución simbólica: y = e^{-2t}'); grid on;
```

## dsolve — EDO de segundo orden

```matlab
syms y(t)
eqn  = diff(y, t, 2) + 4*y == 0;   % y'' + 4y = 0
cond = [y(0) == 1, subs(diff(y, t), t, 0) == 0];
sol  = dsolve(eqn, cond);
disp(sol)        % -> cos(2*t)
```

## Control de tolerancia en ode45

```matlab
opts = odeset('RelTol', 1e-6, 'AbsTol', 1e-8);
[t, y] = ode45(f, [0 5], y0, opts);
```

## Solvers disponibles

| Solver   | Uso recomendado                       |
| -------- | ------------------------------------- |
| `ode45`  | Problemas no rígidos (uso general)    |
| `ode23`  | Tolerancias bajas o ecuaciones suaves |
| `ode15s` | Problemas rígidos (stiff)             |
| `ode23s` | Problemas muy rígidos                 |
