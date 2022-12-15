from Oferta import Oferta
from Parser import Parser
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time

class Webscrapper:

    def recolectarOfertas(listaOfertas, listaTecno):
        TIEMPO_ESPERA = 2
        PATH = r"driver\chromedriver.exe"
        
        #Inicializar webdriver
        options = webdriver.ChromeOptions()

        #headless
        #options.add_argument('headless')

        driver = webdriver.Chrome(executable_path=PATH,options=options)
        url = 'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-software-engineer-empleos-SRCH_IL.0,6_IN169_KO7,24.htm'
        driver.get(url)

        while len(listaOfertas) < 900:
            
            time.sleep(TIEMPO_ESPERA)
            
            botonesOfertas = driver.find_elements_by_class_name("react-job-listing") # botones de las ofertas
            primeraOferta = driver.find_element_by_class_name("react-job-listing") # primera oferta

            primeraOferta.click()

            time.sleep(TIEMPO_ESPERA/2)

            try: 
                driver.find_element_by_class_name("selected").click()
            except ElementClickInterceptedException:
                pass
            try:
                driver.find_element_by_css_selector('[alt="Close"]').click()  # intenta clickear la X
            except NoSuchElementException:
                pass

            i = 1

            for botonOferta in botonesOfertas:
                print("Recolectadas: "+str(len(listaOfertas))+" de 900")
                if len(listaOfertas) >= 900:
                    return listaOfertas, listaTecno
                driver.execute_script("arguments[0].scrollIntoView();", primeraOferta)
                time.sleep(TIEMPO_ESPERA)
                primeraOferta.click()
                
                time.sleep(TIEMPO_ESPERA)

                exitoso = False

                while not exitoso: # valores siempre presentes en las ofertas
                    try:
                        salario = Webscrapper.recolectarSalario(driver)
                        empresa = Webscrapper.recolectarEmpresa(driver)
                        ubicacion = Webscrapper.recolectarUbicacion(driver)
                        modalidad = Webscrapper.recolectarModalidad(driver)
                        descripcion = Webscrapper.recolectarDescripcion(driver)
                        listaTecnologias = Parser.limpiarTecnologias(descripcion, listaTecno)
                        cantidadSoftskills = Parser.limpiarSoftskills(descripcion)
                        rol = Parser.limpiarRol(Parser.limpiarStringTecnologias(listaTecnologias)) #Checar el MultinomialNB
                        exitoso = True
                    except Exception as e:
                        print(e)
                        print("awanta")
                        time.sleep(TIEMPO_ESPERA)
                

                actual = Oferta(salario,empresa,ubicacion,modalidad,listaTecnologias,len(cantidadSoftskills),rol)

                listaOfertas.append(actual)
                i+=1 # pasa a la siguiente oferta
                if i <= 30:
                    primeraOferta = driver.find_element_by_xpath('//*[@id="MainCol"]/div[1]/ul/li['+str(i)+']')

            #Clickea el boton de siguiente pagina
            try:
                driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()
            except NoSuchElementException:
                print("aiuda")
                break

        return listaOfertas,listaTecno

    def recolectarSalario(driver):

        try:
            salario = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
            salario += driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/span').text # si es por mes, año u hora
            salario = Parser.limpiarSalario(salario)
        except NoSuchElementException:
            salario = -1 #Valor por default

      

        return salario

    def recolectarEmpresa(driver):

        try:
            tamano = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
            tamano = Parser.limpiarTamanoEmpresa(tamano)
        except NoSuchElementException:
            tamano = -1
 
        
        return tamano

    def recolectarUbicacion(driver):
        
        try:
            ubicacion = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
            ubicacion = Parser.limpiarUbicacion(ubicacion)
        except:
            ubicacion = "-1"

        return ubicacion 

    def recolectarModalidad(driver):
        
        try:
            modalidad = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
            modalidad = Parser.limpiarModalidad(modalidad)
        except:
            modalidad = "-1"
        return modalidad

    def recolectarDescripcion(driver):

        descripcion = ""

        try:
            verMas = driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]/div[2]')
            verMas.click()
            descripcion = driver.find_element_by_class_name("jobDescriptionContent").text
        except:
            print("Error boton Descripcion")
        

        return descripcion





    

