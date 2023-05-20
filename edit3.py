from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit
from PyQt5.QtGui import QFont, QColor, QTextCursor
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
        self.syntax_colors = {
            'background': QColor('#1E1E1E'),      # Cor de fundo
            'text': QColor('#D4D4D4'),            # Cor do texto
            'keyword': QColor('#569CD6'),         # Cor das palavras-chave
            'number': QColor('#B5CEA8'),          # Cor dos números
            'string': QColor('#CE9178'),          # Cor das strings
            'comment': QColor('#6A9955'),         # Cor dos comentários
        }

        # Definindo folha de estilo para o editor de texto
        style_sheet = """
            QTextEdit {
                background-color: %(background)s;
                color: %(text)s;
                selection-background-color: #264F78;
                selection-color: %(text)s;
            }

            QTextEdit:focus {
                border: 2px solid #528BBD;
            }

            QTextEdit::Whitespace {
                background-color: %(background)s;
            }

            QTextEdit::LineNumber {
                color: %(keyword)s;
            }

            QTextEdit::Text {
                color: %(text)s;
            }

            QTextEdit::Normal {
                color: %(text)s;
            }

            QTextEdit::Keyword {
                color: %(keyword)s;
            }

            QTextEdit::Comment {
                color: %(comment)s;
            }

            QTextEdit::Number {
                color: %(number)s;
            }

            QTextEdit::String {
                color: %(string)s;
            }
        """ % self.syntax_colors
        self.editor.setStyleSheet(style_sheet)

        # Aplicar destaque de sintaxe ao abrir um arquivo
        self.open_file()

    def highlight_text(self):
        """Aplica o destaque de sintaxe ao texto do editor."""
        cursor = self.editor.textCursor()
        text = cursor.document().toPlainText()

        # Implemente aqui a lógica para o destaque de sintaxe
        # Utilize o cursor para aplicar os formatos de estilo necessários

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
