import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QTableWidget, QMessageBox, QListWidget, QListWidgetItem, QFileDialog
from PyQt5.uic import loadUi
from lex import lexAnaliser
import GrammarReader

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
        self.plainTextEditEditor.textChanged.connect(self.setUnsaved)
        self.tabWidget2.hide()

        self.lex =lexAnaliser()
        self.saved = True

        file = open('.\\Grammar.txt', 'r')
        self.grammar = GrammarReader.readGrammar(file.read())
        file.close()


    def setUnsaved(self):
        self.saved = False if self.plainTextEditEditor.toPlainText() is not '' else True

    def setSaved(self):
        self.saved = True

    def TabChanged(self):
        currentTab = self.tabWidget.currentIndex()
        if currentTab is 0:
            None
        elif currentTab is 1:
            self.updateSymbolTable(self.tableTabelaDeSimbolos, self.CheckBoxCleanTable.isChecked())
        elif currentTab is 2:
            self.updateTokens(self.plainTextEditEditorTokens, self.CheckBoxCleanTable.isChecked())
        elif currentTab is 3:
            self.updateFirst()
        elif currentTab is 4:
            self.updateFollow()
        elif currentTab is 5:
            self.updateParseTree()

    def TabChanged2(self):
        currentTab = self.tabWidget2.currentIndex()
        if currentTab is 0:
            self.updateSymbolTable(self.tableTabelaDeSimbolos2, self.CheckBoxCleanTable.isChecked())
        elif currentTab is 1:
            self.updateTokens(self.plainTextEditEditorTokens2, self.CheckBoxCleanTable.isChecked())

    def NewFile(self):
        if not self.saved:
            if QMessageBox.question(self, 'Criar novo?', 'As mudanças não salvas serão perdidas!',  QMessageBox.Yes,  QMessageBox.No) != QMessageBox.Yes:
                return
        self.plainTextEditEditor.setPlainText('')

    def SaveFile(self):
        (filepath,filter) = QFileDialog.getSaveFileName(self, "Selecione o arquivo:", "", "txt (*.txt)")
        if filepath == '':
            return
        try:
            file = open(filepath, 'w')
            file.write(self.plainTextEditEditor.toPlainText())
            file.close()
            self.setSaved()
        except:
            QMessageBox.critical(self, 'Erro!', 'Não foi possível abrir o arquivo selecionado')

    def OpenFile(self):
        if not self.saved:
            if QMessageBox.question(self, 'Criar novo?', 'As mudanças não salvas serão perdidas!',  QMessageBox.Yes,  QMessageBox.No) != QMessageBox.Yes:
                return
        (filepath,filter) = QFileDialog.getOpenFileName(self, "Selecione o arquivo:", "", "txt (*.txt)")
        if filepath == '':
            return
        try:
            file = open(filepath, 'r')
            self.plainTextEditEditor.setPlainText(file.read())
            file.close()
            self.tabWidget.setCurrentIndex(0)
            self.setSaved()
        except:
            QMessageBox.critical(self, 'Erro!', 'Não foi possível abrir o arquivo selecionado')

    def CleanTableClicked(self):
        currentTab = self.tabWidget2.currentIndex()
        if currentTab is 1:
            self.updateSymbolTable(self.tableTabelaDeSimbolos, self.CheckBoxCleanTable.isChecked())
        elif currentTab is 2:
            self.updateTokens(self.plainTextEditEditorTokens, self.CheckBoxCleanTable.isChecked())

        currentTab = self.tabWidget2.currentIndex()
        if currentTab is 0:
            self.updateSymbolTable(self.tableTabelaDeSimbolos2, self.CheckBoxCleanTable.isChecked())
        elif currentTab is 1:
            self.updateTokens(self.plainTextEditEditorTokens2, self.CheckBoxCleanTable.isChecked())

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
                self.updateTokens(self.plainTextEditEditorTokens2, self.CheckBoxCleanTable.isChecked())

    def updateSymbolTable(self, table, clean = True):
        codigo = self.plainTextEditEditor.toPlainText()

        self.lex.setInput(codigo)
        self.lex.generateAllTokens()

        symbolTable = self.lex.getCleanSymbolTable() if clean else self.lex.getSymbolTable()

        table.setColumnCount(2)
        table.setRowCount(len(symbolTable) + 1)

        newitem = QTableWidgetItem('Lexemas')
        table.setItem(0, 0, newitem)
        newitem = QTableWidgetItem('Tokens')
        table.setItem(0, 1, newitem)

        for row, (key, value) in enumerate(symbolTable.items()):
            newitem = QTableWidgetItem(key)
            table.setItem(row + 1, 0, newitem)
            newitem = QTableWidgetItem(value)
            table.setItem(row + 1, 1, newitem)

    def updateTokens(self, textEdit, clean = False):
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
            elif token is 'Error':
                if not clean:
                    printable += 'Error'
            else:
                printable += token

        textEdit.setPlainText(printable)

    def updateFirst(self):
        firstDict = self.grammar.getFirst()

        self.tableFirst.setColumnCount(2)
        self.tableFirst.setRowCount(len(self.grammar.nonTerminals) + 1)

        newitem = QTableWidgetItem('X')
        self.tableFirst.setItem(0, 0, newitem)
        newitem = QTableWidgetItem('FIRST(X)')
        self.tableFirst.setItem(0, 1, newitem)

        for row, (symbol, first) in enumerate(firstDict.items()):
            newitem = QTableWidgetItem(symbol)
            self.tableFirst.setItem(row + 1, 0, newitem)
            newitem = QTableWidgetItem(str(first))
            self.tableFirst.setItem(row + 1, 1, newitem)

        self.tableFirst.resizeColumnsToContents()

    def updateFollow(self):
        followDict = self.grammar.getFollow()

        self.tableFollow.setColumnCount(2)
        self.tableFollow.setRowCount(len(self.grammar.nonTerminals) + 1)

        newitem = QTableWidgetItem('X')
        self.tableFollow.setItem(0, 0, newitem)
        newitem = QTableWidgetItem('FOLLOW(X)')
        self.tableFollow.setItem(0, 1, newitem)

        for row, (symbol, follow) in enumerate(followDict.items()):
            newitem = QTableWidgetItem(symbol)
            self.tableFollow.setItem(row + 1, 0, newitem)
            newitem = QTableWidgetItem(str(follow))
            self.tableFollow.setItem(row + 1, 1, newitem)

        self.tableFollow.resizeColumnsToContents()

    def updateParseTree(self):
        parsing = [ \
            ('<program>',['<block>']),
            ('<block>',['{','<decls>','<stmts>','}']),
            ('<decls>',['&']),
            ('<stmts>',['break', ';'])
        ]

        if len(parsing) is 0:
            return

        self.sintTable.setColumnCount(2)
        self.sintTable.setRowCount(len(parsing) + 2)

        newitem = QTableWidgetItem('X')
        self.sintTable.setItem(0, 0, newitem)
        newitem = QTableWidgetItem('Production:')
        self.sintTable.setItem(0, 1, newitem)

        index = 0
        derivation = [parsing[0][0]]

        for row, (head, production) in enumerate(parsing):

            string = derivation[0]
            for symbol in derivation[1:]:
                string += ' ' + symbol
            newitem = QTableWidgetItem(string)
            self.sintTable.setItem(row + 1, 0, newitem)

            string = head + ' ::='
            for symbol in production:
                string += ' ' + symbol
            newitem = QTableWidgetItem(string)
            self.sintTable.setItem(row + 1, 1, newitem)

            while derivation[index] is not head:
                index += 1
                if index >= len(derivation):
                    return

            derivation = derivation[:index] + production + derivation[index+1:]

        string = derivation[0]
        for symbol in derivation[1:]:
            string += ' ' + symbol
        newitem = QTableWidgetItem(string)
        self.sintTable.setItem(len(parsing) + 1, 0, newitem)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
