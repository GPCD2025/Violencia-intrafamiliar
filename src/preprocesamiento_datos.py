
'''
Este script en Python está diseñado para manipular, limpiar y transformar datos provenientes de un archivo de Excel.
Su objetivo principal es preparar los datos para su uso en análisis posteriores o en modelos de machine learning. El código realiza diferentes tareas como
cargar la base de datos proveniente de un archivo de Excel (`muestra_datos_4.xlsx`) y convertilo en un DataFrame posteriormente
estandarizar valores en las columnas que lo requieran para asegurar consistencia en los datos, asi mismo
eliminar columnas específicas que no se utilizarán en la transformación y finalmente
aplicar un One-Hot Encoding a las columnas restantes para convertir variables categóricas en variables numéricas binarias.
'''

# Importación de bibliotecas
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

# Preprocesamiento
from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Carga de datos
dato40 = pd.read_excel("/content/drive/MyDrive/EAN/proyecto VIC/muestra_datos_4.xlsx")

# Limpieza de datos
dato40["presunto_agresor"].replace("HOMBRE", "Hombre", inplace=True)
dato40["presunto_agresor"].replace("MUJER", "Mujer", inplace=True)
dato40["presunto_agresor"].replace("YERNO", "Yerno", inplace=True)
dato40["presunto_agresor"].replace("NUERA", "Nuera", inplace=True)
dato40["presunto_agresor"].replace("Ex Amante", "Ex amante", inplace=True)
dato40["presunto_agresor"].replace("Ex Esposo (a)", "Ex esposo (a)", inplace=True)
dato40["presunto_agresor"].replace("Ex Novio (a)", "Ex novio (a)", inplace=True)

# Conteo de valores únicos
print(dato40["presunto_agresor"].value_counts())

# Eliminación de columnas no deseadas
datos_tranformar = dato40.drop(columns=[
    "grupo_de_edad_de_la_victima", "tipo_de_discapacidad", "código_dane_municipio",
    "codigo_dane_departamento", "días_de_incapacidad_medicolegal", "pertenencia_etnica",
    "localidad_del_hecho"
])

# Aplicación de One-Hot Encoding
encoder = OneHotEncoder(sparse_output=False, drop="first")
encoded_data = encoder.fit_transform(datos_tranformar)
nombres_columnas = encoder.get_feature_names_out(datos_tranformar.columns)
df_encoded40 = pd.DataFrame(encoded_data, columns=nombres_columnas)

