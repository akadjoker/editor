from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QAction, QMenu
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QColor, QTextCursor, QTextCharFormat, QSyntaxHighlighter,QTextDocument
from PyQt5.QtCore import Qt, QRegExp


class CppSyntaxHighlighter(QSyntaxHighlighter):
    
    def __init__(self, document):
        super().__init__(document)
        
        # Define as cores para cada tipo de token
        self.keyword_format = QTextCharFormat()
        self.keyword_format.setForeground(QColor("#c586c0"))  # Cor das palavras-chave
        self.keyword_format.setFontWeight(QFont.Bold)
        
        self.comment_format = QTextCharFormat()
        self.comment_format.setForeground(QColor("#6a9955"))  # Cor dos comentários
        self.comment_format.setFontItalic(True)
        
        self.quotation_format = QTextCharFormat()
        self.quotation_format.setForeground(QColor("#ce9178"))  # Cor das strings
        
        self.number_format = QTextCharFormat()
        self.number_format.setForeground(QColor("#b5cea8"))  # Cor dos números
        
        self.operator_format = QTextCharFormat()
        self.operator_format.setForeground(QColor("#d4d4d4"))  # Cor dos operadores
                
        # Define as palavras-chave da linguagem C ++
        self.cpp_keywords = [
            "alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel",
            "atomic_commit", "atomic_noexcept", "auto", "bitand", "bitor",
            "bool", "break", "case", "catch", "char", "char8_t", "char16_t",
            "char32_t", "class", "compl", "concept", "const", "consteval",
            "constexpr", "const_cast", "continue", "co_await", "co_return",
            "co_yield", "decltype", "default", "delete", "do", "double",
            "dynamic_cast", "else", "enum", "explicit", "export", "extern",
            "false", "float", "for", "friend", "goto", "if", "inline",
            "int", "long", "mutable", "namespace", "new", "noexcept", "not",
            "not_eq", "nullptr", "operator", "or", "or_eq", "private",
            "protected", "public", "reflexpr", "register", "reinterpret_cast",
            "requires", "return", "short", "signed", "sizeof", "static",
            "static_assert", "static_cast", "struct", "switch", "synchronized",
            "template", "this", "thread_local", "throw", "true", "try", "typedef",
            "typeid", "typename", "union", "unsigned", "using", "virtual",
            "void", "volatile", "wchar_t", "while", "xor", "xor_eq"
        ]
        
        # Define os operadores
        self.operators = [
            "+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "++", "--", "+=",
            "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<", ">>", "<<=", ">>="
        ]
    
    def highlightBlock(self, text):
        # Destaca as palavras-chave
        for word in self.cpp_keywords:
            pattern = "\\b{}\\b".format(word)
            self.highlight(pattern, text, self.keyword_format)
        
        # Destaca os comentários
        self.highlight("//[^\n]*", text, self.comment_format)  # Comentário de linha única
        self.highlight("/\\*.*?\\*/", text, self.comment_format)  # Comentário de várias linhas
        
        # Destaca as strings
        self.highlight("\".*?\"", text, self.quotation_format)
        self.highlight("'.*?'", text, self.quotation_format)
        
        # Destaca os números
        self.highlight("\\b[0-9]+\\b", text, self.number_format)
        
        # Destaca os operadores
        for operator in self.operators:
            pattern = "\\{}".format(operator) if operator in ["*", "+", "?"] else operator
            self.highlight(pattern, text, self.operator_format)

    def highlight(self, pattern, text, format):
        """Aplica a formatação para as string que fazem match no padrão"""
        regex = QRegExp(pattern)
        index = regex.indexIn(text)
        # while index >= 0:
        #     length = regex.matchedLength()
        #     self.setFormat(index, length, format)
        #     index = regex.indexIn(text, index + length)


class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de C/C++")
        self.setGeometry(100, 100, 800, 600)


        document = QTextDocument()
        highlighter = CppSyntaxHighlighter(document)
      
        # Criar widget de edição QTextEdit
        self.editor = QTextEdit(self)
        self.editor.setDocument(document)
        self.editor.setPlainText("int main() {\n    printf(\"Hello, world!\\n\");\n    return 0;\n}")
        font = QFont('Consolas', 12)
        self.editor.setFont(font)
        self.setCentralWidget(self.editor)

         
        
        
        
         # Definindo o destaque de sintaxe




if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.show()
    app.exec_()