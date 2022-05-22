6# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:39:19 2022

@author: EMadera
"""
import pandas as pd
import matplotlib.pyplot as plt
import plottearTecnologias as pt

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
    
    '''
def plottear_tecnologias(df):
    df = pd.read_csv('LT.csv')
    df[['Tecnologia']].plot(kind='bar',color="darkorange,",title = "Frecuencia de aparicion de las tecnologias en las ofertas de trabajo")
    plt.savefig('tecnologias.png',dpi=300,bbox_inches='tight')
    plt.close()
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
def plottear_salario_locacion(df):
    
    dfDatos = df
    dfDatos2 = dfDatos.groupby('Locacion')['Salario Mensual'].sum()
    dfDatos3 = dfDatos.groupby('Locacion')['Salario Mensual'].count()
    
    dfPromedio=pd.Series()
    
    
    for i in range dfDatos2.shape[0] :
        
        a = dfDatos2[0].loc[i] / dfDatos3[0].loc[i]
        dfPromedio[0].loc[i] = a
        print(a)
            
            #dpPromedio = [dfDatos2[0].loc[i]/dfDatos3[0].loc[i]]
        
        
    
    print(dfDatos2)
    print(dfDatos3)
    '''
    
    #tplot = dfDatos.groupby('Salario Mensual')['Salario Mensual'].count().plot(xlabel ="Salario mensual estimado",ylabel="Cantidad de ofertas",color = "darkorange", kind='bar', title = "Cantidad de ofertas por salario mensual estimado",legend=False)
    #tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()), xy=(dfDatos2.count()*.7,dfDatos2.max()*.8), ha='center', va='bottom')
    #for p in tplot.patches:
        #tplot.annotate(str(p.get_height()),xy=((p.get_x()),p.get_height()),ha='left',va='bottom')
        
    #plt.savefig('testplot.png',dpi=300,bbox_inches='tight')
    