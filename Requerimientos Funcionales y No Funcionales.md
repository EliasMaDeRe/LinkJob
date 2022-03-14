# Definición de Requerimientos
## Escala de prioridades

 - Prioridad 1 (Obligatorio)
 - Prioridad 2 (Alta prioridad)
 - Prioridad 3 (Preferido, pero no necesario)
 - Prioridad 5 (Propuesta)

# Descripción de los requerimientos funcionales
## RF-001 Base de datos (Prioridad 1)

El sistema debe almacenar el contenido de las categorías de información (sueldo, locación, tamaño de empresa, modalidad, fecha de publicación), tecnologías solicitadas y los URL de cada una de las ofertas de trabajo que se publican en glassdoor, además de las gráficas generadas a partir de la información recabada. 

## RF-002 Recolectado de información (Prioridad 1)

El sistema debe tener la habilidad de recolectar los datos de las categorías de información y tecnologías asociadas a las ofertas de trabajo que se publican en glassdoor, todo esto a través de palabras claves proporcionadas por un diccionario estático integrado.

## RF-003 Presentador de gráficas (Prioridad 1)

El usuario podrá visualizar las gráficas de barras de las categorías de información y tecnologías solicitadas de las ofertas de trabajo publicadas en glassdoor, las cuales son generadas por el sistema a partir de los filtros seleccionados.

## RF-004 Generador de gráficas (Prioridad 2)

El sistema debe generar gráficas de barras, el primer domingo de cada mes, sobre las categorías de información y tecnologías solicitadas de las ofertas publicadas en glassdoor de 1, 6 y 12 meses atrás de cada categoría.**

## RF-005 Archivado de gráficas (Prioridad 4)

El sistema deberá archivar las gráficas de barras de intervalo de tiempo “12 meses” sobre las categorías de información y tecnologías solicitadas de las ofertas publicadas en glassdoor cuando se termine el año (en el primer día del año siguiente).

## RF-006 Filtros generales (Prioridad 3)

El usuario podrá colocar filtros que le permitan visualizar la información del sueldo clasificada por ubicación en México, tamaño de empresa, modalidad, fecha de publicación de la oferta.

## RF-007 Filtros específicos (Prioridad 3)

El usuario podrá colocar filtros que incluyan las subclasificaciones de cada categoría de información (sueldo, anual; locación, los 32 estados de México; tamaño de empresa, grande, mediana y pequeña; modalidad, presencial y virtual; fecha de publicación, un mes, seis meses y doce meses).


# Descripción y clasificación de los requerimientos no funcionales

# Requerimientos de producto

## RF-001 (Prioridad 4)

Todas las funcionalidades del software (las relacionadas a la visualización de las gráficas de barras del salario y las tecnologías más solicitadas de las propuestas de trabajo) deberán tomar menos de 2 segundos, puesto que investigaciones afirman que 2 segundos es el límite para un buen desempeño.

## RF-002 (Prioridad 4)
El programa debe realizar las gráficas de barras sobre las categorías de información y tecnologías solicitadas de las ofertas publicadas de glassdoor en menos de 10 segundos.

## RF-003 (Prioridad 3)
El programa debe restringir al usuario colocar más de 2 filtros de búsqueda activos al mismo tiempo sobre las categorías de información y tecnologías solicitadas de las ofertas publicadas en glassdoor.

# Requerimientos Organizacionales

## RF-004 (Prioridad 4)
El programa solamente debe realizar la catalogación por año de las gráficas de barras sobre las categorías de información y tecnologías solicitadas de las ofertas publicadas en glassdoor durante los primeros 3 años, cuando suceda, se eliminará el año más antiguo.
