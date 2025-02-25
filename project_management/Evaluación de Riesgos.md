#### Evaluación de Riesgos en Proyectos de Ciencia de Datos

El desarrollo de proyectos de ciencia de datos está inherentemente ligado a la gestión eficiente de los recursos disponibles, especialmente en términos de volumen de datos y capacidad computacional. A continuación, se presenta un análisis detallado de los riesgos identificados durante las distintas fases del proyecto, así como las soluciones adoptadas para mitigar dichos riesgos.

# 1. Volumen de Datos y Capacidad Computacional
Uno de los principales desafíos que enfrentamos fue la relación entre el volumen de datos y los costos computacionales asociados. Tanto la falta como la abundancia de datos tienen implicaciones significativas en el desarrollo de proyectos de ciencia de datos. En nuestro caso, el deseo de trabajar con una fuente de datos robusta y completa no consideró inicialmente el impacto que esto tendría en términos de capacidad computacional. Este error estratégico generó retrasos y limitaciones técnicas durante varias etapas del proyecto.

# 2. Fase de Exploración de Datos (EDA)
Durante la fase de exploración de datos (EDA), la abundancia de datos no representó un problema significativo. Gracias al uso de herramientas como Python y Jupyter Notebook en un entorno local, pudimos realizar visualizaciones y análisis iniciales sin mayores complicaciones. Al no requerir transformaciones complejas en esta etapa, el rendimiento computacional fue óptimo, lo que permitió avanzar sin contratiempos.

Sin embargo, esta fase también sirvió como un indicador temprano de los posibles desafíos que podrían surgir en etapas posteriores. Aunque el procesamiento local fue suficiente para el EDA, quedó claro que trabajar con grandes volúmenes de datos podría volverse problemático en fases más exigentes.

# 3. Fase de Limpieza de Datos
La limpieza de datos es una de las etapas más críticas en cualquier proyecto de ciencia de datos. En nuestro caso, utilizamos la librería Pandas, reconocida por su excelente desempeño en tareas de manipulación y limpieza de datos.

Gracias a sus diversas funciones integradas, logramos realizar esta fase de manera eficiente sin experimentar problemas notables o retrasos significativos.

# 4. Fase de Transformación de Datos

La fase de transformación de datos marcó un punto de inflexión en términos de costos computacionales. Aquí comenzaron a manifestarse los principales desafíos relacionados con el volumen de datos y su impacto en los tiempos de ejecución. Las transformaciones necesarias para preparar los datos para modelos de Machine Learning resultaron ser considerablemente más complejas y demandantes en términos de recursos.

Inicialmente intentamos realizar estas transformaciones en un entorno local, pero pronto nos encontramos con limitaciones técnicas que hicieron inviable continuar de esta manera. Esto nos llevó a migrar el trabajo a Google Colab, una plataforma que ofrece mayor capacidad de procesamiento en comparación con un entorno local. Sin embargo, incluso en Google Colab, el volumen de datos seguía siendo un obstáculo, ya que las operaciones más intensivas seguían ralentizando el avance del proyecto.

Este escenario nos obligó a reconsiderar nuestra estrategia y buscar soluciones alternativas para poder avanzar.

# 5. Solución Parcial: Reducción del Volumen de Datos

Con el objetivo de mitigar los problemas de rendimiento y avanzar en el proyecto, decidimos reducir el volumen de datos mediante un proceso de muestreo. Se extrajeron muestras del 10%, 20% y 30% del conjunto de datos original, evaluando el impacto de cada muestra en términos de tamaño de archivo y capacidad de procesamiento. Finalmente, optamos por trabajar con una muestra del 20%, ya que cumplía con las limitaciones de tamaño de archivo para GitHub y ofrecía un equilibrio algo razonable entre representatividad y rendimiento.

Aunque trabajar con este subconjunto de datos mejoró significativamente la velocidad de procesamiento, sigue siendo evidente que las transformaciones y algoritmos más complejos tienen un costo computacional considerable. Esto sugiere que, para proyectos futuros con volúmenes de datos similares, será necesario adoptar soluciones más robustas y escalables desde el inicio.

