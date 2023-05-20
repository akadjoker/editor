import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QAction, QFileDialog, QMessageBox, QTabWidget, QVBoxLayout
from PyQt5.QtCore import QFileInfo

class CustomTab(QWidget):
    def __init__(self, filepath):
        super().__init__()

        self.filepath = filepath

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)

        self.setLayout(layout)

class EditorC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Editor C/C++')
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)
        self.tabs.setTabsClosable(True)
        self.tabs.tabBar().tabCloseRequested.connect(self.closeTab)

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

        self.closeAllAction = QAction('Fechar Todas', self)
        self.closeAllAction.triggered.connect(self.closeAllTabs)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('Arquivo')
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)

        self.fileMenu.addSeparator()

        self.fileMenu.addAction(self.closeAllAction)

    def newFile(self):
        textEdit = QTextEdit(self)
        self.tabs.addTab(textEdit, 'Novo Arquivo')

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Abrir Arquivo')
        if filename:
            fileInfo = QFileInfo(filename)
            folder = fileInfo.absolutePath()
            filename = fileInfo.fileName()

            customTab = CustomTab(filename)
            self.tabs.addTab(customTab, filename)

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

    def closeTab(self, index):
        customTab = self.tabs.widget(index)
        textEdit = customTab.textEdit
        if textEdit.document().isModified():
            result = QMessageBox.question(self, 'Salvar Alterações', 'Deseja salvar as alterações antes de fechar?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if result == QMessageBox.Yes:
                self.saveFile()
            elif result == QMessageBox.Cancel:
                return

        self.tabs.removeTab(index)

    def closeAllTabs(self):
        while self.tabs.count() > 0:
            self.closeTab(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorC()
    editor.show()
    sys.exit(app.exec_())
