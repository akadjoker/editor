from PyQt5.QtWidgets import QApplication
from PyQt5.Qsci import *

class CodeEditor(QsciScintilla):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de C/C++")
        self.setGeometry(100, 100, 800, 600)

        # Configurar o lexer para a linguagem C/C++
        lexer = QsciLexerCPP()
        self.setLexer(lexer)

        # Configurar estilos de formatação
        self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Consolas')
        self.SendScintilla(QsciScintilla.SCI_STYLESETSIZE, 1, 12)

        self.SendScintilla(QsciScintilla.SCI_STYLESETFORE, QsciScintilla.CPP_COMMENTLINE, 0x008000)  # Comentários
        self.SendScintilla(QsciScintilla.SCI_STYLESETFORE, QsciScintilla.CPP_STRING, 0xA31515)  # Strings
        self.SendScintilla(QsciScintilla.SCI_STYLESETFORE, QsciScintilla.CPP_NUMBER, 0x9F9F00)  # Números
        self.SendScintilla(QsciScintilla.SCI_STYLESETFORE, QsciScintilla.CPP_OPERATOR, 0x808080)  # Operadores

        # Aplicar tema escuro
        self.setPaper(QColor("#1E1E1E"))
        self.setColor(QColor("#D4D4D4"))

if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.show()
    app.exec()
