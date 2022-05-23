# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:49:34 2022

@author: EMadera
"""
import pandas as pd

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

def depurar_modalidad(df):
    
    df = df.dropna()
    df = df[df['Location'] != -1]
    modalidad_virtual = df['Location'].apply(lambda x: x.replace('Trabajo desde casa', '0'))
    modalidad_presencial = modalidad_virtual.apply(lambda x: x != '0')
    modalidad = modalidad_presencial.replace(True, 'Presencial').replace(False, 'Virtual')
    df['Modalidad'] = modalidad
    
    return df     

def depurar_fechas(df):
    
    df = df.dropna()
    fecha = df['Fecha'].apply(lambda x: x.split('d')[0] if type(x) != int else int(x))
    fecha= fecha.apply(lambda x: x.replace('24 horas', '1').replace(' ','') if type(x) != int else int(x))
    fecha= fecha.apply(lambda x: int(x))
    df['Fecha'] = fecha
    
    return df
    
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
def depurar_locacion(df):
    
    df = df.dropna()
    df = df[df['Location'] != 'Trabajo desde casa']
    locacion = df['Location']
    df['Locacion'] = locacion 
    return df

def modalidad_tamano_empresa(df):
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

        elif df2.loc[i,'Modalidad'] == 'Presencial' and df2.loc[i, 'Tamaño Empresa'] == 'Mediana' :
            pres_mediana += 1

        elif df2.loc[i,'Modalidad'] == 'Presencial' and df2.loc[i, 'Tamaño Empresa'] == 'Pequeña' :
            pres_pequena += 1
            
        elif df2.loc[i,'Modalidad'] == 'Virtual' and df2.loc[i, 'Tamaño Empresa'] == 'Grande' :
            vir_grande += 1

        elif df2.loc[i,'Modalidad'] == 'Virtual' and df2.loc[i, 'Tamaño Empresa'] == 'Mediana' :
            vir_mediana += 1

        elif df2.loc[i,'Modalidad'] == 'Virtual' and df2.loc[i, 'Tamaño Empresa'] == 'Pequeña' :
            vir_pequena += 1
            
    
    df_modalidad_te = pd.DataFrame()
    df_modalidad_te['Modalidad'] = ['Presencial', 'Virtual']
    df_modalidad_te['Empresa Grande'] = [ pres_grande, vir_grande]
    df_modalidad_te['Empresa Mediana'] = [ pres_mediana, vir_mediana]
    df_modalidad_te['Empresa Pequena'] = [ pres_pequena, vir_pequena]
    total_ofertas_G = pres_grande + vir_grande 
    total_ofertas_M = pres_mediana + vir_mediana
    total_ofertas_P = pres_pequena + vir_pequena
    df_modalidad_te['Total de ofertas Grande'] = [total_ofertas_G, 'NaD']
    df_modalidad_te['Total de ofertas Mediana'] = [total_ofertas_M, 'NaD']
    df_modalidad_te['Total de ofertas Pequena'] = [total_ofertas_P, 'NaD']
    
    return df_modalidad_te

def locacion_modalidad(df):
    df2 = depurar_locacion(depurar_modalidad(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)
    
    return df2

def locacion_tamano_empresa_grande(df):
    df2 = depurar_locacion(depurar_tamano_empresa(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)

    locacion_grande = []

    for i in range (df2['Tamaño Empresa'].shape[0]):
        if (df2['Tamaño Empresa'].loc[i]) == "Grande":
            locacion_grande.append(df2['Locacion'].loc[i])
        

    locacion_grande = pd.DataFrame(locacion_grande)
    locacion_grande = locacion_grande.value_counts()
    locacion_grande = pd.DataFrame(locacion_grande)
    locacion_grande = locacion_grande.rename(columns={0:'Repeticiones'})
    locacion_grande = locacion_grande.reset_index()
    locacion_grande = locacion_grande.rename(columns={0:'Locaciones'})
    
    return locacion_grande

def locacion_tamano_empresa_mediana(df):
    df2 = depurar_locacion(depurar_tamano_empresa(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)

    locacion_mediana = []

    for i in range (df2['Tamaño Empresa'].shape[0]):
        if (df2['Tamaño Empresa'].loc[i]) == "Mediana":
            locacion_mediana.append(df2['Locacion'].loc[i])

    locacion_mediana = pd.DataFrame(locacion_mediana)
    locacion_mediana = locacion_mediana.value_counts()
    locacion_mediana = pd.DataFrame(locacion_mediana)
    locacion_mediana = locacion_mediana.rename(columns={0:'Repeticiones'})
    locacion_mediana = locacion_mediana.reset_index()
    locacion_mediana = locacion_mediana.rename(columns={0:'Locaciones'})
    
    return locacion_mediana

def locacion_tamano_empresa_pequena(df):
    df2 = depurar_locacion(depurar_tamano_empresa(df))
    df2 = df2.reset_index()
    df2.drop(['index'], axis = 1, inplace = True)

    locacion_pequena = []

    for i in range (df2['Tamaño Empresa'].shape[0]):
        if (df2['Tamaño Empresa'].loc[i]) == "Pequeña":
            locacion_pequena.append(df2['Locacion'].loc[i])

    locacion_pequena = pd.DataFrame(locacion_pequena)
    locacion_pequena = locacion_pequena.value_counts()
    locacion_pequena = pd.DataFrame(locacion_pequena)
    locacion_pequena = locacion_pequena.rename(columns={0:'Repeticiones'})
    locacion_pequena = locacion_pequena.reset_index()
    locacion_pequena = locacion_pequena.rename(columns={0:'Locaciones'})
    
    return locacion_pequena

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

def salario_locacion(df):
    
    df2= depurar_locacion(depurar_salario(df))
    
    return df2

def depurar_df(df):
    
    df = depurar_fechas(df)
    df = depurar_locacion(df)
    df = depurar_modalidad(df)
    df = depurar_salario(df)
    df = depurar_tamano_empresa(df)
    df = modalidad_tamano_empresa (df)
    df = locacion_modalidad(df)
    df = locacion_tamano_empresa_grande(df)
    df = locacion_tamano_empresa_mediana(df)
    df = locacion_tamano_empresa_pequena(df)
    df = tamano_modalidad(df)
    df = salario_tamano(df)
    df = salario_locacion(df)
    
    
    return df






