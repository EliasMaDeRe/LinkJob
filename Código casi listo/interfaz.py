# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:38:11 2022

@author: Carlos
"""

import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import plottearDatos as pld
import plottearTecnologias as pt
import main as mn

largo = 636
alto = 290
fondo = 'sandy brown'

mn.obtener_datos()


def mostrar_imagen ():
    imagen = Image.open('testplot.png')
    imagen = imagen.resize((largo,alto), Image.ANTIALIAS)

    img = ImageTk.PhotoImage(imagen)
    mostrarimagen = Label(ventana, image = img)
    mostrarimagen.config(bg = fondo)
    mostrarimagen.place(relx=1, rely=0.52, relwidth=1,anchor='ne')
    ventana.mainloop()
    
def mostrar_imagen_tec ():
    imagen = Image.open('tecno.png')
    imagen = imagen.resize((largo,alto), Image.ANTIALIAS)

    img = ImageTk.PhotoImage(imagen)
    mostrarimagen = Label(ventana, image = img)
    mostrarimagen.config(bg = fondo)
    mostrarimagen.place(relx=1, rely=0.1, relwidth=1,anchor='ne')
    ventana.mainloop()
    

def imagen_categorias(valor):
    
    filtro_general = clickgen.get()  
    filtro_esp =clickesp.get()
    
    #Filtros generales

    if filtro_general=='Salario' and (filtro_esp=='Ninguno' or filtro_esp=="Elige el filtro específico")  :
        SL = pd.read_csv("SL.csv")
        pld.plottear_salario(SL)
        mostrar_imagen()
            
    elif filtro_general=='Modalidad' and (filtro_esp=='Ninguno' or filtro_esp=="Elige el filtro específico")  :
        ML = pd.read_csv("ML.csv")
        pld.plottear_modalidad(ML)
        mostrar_imagen()
            
    elif filtro_general=='Tamaño de empresa' and (filtro_esp=='Ninguno' or filtro_esp=="Elige el filtro específico")  :
        TL = pd.read_csv("TL.csv")
        pld.plottear_tamano_empresa(TL)
        mostrar_imagen()
            
    elif filtro_general=='Locación' and (filtro_esp=='Ninguno' or filtro_esp=="Elige el filtro específico")  :
        LL = pd.read_csv("LL.csv")
        pld.plottear_locacion(LL)
        mostrar_imagen()
        
    #Filtros generales con específicos
        
    elif filtro_general=='Modalidad' and filtro_esp=='Empresa Grande'  :
        CMT = pd.read_csv("CMT.csv")
        pld.plottear_modalidad_EG(CMT)
        mostrar_imagen()
        
    elif filtro_general=='Modalidad' and filtro_esp=='Empresa Mediana'  :
        CMT = pd.read_csv("CMT.csv")
        pld.plottear_modalidad_EM(CMT)
        mostrar_imagen()
        
    elif filtro_general=='Modalidad' and filtro_esp=='Empresa Pequeña'  :
        CMT = pd.read_csv("CMT.csv")
        pld.plottear_modalidad_EP(CMT)
        mostrar_imagen()
        
    elif filtro_general=='Locación' and filtro_esp=='Presencial'  :
        CLM = pd.read_csv("CLM.csv")
        pld.plottear_locacion_Pres(CLM)
        mostrar_imagen()
            
    elif filtro_general=='Locación' and filtro_esp=='Virtual'  :
        CLM = pd.read_csv("CLM.csv")
        pld.plottear_locacion_Vir(CLM)
        mostrar_imagen()
        
    elif filtro_general=='Locación' and filtro_esp=='Empresa Grande'  :
        CLT = pd.read_csv("CLT.csv")
        pld.plottear_locacion_EG(CLT)
        mostrar_imagen()
            
    elif filtro_general=='Locación' and filtro_esp=='Empresa Mediana'  :
        CLTM = pd.read_csv("CLTM.csv")
        pld.plottear_locacion_EM(CLTM)
        mostrar_imagen()
            
    elif filtro_general=='Locación' and filtro_esp=='Empresa Pequeña'  :
        CLTP = pd.read_csv("CLTP.csv")
        pld.plottear_locacion_EP(CLTP)
        mostrar_imagen()

    elif filtro_general=='Tamaño de empresa' and filtro_esp=='Presencial'  :
        CTM = pd.read_csv("CTM.csv")
        pld.plottear_TE_pres(CTM)
        mostrar_imagen()

    elif filtro_general=='Tamaño de empresa' and filtro_esp=='Virtual'  :
        CTM = pd.read_csv("CTM.csv")
        pld.plottear_TE_pres(CTM)
        mostrar_imagen()  
    
    elif filtro_general=='Salario' and filtro_esp=='Empresa Grande'  :
        STM = pd.read_csv("STM.csv")
        pld.plottear_salario_eg(STM)
        mostrar_imagen()          

    elif filtro_general=='Salario' and filtro_esp=='Empresa Mediana'  :
        STM = pd.read_csv("STM.csv")
        pld.plottear_salario_em(STM)
        mostrar_imagen()    
        
    elif filtro_general=='Salario' and filtro_esp=='Empresa Pequeña'  :
        STM = pd.read_csv("STM.csv")
        pld.plottear_salario_ep(STM)
        mostrar_imagen()    
        
    elif filtro_general=='Salario' and filtro_esp=='Presencial'  :
        SALAMOD = pd.read_csv("SALAMOD.csv")
        pld.plottear_salario_presencial(SALAMOD)
        mostrar_imagen()    
        
    elif filtro_general=='Salario' and filtro_esp=='Virtual'  :
        SALAMOD = pd.read_csv("SALAMOD.csv")
        pld.plottear_salario_virtual(SALAMOD)
        mostrar_imagen()    
                
    ventana.mainloop()
    return None

#Creando la ventana en donde estará el programa
ventana = Tk()

ventana.title("Link Job")
ventana.geometry("800x400")
ventana.config(bg=fondo)

#Crear imagen del logo

logo = Image.open("Logo.png")
logo = logo.resize((1200,75), Image.ANTIALIAS)

log = ImageTk.PhotoImage(logo)
mostrarlogo = Label(ventana, image = log)
mostrarlogo.config(bg = fondo)
mostrarlogo.place(relx=1, rely=0, relwidth=1, anchor='ne')


#Las opciones que tendrá el dropdown general
opcionesgen=[ "Modalidad", "Salario", "Locación", "Tamaño de empresa"]

#Las opciones que tendrá el dropdown general
opcionesesp=[ "Ninguno", "Presencial", "Virtual", "Empresa Grande", "Empresa Mediana", "Empresa Pequeña" ]


#Creando los dropdowns

#Aquí se pone lo que va a aparecer primero en los botones
clickgen = StringVar()
clickgen.set( "Elige el filtro general" )
clickesp = StringVar()
clickesp.set( "Elige el filtro específico" )


#Aquí se crean, el OptionsMenu es para decir que es un menú de opciones, en los paréntesis primero aparece en donde está ubicado, la oración que tendra por default y las opciones que contendrá la lista y lo que hará con las opciones seleccionadas

dropdowngen = OptionMenu( ventana , clickgen, *opcionesgen, command = imagen_categorias)
dropdowngen.config(bg=fondo)
dropdowngen.place(relx=0.49, rely=0.95, relwidth=0.3,anchor='ne')

dropdownesp = OptionMenu( ventana , clickesp, *opcionesesp, command = imagen_categorias)
dropdownesp.config(bg=fondo)
dropdownesp.place(relx=0.79, rely=0.95, relwidth=0.3,anchor='ne')

#Mostrar imagen "estática" de tecnologías"
tec = pd.read_csv('LT.csv')
pld.plottear_tecnologias(tec)
mostrar_imagen_tec()
    
ventana.mainloop()


