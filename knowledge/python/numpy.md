# Python — NumPy (Cómputo Numérico)

## Instalación

```bash
pip install numpy
```

## Arrays básicos

```python
import numpy as np

# Crear arrays
a = np.array([1, 2, 3, 4, 5])          # 1D
b = np.array([[1, 2, 3], [4, 5, 6]])   # 2D (2x3)

print(a.shape)    # (5,)
print(b.shape)    # (2, 3)
print(b.dtype)    # int64
print(b.ndim)     # 2
```

## Creación de arrays especiales

```python
np.zeros((3, 4))          # matriz 3x4 de ceros
np.ones((2, 3))           # matriz 2x3 de unos
np.eye(4)                 # identidad 4x4
np.full((2, 2), 7)        # rellena con 7
np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)      # [0, .25, .5, .75, 1]
np.random.rand(3, 3)      # aleatorios U(0,1)
np.random.randn(3, 3)     # aleatorios N(0,1)
```

## Indexing y slicing

```python
a = np.array([10, 20, 30, 40, 50])
print(a[1])       # 20
print(a[-1])      # 50
print(a[1:4])     # [20 30 40]
print(a[::2])     # [10 30 50]

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[1, 2])    # 6
print(b[:, 1])    # columna 1: [2 5 8]
print(b[0, :])    # fila 0:    [1 2 3]
print(b[1:, 1:])  # submatriz: [[5 6],[8 9]]
```

## Operaciones vectoriales (element-wise)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)      # [5 7 9]
print(a * b)      # [4 10 18]
print(a ** 2)     # [1 4 9]
print(np.sqrt(a)) # [1.   1.41 1.73]

# Broadcasting: operar array con escalar
print(a * 3)      # [3 6 9]
print(a + 10)     # [11 12 13]
```

## Álgebra lineal

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Producto matricial
C = A @ B              # o np.matmul(A, B)

# Determinante e inversa
det = np.linalg.det(A)
inv = np.linalg.inv(A)

# Valores y vectores propios
valores, vectores = np.linalg.eig(A)

# Resolver sistema Ax = b
b = np.array([1, 2])
x = np.linalg.solve(A, b)
```

## Estadística con NumPy

```python
datos = np.array([4, 7, 2, 9, 5, 1, 8, 3, 6, 10])

print(np.mean(datos))    # media
print(np.median(datos))  # mediana
print(np.std(datos))     # desviación estándar
print(np.var(datos))     # varianza
print(np.min(datos))     # mínimo
print(np.max(datos))     # máximo
print(np.percentile(datos, [25, 50, 75]))  # cuartiles
```

## Reshape y transposición

```python
a = np.arange(12)
b = a.reshape(3, 4)    # 3 filas, 4 columnas
c = b.T                # transpuesta (4x3)
d = b.flatten()        # aplanar a 1D
```

## Funciones matemáticas universales (ufunc)

```python
x = np.linspace(0, 2*np.pi, 100)

np.sin(x)
np.cos(x)
np.exp(x)
np.log(x)        # logaritmo natural
np.log10(x)
np.abs(x)
np.ceil(x)
np.floor(x)
```
