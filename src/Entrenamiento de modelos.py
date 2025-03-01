
"""
Este script carga datos de violencia intrafamiliar, los procesa y entrena modelos de clasificación 
multietiqueta utilizando regresión logística, Random Forest y Gradient Boosting. 
Se realiza una limpieza inicial, eliminación de columnas con valores únicos, y 
separación en conjuntos de entrenamiento y prueba. Cada modelo se ajusta y se evalúa en términos 
de precisión, recall, F1-score y pérdida de Hamming, proporcionando métricas comparativas 
de desempeño.
"""

#Manipulacion y Calculo de datos
import pandas as pd
import numpy as np
pd.options.display.max_columns
import scipy.stats as stats

# VIsualización de datos
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
%matplotlib inline

#Manejo de avisos de Warning
import warnings
warnings.filterwarnings('ignore')

# Prepocesamiento
from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#Machine Learning
from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score, hamming_loss
from sklearn.model_selection import GridSearchCV

datos_ml = pd.read_csv("/content/drive/MyDrive/EAN/proyecto VIC/df_encoded40_transformados.csv")

datos_ml2 = datos_ml.sample(frac=0.2, random_state=42)
datos_ml2.shape
datos_ml2.columns

lista_etiquetas = [col for col in datos_ml2.columns if col.startswith('presunto_agresor')]

y = datos_ml2[lista_etiquetas]

X = datos_ml2.drop(lista_etiquetas, axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Forma de X_train:", X_train.shape)
print("Forma de X_test:", X_test.shape)
print("Forma de y_train:", y_train.shape)
print("Forma de y_test:", y_test.shape)

#Regresion logistica
cols_to_drop = []
for col in y_train.columns:
    if len(y_train[col].unique()) <= 1:
        cols_to_drop.append(col)

# Drop the identified columns from y_train and y_test
y_train = y_train.drop(columns=cols_to_drop)
y_test = y_test.drop(columns=cols_to_drop)
print(f"Dropped columns: {cols_to_drop}")
print("Shape of y_train after dropping columns:", y_train.shape)
print("Shape of y_test after dropping columns:", y_test.shape)

#Modelo
model = MultiOutputClassifier(LogisticRegression(C=0.1, penalty="l1", solver="liblinear"))

#Ajuste del Modelo
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
recall = recall_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
f1 = f1_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
hamming = hamming_loss(y_test, y_pred)

print(f'Exactitud: {accuracy:.2f}')
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")
print(f"Hamming Loss: {hamming}")
#Random Forest
cols_to_drop = []
for col in y_train.columns:
    if len(y_train[col].unique()) <= 1:
        cols_to_drop.append(col)

# Drop the identified columns from y_train and y_test
y_train = y_train.drop(columns=cols_to_drop)
y_test = y_test.drop(columns=cols_to_drop)
print(f"Dropped columns: {cols_to_drop}")
print("Shape of y_train after dropping columns:", y_train.shape)
print("Shape of y_test after dropping columns:", y_test.shape)

#Modelo
model = MultiOutputClassifier(RandomForestClassifier(n_estimators=10, max_depth= None, min_samples_split=2))

# Ajuste del Modelo
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
recall = recall_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
f1 = f1_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
hamming = hamming_loss(y_test, y_pred)

print(f'Exactitud: {accuracy:.2f}')
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")
print(f"Hamming Loss: {hamming}")
     
#GradientBoostingClassifier

cols_to_drop = []
for col in y_train.columns:
    if len(y_train[col].unique()) <= 1:
        cols_to_drop.append(col)

# Drop the identified columns from y_train and y_test
y_train = y_train.drop(columns=cols_to_drop)
y_test = y_test.drop(columns=cols_to_drop)
print(f"Dropped columns: {cols_to_drop}")
print("Shape of y_train after dropping columns:", y_train.shape)
print("Shape of y_test after dropping columns:", y_test.shape)

# Modelo
model = MultiOutputClassifier(GradientBoostingClassifier(n_estimators=10, learning_rate=0.1, max_depth=3))

# Ajuste del Modelo
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
recall = recall_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
f1 = f1_score(y_test, y_pred, average='micro') # or 'macro', 'weighted'
hamming = hamming_loss(y_test, y_pred)

print(f'Exactitud: {accuracy:.2f}')
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")
print(f"Hamming Loss: {hamming}")