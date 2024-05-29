from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"C:/Users/andrearicci/Documents/helphour/mainwindow.ui", self)
 
        # find the widgets in the xml file
 
        self.textedit = self.findChild(QLineEdit, "line1")
        self.button = self.findChild(QPushButton, "button")
        self.button.clicked.connect(self.clickedBtn)
        self.table=self.findChild(QTableWidget, "tabella")
        self.table.setColumnCount(3)
        self.table.setRowCount (3)
        self.table.setHorizontalHeaderLabels(["Nome Professore", "Nome Studente","Numero Ore"])
 
        self.show()
 
 
 
    def clickedBtn(self):
        riga = 0
        colonna = 0
        lista=[{"nomeP":"Matteo Picciolini","nomeS":"Andrea Ricci","nOre":5},{"nomeP":"David Stocchi","nomeS":"Anwar Belkheir","nOre":4},{"nomeP":"Samuele Maranghi","nomeS":"Giacomo Poldi","nOre":8}]
        
        for element in lista:
            item_name=QTableWidgetItem(element["nomeP"])
            self.table.setItem(riga, 0, item_name)
            item_name=QTableWidgetItem(element["nomeS"])
            self.table.setItem(riga, 1, item_name)
            item_name=QTableWidgetItem(str(element["nOre"]))
            self.table.setItem(riga, 2, item_name)
            riga = riga+1 


app = QApplication(sys.argv)
window = UI()
app.exec_()