import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QListView, QListWidgetItem, QAction, QMenuBar, QToolBar, QStatusBar, QDockWidget, QSizePolicy
from PyQt5.QtCore import Qt

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QListView, QListWidgetItem, QAction, QMenuBar, QToolBar, QStatusBar, QDockWidget, QSizePolicy, QDialog, QFormLayout, QLineEdit, QTextEdit, QDialogButtonBox

class ProjectPropertiesDialog(QDialog):
    def __init__(self, project_data):
        super().__init__()
        self.setWindowTitle("Propriedades do Projeto")
        self.project_data = project_data

        layout = QVBoxLayout(self)

        form_layout = QFormLayout()
        self.build_flags_edit = QTextEdit()
        self.build_flags_edit.setPlainText(project_data.get("build_flags", ""))
        form_layout.addRow("Build Flags:", self.build_flags_edit)

        self.compile_flags_edit = QTextEdit()
        self.compile_flags_edit.setPlainText(project_data.get("compile_flags", ""))
        form_layout.addRow("Compile Flags:", self.compile_flags_edit)

        layout.addLayout(form_layout)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def accept(self):
        self.project_data["build_flags"] = self.build_flags_edit.toPlainText()
        self.project_data["compile_flags"] = self.compile_flags_edit.toPlainText()
        super().accept()


class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Código")
        self.setGeometry(100, 100, 800, 600)

        self.project_data = {
            "files": [],
            "build_flags": "",
            "compile_flags": ""
        }

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

        open_action = QAction("Abrir Projeto", self)
        open_action.triggered.connect(self.open_project)
        file_menu.addAction(open_action)

        save_action = QAction("Salvar Projeto", self)
        save_action.triggered.connect(self.save_project)
        file_menu.addAction(save_action)

        save_as_action = QAction("Salvar Projeto como", self)
        save_as_action.triggered.connect(self.save_project_as)
        file_menu.addAction(save_as_action)

        properties_action = QAction("Propriedades do Projeto", self)
        properties_action.triggered.connect(self.show_project_properties)
        file_menu.addAction(properties_action)

        exit_action = QAction("Sair", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Criar toolbar
        toolbar = QToolBar("Toolbar", self)
        self.addToolBar(toolbar)

        compile_button = QAction("Compilar", self)
        compile_button.triggered.connect(self.compile_code)
        toolbar.addAction(compile_button)

        build_button = QAction("Build", self)
        build_button.triggered.connect(self.build_code)
        toolbar.addAction(build_button)

    def open_project(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.fileSelected.connect(self.load_project)
        file_dialog.exec()

    def load_project(self, file_path):
        with open(file_path, "r") as file:
            self.project_data = json.load(file)
            self.update_file_list()

    def save_project(self):
        if "project_path" not in self.project_data:
            self.save_project_as()
        else:
            self.save_project_to_path(self.project_data["project_path"])

    def save_project_as(self):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setDefaultSuffix("json")
        file_dialog.fileSelected.connect(self.save_project_to_path)
        file_dialog.exec()

    def save_project_to_path(self, file_path):
        self.project_data["project_path"] = file_path
        with open(file_path, "w") as file:
            json.dump(self.project_data, file, indent=4)

    def show_project_properties(self):
        dialog = ProjectPropertiesDialog(self.project_data)
        if dialog.exec() == QDialog.Accepted:
            # As propriedades do projeto foram atualizadas
            pass

    def compile_code(self):
        # Implemente aqui a lógica para compilar o código
        self.status_label.setText("Compilando código...")

    def build_code(self):
        # Implemente aqui a lógica para fazer o build do código
        self.status_label.setText("Fazendo build do código...")

    def update_file_list(self):
        self.file_list.clear()
        for file_path in self.project_data["files"]:
            item = QListWidgetItem(file_path)
            self.file_list.addItem(item)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Fechar', 'Deseja salvar o projeto antes de sair?',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.save_project()
        elif reply == QMessageBox.Cancel:
            event.ignore()
        else:
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    sys.exit(app.exec_())
