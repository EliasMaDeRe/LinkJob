# Especificación Requerimientos

| **RF-001**  |   |   |  **Base de datos** |
| ------------ | ------------ | ------------ | ------------ |
| **Descripción**   |   |   |  El sistema debe almacenar el contenido de las categorías de información (sueldo, locación, tamaño de empresa, modalidad, fecha de publicación),  tecnologías solicitadas y los URL de cada una de las ofertas de trabajo que se publican en glassdoor, además de las gráficas de barras generadas a partir de la información recabada. |
|**Secuencia normal**  |  **Paso** | **Acción** |   |
|   | 1  |  El sistema detecta la URL de la oferta de trabajo de glassdoor. |   |
|   | 2  |  El sistema almacena en la base de datos la URL de la oferta de trabajo de glassdoor. |   |
|   |  3 |  El sistema localiza los datos de las categorías de información y tecnologías solicitadas a partir de las palabras claves generadas por el diccionario estático integrado. |   |
|   |  4 |  El sistema almacena en una base de datos la información de las categorías de información y tecnologías. |   |
|   |  5 | El sistema genera las gráficas de barras a partir de los datos obtenidos de las categorías de información y tecnologías solicitadas.  |   |
|   |  6 |  El sistema almacena en una base de datos las gráficas de barras generadas a partir de la información obtenida de las categorías de información y tecnologías solicitadas. |   |
| **Excepciones**  | **Paso**  | **Acción**  |   |
|   | 2 | Si el sistema pierde la conexión con la base de datos cuando se está recolectando la URL de la oferta de trabajo de glassdoor:  |   |
|   |   | 2.1   | El sistema deja en espera el envío de la URL  de la oferta de trabajo de glassdoor hasta que se restablezca la conexión con la base de datos.
|   |   |  2.2  | El sistema intenta cada hora del domingo conectarse con la base de datos para enviar la URL correspondiente.
|   | 2.2 |  Si el sistema no logra acceder a la base de datos cuando termine el domingo: |   |
|   |   | 2.2.1  | El sistema desecha la URL de la oferta de trabajo en glassdoor del domingo.   |
|   |   | 2.2.2  | El sistema almacena la URL perdida de la oferta de trabajo en glassdoor hasta el próximo domingo, junto con las demás URL recabadas ese mismo día.   |
|   | 4  |  Si el sistema pierde la conexión con la base de datos cuando se está recolectando los datos de las categorías de la información y tecnologías solicitadas: |   |
|   |   |  4.1 |  El sistema deja en espera el envío de los datos de las categorías de la información y tecnologías solicitadas hasta que se restablezca la conexión con la base de datos. |
|   |   |  4.2 | El sistema continúa cada hora del domingo intentando conectarse con la base de datos para enviar la información correspondiente. |
|   | 4.2  | Si el sistema no logra acceder a la base de datos cuando termine el domingo:  |   |
|   |   | 4.2.1  | El sistema desecha la información recabada de las ofertas de trabajo en glassdoor del domingo.  |
|   |   |  4.2.2 |  El sistema almacena la información perdida de la oferta de trabajo en glassdoor hasta el próximo domingo, junto con los demás datos recabados de ese mismo día.  |
|   |  6 | Si el sistema pierde la conexión con la base de datos cuando se está recolectando las gráficas de barras de las categorías de la información y tecnologías:   |  |
|   |   |  6.1 | El sistema deja en espera el envío de las gráficas de barras generadas a partir de los datos de las categorías de información y tecnologías, hasta que se restablezca la conexión con la base de datos.  |
| | |6.2 | El sistema intentará conectarse cada hora del domingo con la base de datos hasta finalmente poder enviar la gráficas de barras correspondiente.|

| **RF-002**  |   |   |  **Recolectado de información** |
| ------------ | ------------ | ------------ | ------------ |
|**Descripción**   |   |   |  El sistema debe tener la habilidad de recolectar los datos de las categorías de información y tecnologías asociadas a las ofertas de trabajo que se publican en glassdoor, todo esto a través de palabras claves proporcionadas por un diccionario estático integrado. |
| **Secuencia normal**  | **Paso**  | **Acción**  |   |
|   | 1 | El sistema comienza a realizar la recolección de los datos de las categorías de información y tecnologías solicitadas cada primer domingo del mes a las 0:00 hrs.  |   |
|   | 2 | El sistema solicita al diccionario estático integrado las palabras claves almacenadas.   |   |
|   | 3 | El sistema accede a la URL de la oferta de trabajo de glassdoor.  |   |
|   | 4 |El sistema revisa que no se haya almacenado anteriormente la URL de las ofertas de trabajo de glassdoor.   |   |
|   | 5 | El sistema localiza en las ofertas de trabajo de glassdoor las palabras claves proporcionadas por el diccionario estático integrado.  |   |
|   | 6 | El sistema selecciona la información a partir de las palabras claves.  |   |
|   | 7 | El sistema clasifica los datos en los diferentes tipos de categorías de información.   |   |
|**Excepciones**   | **Paso**  |**Acción**   |   |
|   | 4  |Si el sistema detecta que ya se accedió anteriormente a la URL de la propuesta de trabajo:   |   |
|   |   | 4.1  | El sistema no accede a la propuesta de trabajo.  |
|   |   | 4.2  | El sistema pasa a la siguiente categoría.  |
|   | 6  | Si el sistema no encuentra una categoría de información o tecnología de la propuesta de trabajo en glassdoor:  |   |
|   |   | 6.1  |Omite la categoría o tecnología que no está presente.   |
|   |   | 6.2  | El sistema continúa con la búsqueda.  |

|  RF-003 |    | Presentador de gráficas  |
| ------------ | ----------- | ------------ |
| **Descripción** |   | El usuario podrá visualizar las gráficas de barras de las categorías de información y tecnologías solicitadas de las ofertas de trabajo publicadas en glassdoor, las cuales son generadas por el sistema a partir de los filtros seleccionados.  |
|**Secuencia normal**   |**Paso**   |**Acción**   |
|   | 1 | El usuario introduce los filtros que requiera. |
|   | 2 | El sistema busca en la base de datos las gráficas de barras relacionadas a los filtros colocados por el usuario.  |
|   | 3 | El sistema presenta las gráficas de barras correspondientes.  |
|   | 4 | El usuario visualiza las gráficas de barras presentadas por el sistema.  |

|  RF-004 |   | Generador de gráficas  |
| ------------ | ------------ | ------------ |
|  **Descripción** |   | El sistema debe generar gráficas de barras, el primer domingo de cada mes, sobre las categorías de información y tecnologías solicitadas de las ofertas publicadas en glassdoor de 1, 6 y 12 meses atrás de cada categoría.  |
| **Secuencia normal** | **Paso**  |  **Acción** |
|   |  1 |  Los datos de las categorías de información están disponibles para el sistema. |
|   | 2  |  El sistema genera una gráfica de barras el primer domingo de cada mes con la información almacenada. |
|   |  3 | El sistema genera gráficas de barras para cada intervalo de tiempo (1 mes, 6 meses y 12 meses).  |
|   | 4  |  El sistema almacena las gráficas de barras generadas con la información e intervalos correspondientes. |

| RF-005  |   |  Archivado de gráficas |
| ------------ | ------------ | ------------ |
| **Descripción**   |   | El sistema deberá archivar las gráficas de barras de intervalo de tiempo “12 meses” sobre las categorías de información y tecnologías solicitadas de las ofertas publicadas en glassdoor cuando se termine el año (En el primer día del año siguiente).  |
| **Secuencia normal**  |  **Paso** | **Acción**  |
|   | 1 |  El sistema detecta que ha terminado el año (12 meses) transcurrido.
|   | 2 |El sistema identifica las gráficas de barras a archivar.  |
|   | 3| El sistema almacena las gráficas de barras para archivarlas en un apartado que permita acceder a ellas en un futuro.  |
|   |4| El usuario puede ir al apartado correspondiente para poder visualizar las gráficas de barras de años anteriores.  |


|RF-006   |   |   | Filtros generales   |
| ------------ | ------------ | ------------ | ------------ |
| **Descripción**  |   |   | El usuario podrá colocar filtros que le permitan visualizar la información del sueldo clasificada por ubicación en México, tamaño de empresa, modalidad, fecha de publicación de la oferta.  |
| **Secuencia normal**  | **Paso**  |   |**Acción**   |
|   | 1  |   | El usuario selecciona la opción que solicita las categorías de información. |
|   | 2  |   | El sistema despliega una lista de categorías de información.  |
|   | 3  |   |El usuario selecciona las categorías de las cuales necesite la información.  |
|   | 4  |   | El sistema localiza la información relacionada a los parámetros seleccionados.   |
|**Excepciones**   | **Paso**  |   | **Acción**  |
|   | 3  |   | Si el usuario selecciona más de 2 filtros para las cuales necesite la información:  |
|   |   | 3.1  | El sistema le informa al usuario de que no es posible elegir más de dos filtros.  |


|**RF-007**|||**Filtros Específicos**|
|--|--|--|--|
|**Descripción**|||El usuario podrá colocar filtros que incluyan las subclasificaciones de cada categoría de información (locación, los 32 estados de México; tamaño de empresa, grande, mediana y pequeña; modalidad, presencial y virtual; fecha de publicación, un mes, seis meses y doce meses).|
|**Secuencia Normal**|**Paso**|**Acción**||
||1|El usuario solicita al sistema la lista de subclasificaciones de las categorías de información.||
||2|El sistema despliega una lista de subclasificaciones de las categorías de información.||
||3|El usuario selecciona las subclasificaciones que desee.||
||4|El sistema localiza la información relacionada a las subcategorías ingresadas en los filtros.||
|**Excepciones**|**Paso**|**Acción**||
||3|Si el usuario selecciona más de 2 filtros de las subclasificaciones.||
|||3.1|El sistema le informa al usuario de que no es posible elegir más de dos filtros.|

