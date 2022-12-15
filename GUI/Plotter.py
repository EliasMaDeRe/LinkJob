import pandas as pd
from Diccionario import Diccionario
import seaborn as sns
from ColeccionGraficas import ColeccionGraficas

class Plotter:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def plotOfertas(ListaOfertas, ListaRoles, ListaTecno, ListaSoftskills):
        
        archivador = ColeccionGraficas()
        for rol in ListaRoles:
            archivador.imagenes[rol.obtenerNombre()] = 0
        archivador.imagenes["Todos"] = 0
        archivador.crearDir()
        
        # Obtener Dataframe con datos relevantes de la lista de ofertas

        OfertasDf = pd.DataFrame({'Salario':[],'TamanoEmpresa':[],'Ubicacion':[],'Modalidad':[],'Rol':[]})
        for oferta in ListaOfertas:

            OfertaDf = pd.DataFrame({'Salario':[oferta.obtenerSalario()],'TamanoEmpresa':[oferta.obtenerTamanoEmpresa()],
            'Ubicacion':[oferta.obtenerUbicacion()],'Modalidad':[oferta.obtenerModalidad()],'Rol':[oferta.obtenerRol()]})
            OfertasDf = pd.concat([OfertasDf, OfertaDf],ignore_index=True)

        # OfertasDf es el dataframe final

        for rol in ListaRoles:
            imagenLocacion = Plotter.plotLocacion(OfertasDf,rol.obtenerNombre())
            archivador.guardado(rol.obtenerNombre(),"Locacion", imagenLocacion)
            
            imagenSalarioTamano = Plotter.plotSalarioTamano(OfertasDf,rol.obtenerNombre())
            archivador.guardado(rol.obtenerNombre(),"SalarioTamano", imagenSalarioTamano)
            
            imagenSalario = Plotter.plotSalario(OfertasDf,rol.obtenerNombre())
            archivador.guardado(rol.obtenerNombre(),"Salario", imagenSalario)
            
            imagenModalidadTamano =  Plotter.plotModalidadTamano(OfertasDf,rol.obtenerNombre())
            archivador.guardado(rol.obtenerNombre(),"ModalidadTamano", imagenModalidadTamano)
            
            imagenModalidad = Plotter.plotModalidad(OfertasDf,rol.obtenerNombre())
            archivador.guardado(rol.obtenerNombre(),"Modalidad", imagenModalidad)
            
            imagenTamano =  Plotter.plotTamano(OfertasDf,rol.obtenerNombre())
            archivador.guardado(rol.obtenerNombre(),"Tamano", imagenTamano)
            
            imagenSalarioModalidad = Plotter.plotSalarioModalidad(OfertasDf,rol.obtenerNombre())
            archivador.guardado(rol.obtenerNombre(),"SalarioModalidad", imagenSalarioModalidad)

        imagenLocacion = Plotter.plotLocacion(OfertasDf,"Todos")
        archivador.guardado("Todos","Locacion", imagenLocacion)
        
        imagenSalarioTamano = Plotter.plotSalarioTamano(OfertasDf,"Todos")
        archivador.guardado("Todos","SalarioTamano", imagenSalarioTamano)
        
        imagenSalario = Plotter.plotSalario(OfertasDf,"Todos")
        archivador.guardado("Todos","Salario", imagenSalario)
        
        imagenModalidadTamano =  Plotter.plotModalidadTamano(OfertasDf,"Todos")
        archivador.guardado("Todos","ModalidadTamano", imagenModalidadTamano)
        
        imagenModalidad = Plotter.plotModalidad(OfertasDf,"Todos")
        archivador.guardado("Todos","Modalidad", imagenModalidad)
        
        imagenTamano = Plotter.plotTamano(OfertasDf,"Todos")
        archivador.guardado("Todos","Tamano", imagenTamano)
        
        imagenSalarioModalidad = Plotter.plotSalarioModalidad(OfertasDf,"Todos")
        archivador.guardado("Todos","SalarioModalidad", imagenSalarioModalidad)
        
        imagenTecnologiasSolicitadas = Plotter.plotTecnologiasSolicitadas(ListaTecno)
        archivador.guardado("Todos","TecnologiasSolicitadas", imagenTecnologiasSolicitadas)
        
        imagenCantidadSoftskills = Plotter.plotCantidadSoftskills(ListaSoftskills, ListaOfertas)
        archivador.guardado("Todos","CantidadSoftskills", imagenCantidadSoftskills)
        

    
    def plotLocacion(OfertasDf,rol):
        TempDf = OfertasDf
        
        TempDf = TempDf[(TempDf['Ubicacion'] != "-1")]
        
        if(rol != "Todos"):
            TempDf = TempDf[(TempDf['Rol'] == rol)]

        if(TempDf.empty == False):
            sns.set_theme(style="whitegrid")
            grafica = sns.countplot(y = "Ubicacion", data = TempDf, width = 0.35, alpha = 0.6, hatch = "/", palette = "Wistia")
            grafica.set_title("Cantidad de ofertas por locación del rol: " + rol, fontsize = 17, weight = "bold")
            grafica.set_xlabel("Cantidad", fontsize = 17, weight = "bold")
            grafica.set_ylabel("Ubicación", fontsize = 17, weight = "bold")
            imagen = grafica.get_figure()
            return imagen
        
        return 0

    def plotTecnologiasSolicitadas(listaTecnologias):    
        dfPloteo = pd.DataFrame(columns = ['Tecnologia', 'Frecuencia'])
        
        listaTecno = []
        
        for tecnologia in listaTecnologias:
            listaTecno.append([tecnologia.obtenerFrecuencia(),tecnologia.obtenerNombre()])
        
        listaTecno.sort()
        listaTecno = listaTecno[-10:]
        
        for tecnologia in listaTecno:
            dfPloteo = dfPloteo.append({'Tecnologia': tecnologia[1], 'Frecuencia':tecnologia[0]}, ignore_index=True )

        if(dfPloteo.empty == False):
            sns.set_theme(style="whitegrid")
            grafica = sns.barplot(data = dfPloteo,x="Frecuencia", y = 'Tecnologia', width = 0.35, alpha = 0.6, hatch = "/", palette = "Wistia")
            grafica.set_title("Top 10 tecnologías más solicitadas", fontsize = 17, weight = "bold")
            grafica.set_xlabel("Frecuencia", fontsize = 17, weight = "bold")
            grafica.set_ylabel("Tecnologia", fontsize = 17, weight = "bold")
            imagen = grafica.get_figure()
            return imagen

        return 0
    
    def plotCantidadSoftskills(listaSoftskills, listaOfertas):
        sum = 0
        for softskills in listaSoftskills:
            sum += softskills.obtenerFrecuencia()
        
        promd = sum / len(listaOfertas)
        
        dfCantSoftskills = pd.DataFrame()
        dfCantSoftskills["Softskills"] = ["Softskills"]
        dfCantSoftskills["Frecuencia"] = [round(promd)]
        
        sns.set_theme(style="whitegrid")
        grafica = sns.barplot(data = dfCantSoftskills, x = "Softskills", y = "Frecuencia", width = 0.35, alpha = 0.6, hatch = "/", hue = "Frecuencia", palette = ["darkorange"])

        grafica.set_title("Promedio de softskills por Oferta", fontsize = 17, weight = "bold")
        grafica.set_xlabel("Softskills", fontsize = 17, weight = "bold")
        grafica.set_ylabel("Frecuencia", fontsize = 17, weight = "bold")
        imagen = grafica.get_figure()
        return imagen

    def plotSalario(OfertasDf, rol):
        OfertasDf =  OfertasDf[( OfertasDf['Salario'] != -1)]
        if rol != "Todos":
            OfertasDf = OfertasDf[OfertasDf['Rol'] == rol]
  
              
        if(OfertasDf.empty == False):
            dfMean = pd.DataFrame()
            dfMean["salario"] = [round(OfertasDf.describe().loc["mean","Salario"])]
            dfMean["rol"] = [rol]
                
            sns.set_theme(style="whitegrid")
            grafica = sns.barplot(data = dfMean, x = "rol", y = "salario", width = 0.35, alpha = 0.6, hatch = "/", hue = "salario", palette = ["darkorange"])

            grafica.set_title("Salario mensual promedio del rol: " + rol, fontsize = 17, weight = "bold")
            grafica.set_xlabel("Ingeniero de software", fontsize = 17, weight = "bold")
            grafica.set_ylabel("Salario mensual", fontsize = 17, weight = "bold")
            imagen = grafica.get_figure()
            return imagen
        
        return 0
            
    def plotSalarioModalidad (dataFrame,rol):

        dataFrame =  dataFrame[( dataFrame['Salario'] != -1)]
        dataFrame = dataFrame[(dataFrame['Modalidad'] != -1)]
        

        if(dataFrame.empty == False):

            if(rol != "Todos"):
                dataFrame = dataFrame[(dataFrame['Rol'] == rol)]

            if(dataFrame.empty == False):

                dfDatos2 = dataFrame.groupby('Modalidad')['Salario'].sum()

                dfDatos2.columns = ['Modalidad', 'Suma']
                dfDatos3 = dataFrame.groupby('Modalidad')['Salario'].count()
                dfDatos3.columns = ['Modalidad', 'Cantidad']

                df4 = pd.DataFrame()
                df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
                df4.columns = ['Suma', 'Cantidad']

                df4['Salario'] = df4['Suma'] / df4['Cantidad']

                salarioint = df4['Salario'].apply(lambda x: int(x))
                df4['Salario'] = salarioint

                df4.reset_index(inplace=True, drop=False)
                
                if rol == "Todos":
                    grosor = 0.5
                    color = "Wistia"
                else:
                    grosor = 0.35
                    color = ["darkorange"]
                
                sns.set_theme(style="whitegrid")  
                grafica = sns.barplot(data = df4,x="Modalidad", y = 'Salario', hue = "Salario", width = grosor, alpha = 0.6, hatch = "/" ,palette = color)
                grafica.set_title("Salario por modalidad en el rol: " + rol, fontsize = 17, weight = "bold")
                grafica.set_xlabel("Modalidad", fontsize = 17, weight = "bold")
                grafica.set_ylabel("Salario", fontsize = 17, weight = "bold")

                imagen = grafica.get_figure()
                return imagen

        return 0

    def plotTamano(OfertasDf, rol):
        TempDf = OfertasDf
        TempDf = TempDf[(TempDf['TamanoEmpresa'] != -1)]
        TempDf = TempDf[(TempDf['TamanoEmpresa'] != "-1")]

        if rol != "Todos":
            TempDf = TempDf[TempDf['Rol'] == rol]
        
        if(TempDf.empty == False):

            sns.set_theme(style="whitegrid")
            g = sns.countplot(data = TempDf, x = "TamanoEmpresa", width = 0.35, alpha = 0.6, hatch = "/", palette = "Wistia")
            g.set_title("Cantidad de ofertas por tamaño de empresa del rol: " + rol, fontsize = 17, weight = "bold")
            g.set_xlabel("Tamaño de empresa", fontsize = 17, weight = "bold")
            g.set_ylabel("Cantidad", fontsize = 17, weight = "bold")
            imagen = g.get_figure()
            return imagen
                        
                        
        return 0
            

    def plotModalidad(OfertasDf, rol):
        dataFrame = OfertasDf
        dataFrame = dataFrame[(dataFrame['Modalidad'] != -1)]
        if(rol != "Todos"):
            dataFrame = dataFrame[(dataFrame['Rol'] == rol)]
            
        if(dataFrame.empty == False):
            if "Virtual" in dataFrame.values:
                if "Presencial" in dataFrame.values:
                    dfModalidad = dataFrame.groupby('Modalidad')['Modalidad'].count()
                    df2 = pd.DataFrame()
                    df2["Modalidad"] = ["Presencial", "Virtual"]
                    df2["Cantidad"] = [dfModalidad.loc["Presencial"], dfModalidad.loc["Virtual"]]
                else:
                    dfModalidad = dataFrame.groupby('Modalidad')['Modalidad'].count()
                    df2 = pd.DataFrame()
                    df2["Modalidad"] = ["Presencial", "Virtual"]
                    df2["Cantidad"] = [0, dfModalidad.loc["Virtual"]]
            else:
                if "Presencial" in dataFrame.values:
                        dfModalidad = dataFrame.groupby('Modalidad')['Modalidad'].count()
                        df2 = pd.DataFrame()
                        df2["Modalidad"] = ["Presencial", "Virtual"]
                        df2["Cantidad"] = [dfModalidad.loc["Presencial"], 0]
            
            sns.set_theme(style="whitegrid")
            grafica = sns.barplot(data = df2, x="Modalidad", y="Cantidad", width = 0.35, alpha = 0.6, hatch = "/", palette = "Wistia")
            grafica.set_title("Cantidad de ofertas por Modalidad del rol: " + rol, fontsize = 17, weight = "bold")
            grafica.set_xlabel("Modalidad", fontsize = 17, weight = "bold")
            grafica.set_ylabel("Cantidad", fontsize = 17, weight = "bold")
            imagen = grafica.get_figure()
            return imagen

        return 0
        
    def plotModalidadTamano(OfertasDf,rol):
        TempDf = OfertasDf
        if (rol != "Todos"):
            TempDf = TempDf[TempDf['Rol'] == rol]
            
        TempDf = TempDf[(TempDf['Modalidad'] != -1)]
        TempDf = TempDf[(TempDf['Modalidad'] != "-1")]
        TempDf =  TempDf[(TempDf['TamanoEmpresa'] != -1)]
        TempDf =  TempDf[(TempDf['TamanoEmpresa'] != "-1")]


        if(TempDf.empty == False):
    
            sns.set_theme(style="whitegrid")
            grafica = sns.countplot(data=TempDf, x="TamanoEmpresa", hue="Modalidad", width = 0.35, alpha = 0.6, hatch = "/", palette = "Wistia")
            grafica.set_title("Cantidad de ofertas por Tamaño de empresa por Modalidad del rol: " + rol, fontsize = 17, weight = "bold")
            grafica.set_xlabel("Tamaño de empresa por Modalidad", fontsize = 17, weight = "bold")
            grafica.set_ylabel("Cantidad", fontsize = 17, weight = "bold")
            imagen = grafica.get_figure()
            return imagen

        return 0

    def plotSalarioTamano (dataFrame, rol):

        if(rol != "Todos"):
            dataFrame = dataFrame[(dataFrame['Rol'] == rol)]

        dataFrame = dataFrame[(dataFrame['Salario'] != -1)]
        dataFrame = dataFrame[(dataFrame['Salario'] != "-1")]
        dataFrame = dataFrame[(dataFrame['TamanoEmpresa'] != -1)]
        dataFrame = dataFrame[(dataFrame['TamanoEmpresa'] != "-1")]


        if(dataFrame.empty == False):

            dfTamSal = dataFrame.groupby('TamanoEmpresa')['Salario'].sum()

            dfTamSal.columns = ['Tamano de Empresa', 'Suma']
            dfTamSal2 = dataFrame.groupby('TamanoEmpresa')['Salario'].count()
            dfTamSal2.columns = ['Tamano de Empresa', 'Cantidad']

            dfTamSal3 = pd.DataFrame()
            dfTamSal3 = pd.concat([dfTamSal, dfTamSal2], axis=1)
            dfTamSal3.columns = ['Suma', 'Cantidad']

            dfTamSal3['Salario'] = dfTamSal3['Suma'] / dfTamSal3['Cantidad']

            salarioint = dfTamSal3['Salario'].apply(lambda x: int(x))
            dfTamSal3['Salario'] = salarioint

            dfTamSal3.reset_index(inplace=True, drop=False)
            
            if rol == "Todos":
                grosor = 0.5
                color = "Wistia"
            else:
                grosor = 0.35
                color = ["darkorange"]
                
            sns.set_theme(style="whitegrid")
            grafica = sns.barplot(data = dfTamSal3,x="TamanoEmpresa", y = 'Salario', width = grosor, hue = "Salario", alpha = 0.6, hatch = "/", palette = color)
            grafica.set_title("Salario mensual por Tamaño de Empresa en el rol: " + rol, fontsize = 17, weight = "bold")
            grafica.set_xlabel("Tamaño de Empresa", fontsize = 17, weight = "bold")
            grafica.set_ylabel("Salario", fontsize = 17, weight = "bold")
            imagen = grafica.get_figure()
            return imagen

        return 0



