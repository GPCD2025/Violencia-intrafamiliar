# Calidad de Datos

En general, la base de datos desde su origen en general contaba con una buena calidad de datos,
al ser una base de datos casi en su totalidad de datos categoricos (strings) al realizar un conteo tipico
de valores nulos, esta no presentaba ninguno.

![image](https://github.com/user-attachments/assets/afb6ce5a-dcaf-4171-a68e-b15ce6702a07)


Al profundizar en el informe de cada una de la variables, se identificaron 6 columnas que en su totalidad
contaban con datos que podrian ser considerados como nulos (NO APLICA)


![image](https://github.com/user-attachments/assets/a6cfcc6f-df15-49af-993e-5248d930c79d)

Al ser variables que en su totalidad no entregaban ningún tipo de información, se descartaron del dataset
con el metodo Drop de pandas

![image](https://github.com/user-attachments/assets/75b137f3-c54f-4a02-adb4-4632ce946b50)

Se encontraron datos denomidados (Por Determinar) que correspondian a 5 filas,
en ninguna de la variables contaba con información por lo que fueron eliminadas 
ya que no aportaban ningun tipo de información y tampoco era un número relevante
de filas que pudiera impactar de forma importante en el analisis posterior

![image](https://github.com/user-attachments/assets/a44115b9-e6fb-42a2-b311-f1788c5b7fcf)

![image](https://github.com/user-attachments/assets/d2867d75-d6df-45b6-adad-c6dc23c65774)


# Inconsistencia en los registros Minusculas y Mayusculas

![image](https://github.com/user-attachments/assets/d483f4bf-cc23-4e47-a877-64378a361185)![image](https://github.com/user-attachments/assets/a81ff4e8-89b6-4846-ace0-c9eb9caa38be)

Se estandarizaron los registro, aquellos que estaban en mayusculas pasaron a minusculas 
para estandarizar el tipo de registro.

![image](https://github.com/user-attachments/assets/a7b2d1b3-217e-4f8b-86e4-1b573ddb0b1a)


# Estandarización de nombre de columnas para eliminar espacios entre palabras "nombre columna" a "nombre_columna"

![image](https://github.com/user-attachments/assets/35856431-6d54-44c4-94b0-5b5dbc33a71a)

![image](https://github.com/user-attachments/assets/8c5caf14-2c94-4a87-8f14-d178549274f2)

![image](https://github.com/user-attachments/assets/88131fa8-4cf4-4499-ba05-3e501adc39b3)


