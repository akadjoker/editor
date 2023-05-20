import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QListView, QListWidgetItem, QAction, QMenuBar, QToolBar, QStatusBar, QGridLayout

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Código")
        self.setGeometry(100, 100, 800, 600)

        # Criar widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Criar layout principal
        main_layout = QGridLayout(central_widget)

        # Criar lista de arquivos
        self.file_list = QListView()
        self.file_list.setAcceptDrops(True)
        self.file_list.setDragEnabled(True)
        self.file_list.setDragDropMode(QListView.InternalMove)
        main_layout.addWidget(self.file_list, 0, 0, 2, 1)

        # Criar editor de texto
        self.text_edit = QTextEdit()
        main_layout.addWidget(self.text_edit, 0, 1)

        # Criar console
        self.console_edit = QTextEdit()
        main_layout.addWidget(self.console_edit, 1, 1)

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

        compile_button = QPushButton("Compilar")
        compile_button.clicked.connect(self.compile_code)
        toolbar.addWidget(compile_button)

        compile_clean_button = QPushButton("Compilar e Limpar")
        compile_clean_button.clicked.connect(self.compile_clean_code)
        toolbar.addWidget(compile_clean_button)

        run_button = QPushButton("Executar")
        run_button.clicked.connect(self.run_code)
        toolbar.addWidget(run_button)

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Arquivos C (*.c)")
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
    sys.exit(app.exec())

