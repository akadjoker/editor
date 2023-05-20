from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QAction, QMenu
from PyQt5.QtGui import QFont, QColor, QTextCursor, QTextCharFormat, QSyntaxHighlighter, QPalette,QTextDocument
from PyQt5.QtCore import Qt, QRegExp

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de C/C++")
        self.setGeometry(100, 100, 800, 600)

        self.document = QTextDocument()
      
        # Criar widget de edição QTextEdit
        self.editor = QTextEdit(self)
        self.editor.setDocument(self.document)
        self.editor.setPlainText("int main() {\n    printf(\"Hello, world!\\n\");\n    return 0;\n}")
        font = QFont('Consolas', 12)
        self.editor.setFont(font)
        self.setCentralWidget(self.editor)

        # Definindo o destaque de sintaxe
        self.highlight_syntax()

        # Aplicar tema Modern Dark
        self.set_modern_dark_theme()

        # Adicionar menu "File" com opção "Open"
        self.add_file_menu()

    def highlight_syntax(self):
        """Realça a sintaxe do código C/C++."""
        highlighter = SyntaxHighlighter(self.document)

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))
        keyword_format.setFontWeight(QFont.Bold)

        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))

        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))

        operator_format = QTextCharFormat()
        operator_format.setForeground(QColor("#D4D4D4"))

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))

        directive_format = QTextCharFormat()
        directive_format.setForeground(QColor("#D4D4D4"))

        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#DCDCAA"))

        preprocessor_format = QTextCharFormat()
        preprocessor_format.setForeground(QColor("#C586C0"))

        variable_format = QTextCharFormat()
        variable_format.setForeground(QColor("#4EC9B0"))


        keywords = [
            "auto", "break", "case", "char","false","true", "bool","const", "continue", "default", "do",
            "double", "else", "enum", "extern", "float", "for", "goto", "if", "int",
            "long", "register", "return", "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union", "unsigned", "void", "volatile",
            "while"
        ]

        for keyword in keywords:
            pattern = "\\b" + keyword + "\\b"
            expression = QRegExp(pattern)
            highlighter.setFormatForPattern(expression, keyword_format)

        punctuation_format = QTextCharFormat()
        punctuation_format.setForeground(QColor("#D4D4D4"))

        punctuation_patterns = [
            "\\.", ",", ";", ":", "\\(", "\\)", "\\{", "\\}", "\\[", "\\]"
        ]

        for pattern in punctuation_patterns:
            expression = QRegExp(pattern)
            highlighter.setFormatForPattern(expression, punctuation_format)

        number_pattern = QRegExp("\\b\\d+\\b")
        highlighter.setFormatForPattern(number_pattern, number_format)

        string_pattern = QRegExp("\".*\"")
        highlighter.setFormatForPattern(string_pattern, string_format)

        operator_pattern = QRegExp("[+\\-*/=]")
        highlighter.setFormatForPattern(operator_pattern, operator_format)

        comment_pattern = QRegExp("//[^\n]*")
        highlighter.setFormatForPattern(comment_pattern, comment_format)

        directive_pattern = QRegExp("#\\w+")
        highlighter.setFormatForPattern(directive_pattern, directive_format)

        function_pattern = QRegExp("\\b\\w+\\s*(?=\\()")
        highlighter.setFormatForPattern(function_pattern, function_format)



    def set_modern_dark_theme(self):
        """Define o tema Modern Dark para o editor de texto."""
        palette = self.editor.palette()
        palette.setColor(QPalette.Base, QColor("#1E1E1E"))
        palette.setColor(QPalette.Text, QColor("#D4D4D4"))
        palette.setColor(QPalette.Highlight, QColor("#264F78"))
        palette.setColor(QPalette.HighlightedText, QColor("#D4D4D4"))
        self.editor.setPalette(palette)

    def add_file_menu(self):
        """Adiciona um menu 'File' com opção 'Open'."""
        open_action = OpenFileAction(self)
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(open_action)

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)
        self.highlight_rules = []

    def highlightBlock(self, text):
        """Realça um bloco de texto."""
        for pattern, format in self.highlight_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

    def setFormatForPattern(self, pattern, format):
        """Define o formato de destaque para um padrão de expressão regular."""
        highlight_rule = (pattern, format)
        self.highlight_rules.append(highlight_rule)

class OpenFileAction(QAction):
    def __init__(self, parent):
        super().__init__("Open", parent)
        self.setShortcut("Ctrl+O")
        self.triggered.connect(self.open_file)

    def open_file(self):
        """Abre um arquivo para edição."""
        filename, _ = QFileDialog.getOpenFileName(self.parent(), "Open File", "", "C/C++ Files (*.c *.cpp)")
        if filename:
            with open(filename, "r") as file:
                content = file.read()
            self.parent().editor.setPlainText(content)

if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.show()
    app.exec_()
