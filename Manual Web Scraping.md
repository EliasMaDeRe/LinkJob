# Guía Web-Scrapping 

## Instalar librerías
- Selenium
- Pandas
- Web driver de Google Chrome

## Identificar los elementos que deseamos obtener de la página

En este caso, de todos los datos de podemos obtener decidimos recolectar la posición de la moneda, su nombre, la abreviatura y el precio actual de la moneda

Para hacer más rápida e intuitiva la recolección, en este ejemplo, recolectaremos la información de 10 monedas, además que el tiempo de espera será de 1 segundo

## ¡Ahora a codificar!

### Importar nuestras librerías a utilizar en el programa

#### selenium
from selenium import webdriver 

Esta parte de la librería permite automatizar el navegador google chrome

#### time
import time

Esta librería que llega por defecto con python y nos permite controlar tiempos en el programa

#### pandas
import pandas as pd

Gracias a esta importacion podemos exportar nuestros resultados a un .csv

### Creamos nuestra función principal de nuestro programa

def obtener_monedas():

### Inicializamos nuestras variables 

#### Buscar la ruta donde se encuenra instalado el driver que instalamos 

path = "C:/Users/EMadera/proyectos/Python/chromedriver"

#### Determinamos el url de la página a scrapear

url = 'https://coinmarketcap.com' 

#### Definimos las variables restantes 

tiempo_de_espera = 1  Tiempo de espera para el programa (segundos)

numero_de_monedas = 10  Numero de monedas a scrapear

monedas = [] Arreglo donde se almacenarán nuestros datos

#### Primero debemos abrir el navegador

options = webdriver.ChromeOptions() 

driver = webdriver.Chrome(executable_path=path,options=options)

driver.set_window_size(1120, 1000) Definimos el tamaño de la ventana que abriremos

driver.get(url)

time.sleep(tiempo_de_espera) Definimos el tiempo de espera entre cada orden 

### Hora de Scrapear

    for i in range(numero_de_monedas): Las cantidad de monedas a recolectar, siempre que sea vedadero continua 

        time.sleep(tiempo_de_espera)

        recolectado = False #Inicializamos nuestra bandera para saber si recolectamos 

        while not recolectado: #Aquí vemos si ya hemos recolectado la información, si no lo hemos recolectado, lo intenta 
            try:
                posicion = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr['+str(i+1)+']/td[2]/p').text
                nombre = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr['+str(i+1)+']/td[3]/div/a/div/div/p').text
                siglas = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr['+str(i+1)+']/td[3]/div/a/div/div/div/p').text
                precio = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr['+str(i+1)+']/td[4]/div/a/span').text

                recolectado = True #Cambiamos nuestra bandera si recolectamos
                print("Recolecto correctamente: "+str(i+1))
            except:
                print("Fallo la coleccion") 
                time.sleep(tiempo_de_espera)

        #Aquí agregamos la información que recolectamos al arreglo que definimos al principio
        monedas.append({"Posicion de moneda" : posicion,"Nombre de moneda" : nombre,"Siglas" : siglas,"Precio" : precio}) 

    return pd.DataFrame(monedas) #Al finalizar la función regresa nuestro dataframe gracias a pandas
	
	df = obtener_monedas() # Asignamos nuestro dataframe generado, a una variable
	df.to_csv('crypto.csv',index = False) #Transformamos nuestro dataframe a un tipo de archivo, en este caso .csv y le ponemos un nombre con su extensión, en este caso crypto.csv

#### Al final nuestro código se verá así

	def obtener_monedas():

    path = "C:/Users/EMadera/proyectos/Python/chromedriver" 
    url = 'https://coinmarketcap.com' 
    tiempo_de_espera = 1 
    numero_de_monedas = 10 
    monedas = []

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path,options=options)
    driver.set_window_size(1120, 1000)
    driver.get(url)
    
    time.sleep(tiempo_de_espera)


    for i in range(numero_de_monedas): 

        time.sleep(tiempo_de_espera)

        recolectado = False

        while not recolectado:
            try:
                posicion = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr['+str(i+1)+']/td[2]/p').text
                nombre = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr['+str(i+1)+']/td[3]/div/a/div/div/p').text
                siglas = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr['+str(i+1)+']/td[3]/div/a/div/div/div/p').text
                precio = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr['+str(i+1)+']/td[4]/div/a/span').text

                recolectado = True
                print("Recolecto correctamente: "+str(i+1))
            except:
                print("Fallo la coleccion")
                time.sleep(tiempo_de_espera)

        monedas.append({"Posicion de moneda" : posicion,"Nombre de moneda" : nombre,"Siglas" : siglas,"Precio" : precio})

    return pd.DataFrame(monedas)

	df = obtener_monedas()
	df.to_csv('crypto.csv',index = False)

#### Nos generará un archivo .csv que podremos abrir con algún editor de hojas de cálculo, como excel



