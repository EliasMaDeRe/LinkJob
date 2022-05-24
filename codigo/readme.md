## Archivos: 
- interfaz.py 
> Se encarga de generar toda la interfaz para el usuario, obtiene como input los filtros seleccionados por el usuario, llama a 'exportardatos.py' y obtiene los datos parseados en forma de .csv exportados, para luego llamar a las funciones de 'plottearDatos.py' para generar las gráficas, posterior a esto, muestra las imágenes generadas en la interfaz.
- exportardatos.py
> Se encarga de importar el archivo .csv pre-cargado (default) o de llamar a la funcion del archivo 'recolectarDatos.py' para realizar el proceso de webscraping. Esta linea se encuentra comentada por defecto. Una vez importado, llama a las funciones de 'limpiarDatos.py' para parsear la información y obtenerla en forma de dataframe. Posterior a esto, exporta los dataframes a archivos .csv
- recolectarDatos.py
> Se encarga de realizar el proceso de webscraping en la pagina de glassdoor, utiliza una ventana de chrome automatizada y recolecta hasta un máximo de 900 ofertas de trabajo que se encuentren en el sitio, así como la información completa de estas.
- limpiarDatos.py
> Se encarga de recibir un dataframe y parsear sus datos de acuerdo a los filtros que se requieran. Retorna un dataframe parseado.
- plottearDatos.py
> Se encarga de recibir un dataframe, genera el 'plot' o gráfica de la información con los filtros de acuerdo a la función llamada, no retorna nada, pero exporta un archivo de la gráfica generada.
