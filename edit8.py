        
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QAction, QMenu,QWidget,QVBoxLayout, QLabel,QHBoxLayout
from PyQt5.QtGui import QFont, QColor, QTextCursor, QTextCharFormat, QSyntaxHighlighter, QPalette,QTextDocument, QPainter
from PyQt5.QtCore import Qt, QRegExp, QRegularExpression, QRect, QSize,QPoint

class NumberBar(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor
        self.editor.verticalScrollBar().valueChanged.connect(self.update_bar)
        self.setGeometry(0,0,300,30)

    def update_bar(self, value):
        self.update()

    def paintEvent(self, event):
        block = self.editor.firstVisibleBlock()
        height = self.editor.fontMetrics().height()
        number = block.blockNumber() + 1

        painter = QPainter(self)
        painter.fillRect(event.rect(), QColor("#2B2B2B"))
        painter.setPen(QColor("#BBBBBB"))
        painter.drawText(5,5,self.width(),100,"dasd", Qt.AlignRight, text)
        while block.isValid():
            offset = self.editor.contentOffset().y()
            position = self.editor.document().documentLayout().blockBoundingRect(block).topLeft() - QPoint(0, offset)
            position_x = self.width() - painter.fontMetrics().width(text) - 5
            text = str(number)
            painter.drawText(position_x, position.y()+height, self.width(), height, Qt.AlignRight, text)

            block = block.next()
            number += 1

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de C/C++")
        self.setGeometry(100, 100, 800, 600)

        self.document = QTextDocument()
      
        # Criar widget de edição QTextEdit
        self.editor = QTextEdit(self)
        font = self.editor.font()
        font.setPointSize(font.pointSize() + 2)
        self.setFont(font)
        self.editor.setDocument(self.document)
        self.editor.setPlainText('''
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
} 

        ''')
        font = QFont('Consolas', 12)
        self.editor.setFont(font)
        #self.setCentralWidget(self.editor)
        layout = QHBoxLayout()
        self.number_bar = NumberBar(self.editor)
        layout.addWidget(self.number_bar)
        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

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
        comment_format.setForeground(QColor("#57A64A"))

        preprocessor_format = QTextCharFormat()
        preprocessor_format.setForeground(QColor("#C586C0"))

        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#DCDCAA"))



        keywords_c = ["false","true", "bool",'auto', 'break', 'case', 'char', 'const', 'continue', 'default',
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

    
        for keyword in keywords_cpp:
            pattern = "\\b" + keyword + "\\b"
            expression = QRegExp(pattern)
            highlighter.setFormatForPattern(expression, keyword_format)

        number_pattern = QRegExp("\\b\\d+\\b")
        highlighter.setFormatForPattern(number_pattern, number_format)

        string_pattern = QRegExp("\".*\"")
        highlighter.setFormatForPattern(string_pattern, string_format)

        operator_pattern = QRegExp("[+\\-*/=]")
        highlighter.setFormatForPattern(operator_pattern, operator_format)

        comment_pattern = QRegExp("//[^\n]*")
        highlighter.setFormatForPattern(comment_pattern, comment_format)
        
        multiline_comment_pattern = QRegExp("/\\*[^*]*\\*+([^/*][^*]*\\*+)*/")
        highlighter.setFormatForPattern(multiline_comment_pattern, comment_format)

        preprocessor_pattern = QRegExp("#[^\n]*")
        highlighter.setFormatForPattern(preprocessor_pattern, preprocessor_format)

        include_pattern = QRegExp("#include\\s*<.*>")
        highlighter.setFormatForPattern(include_pattern, preprocessor_format)

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
