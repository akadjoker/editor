

import sys
import json
import os
from PyQt5.QtWidgets import QApplication,QListWidget,QPlainTextEdit,QTabWidget,  QMessageBox,QComboBox,QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QListView, QListWidgetItem, QAction, QMenuBar, QToolBar, QStatusBar, QDockWidget, QSizePolicy, QDialog, QFormLayout, QLineEdit, QTextEdit, QDialogButtonBox, QRadioButton, QGroupBox
from PyQt5.QtGui import QKeySequence, QIcon, QFont,QTextCursor
from PyQt5.QtCore import Qt




class ProjectType:
    APPLICATION = 0
    LIBRARY = 1


class LibraryType:
    STATIC = 0
    SHARED = 1

class Platform:
    LINUX = 0
    WEB = 1
    ANDROID = 2
    WINDOWS = 3

class ProjectPropertiesDialog(QDialog):
    def __init__(self, project_data):
        super().__init__()
        self.setWindowTitle("Propriedades do Projeto")
        self.project_data = project_data

        layout = QVBoxLayout(self)

        self.project_type_group = QGroupBox("Tipo de Projeto")
        self.project_type_radio_application = QRadioButton("Aplicação")
        self.project_type_radio_library = QRadioButton("Biblioteca")
        self.project_type_layout = QVBoxLayout(self.project_type_group)
        self.project_type_layout.addWidget(self.project_type_radio_application)
        self.project_type_layout.addWidget(self.project_type_radio_library)

        self.library_type_group = QGroupBox("Tipo de Biblioteca")
        self.library_type_radio_static = QRadioButton("Static")
        self.library_type_radio_shared = QRadioButton("Shared")
        self.library_type_layout = QVBoxLayout(self.library_type_group)
        self.library_type_layout.addWidget(self.library_type_radio_static)
        self.library_type_layout.addWidget(self.library_type_radio_shared)

        form_layout = QFormLayout()
        form_layout.addRow("Build Flags:", QTextEdit(self.project_data.get("build_flags", "")))
        form_layout.addRow("Compile Flags:", QTextEdit(self.project_data.get("compile_flags", "")))
        form_layout.addRow(self.project_type_group)

        self.project_type_radio_application.toggled.connect(self.update_library_type_options)
        form_layout.addRow(self.library_type_group)

        layout.addLayout(form_layout)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.update_library_type_options()
        self.load_project_data()

    def update_library_type_options(self):
        is_library = self.project_type_radio_library.isChecked()
        self.library_type_group.setEnabled(is_library)
        self.library_type_radio_static.setEnabled(is_library)
        self.library_type_radio_shared.setEnabled(is_library)

        if not is_library:
            self.library_type_radio_static.setChecked(False)
            self.library_type_radio_shared.setChecked(False)

    def load_project_data(self):
        project_type = self.project_data.get("project_type", ProjectType.APPLICATION)
        library_type = self.project_data.get("library_type", LibraryType.STATIC)

        self.project_type_radio_application.setChecked(project_type == ProjectType.APPLICATION)
        self.project_type_radio_library.setChecked(project_type == ProjectType.LIBRARY)

        self.library_type_radio_static.setChecked(library_type == LibraryType.STATIC)
        self.library_type_radio_shared.setChecked(library_type == LibraryType.SHARED)

        self.update_library_type_options()

    def accept(self):
        self.project_data["build_flags"] = self.findChild(QTextEdit).toPlainText()
        self.project_data["compile_flags"] = self.findChildren(QTextEdit)[1].toPlainText()
        self.project_data["project_type"] = ProjectType.LIBRARY if self.project_type_radio_library.isChecked() else ProjectType.APPLICATION
        self.project_data["library_type"] = LibraryType.SHARED if self.library_type_radio_shared.isChecked() else LibraryType.STATIC
        super().accept()


class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cross Editor By @DjokerSoft")
        self.setGeometry(100, 100, 900, 800)
        self.plataform = Platform.LINUX
        font = QFont("FontAwesome", 12)
        QApplication.instance().setFont(font)

        self.project_data = {
            "files": [],
            "build_flags": "",
            "compile_flags": "",
            "project_type": ProjectType.APPLICATION,
            "library_type": LibraryType.STATIC
        }

       
        self.codeTab = QTabWidget()
        self.codeTab.setTabBarAutoHide(False)
        self.codeTab.setMovable(True)
        self.codeTab.setTabsClosable(True)


        # Criar editor de texto
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.codeTab)
        self.text_edit.textChanged.connect(self.update_toolbar)
        #self.text_edit.copyAvailable.connect(self.update_toolbar)
        self.codeTab.addTab(self.text_edit, "no name")

        
        # Criar console
        self.console_edit = QPlainTextEdit()
        dock_console = QDockWidget("Console", self)
        dock_console.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock_console)
        dock_console.setWidget(self.console_edit)

       
        # Criar status bar
        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)
        self.status_label = QLabel("Pronto")
        status_bar.addWidget(self.status_label)

        # Criar menu
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        project_menu = menu_bar.addMenu("Code")
        
        new_action = QAction("Open", self)
        open_action.triggered.connect(self.new_file)
        project_menu.addAction(new_action)


        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        project_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        project_menu.addAction(save_action)

        save_as_action = QAction("Save", self)
        save_as_action.triggered.connect(self.save_file_as)
        project_menu.addAction(save_as_action)

        properties_action = QAction("Options", self)
        properties_action.triggered.connect(self.show_code_properties)
        project_menu.addAction(properties_action)
        
        #file_menu.addSeparator()
      

        # Criar toolbar
        toolbar = QToolBar("Toolbar", self)
        self.addToolBar(toolbar)

        rsrcPath = os.getcwd()+os.path.sep+"res"+os.path.sep
        compile_button = toolbar.addAction( QIcon(rsrcPath + 'build.xpm'),"Build")
     
        
        compile_button.triggered.connect(self.compile_code)
        toolbar.addAction(compile_button)
        build_button = toolbar.addAction( QIcon(rsrcPath + 'buildrun.xpm'),"Build and run")
        build_button.triggered.connect(self.build_code)
        toolbar.addAction(build_button)


        run_button = QAction(QIcon(rsrcPath + 'Go.png'), "Run", self)
        toolbar.addAction(run_button)
        run_button.triggered.connect(self.run_code)

        clean_button = QAction(QIcon(rsrcPath + 'clean.png'), "Clean", self)
        toolbar.addAction(clean_button)
        run_button.triggered.connect(self.clean_code)

        platform_combo = QComboBox()
        platform_combo.addItem("Linux")
        platform_combo.addItem("Web")
        platform_combo.addItem("Android")
        platform_combo.addItem("Windows")
        toolbar.addWidget(platform_combo)
        #platform_combo.currentTextChanged.connect(self.set_platform)
        platform_combo.currentIndexChanged.connect(self.set_platform)

        separator = toolbar.addSeparator()
        self.undo_action = QAction(QIcon.fromTheme("edit-undo"), "Undo", self)
        self.undo_action.setShortcut(QKeySequence.Undo)
        toolbar.addAction(self.undo_action)

        self.redo_action = QAction(QIcon.fromTheme("edit-redo"), "Redo", self)
        self.redo_action.setShortcut(QKeySequence.Redo)
        toolbar.addAction(self.redo_action)

        self.copy_action = QAction(QIcon.fromTheme("edit-copy"), "Copy", self)
        self.copy_action.setShortcut(QKeySequence.Copy)
        toolbar.addAction(self.copy_action)

        self.paste_action = QAction(QIcon.fromTheme("edit-paste"), "Paste", self)
        self.paste_action.setShortcut(QKeySequence.Paste)
        toolbar.addAction(self.paste_action)

     
        # self.undo_action.triggered.connect(self.undo)
        # self.redo_action.triggered.connect(self.redo)
        # self.copy_action.triggered.connect(self.copy)
        # self.paste_action.triggered.connect(self.paste)

      
        self.undo_action.setEnabled(False)
        self.redo_action.setEnabled(False)
        self.copy_action.setEnabled(False)
        #self.paste_action.setEnabled(False)



        # Criar menu Compiler
        compiler_menu = menu_bar.addMenu("Compiler")

        compile_action = compiler_menu.addAction( QIcon(rsrcPath + 'build.xpm'),"Build")
        compile_action.triggered.connect(self.compile_code)
        compiler_menu.addAction(compile_action)

        build_action = compiler_menu.addAction( QIcon(rsrcPath + 'buildrun.xpm'),"Build and run")
        build_action.triggered.connect(self.build_code)
        compiler_menu.addAction(build_action)

        clean_action =QAction(QIcon(rsrcPath + 'clean.png'), "Clean", self)
        build_action.triggered.connect(self.clean_code)
        compiler_menu.addAction(clean_action)
    


    def update_toolbar(self):
        if self.text_edit.textCursor().hasSelection():
            self.copy_action.setEnabled(True)
        else:
            self.copy_action.setEnabled(False)
    
        cursor = self.text_edit.textCursor()

        if cursor.position() <= len(self.text_edit.toPlainText()):
            self.undo_action.setEnabled(self.text_edit.document().isUndoAvailable())
            self.redo_action.setEnabled(self.text_edit.document().isRedoAvailable())
            #self.paste_action.setEnabled(self.text_edit.canPaste())

        # Verifica se a posição do cursor é válida antes de atualizá-la
        new_position = self.text_edit.document().characterCount() - 1
        if cursor.position() > new_position:
            cursor.setPosition(new_position, QTextCursor.KeepAnchor)
            self.text_edit.setTextCursor(cursor)




    def set_platform(self, platform):
        #self.project_data["platform"] = Platform(platform)
        if platform==0:
            self.plataform = Platform.LINUX
        elif platform==1:
            self.plataform = Platform.WEB
        elif platform==2:
            self.plataform = Platform.ANDROID
        elif platform==3:
            self.plataform = Platform.WINDOWS
            
        print("Plataforma selecionada:", platform)

    def clean_code(self):
        print("Plataforma selecionada:", self.plataform)
    def run_code(self):
        print("Plataforma selecionada:", self.plataform)

    def undo(self):
        self.text_edit.undo()

    def redo(self):
        self.text_edit.redo()

    def copy(self):
        self.text_edit.copy()

    def paste(self):
        self.text_edit.paste()

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.fileSelected.connect(self.load_project)
        file_dialog.exec()

    def load_file(self, file_path):
        #with open(file_path, "r") as file:
        pass
            
            

    def save_file(self):
        pass
  
    def save_project_as(self):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setDefaultSuffix("cpp")
        file_dialog.fileSelected.connect(self.save_file_to_path)
        file_dialog.exec()

    def save_file_to_path(self, file_path):
        pass
        

    def show_file_properties(self):
        dialog = ProjectPropertiesDialog(self.project_data)
        if dialog.exec() == QDialog.Accepted:
            self.project_data = dialog.project_data

    def compile_code(self):
        self.status_label.setText("Compilando código...")

    def build_code(self):
        self.status_label.setText("Fazendo build do código...")


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
