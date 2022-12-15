import re
from Diccionario import Diccionario
from Tecnologia import Tecnologia
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


class Parser:
    
    clf = None
    tf = None
    text_tf = None
    df_roles = None
    
    @staticmethod
    def limpiarSalario(salario):
        tipoSalario = salario.split('/')[1]
        salario = salario.split('/')[0]
        salario = salario.split(':')[1]
        salario = salario.replace('k', '').replace('$', '').replace(' M', '000').replace('Por hora', '')
        
        if '-' in salario:
            salarioMin = float(salario.split('-')[0])
            salarioMax = float(salario.split('-')[1])
        else:
            salarioMin = float(salario)
            salarioMax = float(salario)
        
        if 'h' in tipoSalario:
            salarioMensual = ((salarioMin + salarioMax) / 2) * 720 
        elif 'a' in tipoSalario:
            salarioAnual = ((salarioMin + salarioMax) / 2) * 1000
            salarioMensual = salarioAnual / 12
        elif 'mes' in tipoSalario:
            salarioMensual = ((salarioMin + salarioMax) / 2) * 1000
        else:
            salarioMensual = -1
            
        return salarioMensual
    
    @staticmethod
    def limpiarTamanoEmpresa(tamanoEmpresa):
        if tamanoEmpresa == "No se sabe":
            tamanoEmpresa = tamanoEmpresa.replace(tamanoEmpresa, "-1")
        else:
            tamanoEmpresa = tamanoEmpresa.split('e')[1]
            tamanoEmpresa = tamanoEmpresa.replace(' ', '').replace('a', '-')
            if '-' in tamanoEmpresa:
                tamanoEmpresa = tamanoEmpresa.split('-')[1]
            
            if tamanoEmpresa == "50" or tamanoEmpresa == "200" or tamanoEmpresa == "500":
                tamanoEmpresa = tamanoEmpresa.replace(tamanoEmpresa, "Pequeña")
            elif tamanoEmpresa == "1000" or tamanoEmpresa == "5000":
                tamanoEmpresa = tamanoEmpresa.replace(tamanoEmpresa, "Mediana")
            elif tamanoEmpresa == "10000":
                tamanoEmpresa = tamanoEmpresa.replace(tamanoEmpresa, "Grande")
            else:
                tamanoEmpresa = tamanoEmpresa.replace(tamanoEmpresa, "-1")
            
        return tamanoEmpresa
    

    @staticmethod
    def limpiarUbicacion(ubicacion):
        if ubicacion == 'Trabajo desde casa' or ubicacion == "":
            ubicacion = "-1"
        return ubicacion


    @staticmethod
    def buscarTecnologiasSolicitadas(listaTecnologias):
        tecsSolicitadas = []

        tecsOrdenadas = sorted (listaTecnologias, key= lambda x : x.obtenerFrecuencia(), reverse = True)

        if tecsOrdenadas.__len__() <10:
            for i in range (tecsOrdenadas.__len__()): 
                tecsSolicitadas.append(tecsOrdenadas[i])
        else:
            for i in range (10): 
                tecsSolicitadas.append(tecsOrdenadas[i])

        return tecsSolicitadas 



    @staticmethod
    def limpiarModalidad(modalidad):
        if modalidad == 'Trabajo desde casa':
            modalidad = modalidad.replace(modalidad, "Virtual")
        else:
            modalidad = modalidad.replace(modalidad, "Presencial")
        return modalidad

    @staticmethod
    def buscarTecnologiasSolicitadas(listaTecnologias):
        tecsSolicitadas = []

        tecsOrdenadas = sorted (listaTecnologias, key= lambda x : x.obtenerFrecuencia(), reverse = True)

        if tecsOrdenadas.__len__() <10:
            for i in range (tecsOrdenadas.__len__()): 
                tecsSolicitadas.append(tecsOrdenadas[i])
        else:
            for i in range (10): 
                tecsSolicitadas.append(tecsOrdenadas[i])

        return tecsSolicitadas 
    
    @staticmethod
    def limpiarTecnologias(Descripcion, listaTecnologias):
        listaTecno = listaTecnologias
        listaOfertaTecno = []
        
        Descripcion = Descripcion.lower()
        listaText = re.findall(r'\w+', Descripcion)
        listaText = set(listaText)
        listaText = list(listaText)
        
        for index in listaText:
            for tecno in listaTecno:
                compararTecno = tecno.obtenerNombre()
                compararTecno = compararTecno.lower()
                if compararTecno == index:
                    tecno.aumentarFrecuencia()
                    listaOfertaTecno.append(tecno)
        return listaOfertaTecno
    
    @staticmethod
    def limpiarSoftskills(Descripcion):
        listaSoftskills = Diccionario.obtenerListaSoftskills()
        listaOfertaSoftskills = []
        
        Descripcion = Descripcion.replace('á', 'a').replace('é', 'e').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        Descripcion = Descripcion.lower()
        
        for softskills in listaSoftskills:
            compararSoftskills = softskills.obtenerNombre()
            compararSoftskills = compararSoftskills.lower()
            if compararSoftskills in Descripcion:
                softskills.aumentarFrecuencia()
                listaOfertaSoftskills.append(softskills)

        return listaOfertaSoftskills
    
    @staticmethod
    def obtenerDfRoles():
        ListaListaTecnologias = []
        ListaNombres = []
        for rol in Diccionario.obtenerListaRoles():
            ListaNombreTecnologias = ""
            for tecnologia in rol.obtenerTecnologias():
                ListaNombreTecnologias+=tecnologia.obtenerNombre()+" "
            ListaNombres.append(rol.obtenerNombre())
            ListaListaTecnologias.append(ListaNombreTecnologias)
        data = {'tecnologias': ListaListaTecnologias, 'nombrerol': ListaNombres}
        df_roles  = pd.DataFrame(data)
        return df_roles
    
    @staticmethod
    def limpiarRol(StringTecnologias):
        if(StringTecnologias == ""):
            return "indefinido"
        if(Parser.tf == None):
            Parser.df_roles = Parser.obtenerDfRoles()
            Parser.tf=TfidfVectorizer()
            Parser.inicializarModelo()
        Parser.df_roles.head()
        newdf_roles = Parser.df_roles.append(pd.DataFrame({'tecnologias':[StringTecnologias],'nombrerol': [""]}),ignore_index = True)
        test_tf = Parser.tf.fit_transform(newdf_roles['tecnologias'])
        descs = newdf_roles['tecnologias']
        predicted = Parser.clf.predict(test_tf)
        output = pd.DataFrame({'tecnologias':descs,'nombrerol':predicted})
        Parser.df_roles = output
        return output.loc[len(newdf_roles)-1][1]

    @staticmethod
    def inicializarModelo():
        Parser.text_tf= Parser.tf.fit_transform(Parser.df_roles['tecnologias'])
        Parser.clf = MultinomialNB().fit(Parser.text_tf,Parser.df_roles['nombrerol'])

    @staticmethod
    def limpiarStringTecnologias(ListaTecnologias):
        StringTecnologias = ""
        for tecnologia in ListaTecnologias:
            StringTecnologias+=tecnologia.obtenerNombre()+" "
        if(StringTecnologias == ""):
            return StringTecnologias
        StringTecnologias = StringTecnologias[:-1]
        return StringTecnologias