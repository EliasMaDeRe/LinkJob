from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_jobs(num_jobs, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Inicializar webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    url = 'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-software-engineer-empleos-SRCH_IL.0,6_IN169_KO7,24.htm'
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #Si es verdadero, queremos seguir buscando

        #Tiempo de espera para dejar que la pagina cargue
        time.sleep(slp_time)
        
        job_buttons = driver.find_elements_by_class_name("react-job-listing")  #Estos son los botones que de las ofertas
        fechas = driver.find_elements_by_css_selector("div[data-test=job-age]")
        
        first_job = driver.find_element_by_class_name("react-job-listing")
        
        first_job.click()
         
        time.sleep(1)            
        
        i = 1
         
        try:
            driver.find_element_by_class_name("selected").click()
     
        except ElementClickInterceptedException:
             pass
     
        try:
             driver.find_element_by_css_selector('[alt="Close"]').click()  #Clcikeando la X
        except NoSuchElementException:
             pass
        
        for job_button in job_buttons:  
            
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                 break
            
            first_job.click()
            
            
            time.sleep(2)            
            
            collected_successfully = False
             
            while not collected_successfully:
                 try:
                     company_name = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]').text
                     location = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                     job_title = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                     ver_mas = driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]/div[2]')
                     ver_mas.click()
                     time.sleep(1)
                     job_description = driver.find_element_by_class_name("jobDescriptionContent").text
                     collected_successfully = True
                 except:
                     print("collect failed")
                     time.sleep(2)
             
            try:
                 salary_estimate = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
            except NoSuchElementException:
                 salary_estimate = -1 #Valor por default
                         
        
            try:
                size = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
            except NoSuchElementException:
                size = -1
        
        
            try:
                type_of_ownership = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
            except NoSuchElementException:
                type_of_ownership = -1
            
            fechas = driver.find_elements_by_css_selector("div[data-test=job-age]")
            fecha_publicacion = fechas[i-1].text

             
            jobs.append({"Job Title" : job_title,
             "Salary Estimate" : salary_estimate,
             "Job Description" : job_description,
             "Company Name" : company_name,
             "Location" : location,
             "Size" : size,
             "Fecha" : fecha_publicacion,
             "Type of ownership" : type_of_ownership,})

            #Pasar al siguiente elemento de la lista
            
            i += 1
            
            if i <= 30:
                first_job = driver.find_element_by_xpath('//*[@id="MainCol"]/div[1]/ul/li['+str(i)+']')

       #Clickeando en el boton de siguiente pagina
       
        try:
            driver.find_element_by_css_selector("button[aria-label=Next]").click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  # Convertir a dataframe y retornarlo
