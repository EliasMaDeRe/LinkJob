from Diccionario import Diccionario
from Webscrapper import Webscrapper
from ColeccionGraficas import ColeccionGraficas
from Plotter import Plotter
import os
class Sistema:

    Dict = None

    def __init__(self):
        Sistema.Dict = Diccionario()
        self.listaOfertas = []
        self.listaColeccionGraficas = []
        self.ListaRoles = Diccionario.obtenerListaRoles()
        self.ListaTecno = Diccionario.obtenerListaTecnologias()
        self.ListaSoftskills = Diccionario.obtenerListaSoftskills()
        
        

    def getDict():
        return Sistema.Dict

    def consultarDatosActuales(self, nuevaInfo,rol, filtro1, filtro2):
        if (nuevaInfo==True):
            Sistema.generarDatos(self.listaOfertas)
            ColeccionGraficas.mostrarGrafica(rol,filtro1,filtro2)
        else:
            ColeccionGraficas.mostrarGrafica(rol,filtro1,filtro2)

    def generarDatos(self):  
        self.listaOfertas,self.ListaTecno = Webscrapper.recolectarOfertas(self.listaOfertas, self.ListaTecno)
        Plotter.plotOfertas(self.listaOfertas, self.ListaRoles, self.ListaTecno, self.ListaSoftskills)
    
    @staticmethod
    def getFechas():
        nombreDirectorio = 'ColeccionGraficas'

        if os.path.exists(nombreDirectorio) and os.path.isdir(nombreDirectorio):
            with os.scandir(nombreDirectorio) as ficheros:
                fechasPloteos = [fichero.name for fichero in ficheros if fichero.is_dir()]
                return fechasPloteos
        return []

    @staticmethod
    def getRoles(fecha):
        nombreDirectorio = 'ColeccionGraficas/'+fecha

        if os.path.exists(nombreDirectorio) and os.path.isdir(nombreDirectorio):
            with os.scandir(nombreDirectorio) as ficheros:
                fechasPloteos = [fichero.name for fichero in ficheros if fichero.is_dir()]
                return fechasPloteos
        return []

    def getFiltros(fecha,rol):
        nombreDirectorio = 'ColeccionGraficas/'+fecha+'/'+rol

        if os.path.exists(nombreDirectorio) and os.path.isdir(nombreDirectorio):
            with os.scandir(nombreDirectorio) as ficheros:
                fechasPloteos = [fichero.name[:-4] for fichero in ficheros if fichero.is_file()]
                return fechasPloteos
        return []
