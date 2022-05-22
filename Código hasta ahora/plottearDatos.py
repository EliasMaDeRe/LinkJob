6# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:39:19 2022

@author: EMadera
"""
import pandas as pd
import matplotlib.pyplot as plt
import plottearTecnologias as pt
import math as mt

#Plottear salario

def plottear_salario(df):
    
    dfDatos = pd.DataFrame(df['Salario Mensual'])
    dfDatos2 = dfDatos.groupby('Salario Mensual')['Salario Mensual'].count()
    tplot = dfDatos.groupby('Salario Mensual')['Salario Mensual'].count().plot(xlabel ="Salario mensual estimado",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por salario mensual estimado",legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()), xy=(dfDatos2.count()*.7,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
#Plottear modalidad

def plottear_modalidad(df):

    dfDatos = pd.DataFrame(df['Modalidad'])
    dfDatos2 = dfDatos.groupby('Modalidad')['Modalidad'].count()
    tplot = dfDatos.groupby('Modalidad')['Modalidad'].count().plot(xlabel ="Tipo de modalidad",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por modalidad de trabajo", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()), xy=(dfDatos2.count()*.5,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()

#Plottear tamaño de empresa

def plottear_tamano_empresa(df):

    dfDatos = pd.DataFrame(df['Tamaño Empresa'])
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count()
    tplot = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count().plot(xlabel ="Tamaño de empresa",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por tamaño de la empresa", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos['Tamaño Empresa'].count()), xy=(dfDatos2.count()*.5,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
def plottear_locacion(df):
    
    dfDatos = pd.DataFrame(df['Locacion'])
    dfDatos2 = dfDatos.groupby('Locacion')['Locacion'].count()
    tplot = dfDatos.groupby('Locacion')['Locacion'].count().plot(xlabel ="Locacion",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por locacion en México del trabajo", width =.6,legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()), xy=(dfDatos2.count()*.7,dfDatos2.max()*.8), ha='center', va='bottom')
    tplot.set_yscale('log')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
    
def plottear_tecnologias(df):
    df = pd.read_csv('LT.csv')
    df[['Tecnologia']].plot(kind='bar',color="darkorange,",title = "Frecuencia de aparicion de las tecnologias en las ofertas de trabajo")
    plt.savefig('tecnologias.png',dpi=300,bbox_inches='tight')
    plt.close()
    
    
#Estas las hace Joachin
'''
def plottear_modalidad_EG(df):
    
    
    dfDatos = pd.DataFrame(df['Presencial Grande'])
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count()
    tplot = dfDatos.plot(xlabel ="Empresas grandes con modalidad presencial",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por modalidad presencial", width =.2,legend=False)
    #tplot.annotate('Total de ofertas: '+str(dfDatos['Tamaño Empresa'].count()), xy=(dfDatos2.count()*.5,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
def plottear_modalidad_EM(df):
    
    
    dfDatos = pd.DataFrame(df['Presencial Grande'])
    dfDatos.plot(kind= 'bar', x='Presencial Grande', y= 0)
    #dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count()
    #tplot = dfDatos.plot(xlabel ="Empresas grandes con modalidad presencial",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por modalidad presencial", width =.2,legend=False)
    #tplot.annotate('Total de ofertas: '+str(dfDatos['Tamaño Empresa'].count()), xy=(dfDatos2.count()*.5,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in dfDatos.patches:
        dfDatos.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
def plottear_modalidad_EP(df):
    
    
    dfDatos = pd.DataFrame(df['Presencial Grande'])
    dfDatos.plot(kind= 'bar', x='Presencial Grande', y= 0)
    #dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count()
    #tplot = dfDatos.plot(xlabel ="Empresas grandes con modalidad presencial",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por modalidad presencial", width =.2,legend=False)
    #tplot.annotate('Total de ofertas: '+str(dfDatos['Tamaño Empresa'].count()), xy=(dfDatos2.count()*.5,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in dfDatos.patches:
        dfDatos.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
'''
    
    #Estas las debe estar haciendo vale
'''
def plottear_modalidad_EG(df):
    
    
    dfDatos = pd.DataFrame(df['Presencial Grande'])
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count()
    tplot = dfDatos.plot(xlabel ="Empresas grandes con modalidad presencial",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por modalidad presencial", width =.2,legend=False)
    #tplot.annotate('Total de ofertas: '+str(dfDatos['Tamaño Empresa'].count()), xy=(dfDatos2.count()*.5,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
   

def plottear_locacion_EM(df):
    dfDatos = pd.DataFrame(df['Locacion', 'Modalidad'])
    dfDatos2 = dfDatos.groupby('Locación')['Modalidad'].count()
    tplot = dfDatos.groupby('Locación')['Modalidad'].count().plot(xlabel ="Locación por modalidad",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por locación y modalidad", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()), xy=(dfDatos2.count()*.7,dfDatos2.max()*.8), ha='center', va='bottom')
    tplot.set_yscale('log')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
def plottear_locacion_EP(df):
    dfDatos = pd.DataFrame(df['Locacion', 'Modalidad'])
    dfDatos2 = dfDatos.groupby('Locación')['Modalidad'].count()
    tplot = dfDatos.groupby('Locación')['Modalidad'].count().plot(xlabel ="Locación por modalidad",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por locación y modalidad", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()), xy=(dfDatos2.count()*.7,dfDatos2.max()*.8), ha='center', va='bottom')
    tplot.set_yscale('log')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
def plottear_locacion_Pres(df):
    dfDatos = pd.DataFrame(df['Locacion', 'Modalidad'])
    dfDatos2 = dfDatos.groupby('Locación')['Modalidad'].count()
    tplot = dfDatos.groupby('Locación')['Modalidad'].count().plot(xlabel ="Locación por modalidad",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por locación y modalidad", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()), xy=(dfDatos2.count()*.7,dfDatos2.max()*.8), ha='center', va='bottom')
    tplot.set_yscale('log')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
def plottear_locacion_Vir(df):
    dfDatos = pd.DataFrame(df['Locacion', 'Modalidad'])
    dfDatos2 = dfDatos.groupby('Locación')['Modalidad'].count()
    tplot = dfDatos.groupby('Locación')['Modalidad'].count().plot(xlabel ="Locación por modalidad",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por locación y modalidad", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()), xy=(dfDatos2.count()*.7,dfDatos2.max()*.8), ha='center', va='bottom')
    tplot.set_yscale('log')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
'''
#Estas las debe estar haciendo Leo    
'''
def plottear_TE_vir(df):
    
    
    dfDatos = pd.DataFrame(df['Presencial Grande'])
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count()
    tplot = dfDatos.plot(xlabel ="Empresas grandes con modalidad presencial",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por modalidad presencial", width =.2,legend=False)
    #tplot.annotate('Total de ofertas: '+str(dfDatos['Tamaño Empresa'].count()), xy=(dfDatos2.count()*.5,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()


def plottear_TE_pres(df):
    
    
    dfDatos = pd.DataFrame(df['Presencial Grande'])
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count()
    tplot = dfDatos.plot(xlabel ="Empresas grandes con modalidad presencial",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por modalidad presencial", width =.2,legend=False)
    #tplot.annotate('Total de ofertas: '+str(dfDatos['Tamaño Empresa'].count()), xy=(dfDatos2.count()*.5,dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
'''
 
    
#Estas son de nosotros 
    
def plottear_salario_locacion(df):
    
    dfDatos = df
    dfDatos2 = dfDatos.groupby('Locacion')['Salario Mensual'].sum()
    dfDatos2.columns= ['Locacion','Suma']
    dfDatos3 = dfDatos.groupby('Locacion')['Salario Mensual'].count()
    dfDatos2.columns= ['Locacion','Cantidd']

    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4['Promedio'] = df4['Suma']/ df4['Cantidad']
    dfsalario_locacion = pd.DataFrame(df4['Promedio'])
    tplot = dfsalario_locacion.plot(xlabel ="Locación",ylabel="Salario en pesos",color = "darkorange", kind='bar', title = "Salario promedio por locación en México", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos3.sum()), xy=(dfDatos3.count()*.75,dfDatos3.max()*0), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
    
    '''
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
    
    df4.to_csv('df4.csv', index=False)
    '''
    print(dfDatos2)
    print(dfDatos3)
    print(df4)
    
    
def plottear_salario_eg (df):
    
    dfDatos = df
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].sum()
    dfDatos2.columns= ['Tamaño Empresa','Suma']
    dfDatos3 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].count()
    dfDatos2.columns= ['Tamaño Empresa','Cantidd']
    

    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4['Promedio'] = df4['Suma']/ df4['Cantidad']
    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    dfsalario_grande= dfsalario_grande_ambos.drop(['Pequeña'])
    tplot = dfsalario_grande.plot(xlabel ="Tamaño",ylabel="Salario en pesos",color = "darkorange", kind='bar', title = "Salario promedio por empresas grandes en México", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad']), xy=(dfDatos3.count()*.75,dfDatos3.max()*0), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
    
    '''
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
    
    df4.to_csv('df4.csv', index=False)
    
    '''
    print(dfDatos2)
    print(dfDatos3)
    print(df4)
    
    
def plottear_salario_em (df):
    
    dfDatos = df
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].sum()
    dfDatos2.columns= ['Tamaño Empresa','Suma']
    dfDatos3 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].count()
    dfDatos2.columns= ['Tamaño Empresa','Cantidd']
    

    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4['Promedio'] = df4['Suma']/ df4['Cantidad']
    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    dfsalario_grande= dfsalario_grande_ambos.drop(['Mediana'])
    tplot = dfsalario_grande.plot(xlabel ="Tamaño",ylabel="Salario en pesos",color = "darkorange", kind='bar', title = "Salario promedio por empresas medianas en México", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad']), xy=(dfDatos3.count()*.75,dfDatos3.max()*0), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
    
    print(dfDatos2)
    print(dfDatos3)
    print(df4)
    
def plottear_salario_ep (df):
    
    dfDatos = df
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].sum()
    dfDatos2.columns= ['Tamaño Empresa','Suma']
    dfDatos3 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].count()
    dfDatos2.columns= ['Tamaño Empresa','Cantidd']
    

    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4['Promedio'] = df4['Suma']/ df4['Cantidad']
    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    dfsalario_grande= dfsalario_grande_ambos.drop(['Grande'])
    tplot = dfsalario_grande.plot(xlabel ="Tamaño",ylabel="Salario en pesos",color = "darkorange", kind='bar', title = "Salario promedio por empresas pequeñas en México", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad']), xy=(dfDatos3.count()*.75,dfDatos3.max()*0), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
    '''
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
    
    df4.to_csv('df4.csv', index=False)
    
    '''
    print(dfDatos2)
    print(dfDatos3)
    print(df4)
    
def plottear_salario_presencial(df):
    
    dfDatos = df
    dfDatos2 = dfDatos.groupby('Modalidad')['Salario Mensual'].sum()
    dfDatos2.columns= ['Modalidad','Suma']
    dfDatos3 = dfDatos.groupby('Modalidad')['Salario Mensual'].count()
    dfDatos2.columns= ['Modalidad','Cantidd']
    
    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4['Promedio'] = df4['Suma']/ df4['Cantidad']
    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    dfsalario_grande= dfsalario_grande_ambos.drop(['Virtual'])
    tplot = dfsalario_grande.plot(xlabel ="Modalidad",ylabel="Salario en pesos",color = "darkorange", kind='bar', title = "Salario promedio por modalidad presencial en México", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad']), xy=(dfDatos3.count()*.75,dfDatos3.max()*0), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
    '''
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
    
    df4.to_csv('df4.csv', index=False)
    
    '''
    print(dfDatos2)
    print(dfDatos3)
    print(df4)
    
def plottear_salario_virtual(df):
    
    dfDatos = df
    dfDatos2 = dfDatos.groupby('Modalidad')['Salario Mensual'].sum()
    dfDatos2.columns= ['Modalidad','Suma']
    dfDatos3 = dfDatos.groupby('Modalidad')['Salario Mensual'].count()
    dfDatos2.columns= ['Modalidad','Cantidd']
    
    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4 = pd.DataFrame()
    df4= pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns= ['Suma', 'Cantidad']
    
    df4['Promedio'] = df4['Suma']/ df4['Cantidad']
    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    dfsalario_grande= dfsalario_grande_ambos.drop(['Presencial'])
    tplot = dfsalario_grande.plot(xlabel ="Modalidad",ylabel="Salario en pesos",color = "darkorange", kind='bar', title = "Salario promedio por modalidad virtual en México", width =.2,legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad']), xy=(dfDatos3.count()*.75,dfDatos3.max()*0), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
    '''
    plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    plt.close()
    
    
    df4.to_csv('df4.csv', index=False)
    
    '''
    print(dfDatos2)
    print(dfDatos3)
    print(df4)
    
    
    
