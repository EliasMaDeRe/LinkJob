# ![Logo](./img/LogoLinkJob.png)
> LinkJob es una aplicación que permite visualizar la información acerca de las ofertas de trabajo para ingenieros de software en México, por medio de gráficas y archivos .csv.
> - Video demo: [aquí](https://alumnosuady-my.sharepoint.com/personal/a18000621_alumnos_uady_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fa18000621%5Falumnos%5Fuady%5Fmx%2FDocuments%2F2022%2D05%2D23%2022%2D02%2D02%2Emp4&parent=%2Fpersonal%2Fa18000621%5Falumnos%5Fuady%5Fmx%2FDocuments&ga=1) <!-- If you have the project hosted somewhere, include the link here. -->

## Tabla de Contenidos
* [Información General](#información-general)
* [Tecnologías Usadas](#tecnologías-usadas)
* [Funcionalidades](#funcionalidades)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Estado del Proyecto](#estado-del-proyecto)
* [Espacio para Mejora](#espacio-para-mejora)
* [Agradecimientos](#agradecimientos)
* [Contacto](#contacto)
<!-- * [License](#license) -->


## Información General
- Este proyecto fue realizado para la asignatura Programación Orientada a Objetos.
- Existe una falta de información sobre las ofertas de empleo para Ingenieros de Software en México, no hay una manera clara y visual de tener la información acerca del mercado para este puesto.
- Esperamos que nuestro proyecto sea de utilidad para los estudiantes de Ingeniería de Software en México, y sea herramienta para informarse acerca de la situación actual del mercado, salarios, lugares de alta demanda, tecnologías solicitadas, softskills y otra información útil para su elección.
- Como actuales estudiantes de Ingeniería de Software, queríamos acceder a esta información, y al no estar disponible, decidimos solucionar esta problemática.

## Tecnologías Usadas
- Python - version 3
- Pandas - version 1.5.2
- Selenium - version 4.1.5
- PySide6 - version 6.4.1
- Nltk - version 3.7
- Scikit-learn - version 1.1.3
- Seaborn - 0.12.1
- QT Designer
- Chromedriver Webdriver

## Funcionalidades
Lista de las funcionalidades:
- Webscraping de el sitio Glassdoor, exportación de la información recabada en un archivo .csv
- Parsing de la información en un archivo .csv a información manejable, útil y compacta, exportación a un archivo .csv
- Plotteo de un archivo .csv en forma de gráfica de barras, con escalas, etiquetas del total y valor individual de las gráficas, exportación a un archivo .png
- Análisis sentimental de la información recabada del sitio Glassdoor, para identificar los roles de Ingenieros de Software en cada oferta de trabajo
- Interfaz gráfica con botones dropdown que permiten visualizar una gráfica dependiendo de la información solicitada. Esta llama a las funciones anteriores y muestra el .png exportado


## Screenshots
![Interfaz1](./img/ss1.png)
![Interfaz2](./img/ss2.png)
![Interfaz3](./img/ss3.png)


## Setup

Es necesario instalar las [librerías de python](#tecnologías-usadas) mencionadas anteriormente.

Se requiere el chromedriver webdriver para la version de chrome que se tenga instalado. 

- [Chromedriver](https://chromedriver.chromium.org/downloads)

Cuando se tengan todas las piezas de la [carpeta 'codigo'](./codigo) de este repositorio, solo es necesario correr el archivo 'main.py'

`main.py`

Todas las gráficas son generadas al momento.


## Estado del Proyecto
El proyecto está:  _completado_. 


## Espacio para Mejora

Estas son áreas que consideramos pueden tener mejora y cosas que nos hubiese gustado implementar pero no se pudieron realizar por cuestión de tiempo y viabilidad.

Espacio para mejorar:
- Mejorar la interfaz. (Realizar cambios en resolución de las gráficas, usabilidad de la interfaz)
- Mensajes explicativos para los casos cuando no se encuentra información en los datos. (Actualmente solo es un output en consola de ejecución)

Para realizar:
- Opción de archivar las gráficas por intervalo de tiempo. (Por ejemplo, poder consultar las gráficas de meses/años anteriores)
- Mayor cantidad de filtros. (Por ejemplo, añadir a filtros específicos las locaciones encontradas)

## Agradecimientos

Este proyecto fue realizado por: 
- [Fernando Joachín Prieto](https://github.com/FernandoJoachin)
- [José Carlos Leo Fernandez](https://github.com/JoCaLeFe)
- [Elías Madera De Regil](https://github.com/EliasMaDeRe/LinkJob)
- [Carlos Augusto May Vivas](https://github.com/CarlosMay7)
- [Reyna Valentina Ortiz Porras](https://github.com/valeeortiz)


Este proyecto fue inspirado por [este artículo de Omer Sakarya](https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905), y [este video por Ken Jee](https://www.youtube.com/watch?v=MpF9HENQjDo).

Un agradecimiento especial al [Dr. Edgar Cambranes](https://twitter.com/cambranes), por su mentoría durante la realización de este proyecto.


## Contacto

Siéntanse libres de mandarnos mensaje a través de correo byemadera@gmail.com.
