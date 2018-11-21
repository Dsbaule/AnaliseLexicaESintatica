import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QTableWidget, QMessageBox, QListWidget, QListWidgetItem, QFileDialog
from PyQt5.uic import loadUi
from lex import lexAnaliser

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('./mainWindow.ui', self)

        # General UI
        self.tabWidget.currentChanged.connect(self.TabChanged)
        self.ButtonNew.triggered.connect(self.NewFile)
        self.ButtonSave.triggered.connect(self.SaveFile)
        self.ButtonOpen.triggered.connect(self.OpenFile)
        self.CheckBoxCleanTable.triggered.connect(self.CleanTableClicked)

        self.lex =lexAnaliser()


    def TabChanged(self):
        currentTab = self.tabWidget.currentIndex()
        if currentTab is 0:
            None
        elif currentTab is 1:
            self.updateSymbolTable(self.CheckBoxCleanTable.isChecked())

    def NewFile(self):
        None

    def SaveFile(self):
        None

    def OpenFile(self):
        None

    def CleanTableClicked(self):
        if self.tabWidget.currentIndex() is 1:
            self.updateSymbolTable(self.CheckBoxCleanTable.isChecked())

    def updateSymbolTable(self, clean = True):
        codigo = self.plainTextEditEditor.toPlainText()

        self.lex.setInput(codigo)
        self.lex.generateSymbolTable()


        symbolTable = self.lex.getCleanSymbolTable() if clean else self.lex.getSymbolTable()

        self.tableTabelaDeSimbolos.setColumnCount(2)
        self.tableTabelaDeSimbolos.setRowCount(len(symbolTable))

        for row, (key, value) in enumerate(symbolTable.items()):
            newitem = QTableWidgetItem(key)
            self.tableTabelaDeSimbolos.setItem(row + 1, 0, newitem)
            newitem = QTableWidgetItem(value)
            self.tableTabelaDeSimbolos.setItem(row + 1, 1, newitem)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
