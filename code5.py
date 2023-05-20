from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QFontMetrics
from PyQt5.QtWidgets import QApplication
from PyQt5.Qsci import QsciScintilla, QsciLexerCPP


class CodeEditor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Configurações gerais do editor
        self.setup_editor()

        # Configuração do tema e lexer
        self.setup_theme()
        self.setup_lexer()

    def setup_editor(self):
        self.setAutoCompletionThreshold(1)
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setBackspaceUnindents(True)
        self.setIndentationGuides(True)
        self.setFolding(QsciScintilla.CircledTreeFoldStyle)
        self.setWrapMode(QsciScintilla.WrapNone)
        self.setCaretWidth(2)
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor(239, 240, 241))
        self.setCaretForegroundColor(QColor(0, 0, 0))
        self.setMarginsBackgroundColor(QColor(39, 40, 34))
        self.setMarginsForegroundColor(QColor(128, 128, 128))
        self.setMarginLineNumbers(0, True)
        self.setMarginWidth(0, self.font_metrics().width("000") + 6)

    def setup_theme(self):
        # Configurações de cores do tema
        bg_color = QColor(39, 40, 34)
        fg_color = QColor(247, 247, 241)
        self.setPaper(bg_color)
        self.setColor(fg_color)
        self.setMarginsBackgroundColor(bg_color)
        self.setMarginsForegroundColor(QColor(128, 128, 128))

        # Configuração da barra de rolagem
        scroll_bar_style = """
            QScrollBar:vertical {
                background-color: #282a36;
                width: 16px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #44475a;
                min-height: 20px;
            }
            QScrollBar:horizontal {
                background-color: #282a36;
                height: 18px;
                margin: 0px;
            }
            QScrollBar::handle:horizontal {
                background-color: #44475a;
                min-width: 30px;
            }
            QScrollBar::add-line:vertical {
                background: none;
            }
            QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: none;
            }
        """
        self.setStyleSheet(scroll_bar_style)

    def setup_lexer(self):
        lexer = QsciLexerCPP(self)
        lexer.setDefaultColor(QColor(247, 247, 241))
        lexer.setColor(QColor(249, 38, 114), QsciLexerCPP.Keyword)
        lexer.setColor(QColor(174, 129, 255), QsciLexerCPP.Number)
        lexer.setColor(QColor(249, 38, 114), QsciLexerCPP.Operator)
        lexer.setColor(QColor(117, 113, 94), QsciLexerCPP.Comment)
        self.setLexer(lexer)

    def font_metrics(self):
        font = QFont()
        font.setFamily('Consolas')
        font.setFixedPitch(True)
        font.setPointSize(12)
        font.setBold(False)
        return QFontMetrics(font)

    def setMarginWidth(self, margin, width):
        """
        Redefine o método setMarginWidth para atualizar a largura da margem
        corretamente ao alterar a fonte.
        """
        super().setMarginWidth(margin, self.font_metrics().width("000") + 6)

    def resizeEvent(self, event):
        """
        Redefine o evento resizeEvent para atualizar a largura da margem ao
        redimensionar a janela.
        """
        super().resizeEvent(event)
        self.setMarginWidth(0, self.font_metrics().width("000") + 6)


if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.show()
    app.exec()
