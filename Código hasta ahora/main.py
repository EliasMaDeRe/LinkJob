# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:01:17 2022

@author: EMadera
"""

#import recolectarDatos as rd
import limpiarDatos as ld
import plottearDatos as pld
import pandas as pd
import plottearTecnologias as pt

#path = "C:/Users/EMadera/.spyder-py3/GlassdoorScraping/chromedriver"


def obtener_datos():
    
    #df = rd.get_jobs(900, path, 6) #Este proceso tarda aproximadamente 2 horas para recolectar 900 ofertas de trabajo
    df = pd.read_csv("glassdoor_jobs.csv") #Forma alternativa de cargar datos alternativos.

    SL = ld.depurar_salario(df)
    ML = ld.depurar_modalidad(df)
    FL = ld.depurar_fechas(df)
    TL = ld.depurar_tamano_empresa(df)
    LL = ld.depurar_locacion(df)
    #pt.obtener_tecnologias() #Exportar datos de tecnologia en csv
    
    CLM = ld.locacion_modalidad(df)
    CLT = ld.locacion_tamano_empresa(df)
    CTM = ld.tamano_modalidad(df)
    #CST = ld.salario_tamano(df)
    #CSM = ld.salario_modalidad(df)
    MT= ld.modalidad_tamano(df)
    
    #SLLL = ld.depurar_locacion(SL)
    
    
    #pld.plottear_salario_locacion(SLLL)

    SL.to_csv('SL.csv',index = False)
    ML.to_csv('ML.csv',index = False)
    FL.to_csv('FL.csv',index = False)
    TL.to_csv('TL.csv',index = False)
    LL.to_csv('LL.csv',index = False)
    MT.to_csv('Mt.csv',index=False)
    
    CLT.to_csv('CLT.csv', index=False)
    CLM.to_csv('CLM.csv', index=False)
    CTM.to_csv('CTM.csv', index=False)
    #CSM.to_csv('CSM.csv', index=False)
    #SLLL.to_csv('SLLL.csv', index = False)
    MT.to_csv('MT.csv', index=False)
