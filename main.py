import sys
from turtle import width
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
# from conexion import Comunicacion

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('inventario_gui.ui', self)

        self.menu.clicked.connect(self.mover_menu)
        # self.inventario = Comunicacion()

        #funciones de los botones de la ventana
        self.cerrar.clicked.connect(lambda: self.close())

        #elimina barra de titulo -opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #funciones botones del menu lateral
        self.btn_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_registrar))
        self.btn_todo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_todo))
        self.btn_registrarRes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_registrarRes))
        self.btn_todoRes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_todoRes))

        #funciones de los botones de las paginas
        self.btn_agregar.clicked.connect(self.insertar_productos)
        self.btn_agregarRes.clicked.connect(self.insertar_restaurante)
        self.btn_todo.clicked.connect(self.mostrar_productos)
        self.btn_todoRes.clicked.connect(self.mostrar_restaurantes)

        #ancho de columna adaptable
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.navbar.mouseMoveEvent = self.mover_ventana
        
        
    #mover ventana
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

    def mover_ventana(self, event):
        if event.buttons()== QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.click_position)
            self.click_position = event.globalPos()
            event.accept()
        if event.globalPos().y() <=5:
            self.showMaximized()


    #mover el menu lateral izquierdo
    def mover_menu(self):
        if True:
            width = self.sidebar.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.sidebar, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()


    def insertar_productos(self):
        nombre = self.input_producto.text().upper()
        cantidad = self.input_cantidad.text().upper()
        restaurante = self.combo.text().upper()

        if nombre != '' and cantidad != '' and restaurante != '' :
            # self.inventario.insertar_productos(nombre, cantidad,restaurante)
            self.input_producto.clear()            
            self.input_cantidad.clear()
            self.combo.clear()


    def insertar_restaurante(self):
        nombre = self.input_nombreRes.text().upper()

        if nombre != '':
            # self.inventario.insertar_restaurante(nombre)
            self.input_nombreRes.clear()


    def mostrar_productos(self):
        # datos = self.inventario.mostrar_productos
        i = len(datos)
        self.tabla.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.id = row[0]
            self.tabla.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1])) 
            self.tabla.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2])) 
            self.tabla.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3])) 
            
            tablerow +=1

    def mostrar_restaurantes(self):
        # datos = self.inventario.mostrar_restaurantes
        i = len(datos)
        self.tablaRes.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.id = row[0]
            self.tablaRes.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1])) 
            self.tablaRes.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2])) 
            self.tablaRes.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3])) 
            
            tablerow +=1



    def llenarComboBox(self):
        # results = self.inventario.mostrar_restaurantes()
        for row in results:
            self.combo.addItem(row[0])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
    