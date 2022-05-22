# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:38:11 2022

@author: Carlos
"""

import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import main as mn
#import plottearTecnologias as pt

largo = 636
alto = 290

mn.obtener_datos()


def mostrar_imagen ():
    imagen = Image.open('testplot.png')
    imagen = imagen.resize((largo,alto), Image.ANTIALIAS)

    img = ImageTk.PhotoImage(imagen)
    mostrarimagen = Label(ventana, image = img)
    mostrarimagen.config(bg = "ghost white")
    mostrarimagen.place(relx=1, rely=0.52, relwidth=1,anchor='ne')
    ventana.mainloop()
    

def imagen_categorias(valor):
    
    filtro_general = clickgen.get()  
    filtro_esp =clickesp.get()
   # print (general)
    if filtro_general=='Salario' and (filtro_esp=='Ninguno' or filtro_esp=="Elige el filtro específico")  :
        print(filtro_general)
        SL = pd.read_csv("SL.csv")
        mn.pld.plottear_salario(SL)
        mostrar_imagen()
            
    elif filtro_general=='Modalidad' and (filtro_esp=='Ninguno' or filtro_esp=="Elige el filtro específico")  :
        print(filtro_general)
        ML = pd.read_csv("ML.csv")
        mn.pld.plottear_modalidad(ML)
        mostrar_imagen()
            
    elif filtro_general=='Tamaño de empresa' and (filtro_esp=='Ninguno' or filtro_esp=="Elige el filtro específico")  :
        print(filtro_general)
        TL = pd.read_csv("TL.csv")
        mn.pld.plottear_tamano_empresa(TL)
        mostrar_imagen()
            
    elif filtro_general=='Locación' and (filtro_esp=='Ninguno' or filtro_esp=="Elige el filtro específico")  :
        print(filtro_general)
        LL = pd.read_csv("LL.csv")
        mn.pld.plottear_locacion(LL)
        mostrar_imagen()
        
        
    elif filtro_general=='Modalidad' and filtro_esp=='Empresa Grande'  :
        print(filtro_general)
        MT = pd.read_csv("MT.csv")
        mn.pld.plottear_modalidad_EG(MT)
        mostrar_imagen()
        
    elif filtro_general=='Modalidad' and filtro_esp=='Empresa Mediana'  :
        print(filtro_general)
        MT = pd.read_csv("MT.csv")
        mn.pld.plottear_modalidad_EG(MT)
        mostrar_imagen()
        
    elif filtro_general=='Modalidad' and filtro_esp=='Empresa Pequeña'  :
        print(filtro_general)
        MT = pd.read_csv("MT.csv")
        mn.pld.plottear_modalidad_EG(MT)
        mostrar_imagen()
        
    elif filtro_general=='Locación' and filtro_esp=='Presencial'  :
        print(filtro_general)
        CLM = pd.read_csv("CLM.csv")
        mn.pld.plottear_modalidad_EG(CLM)
        mostrar_imagen()
            
    elif filtro_general=='Locación' and filtro_esp=='Virtual'  :
        print(filtro_general)
        CLM = pd.read_csv("CLM.csv")
        mn.pld.plottear_modalidad_EG(CLM)
        mostrar_imagen()
        
    elif filtro_general=='Locación' and filtro_esp=='Empresa Grande'  :
        print(filtro_general)
        CLM = pd.read_csv("CLM.csv")
        mn.pld.plottear_modalidad_EG(CLM)
        mostrar_imagen()
            
    elif filtro_general=='Locación' and filtro_esp=='Empresa Mediana'  :
        print(filtro_general)
        CLM = pd.read_csv("CLM.csv")
        mn.pld.plottear_modalidad_EG(CLM)
        mostrar_imagen()
            
    elif filtro_general=='Locación' and filtro_esp=='Empresa Pequeña'  :
        print(filtro_general)
        CLM = pd.read_csv("CLM.csv")
        mn.pld.plottear_modalidad_EG(CLM)
        mostrar_imagen()

    elif filtro_general=='Tamaño de empresa' and filtro_esp=='Presencial'  :
        print(filtro_general)
        CLM = pd.read_csv("CLM.csv")
        mn.pld.plottear_modalidad_EG(CLM)
        mostrar_imagen()

    elif filtro_general=='Tamaño de empresa' and filtro_esp=='Virtual'  :
        print(filtro_general)
        CLM = pd.read_csv("CLM.csv")
        mn.pld.plottear_modalidad_EG(CLM)
        mostrar_imagen()           
                
    ventana.mainloop()
    return None

'''
def imagen_categorias_esp(especifico):
    
    filtro_general = clickgen.get()    
    if filtro_general == "Modalidad" and especifico == "Virtual":
            genesp = Image.open("UVT.png")
            genesp = genesp.resize((largo,alto), Image.ANTIALIAS)
            
            
            
            
            
            
            
            
            
            
            
            

            genespes = ImageTk.PhotoImage(genesp)
            mostrargenesp = Label(ventana, image = genespes)
            mostrargenesp.config(bg = "ghost white")
            mostrargenesp.place(relx=1, rely=0.52, relwidth=1,anchor='ne')
            
    else :
        print("hola_especifico")
        print (filtro_general)
        print (especifico)
            
    ventana.mainloop()
    return None
    '''


#Guardando lo que tenía

'''          
    if filtro_general == "Modalidad" and filtro_esp== "Empresa Grande":
            genesp = Image.open("Mockup de la gráfica de barras sobre los filtros generales y específicos.png")
            genesp = genesp.resize((largo,alto), Image.ANTIALIAS)

            genespes = ImageTk.PhotoImage(genesp)
            mostrargenesp = Label(ventana, image = genespes)
            mostrargenesp.config(bg = "ghost white")
            mostrargenesp.place(relx=1, rely=0.52, relwidth=1,anchor='ne')
            
    else :
        print("hola_general")
    
    ventana.mainloop()
    return None

def imagen_categorias_esp(especifico):
    
    filtro_general = clickgen.get()    
    if filtro_general == "Modalidad" and especifico == "Virtual":
            genesp = Image.open("UVT.png")
            genesp = genesp.resize((largo,alto), Image.ANTIALIAS)

            genespes = ImageTk.PhotoImage(genesp)
            mostrargenesp = Label(ventana, image = genespes)
            mostrargenesp.config(bg = "ghost white")
            mostrargenesp.place(relx=1, rely=0.52, relwidth=1,anchor='ne')
            
    else :
        print("hola_especifico")
        print (filtro_general)
        print (especifico)
            
    ventana.mainloop()
    return None
    
'''
#Creando la ventana en donde estará el programa
ventana = Tk()

ventana.title("Link Job")
ventana.geometry("800x400")
ventana.config(bg="ghost white")

#Crear imagen del logo

logo = Image.open("Logo.png")
logo = logo.resize((1200,75), Image.ANTIALIAS)

log = ImageTk.PhotoImage(logo)
mostrarlogo = Label(ventana, image = log)
mostrarlogo.config(bg = "sandy brown")
mostrarlogo.place(relx=1, rely=0, relwidth=1, anchor='ne')

#Definir imagenes de gráficas
'''
pt.obtener_tecnologias()
dft = pd.read_csv("LT.csv")
mn.pld.plottear_tecnologias(dft)
tecnologias = Image.open("tecnologias.png")
tecnologias = tecnologias.resize((largo,alto), Image.ANTIALIAS)

tec = ImageTk.PhotoImage(tecnologias)
mostrartec = Label(ventana, image = tec)
mostrartec.config(bg = "ghost white")
mostrartec.place(relx=1, rely=0.1, relwidth=1,anchor='ne')
'''

#Las opciones que tendrá el dropdown general
opcionesgen=[ "Modalidad", "Salario", "Locación", "Tamaño de empresa"]

#Las opciones que tendrá el dropdown general
opcionesesp=[ "Ninguno", "Presencial", "Virtual", "Locación", "Empresa Grande", "Empresa Mediana", "Empresa Pequeña" ]


#Creando los dropdowns

#Aquí se pone lo que va a aparecer primero en los botones
clickgen = StringVar()
clickgen.set( "Elige el filtro general" )
clickesp = StringVar()
clickesp.set( "Elige el filtro específico" )


#Aquí se crean, el OptionsMenu es para decir que es un menú de opciones, en los paréntesis primero aparece en donde está ubicado, la oración que tendra por default y las opciones que contendrá la lista y lo que hará con las opciones seleccionadas
dropdowngen = OptionMenu( ventana , clickgen, *opcionesgen, command = imagen_categorias)
dropdowngen.config(bg="sandy brown")
dropdowngen.place(relx=0.49, rely=0.95, relwidth=0.3,anchor='ne')

dropdownesp = OptionMenu( ventana , clickesp, *opcionesesp, command = imagen_categorias)
dropdownesp.config(bg="sandy brown")
dropdownesp.place(relx=0.79, rely=0.95, relwidth=0.3,anchor='ne')


#Probando los dropdowns
'''
def print_answers():
    print("General {}".format(clickgen.get()))
    print("Específico {}".format(clickesp.get()))
    return None
  
  
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = Button(ventana, text='Submit', command=print_answers)
submit_button.pack(side="bottom")
'''

    
ventana.mainloop()


