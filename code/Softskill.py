from Oferta import Oferta
class Softskill:
    
    __nombre = ""
    __frecuencia = 0
    __frecuenciaTotal = 0
    __promedioSoftskills = 0

    def __init__(self,nombre):
        self.__nombre = nombre
        self.__frecuencia = 0

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerFrecuencia(self):
        return self.__frecuencia
    
    def aumentarFrecuencia(self):
        self.__frecuencia += 1
        Softskill.__frecuenciaTotal += 1
    
    def calcularPromedioSoftskills():
        if(Oferta.obtenerOfertasTotales() != 0):
            Softskill.__promedioSoftskills = Softskill.__frecuenciaTotal/Oferta.obtenerOfertasTotales()
        else:
             Softskill.__promedioSoftskills = -1

    def obtenerPromedioSoftskills():
        return Softskill.__promedioSoftskills


    
