from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit
from PyQt5.QtGui import QFont, QTextCharFormat, QColor, QTextCursor
from PyQt5.QtCore import Qt, QRegExp

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de C/C++")
        self.setGeometry(100, 100, 800, 600)

        # Criar widget de edição QTextEdit
        self.editor = QTextEdit(self)
        font = QFont('Consolas', 12)
        self.editor.setFont(font)
        self.setCentralWidget(self.editor)

        # Definindo cores para destaque de sintaxe
        format1 = QTextCharFormat()
        format1.setForeground(QColor("#C8C8C8"))  # Cor do texto
        format2 = QTextCharFormat()
        format2.setForeground(QColor("#4EC9B0"))  # Cor do destaque de sintaxe

        # Definindo folha de estilo
        style_sheet = """
            QTextEdit {
                background-color: #1E1E1E;  /* Cor de fundo */
                color: #C8C8C8;  /* Cor do texto */
                selection-background-color: #375F7F;  /* Cor da seleção de texto */
            }
            
            QTextEdit:focus {
                border: 2px solid #4EC9B0;  /* Cor da borda quando o widget tem foco */
            }
        """
        self.editor.setStyleSheet(style_sheet)

    def highlight_text(self):
        """Aplica o destaque de sintaxe ao texto do editor."""
        text = self.editor.toPlainText()
        cursor = self.editor.textCursor()

        # Restante do código de destaque de sintaxe...

    def open_file(self):
        """Abre um arquivo para edição."""
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "C/C++ Files (*.c *.cpp)")
        if filename:
            with open(filename, "r") as file:
                content = file.read()
            self.editor.setPlainText(content)
            self.highlight_text()


if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.show()
    app.exec_()
