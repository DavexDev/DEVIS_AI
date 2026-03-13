# Python — Pandas (Análisis de Datos)

## Instalación

```bash
pip install pandas
```

## Crear un DataFrame

```python
import pandas as pd

# Desde diccionario
df = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'María', 'Carlos'],
    'edad':   [25, 30, 22, 35],
    'nota':   [8.5, 7.0, 9.2, 6.8],
})

print(df)
print(df.dtypes)
print(df.shape)   # (4, 3)
```

## Leer y guardar archivos

```python
# CSV
df = pd.read_csv('datos.csv', sep=',', encoding='utf-8')
df.to_csv('salida.csv', index=False)

# Excel
df = pd.read_excel('datos.xlsx', sheet_name='Hoja1')
df.to_excel('salida.xlsx', index=False)

# JSON
df = pd.read_json('datos.json')
df.to_json('salida.json', orient='records')
```

## Inspección de datos

```python
df.head(5)        # primeras 5 filas
df.tail(5)        # últimas 5 filas
df.info()         # tipos de datos y valores nulos
df.describe()     # estadísticas descriptivas
df.isnull().sum() # conteo de NaN por columna
```

## Selección de datos

```python
# Columna
df['nombre']
df[['nombre', 'nota']]

# Filas por índice numérico (iloc)
df.iloc[0]        # primera fila
df.iloc[1:3]      # filas 1 y 2
df.iloc[:, 0:2]   # todas las filas, columnas 0 y 1

# Filas por etiqueta/condición (loc)
df.loc[df['edad'] > 25]
df.loc[df['nota'] >= 8, ['nombre', 'nota']]
```

## Filtrado y condiciones

```python
# Filtro simple
aprobados = df[df['nota'] >= 7]

# Múltiples condiciones
filtro = df[(df['edad'] < 30) & (df['nota'] > 8)]

# isin
df[df['nombre'].isin(['Ana', 'María'])]

# Negación
df[~df['nombre'].isin(['Luis'])]
```

## Operaciones con columnas

```python
# Nueva columna calculada
df['aprobado'] = df['nota'] >= 7

# Aplicar función
df['nombre_upper'] = df['nombre'].str.upper()
df['nota_redondeada'] = df['nota'].apply(round)

# Eliminar columna
df.drop(columns=['aprobado'], inplace=True)

# Renombrar columnas
df.rename(columns={'nota': 'calificacion'}, inplace=True)
```

## Valores nulos

```python
df.dropna()                        # eliminar filas con NaN
df.dropna(subset=['nota'])         # solo si NaN en columna nota
df.fillna(0)                       # rellenar con 0
df['nota'].fillna(df['nota'].mean(), inplace=True)  # rellenar con media
```

## Agrupación y agregación (groupby)

```python
# Agrupar por categoría y calcular media
df.groupby('departamento')['salario'].mean()

# Múltiples agregaciones
resumen = df.groupby('departamento').agg(
    total    = ('salario', 'sum'),
    promedio = ('salario', 'mean'),
    cantidad = ('nombre',  'count'),
)
print(resumen)
```

## Ordenar datos

```python
df.sort_values('nota', ascending=False)
df.sort_values(['departamento', 'nota'], ascending=[True, False])
```

## Merge / Join entre DataFrames

```python
df1 = pd.DataFrame({'id': [1,2,3], 'nombre': ['Ana','Luis','María']})
df2 = pd.DataFrame({'id': [1,2,4], 'nota': [8.5, 7.0, 9.0]})

# Inner join (solo coincidencias)
merged = pd.merge(df1, df2, on='id', how='inner')

# Left join (todos del izquierdo)
merged = pd.merge(df1, df2, on='id', how='left')
```

## Tablas pivote

```python
pivot = df.pivot_table(
    values='nota',
    index='departamento',
    columns='semestre',
    aggfunc='mean',
)
```

## Estadísticas rápidas

```python
df['nota'].mean()
df['nota'].median()
df['nota'].std()
df['nota'].value_counts()     # frecuencia de valores únicos
df['nota'].corr(df['edad'])   # correlación entre dos columnas
```
