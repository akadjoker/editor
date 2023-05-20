from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QAction
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
        format1.setForeground(QColor('#000080'))  # Azul escuro
        format2 = QTextCharFormat()
        format2.setForeground(QColor('#0000FF'))  # Azul

        # Definindo palavras-chave da linguagem C e C++
        keywords_c = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
                      'do', 'double', 'else', 'enum', 'extern', 'float', 'for',
                      'goto', 'if', 'int', 'long', 'register', 'return', 'short',
                      'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef',
                      'union', 'unsigned', 'void', 'volatile', 'while']
        keywords_cpp = keywords_c + ['asm', 'bool', 'catch', 'class', 'const_cast',
                                     'delete', 'dynamic_cast', 'explicit', 'export',
                                     'false', 'friend', 'inline', 'mutable', 'namespace',
                                     'new', 'operator', 'private', 'protected', 'public',
                                     'reinterpret_cast', 'static_cast', 'template',
                                     'this', 'throw', 'true', 'try', 'typeid', 'typename',
                                     'using', 'virtual']

        # Definindo regras de destaque de sintaxe para a linguagem C
        rules_c = [(r'\b{}\b'.format(keyword), format1) for keyword in keywords_c]

        # Definindo regras de destaque de sintaxe para a linguagem C++
        rules_cpp = [(r'\b{}\b'.format(keyword), format2) for keyword in keywords_cpp]

        # Combinação de regras para ambas as linguagens
        self.highlight_rules = rules_c + rules_cpp

        # Adicionar ação do menu "Open"
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)

        # Criar menu "File" e adicionar ação "Open"
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(open_action)

    def highlight_text(self):
        """Aplica o destaque de sintaxe ao texto do editor."""
        text = self.editor.toPlainText()
        cursor = self.editor.textCursor()

        for pattern, fmt in self.highlight_rules:
            expression = QRegExp(pattern)
            start = 0
            index = expression.indexIn(text, start)
            while index >= 0:
                length = expression.matchedLength()
                cursor.setPosition(index)
                cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, length)
                cursor.mergeCharFormat(fmt)
                start = index + length
                index = expression.indexIn(text, start)

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
