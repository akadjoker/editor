import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QListView, QListWidgetItem

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Código")
        self.setGeometry(100, 100, 800, 600)
        
        # Criar widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Criar layout principal
        main_layout = QHBoxLayout(central_widget)

        # Criar lista de arquivos
        file_list = QListView()
        file_list.setAcceptDrops(True)
        file_list.setDragEnabled(True)
        file_list.setDragDropMode(QListView.InternalMove)
        #file_list.itemDoubleClicked.connect(self.open_file_from_list)
        main_layout.addWidget(file_list)

        # Criar layout para o editor de texto
        text_editor_layout = QVBoxLayout()
        main_layout.addLayout(text_editor_layout)

        # Criar toolbar
        toolbar = self.addToolBar("Toolbar")
        compile_button = QPushButton("Build/Compile")
        compile_button.clicked.connect(self.compile_code)
        toolbar.addWidget(compile_button)

        # Criar menu
        menu = self.menuBar()
        file_menu = menu.addMenu("Arquivo")
        open_action = file_menu.addAction("Abrir")
        open_action.triggered.connect(self.open_file)

        # Criar status bar
        status_bar = self.statusBar()
        status_label = QLabel("Status")
        status_bar.addWidget(status_label)

        self.text_edit = QTextEdit(self)
        text_editor_layout.addWidget(self.text_edit)

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Arquivos C (*.c)")
        file_dialog.fileSelected.connect(self.load_file)
        file_dialog.exec()

    def load_file(self, file_path):
        with open(file_path, "r") as file:
            self.text_edit.setPlainText(file.read())

    def open_file_from_list(self, item):
        file_path = item.text()
        self.load_file(file_path)

    def compile_code(self):
        # Implemente aqui a lógica para compilar o código
        status_label.setText("Compilando código...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    sys.exit(app.exec())

