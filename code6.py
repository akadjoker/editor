from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QFile, QMetaObject, QFileInfo, QRect, QRegExp, QSize, QStringListModel, Qt, QTextCodec, pyqtSlot, QThread, QRunnable, Qt, QThreadPool, pyqtSignal, QObject
from PyQt5.QtGui import (QColor, QCursor, QFont, QFontDatabase, QFontInfo, QIcon, QKeySequence, QPainter,
        QPixmap, QSyntaxHighlighter, QTextBlockFormat, QTextCharFormat, QTextCursor, QFontMetrics,
        QTextDocumentWriter, QTextFormat, QTextListFormat)
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QColorDialog, QProgressBar, QStatusBar, QDesktopWidget, QRadioButton,
        QComboBox, QCompleter, QFileDialog, QFontComboBox, QGroupBox, QHBoxLayout, QListWidget, QMainWindow, QMenu, QMessageBox, QPlainTextEdit, QPushButton, QSizePolicy,
        QTextEdit, QToolBar, QSpacerItem, QVBoxLayout)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import (QFont, QTextCharFormat, QTextCursor, QTextFrameFormat,
        QTextLength, QTextTableFormat)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDialog, QWidget, QDockWidget,
        QDialogButtonBox, QGridLayout, QLabel, QLineEdit, QMainWindow,
        QMessageBox, QMenu, QTableWidget, QTableWidgetItem, QTabWidget,
        QTextEdit)
from PyQt5.QtPrintSupport import QAbstractPrintDialog, QPrintDialog, QPrinter
from PyQt5.Qsci import QsciScintilla, QsciLexerCPP


class Theme():
    class LexerCPP(QsciLexerCPP):
        def __init__(self, parent=None):
            super().__init__(parent)

        def defaultColor(self, style):
            DEFAULT = QColor(247, 247, 241)
            KEYWORD = QColor(249, 38, 114)
            DATATYPE = QColor(102, 216, 238)
            NUMBER = QColor(174, 129, 255)
            OPERATOR = QColor(249, 38, 114)
            STRING = QColor(255, 219, 116)
            FUNCTION = QColor(166, 226, 46)
            COMMENT = QColor(117, 113, 94)
            HASHCOMMENT = QColor(174, 129, 255)

            dct = {
                self.Comment: COMMENT,
                self.CommentLine: COMMENT,
                self.CommentDoc: COMMENT,
                self.CommentLineDoc: COMMENT,
                self.PreProcessorCommentLineDoc: COMMENT,
                self.Number: NUMBER,
                self.Keyword: FUNCTION,
                # self.Keyword: KEYWORD,
                self.KeywordSet2: QColor(102, 216, 238),
                self.DoubleQuotedString: STRING,
                self.SingleQuotedString: STRING,
                self.RawString: STRING,
                self.PreProcessor: QColor(0x7f, 0x7f, 0x00),
                self.Operator: DEFAULT,
            }

            return dct.get(style, DEFAULT)


class Monokai():
    def __init__(self, sci):
        self.sci = sci

        # Set default font
        sci.font = QFont()
        sci.font.setFamily('Consolas')
        sci.font.setFixedPitch(True)
        sci.font.setPointSize(8)
        sci.font.setBold(True)
        sci.setFont(sci.font)
        sci.setMarginsFont(sci.font)
        sci.setUtf8(True)

        # Set paper
        sci.setPaper(QColor(39, 40, 34))

        # Set margin defaults
        fontmetrics = QFontMetrics(sci.font)
        sci.setMarginsFont(sci.font)
        sci.setMarginWidth(0, fontmetrics.width("000") + 6)
        sci.setMarginLineNumbers(0, True)
        sci.setMarginsForegroundColor(QColor(128, 128, 128))
        sci.setMarginsBackgroundColor(QColor(39, 40, 34))
        sci.setMarginType(1, sci.SymbolMargin)
        sci.setMarginWidth(1, 12)

        #Set indentation defaults
        sci.setIndentationsUseTabs(False)
        sci.setIndentationWidth(4)
        sci.setBackspaceUnindents(True)
        sci.setIndentationGuides(True)
        sci.setFoldMarginColors(QColor(39, 40, 34), QColor(39, 40, 34))

        # Set caret defaults
        sci.setCaretForegroundColor(QColor(247, 247, 241))
        sci.setCaretWidth(2)

        #Set edge defaults
        sci.setEdgeColumn(100)
        sci.setEdgeColor(QColor('#dddddd'))
        sci.setEdgeMode(sci.EdgeLine)

        #Set folding defaults
        sci.setFolding(QsciScintilla.BoxedFoldStyle)

        # Set selection color defaults
        # sci.setSelectionBackgroundColor(QColor(61, 61, 52))
        # sci.resetSelectionForegroundColor()

        # Set scrollwidth defaults
        #sci.SendScintilla(QsciScintilla.SCI_SETSCROLLWIDTHTRACKING, 1)


class CodeEditor(QsciScintilla):
    def __init__(self, parent=None):
        QsciScintilla.__init__(self, parent)

        self.setup()

        features = [
            Theme(),
            Monokai(self)
        ]

    def setup(self):
        self.setIndentationsUseTabs(False)
        # self.setIndentationWidth(4)
        # self.setBackspaceUnindents(True)
        # self.setIndentationGuides(True)

        # self.setFoldMarginColors(QColor(30, 30, 30), QColor(30, 30, 30))
        # self.setEdgeColumn(80)
        # self.setEdgeColor(QColor('#dddddd'))
        # self.setEdgeMode(QsciScintilla.EdgeLine)
        # self.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        # self.setSelectionBackgroundColor(QColor(61, 61, 52))
        # self.resetSelectionForegroundColor()
        # self.SendScintilla(QsciScintilla.SCI_SETSCROLLWIDTHTRACKING, 1)


if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.show()
    app.exec()
