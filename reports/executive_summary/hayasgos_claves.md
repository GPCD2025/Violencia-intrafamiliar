# Hallazgos Clave

## Descripción

El analisis descriptivo nos permitió encontrar información relevante que nos llevarón a comprender 
mejor  como variables socio economicas y demograficas impactan en los caso de violencia intrafamiliar,
aún asi, con el uso de tecnicas de analisis exploratorio implementamos la identificación Clustering,
para encontrar potenciales patrones en los datos que no eran tan obvios a analisis descriptivo sobre 
todo en la identificación de los potenciales agresores.

![image](https://github.com/user-attachments/assets/4807cf3f-5501-4283-99a9-c42af1ac3f2e)


Con el fin de indentificar el numero de clusteres ideal, implementamos el methodo de codo (Elbow Method)
identificando 4 potenciales clusteres dentro de nuestros set de datos

![image](https://github.com/user-attachments/assets/d86f946b-bc24-4738-acde-18ed93f47804)

# Distribución de los clusters
Cluster 0: 48,440 puntos.
Cluster 1: 90,980 puntos.
Cluster 2: 66,291 puntos.
Cluster 3: 40,571 puntos.

El Cluster 1 es el más grande, seguido por el Cluster 2, luego el Cluster 0, y finalmente el Cluster 3.
Esto sugiere que los datos están distribuidos de manera desigual entre los clusters, 

# Características principales por cluster

### Cluster 0

Año del hecho: Las proporciones de los años están bastante equilibradas, con un ligero aumento en 2019 (12.92%) y 2023 (10.30%).

Sexo de la víctima: El 64.43% de las víctimas son mujeres.

Grupo de edad: El 100% de los casos corresponden a mayores de edad (>18 años).

Presunto agresor: Los agresores más comunes son el padre (5.99%) y el tío (5.55%).

### Cluster 1

Año del hecho: Similar al Cluster 0, con proporciones equilibradas y un ligero aumento en 2023 (12.33%).

Sexo de la víctima: El 83.47% de las víctimas son mujeres.

Grupo de edad: El 98.78% de los casos corresponden a mayores de edad (>18 años).

Presunto agresor: No hay un agresor predominante, ya que la mayoría de los valores son cercanos a 0.

### Cluster 2

Año del hecho: Proporciones similares a los clusters anteriores, con un ligero aumento en 2016 (13.52%) y 2017 (13.72%).

Sexo de la víctima: El 90.15% de las víctimas son mujeres.

Grupo de edad: El 99.82% de los casos corresponden a mayores de edad (>18 años).

Presunto agresor: No hay un agresor predominante, con valores cercanos a 0.

### Cluster 3

Año del hecho: Proporciones equilibradas, con un ligero aumento en 2019 (13.69%) y 2023 (11.55%).

Sexo de la víctima: El 55.53% de las víctimas son mujeres.

Grupo de edad: Solo el 18.63% de los casos corresponden a mayores de edad (>18 años), lo que indica que este cluster está más asociado a menores de edad.

Presunto agresor: Los agresores más comunes son el padre (23.95%) y el tío (4.21%).


# Diferencias clave entre clusters

### Sexo de la víctima:

Los Clusters 1 y 2 tienen una proporción muy alta de víctimas mujeres (83.47% y 90.15%, respectivamente).

El Cluster 0 tiene una proporción moderada (64.43%).

El Cluster 3 tiene una proporción más equilibrada (55.53% mujeres).

### Grupo de edad:

Los Clusters 0, 1 y 2 están dominados por mayores de edad (>18 años).

El Cluster 3 tiene una proporción significativa de menores de edad (81.37%).

### Presunto agresor:

El Cluster 0 tiene una presencia notable de agresores como el padre y el tío.

El Cluster 3 tiene una presencia aún mayor del padre como agresor (23.95%).

Los Clusters 1 y 2 no muestran un agresor predominante.

# Observaciones adicionales
Año del hecho: No hay diferencias significativas en la distribución temporal entre los clusters, lo que sugiere que el tiempo no es un factor determinante en la formación de los clusters.

Agresores: Los agresores más comunes (padre y tío) están asociados principalmente con los Clusters 0 y 3, lo que podría indicar patrones específicos de violencia familiar en estos grupos.

Menores de edad: El Cluster 3 es el único que tiene una proporción significativa de menores de edad, lo que lo hace único en comparación con los otros clusters.

# Conclusiones

El Cluster 3 es particularmente interesante, ya que combina una alta proporción de menores de edad con agresores familiares (padre y tío), lo que podría indicar un patrón de violencia intrafamiliar dirigida a menores.

Los Clusters 1 y 2 están más asociados con víctimas mujeres mayores de edad, pero no muestran un agresor predominante, lo que sugiere que estos casos podrían estar relacionados con otro tipo de violencia (por ejemplo, violencia de género no familiar).

