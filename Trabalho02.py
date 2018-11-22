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
        self.tabWidget2.currentChanged.connect(self.TabChanged2)
        self.ButtonNew.triggered.connect(self.NewFile)
        self.ButtonSave.triggered.connect(self.SaveFile)
        self.ButtonOpen.triggered.connect(self.OpenFile)
        self.CheckBoxCleanTable.triggered.connect(self.CleanTableClicked)
        self.CheckBoxShowSecondary.triggered.connect(self.ShowSecondaryClicked)
        self.plainTextEditEditor.textChanged.connect(self.UpdateSecondary)
        self.tabWidget2.hide()

        self.lex =lexAnaliser()


    def TabChanged(self):
        currentTab = self.tabWidget.currentIndex()
        if currentTab is 0:
            None
        elif currentTab is 1:
            self.updateSymbolTable(self.tableTabelaDeSimbolos, self.CheckBoxCleanTable.isChecked())
        elif currentTab is 2:
            self.updateTokens(self.plainTextEditEditorTokens)

    def TabChanged2(self):
        currentTab = self.tabWidget2.currentIndex()
        if currentTab is 0:
            self.updateSymbolTable(self.tableTabelaDeSimbolos2, self.CheckBoxCleanTable.isChecked())
        elif currentTab is 1:
            self.updateTokens(self.plainTextEditEditorTokens2)

    def NewFile(self):
        None

    def SaveFile(self):
        None

    def OpenFile(self):
        None

    def CleanTableClicked(self):
        if self.tabWidget.currentIndex() is 1:
            self.updateSymbolTable(self.tableTabelaDeSimbolos, self.CheckBoxCleanTable.isChecked())
        if self.tabWidget2.currentIndex() is 0:
            self.updateSymbolTable(self.tableTabelaDeSimbolos2, self.CheckBoxCleanTable.isChecked())

    def ShowSecondaryClicked(self):
        if self.CheckBoxShowSecondary.isChecked():
            self.TabChanged2()
            self.tabWidget2.show()
        else:
            self.tabWidget2.hide()

    def UpdateSecondary(self):
        if self.CheckBoxShowSecondary.isChecked():
            codigo = self.plainTextEditEditor.toPlainText()

            self.lex.setInput(codigo)
            self.lex.generateAllTokens()

            currentTab = self.tabWidget2.currentIndex()

            if currentTab is 0:
                self.updateSymbolTable(self.tableTabelaDeSimbolos2, self.CheckBoxCleanTable.isChecked())
            elif currentTab is 1:
                self.updateTokens(self.plainTextEditEditorTokens2)

    def updateSymbolTable(self, table, clean = True):
        codigo = self.plainTextEditEditor.toPlainText()

        self.lex.setInput(codigo)
        self.lex.generateAllTokens()

        symbolTable = self.lex.getCleanSymbolTable() if clean else self.lex.getSymbolTable()

        table.setColumnCount(2)
        table.setRowCount(len(symbolTable))

        newitem = QTableWidgetItem('Lexemas')
        table.setItem(0, 0, newitem)
        newitem = QTableWidgetItem('Tokens')
        table.setItem(0, 1, newitem)

        for row, (key, value) in enumerate(symbolTable.items()):
            newitem = QTableWidgetItem(key)
            table.setItem(row + 1, 0, newitem)
            newitem = QTableWidgetItem(value)
            table.setItem(row + 1, 1, newitem)

    def updateTokens(self, textEdit):
        codigo = self.plainTextEditEditor.toPlainText()

        self.lex.setInput(codigo)
        self.lex.generateAllTokens()

        tokens = self.lex.getTokens()

        printable = ""
        for token in tokens:
            if token is 'ws':
                printable += ' '
            elif token is 'tb':
                printable += '\t'
            elif token is 'nl':
                printable += '\n'
            else:
                printable += token

        textEdit.setPlainText(printable)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
