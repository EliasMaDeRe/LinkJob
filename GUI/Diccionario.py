import csv
from Softskill import Softskill
from Tecnologia import Tecnologia
from Rol import Rol

class Diccionario:

    def __init__(self):
        Diccionario.listaTecnologias = Diccionario.crearListaTecnologias()
        Diccionario.listaRoles = Diccionario.crearListaRoles(Diccionario.listaTecnologias)
        Diccionario.listaSoftskills = Diccionario.crearListaSoftskills()

    def obtenerListaTecnologias():
        return Diccionario.listaTecnologias
    
    def obtenerListaSoftskills():
        return Diccionario.listaSoftskills

    def obtenerListaRoles():
        return Diccionario.listaRoles

    def crearListaTecnologias ():
        tecnologias = []

        with open('src\Tecnologias.csv',"r") as tecs:
            for tecnologia in tecs:
                lista = tecnologia.split(',')

            for tec in lista:
                tecnologias.append(Tecnologia(tec))

        return tecnologias 
    
    def crearListaRoles(listaTecnologias):
        listaRoles = []
        with open('src\Roles.csv', "r") as rol:
            for fila in rol:
                fila = fila.rstrip()
                lista = fila.split(";")
                rolIng = lista[0]
                rolIngTecno = lista[1]
                rolIngTecno = rolIngTecno.split(",")
                
                nuevoRol = Rol(rolIng)
                listaRoles.append(nuevoRol)
                for tecnologia in rolIngTecno:
                    nuevoRol.agregarTecnologiasBuscadas(tecnologia, listaTecnologias)
                    
        return listaRoles

    
    def crearListaSoftskills():
        listaSoftskills = []
        with open('src\Softskills.csv',mode = 'r')as file:
            archivoSoftskills = csv.reader(file)

            for line in archivoSoftskills:
                for softskill in line:
                    listaSoftskills.append(Softskill(softskill))
        
        return listaSoftskills