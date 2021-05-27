import sys
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QMainWindow,  QLabel, QLineEdit,QPushButton
from docxtpl import DocxTemplate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializedUI()

    def initializedUI(self):
        self.setGeometry(400, 400, 500, 350)
        self.setWindowTitle('Sistema de Automatización de Contratos')
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        self.label()
        self.boton()
        self.name_dest()
        self.address_dest()
        self.city_dest()
        self.name_remit()
        self.address_remit()
        self.caracter_remit()
        self.label()
        self.label_ok()

    def label(self):
        label = QLabel("Ingrese los datos requeridos", self)
        label.move(50,10)
        label.adjustSize()

    def name_dest(self):
        name_dest_label = QLabel("Nombre del destinatario:", self)
        name_dest_label.move(50, 80)
        name_dest_label.adjustSize()
        self.name_dest_entry = QLineEdit(self)
        self.name_dest_entry.move(200, 80)
        self.name_dest_entry.resize(200, 20)

    def address_dest(self):
        address_dest_label = QLabel("Dirección del destinatario:", self)
        address_dest_label.move(50, 110)
        address_dest_label.adjustSize()
        self.address_dest_entry = QLineEdit(self)
        self.address_dest_entry.move(200, 110)
        self.address_dest_entry.resize(200, 20)

    def city_dest(self):
        city_dest_label = QLabel("Ciudad del destinatario:", self)
        city_dest_label.move(50, 140)
        city_dest_label.adjustSize()
        self.city_dest_entry = QLineEdit(self)
        self.city_dest_entry.move(200, 140)
        self.city_dest_entry.resize(200, 20)

    def name_remit(self):
        name_remit_label = QLabel("Nombre del remitente:", self)
        name_remit_label.move(50, 170)
        name_remit_label.adjustSize()
        self.name_remit_entry = QLineEdit(self)
        self.name_remit_entry.move(200, 170)
        self.name_remit_entry.resize(200, 20)

    def address_remit(self):
        address_remit_label = QLabel("Dirección del remitente:", self)
        address_remit_label.move(50, 200)
        address_remit_label.adjustSize()
        self.address_remit_entry = QLineEdit(self)
        self.address_remit_entry.move(200, 200)
        self.address_remit_entry.resize(200, 20)

    def caracter_remit(self):
        caracter_remit_label = QLabel("Caracter del remitente:", self)
        caracter_remit_label.move(50, 230)
        caracter_remit_label.adjustSize()
        self.caracter_remit_entry = QLineEdit(self)
        self.caracter_remit_entry.move(200, 230)
        self.caracter_remit_entry.resize(200, 20)

    def boton(self):
        pybutton = QPushButton('Confirmar', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(50, 300)

    def label_ok(self):
        global label_ok
        label_ok = QLabel("", self)
        label_ok.move(50,250)
        label_ok.resize(250,50)


    def clickMethod(self):
        doc = DocxTemplate("Indemnidad_Mock.docx")
        context = {'destinatario_name': self.name_dest_entry.text(),
                   'destinatario_address': self.address_dest_entry.text(),
                   'destinatario_city': self.city_dest_entry.text(),
                   'caracter_firmante': self.caracter_remit_entry.text(),
                   'remitente_name': self.name_remit_entry.text(),
                   'remitente_address': self.address_remit_entry.text()}
        doc.render(context)
        doc.save("Indemnidad_{}.docx".format(self.name_remit_entry.text()))
        label_ok.setText("El contrato se generó de forma satisfactoria")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )