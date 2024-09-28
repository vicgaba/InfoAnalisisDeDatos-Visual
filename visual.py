import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ventas.csv', delimiter=';')

#print(df.head())

# EDA

# Eliminar filas con valores nulos
df_limpio = df.dropna()

# Configuración el estilo visual de seaborn
sns.set_theme(style='whitegrid')


#  Distribución del precio de venta
# plt.figure(figsize=(10,6))
# sns.histplot(df_limpio['precio de venta'], kde=True, bins= 30
#              ,element='step', alpha = 0.4) #Kernel Density Estimation - bins divide los datos para el histograma - step dibuja en forma de escalera - alpha le agrega transparencia (de 0 a 1)
# plt.title('Distribución del Precio de Venta')
# plt.xlabel('Precio de Venta')
# plt.ylabel('Frecuencia')
# plt.show()


# 2 Ventas por categoría
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Categoria', order=df_limpio['Categoria'].value_counts().index, palette='viridis', hue='Categoria', legend=True) #hue genera la leyenda de por lo cual fue agrupado
# plt.title('Venta por Categoria de Producto')
# plt.xlabel('Categoría')
# plt.ylabel('Número de ventas')
# plt.xticks(rotation=45) #Rota las etiquetas del eje x
# plt.show()

# 3 Ventas por genero
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Genero', order=df_limpio['Genero'].value_counts().index, palette='viridis', hue='Genero', legend=True) #hue genera la leyenda de por lo cual fue agrupado
# plt.title('Venta por Genero de Producto')
# plt.xlabel('Genero')
# plt.ylabel('Número de ventas')
# plt.xticks(rotation=45) #Rota las etiquetas del eje x
# plt.show()

# 4 Ventas por marca
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Marca', order=df_limpio['Marca'].value_counts().index, palette='viridis', hue='Marca', legend=True) #hue genera la leyenda de por lo cual fue agrupado
# plt.title('Venta por Marca de Producto')
# plt.xlabel('Marca')
# plt.ylabel('Número de ventas')
# plt.xticks(rotation=45) #Rota las etiquetas del eje x
# plt.show()

# 5 Ventas por color
plt.figure(figsize=(10,6))
sns.countplot(data=df_limpio, x='Color', order=df_limpio['Color'].value_counts().index, palette='viridis', hue='Genero', legend=True) #hue genera la leyenda de por lo cual fue agrupado
plt.title('Venta por Color de Producto')
plt.xlabel('Color')
plt.ylabel('Número de ventas')
plt.xticks(rotation=45) #Rota las etiquetas del eje x
plt.show()



