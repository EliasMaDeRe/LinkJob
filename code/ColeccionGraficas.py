import os
import shutil
from datetime import datetime

class ColeccionGraficas:
    imagenes = {}
    day = 0
    month = 0
    year = 0
    
    def crearDir(self):
        now = datetime.now()
        self.day = now.day
        self.month = now.month
        self.year = now.year
        
        dirPlotter = "ColeccionGraficas"
        if not os.path.exists(dirPlotter):
            os.makedirs(dirPlotter)
        
        dirFecha = dirPlotter + "/" + str(self.day) + "-" + str(self.month) + "-" + str(self.year)
        if os.path.exists(dirFecha):
            shutil.rmtree(dirFecha)
        os.makedirs(dirFecha)
        
        #print(self.imagenes)
        for clave in self.imagenes:
            dirRol = dirFecha + "/" + clave
            os.makedirs(dirRol)
            
    
    def guardado(self, rol, nombre, grafica):
        if grafica != 0:
            grafica.savefig("ColeccionGraficas"+ "/" + str(self.day) + "-" + str(self.month) + "-" + str(self.year) + "/" + rol + "/" + nombre + ".png", dpi=300, bbox_inches='tight')
            grafica.clear()
    
    
                