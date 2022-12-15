class Rol:
    __nombre = ""
    __tablaTecnologia = []
    __frecuencia = 0
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__tablaTecnologia = []
        self.__frecuencia = 0
    
    def compararTecnologias():
        return 0
    
    def obtenerNombre(self):
        return self.__nombre

    def obtenerTecnologias(self):
        return self.__tablaTecnologia
    
    def obtenerFrecuencia(self):
        return self.__frecuencia
    
    def aumentarFrecuencia (self):
        self.__frecuencia = self.__frecuencia + 1
    
    def agregarTecnologiasBuscadas(self, agregarTecnologia, listaTecnologias):
        for index in listaTecnologias:
            if index.obtenerNombre() == agregarTecnologia:
                self.__tablaTecnologia.append(index)
    
    def removerTecnologiasBuscadas(self, removerTecnologia, listaTecnologias):
        for index in listaTecnologias:
            if index.obtenerNombre() == removerTecnologia:
                self.__tablaTecnologia.remove(index)     