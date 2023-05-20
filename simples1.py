import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox, QTabWidget

class EditorC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Editor C/C++')
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        self.createActions()
        self.createMenus()

    def createActions(self):
        self.newAction = QAction('Novo', self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.triggered.connect(self.newFile)

        self.openAction = QAction('Abrir', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.triggered.connect(self.openFile)

        self.saveAction = QAction('Salvar', self)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.triggered.connect(self.saveFile)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('Arquivo')
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)

    def newFile(self):
        textEdit = QTextEdit(self)
        self.tabs.addTab(textEdit, 'Novo Arquivo')

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Abrir Arquivo')
        if filename:
            file = open(filename, 'r')
            text = file.read()
            file.close()

            textEdit = QTextEdit(self)
            textEdit.setText(text)

            self.tabs.addTab(textEdit, filename)

    def saveFile(self):
        currentWidget = self.tabs.currentWidget()
        if currentWidget is not None:
            text = currentWidget.toPlainText()
            if not text:
                QMessageBox.warning(self, 'Aviso', 'O arquivo está vazio.')
                return

            filename = self.tabs.tabText(self.tabs.currentIndex())
            if filename == 'Novo Arquivo':
                filename, _ = QFileDialog.getSaveFileName(self, 'Salvar Arquivo')
                if not filename:
                    return

            file = open(filename, 'w')
            file.write(text)
            file.close()

            self.tabs.setTabText(self.tabs.currentIndex(), filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorC()
    editor.show()
    sys.exit(app.exec_())
