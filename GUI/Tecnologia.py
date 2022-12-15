from Oferta import Oferta
class Tecnologia:
   
    __nombre = ""
    __frecuencia = 0
    __frecuenciaTotal = 0
    __promedioTecnologias=0


    def __init__(self, nombre):
        self.__nombre = nombre
        self.__frecuencia = 0

    def obtenerNombre(self):
        return self.__nombre

    def aumentarFrecuencia (self):
        self.__frecuencia = self.__frecuencia + 1
        Tecnologia.__frecuenciaTotal=Tecnologia.__frecuenciaTotal+1
        
    def obtenerFrecuencia (self):
        return self.__frecuencia
    
    def calcularPromedioTecnologias ():
        if Oferta.obtenerOfertasTotales() <=0:
            Tecnologia.__promedioTecnologias = -1
        else:
            Tecnologia.__promedioTecnologias = Tecnologia.__frecuenciaTotal / Oferta.obtenerOfertasTotales()


    def obtenerFrecuenciaTotal():
        return Tecnologia.__frecuenciaTotal

    def obtenerPromedioTecnologias ():
        return Tecnologia.__promedioTecnologias







