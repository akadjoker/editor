import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QListView, QListWidgetItem, QAction, QMenuBar, QToolBar, QStatusBar, QDockWidget, QSizePolicy
from PyQt5.QtCore import Qt

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Código")
        self.setGeometry(100, 100, 800, 600)

        # Criar widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Criar layout principal
        main_layout = QVBoxLayout(central_widget)

        # Criar dock widget para a lista de arquivos
        dock_widget = QDockWidget("Lista de Arquivos", self)
        dock_widget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

        # Criar lista de arquivos
        self.file_list = QListView()
        self.file_list.setAcceptDrops(True)
        self.file_list.setDragEnabled(True)
        self.file_list.setDragDropMode(QListView.InternalMove)
        dock_widget.setWidget(self.file_list)

        # Criar editor de texto
        self.text_edit = QTextEdit()
        main_layout.addWidget(self.text_edit)

        # Criar console
        self.console_edit = QTextEdit()
        main_layout.addWidget(self.console_edit)

        # Criar status bar
        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)
        self.status_label = QLabel("Pronto")
        status_bar.addWidget(self.status_label)

        # Criar menu
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu("Arquivo")

        open_action = QAction("Abrir", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Salvar", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        save_as_action = QAction("Salvar como", self)
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)

        exit_action = QAction("Sair", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Criar toolbar
        toolbar = QToolBar("Toolbar", self)
        self.addToolBar(toolbar)

        compile_button = QAction("Compilar", self)
        compile_button.triggered.connect(self.compile_code)
        toolbar.addAction(compile_button)

        compile_clean_button = QAction("Compilar e Limpar", self)
        compile_clean_button.triggered.connect(self.compile_clean_code)
        toolbar.addAction(compile_clean_button)

        run_button = QAction("Executar", self)
        run_button.triggered.connect(self.run_code)
        toolbar.addAction(run_button)

        # Criar menu Compiler
        compiler_menu = menu_bar.addMenu("Compiler")

        compile_action = QAction("Compilar", self)
        compile_action.triggered.connect(self.compile_code)
        compiler_menu.addAction(compile_action)

        compile_clean_action = QAction("Compilar e Limpar", self)
        compile_clean_action.triggered.connect(self.compile_clean_code)
        compiler_menu.addAction(compile_clean_action)

        run_action = QAction("Executar", self)
        run_action.triggered.connect(self.run_code)
        compiler_menu.addAction(run_action)

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.fileSelected.connect(self.load_file)
        file_dialog.exec()

    def load_file(self, file_path):
        with open(file_path, "r") as file:
            self.text_edit.setPlainText(file.read())

    def save_file(self):
        # Implemente aqui a lógica para salvar o arquivo
        self.status_label.setText("Arquivo salvo")

    def save_file_as(self):
        # Implemente aqui a lógica para salvar o arquivo como
        self.status_label.setText("Arquivo salvo como")

    def compile_code(self):
        # Implemente aqui a lógica para compilar o código
        self.status_label.setText("Compilando código...")

    def compile_clean_code(self):
        # Implemente aqui a lógica para compilar e limpar o código
        self.status_label.setText("Compilando e limpando código...")

    def run_code(self):
        # Implemente aqui a lógica para executar o código
        self.status_label.setText("Executando código...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    sys.exit(app.exec_())
