|  RF-003 | Presentador de gráficas   |   |
| ------------ | ----------- | ------------ |
| **Descripción** |El usuario podrá visualizar las gráficas de barras de las categorías de información y tecnologías solicitadas de las ofertas de trabajo publicadas en glassdoor, las cuales son generadas por el sistema a partir de los filtros seleccionados.   |   |
|**Secuencia normal**   |**Paso**   |**Acción**   |
|   | 1 | El usuario introduce los filtros que requiera. |
|   | 2 | El sistema busca en la base de datos las gráficas de barras relacionadas a los filtros colocados por el usuario.  |
|   | 3 | El sistema presenta las gráficas de barras correspondientes.  |
|   | 4 | El usuario visualiza las gráficas de barras presentadas por el sistema.  |

|  RF-004 |   | Generador de gráficas  |
| ------------ | ------------ | ------------ |
|  **Descripción** | El sistema debe generar gráficas de barras, el primer domingo de cada mes, sobre las categorías de información y tecnologías solicitadas de las ofertas publicadas en glassdoor de 1, 6 y 12 meses atrás de cada categoría.  |   |
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


