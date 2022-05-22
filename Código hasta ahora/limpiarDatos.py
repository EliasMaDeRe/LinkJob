# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:49:34 2022

@author: EMadera
"""
import pandas as pd
#depurar salario

def depurar_salario(df):

    df = df[df['Salary Estimate'] != '-1']
    
    salario = df['Salary Estimate'].apply(lambda x: x.split(':')[1])
    salario = salario.apply(lambda x: x.replace('k','').replace('$','').replace(' M','000'))
    salariomin = salario.apply(lambda x: int(x.split('-')[0]) if '-' in x else int(x))
    salariomax = salario.apply(lambda x: int(x.split('-')[1]) if '-' in x else int(x))
    salarioanual = (((salariomax + salariomin)/2)*1000)
    salariomensual = salarioanual.apply(lambda x: int(x/12))
    df['Salario Mensual'] = salariomensual
    
    return df

#depurar modalidad

def depurar_modalidad(df):
    
    df = df.dropna()
    df = df[df['Location'] != -1]
    modalidad_virtual = df['Location'].apply(lambda x: x.replace('Trabajo desde casa', '0'))
    modalidad_presencial = modalidad_virtual.apply(lambda x: x != '0')
    modalidad = modalidad_presencial.replace(True, 'Presencial').replace(False, 'Virtual')
    df['Modalidad'] = modalidad
    
    return df
    
    
#depurar fechas

def depurar_fechas(df):
    
    df = df.dropna()
    fecha = df['Fecha'].apply(lambda x: x.split('d')[0] if type(x) != int else int(x))
    fecha= fecha.apply(lambda x: x.replace('24 horas', '1').replace(' ','') if type(x) != int else int(x))
    fecha= fecha.apply(lambda x: int(x))
    df['Fecha'] = fecha
    
    return df
    
#depurar tamaño de empresa

def depurar_tamano_empresa(df):
    
    df = df[df['Size'] != '-1']
    df = df[df['Size'] != 'No se sabe']
    
    size = df['Size'].apply(lambda x: x.split('e')[1])
    size = size.apply(lambda x: x.replace(' ', '').replace('a', '-'))
    sizeMin = size.apply(lambda x: (x.split('-')[0]) if '-' in x else x)
    sizeMax = size.apply(lambda x: (x.split('-')[1]) if '-' in x else x)
    sizenew= sizeMax.replace(["50","200","500"],"Pequeña").replace(["1000","5000"],"Mediana").replace("10000","Grande")
    sizecontar = sizenew.value_counts()
    
    df['Tamaño Empresa'] = sizenew
    
    return df
    
#depurar locacion

def depurar_locacion(df):
    
    df = df.dropna()
    df = df[df['Location'] != 'Trabajo desde casa']
    locacion = df['Location']
    df['Locacion'] = locacion
    
    return df

def modalidad_tamano (df):
    
    df2 = depurar_modalidad(depurar_tamano_empresa(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)
    pres_grande = 0
    pres_mediana = 0
    pres_pequena = 0
    vir_grande = 0
    vir_mediana = 0
    vir_pequena = 0
    

    for i in range (df2.shape[0]) :
        if df2.loc[i,'Modalidad'] == 'Presencial' and df2.loc[i, 'Tamaño Empresa'] == 'Grande' :
            pres_grande += 1

        if df2.loc[i,'Modalidad'] == 'Presencial' and df2.loc[i, 'Tamaño Empresa'] == 'Mediana' :
            pres_mediana += 1

        if df2.loc[i,'Modalidad'] == 'Presencial' and df2.loc[i, 'Tamaño Empresa'] == 'Pequeña' :
            pres_pequena += 1
            
        if df2.loc[i,'Modalidad'] == 'Virtual' and df2.loc[i, 'Tamaño Empresa'] == 'Grande' :
            vir_grande += 1

        if df2.loc[i,'Modalidad'] == 'Virtual' and df2.loc[i, 'Tamaño Empresa'] == 'Mediana' :
            vir_mediana += 1

        if df2.loc[i,'Modalidad'] == 'Virtual' and df2.loc[i, 'Tamaño Empresa'] == 'Pequeña' :
            vir_pequena += 1
            
            
    print(pres_grande)
    cantidad_modalidad_tamano = pd.DataFrame()
    cantidad_modalidad_tamano ['Presencial Grande'] = [pres_grande]
    cantidad_modalidad_tamano ['Presencial Mediana'] = [pres_mediana]
    cantidad_modalidad_tamano ['Presencial Pequeña'] = [pres_pequena]
    cantidad_modalidad_tamano ['Virtual Grande'] = [vir_grande]
    cantidad_modalidad_tamano ['Virtual Mediana'] = [vir_mediana]
    cantidad_modalidad_tamano ['Virtual Pequeña'] = [vir_pequena]
    
    '''
    Vertical
    cantidad_modalidad_tamano.loc [0,'Cantidad'] = pres_grande
    cantidad_modalidad_tamano.loc [1,'Cantidad'] = pres_mediana
    cantidad_modalidad_tamano.loc [2,'Cantidad'] = pres_pequena
    cantidad_modalidad_tamano.loc [3,'Cantidad'] = vir_grande
    cantidad_modalidad_tamano.loc [4,'Cantidad'] = vir_mediana
    cantidad_modalidad_tamano.loc [5,'Cantidad'] = vir_pequena
    '''

    return cantidad_modalidad_tamano

def locacion_modalidad(df):
    df2 = depurar_locacion(depurar_modalidad(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)
    
    return df2

def locacion_tamano_empresa(df):
    df2 = depurar_locacion(depurar_tamano_empresa(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)
    
    return df2

def tamano_modalidad(df) :
    df2 = depurar_tamano_empresa(depurar_modalidad(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)
    
    return df2

def salario_tamano(df):
    
    df2= depurar_salario(depurar_tamano_empresa(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)
    
    return df2

def salario_modalidad (df):
    df2 = depurar_modalidad(depurar_salario(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)
    
    return df2

def depurar_df(df):
    
    df = depurar_fechas(df)
    df = depurar_locacion(df)
    df = depurar_modalidad(df)
    df = depurar_salario(df)
    df = depurar_tamano_empresa(df)
    df = modalidad_tamano (df)
    df = locacion_modalidad(df)
    df = locacion_tamano_empresa(df)
    df = tamano_modalidad(df)
    
    
    return df






