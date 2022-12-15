import sys
from Sistema import Sistema
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

window = loader.load("widget.ui",None)

def ConsultarDatosClick():
    pix = QPixmap("ColeccionGraficas/seleccionelosfiltros.png")
    window.Grafica.setScaledContents(True)
    window.Grafica.setPixmap(pix)
    window.MenuPrincipal.setCurrentIndex(1)
    window.Fecha_Button.clear()
    window.Filtro_Button.clear()
    window.Rol_Button.clear()

    listaFechas = Sistema.getFechas()
    listaRoles = ["Selecciona uno"]
    listaFiltros = ["Selecciona uno"]

    for fecha in listaFechas:
        window.Fecha_Button.addItem(fecha)
    for rol in listaRoles:
        window.Rol_Button.addItem(rol)
    for filtro in listaFiltros:
        window.Filtro_Button.addItem(filtro)

def mimagen(fecha):
    
    
    listaRoles = Sistema.getRoles(fecha)
    window.Rol_Button.clear()
    for rol in listaRoles:
        window.Rol_Button.addItem(rol)

def mimagen2(rol):

    fecha = window.Fecha_Button.currentText()
    listaFiltros = Sistema.getFiltros(fecha,rol)
    window.Filtro_Button.clear()
    for filtro in listaFiltros:
        if filtro == "CantidadSoftskills" or filtro == "TecnologiasSolicitadas":
            continue
        window.Filtro_Button.addItem(filtro)

def TecnologiasSolicitadasClick():
    
    pix = QPixmap("ColeccionGraficas/seleccionelosfiltros.png")
    window.TecnologiasSolicitadasGrafica.setScaledContents(True)
    window.TecnologiasSolicitadasGrafica.setPixmap(pix)
    window.MenuPrincipal.setCurrentIndex(2)
    window.Fecha_Button_2.clear()

    listaFechas = Sistema.getFechas()

    for fecha in listaFechas:
        window.Fecha_Button_2.addItem(fecha)

def ConsultarHistorialClick():
    pix = QPixmap("ColeccionGraficas/seleccionelosfiltros.png")
    window.ConsultarHistorialGrafica.setScaledContents(True)
    window.ConsultarHistorialGrafica.setPixmap(pix)
    window.MenuPrincipal.setCurrentIndex(3)
    window.Fecha_Button_5.clear()

    listaFechas = Sistema.getFechas()

    for fecha in listaFechas:
        window.Fecha_Button_5.addItem(fecha)

def mimagen3(filtro):

    pix = QPixmap("ColeccionGraficas/"+window.Fecha_Button.currentText()+"/"+window.Rol_Button.currentText()+"/"+filtro+".png")
    window.Grafica.setScaledContents(True)
    window.Grafica.setPixmap(pix)

def mostrarTecnologias(fecha):
    pix = QPixmap("ColeccionGraficas/"+fecha+"/Todos/TecnologiasSolicitadas.png")
    window.TecnologiasSolicitadasGrafica.setScaledContents(True)
    window.TecnologiasSolicitadasGrafica.setPixmap(pix)

def mostrarHistorial(fecha):
    pix = QPixmap("ColeccionGraficas/"+fecha+"/Todos/CantidadSoftskills.png")
    window.ConsultarHistorialGrafica.setScaledContents(True)
    window.ConsultarHistorialGrafica.setPixmap(pix)
    

window.setWindowTitle("LinkJob")

#Botones consultar datos
window.GenerarDatos_Button.clicked.connect(lambda:Sistema().generarDatos())
window.Fecha_Button.activated.connect(lambda:mimagen(window.Fecha_Button.currentText()))
window.Rol_Button.activated.connect(lambda:mimagen2(window.Rol_Button.currentText()))
window.Filtro_Button.activated.connect(lambda:mimagen3(window.Filtro_Button.currentText()))

#Botones consultar tecnologias
window.Fecha_Button_2.activated.connect(lambda:mostrarTecnologias(window.Fecha_Button_2.currentText()))

#Botones consultar historial
window.Fecha_Button_5.activated.connect(lambda:mostrarHistorial(window.Fecha_Button_5.currentText()))

#Botones del menu principal
window.ConsultarDatos_Button.clicked.connect(lambda:ConsultarDatosClick())
window.TecnologiasSolicitadas_Button.clicked.connect(lambda:TecnologiasSolicitadasClick())
window.ConsultarHistorial_Button.clicked.connect(lambda:ConsultarHistorialClick())

#Botones regresar al menu principal
window.MenuPrincipal_Button.clicked.connect(lambda:window.MenuPrincipal.setCurrentIndex(0))
window.MenuPrincipal_Button_2.clicked.connect(lambda:window.MenuPrincipal.setCurrentIndex(0))
window.MenuPrincipal_Button_5.clicked.connect(lambda:window.MenuPrincipal.setCurrentIndex(0))

window.show()
app.exec()