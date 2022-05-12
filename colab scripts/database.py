# -*- coding: utf-8 -*-
"""DataBase.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15O-gUsM97hwWDJj5A6zM1N9w185Ec4mR
"""

import pandas as pd # importa la librería pandas y la asigna a la variable pd
datos_consumo = pd.read_excel('/DataBase.xlsx') # indicamos el nombre de nuestro archivo a ser leído
import matplotlib.pyplot as plt 
import seaborn as sns
import sys

datos_consumo.head()

from google.colab import drive
drive.mount('/content/drive')

print("filas y columnas del archivo: ",datos_consumo.shape)

print("caracteristicas de los datos:", datos_consumo.columns)

print("tipo de datos de nuestro DataFrame: ", datos_consumo.dtypes)

print("información de datos:",datos_consumo.info())

print("estdistica descriptiva")
datos_consumo.describe()

"""Conclusiones de los datos (media, moda y mediana):
los datos a evaluar que tienen sentido con este criterio son: 


1.   Content Rating
2.   In App purchases
3.   Ad Supported
4.   Developer ID
5.   Category

Determinamos esto debido a que son estadisticas cuya frecuencia se puede obtener y serian relevantes para un analisis, al no tratarse de informacion de contacto o enlaces a otros sitios. 

A causa de la naturaleza de nuestros datos, no seria posible calcular media y mediana directamente, puesto que se trata de datos textuales y no numericos. 

Puede obtenerse una moda de la fila 'freq' junto con la fila 'top', y es asi que obtenemos que el desarrollador mas frecuente de la lista es Google LLC, la categoria mas frecuente es Tools, el content rating mas utilizado es Everyone, y que la mayoria de las aplicaciones no tienen soporte para anuncios ni compras en la app. 

Igualment, existen datos no numericos en la tabla que se pueden convertir en cifras cuantitativas. Las columnas Ad Supported y In-App purchases, por ejemplo, pueden convertirse en valores binarios (0 y 1). Content Rating, al ser una clase de escala, se puede numerar cada uno de sus niveles y obtener estadisticas de ahi. 

 




"""

datos_consumo[['Ad Supported','In App Purchases']] = datos_consumo[['Ad Supported','In App Purchases']].replace(to_replace=[False, True], value=[0,1])
datos_consumo[['Content Rating']] = datos_consumo[['Content Rating']].replace(to_replace=['Everyone', 'Everyone 10+', 'Teen', 'Mature 17+'], value=[0,1,2,3])
datosLimpio = datos_consumo.drop(['App Id', 'Developer Website', 'Developer Email'], axis=1)
datosLimpio.describe()

"""Una vez realizados los cambios propuestos tenemos una tabla de datos numericos que interpretar. Para la media tenemos que 'Ad Supported' y 'In App Purchases' tienen una media mas cercana a 0. Siendo que los unicos datos posibles son 0 y 1, podemos asumir que es mucho mas comun que las apps no tengan ninguna de estas dos caracteristicas. En el caso de 'Content Rating', la media se encuentra entre 0 y 1, pero se debe tomar en cuenta que existen datos del 0 al 3 ahora, en donde cada uno representa una categoria en la escala de clasificación. 0 y 1 representan a Everyone y Everyone +10, por lo que serian estos entonces los ratings mas comunes. 
La desviacion estandar representa la diferencia que hay entre los datos de la tabla. Cuanto mas alta, mayor diferencia hay entre los datos, y viceversa. Para 'Content Rating' la desviacion estandar esta muy cercana a 1, por lo que nos dice que la dispersion entre los datos es muy alta, mientras que para 'Ad Supported' y 'In App Purchases', donde esta se acerca un poco mas al 0. Esto tiene sentido, ya que en la primera columna existen mas tipos de datos y por lo tanto estan mas dispersos, mientras que en las otras dos solo existen dos tipos de datos, dando un numero mas cercano al 0. 
"""

datosLimpio.head()

anuncio = datosLimpio[datosLimpio['Ad Supported']==1][['App Name','Category', 'Developer Id', 'Content Rating', 'In App Purchases']] 

compras = datosLimpio[datosLimpio['In App Purchases']==1][['App Name','Category', 'Developer Id', 'Content Rating', 'Ad Supported']]

anuncioContent = datosLimpio[datosLimpio['Ad Supported']==1][['Content Rating']]

comprasContent = datosLimpio[datosLimpio['In App Purchases']==1][['Content Rating']]

comprasDev = datosLimpio[datosLimpio['In App Purchases']==1][['Developer Id']]

anunciosDev = datosLimpio[datosLimpio['Ad Supported']==1][['Developer Id']]


anunciosDev.head(10)

#purchase_ad = datosLimpio[datosLimpio['Ad Supported']==1][['App Name','Category', 'Developer Id', 'Content Rating']]

fig, ax = plt.subplots(1,2,figsize=(10,8),sharey=True)


# Aplicaciones que ofrecen anuncios por Clasificacion de Contenido
sns.boxplot(ax=ax[0], data = anuncioContent)
# Aplicaciones que ofrecen compras por Clasificacion de Contenido
sns.boxplot(ax=ax[1], data = comprasContent)

fig, ax = plt.subplots(figsize=(30,16))

ax.hist(comprasDev,ec='black')

plt.xlabel('Desarrolladores')
plt.ylabel('Ofrece Compras en La App')
plt.show()

fig, ax = plt.subplots(figsize=(30,16))

ax.hist(anunciosDev,ec='black')

plt.xlabel('Desarrolladores')
plt.ylabel('Ofrece Anuncios')
plt.show()

