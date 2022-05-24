# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:01:17 2022

@author: EMadera
"""
import limpiarDatos as ld
import pandas as pd


def obtener_datos():

    # Forma alternativa de cargar datos alternativos.
    df = pd.read_csv("glassdoor_jobs.csv")

    ld.obtener_tecnologias()  # Exportar datos de tecnologia en csv

    # Filtros generales
    SL = ld.depurar_salario(df)
    ML = ld.depurar_modalidad(df)
    FL = ld.depurar_fechas(df)
    TL = ld.depurar_tamano_empresa(df)
    LL = ld.depurar_locacion(df)

    # Filtros generales con específicos
    CMT = ld.modalidad_tamano_empresa(df)
    CLM = ld.locacion_modalidad(df)
    CLT = ld.locacion_tamano_empresa_grande(df)
    CLTM = ld.locacion_tamano_empresa_mediana(df)
    CLTP = ld.locacion_tamano_empresa_pequena(df)
    CTM = ld.tamano_empresa_modalidad(df)
    STM = ld.salario_tamano(df)
    SALAMOD = ld.salario_modalidad(df)

    # Creación de csv's filtros generles
    SL.to_csv('SL.csv', index=False)
    ML.to_csv('ML.csv', index=False)
    FL.to_csv('FL.csv', index=False)
    TL.to_csv('TL.csv', index=False)
    LL.to_csv('LL.csv', index=False)

    # Creación de csv's filtros generales con específicos
    CMT.to_csv('CMT.csv', index=False)
    CLM.to_csv('CLM.csv', index=False)
    CLT.to_csv('CLT.csv', index=False)
    CLTM.to_csv('CLTM.csv', index=False)
    CLTP.to_csv('CLTP.csv', index=False)
    CTM.to_csv('CTM.csv', index=False)
    STM.to_csv('STM.csv', index=False)
    SALAMOD.to_csv('SALAMOD.csv', index=False)
