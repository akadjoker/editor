
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QFile, QMetaObject,QFileInfo, QRect, QRegExp, QSize, QStringListModel, Qt, QTextCodec, pyqtSlot,QThread,QRunnable, Qt, QThreadPool,pyqtSignal,QObject

from PyQt5.QtGui import (QColor, QCursor, QFont, QFontDatabase, QFontInfo, QIcon, QKeySequence, QPainter,
        QPixmap, QSyntaxHighlighter, QTextBlockFormat, QTextCharFormat, QTextCursor,QFontMetrics,
        QTextDocumentWriter, QTextFormat, QTextListFormat)
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QColorDialog, QProgressBar,QStatusBar,QDesktopWidget,QRadioButton,
        QComboBox, QCompleter, QFileDialog, QFontComboBox, QGroupBox, QHBoxLayout, QListWidget, QMainWindow, QMenu, QMessageBox, QPlainTextEdit, QPushButton, QSizePolicy,
        QTextEdit, QToolBar,QSpacerItem,QVBoxLayout)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import (QFont, QTextCharFormat, QTextCursor, QTextFrameFormat,
        QTextLength, QTextTableFormat)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDialog, QWidget,QDockWidget,
        QDialogButtonBox, QGridLayout, QLabel, QLineEdit, QMainWindow,
        QMessageBox, QMenu, QTableWidget, QTableWidgetItem, QTabWidget,
        QTextEdit)
from PyQt5.QtPrintSupport import QAbstractPrintDialog, QPrintDialog, QPrinter
from PyQt5.Qsci import *


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
                self.UnclosedString: STRING,
                self.VerbatimString: STRING,
                self.TripleQuotedVerbatimString: STRING,
                self.HashQuotedString: STRING,
                self.Regex: QColor(0x3f, 0x7f, 0x3f),
                self.CommentDocKeyword: QColor(0x30, 0x60, 0xa0),
                self.CommentDocKeywordError: QColor(0x80, 0x40, 0x20),
                self.PreProcessorComment: QColor(0x65, 0x99, 0x00),
                self.InactiveDefault: QColor(0xc0, 0xc0, 0xc0),
                self.InactiveUUID: QColor(0xc0, 0xc0, 0xc0),
                self.InactiveCommentLineDoc: QColor(0xc0, 0xc0, 0xc0),
                self.InactiveKeywordSet2: QColor(0xc0, 0xc0, 0xc0),
                self.InactiveCommentDocKeyword: QColor(0xc0, 0xc0, 0xc0),
                self.InactiveCommentDocKeywordError: QColor(0xc0, 0xc0, 0xc0),
                self.InactivePreProcessorCommentLineDoc: QColor(0xc0, 0xc0, 0xc0),
                self.InactiveComment: QColor(0x90, 0xb0, 0x90),
                self.InactiveCommentLine: QColor(0x90, 0xb0, 0x90),
                self.InactiveNumber: QColor(174, 129, 255),
                self.InactiveVerbatimString: STRING,
                self.InactiveTripleQuotedVerbatimString: STRING,
                self.InactiveHashQuotedString: QColor(0x90, 0xb0, 0x90),
                self.InactiveCommentDoc: QColor(0xd0, 0xd0, 0xd0),
                self.InactiveKeyword: QColor(0x90, 0x90, 0xb0),
                self.InactiveDoubleQuotedString: STRING,
                self.InactiveSingleQuotedString: STRING,
                self.InactiveRawString: STRING,
                self.InactivePreProcessor: QColor(0xb0, 0xb0, 0x90),
                self.InactiveOperator: QColor(0xb0, 0xb0, 0xb0),
                self.InactiveIdentifier: QColor(0xb0, 0xb0, 0xb0),
                self.InactiveGlobalClass: QColor(0xb0, 0xb0, 0xb0),
                self.InactiveUnclosedString: STRING,
                self.InactiveRegex: QColor(0x7f, 0xaf, 0x7f),
                self.InactivePreProcessorComment: QColor(0xa0, 0xc0, 0x90),
                self.UserLiteral: QColor(0xc0, 0x60, 0x00),
                self.InactiveUserLiteral: QColor(0xd7, 0xa0, 0x90),
                self.TaskMarker: QColor(0xbe, 0x07, 0xff),
                self.InactiveTaskMarker: QColor(0xc3, 0xa1, 0xcf)
            }

            return dct.get(style, DEFAULT)

        def defaultPaper(self, style):
            # return self.parent().paper()
            return QColor(39, 40, 34)

        def defaultFont(self, style):
            font = QFont()
            font.setFamily('Consolas')
            font.setFixedPitch(True)
            font.setPointSize(12)
            font.setBold(False)
            return font

    def __init__(self, sci):
        self.sci = sci

        sci.setFolding(QsciScintilla.CircledFoldStyle)
        sci.setMarginType(1, QsciScintilla.NumberMargin)
        sci.setMarginSensitivity(1, True)
        sci.markerDefine(QsciScintilla.RightArrow, 8)
        sci.setMarkerBackgroundColor(QColor("#ee1111"), 8)

        lexer = self.LexerCPP()
        lexer.setFoldAtElse(True)
        lexer.setFoldComments(True)
        lexer.setFoldCompact(False)
        lexer.setFoldPreprocessor(True)
        sci.setLexer(lexer)


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

        # Set indentation defaults
        sci.setIndentationsUseTabs(False)
        sci.setIndentationWidth(4)
        sci.setBackspaceUnindents(True)
        sci.setIndentationGuides(True)
        # sci.setIndentationGuidesBackgroundColor(QColor("#2a2b24"))
        # sci.setIndentationGuidesForegroundColor(QColor("#2a2b24"))
        sci.setFoldMarginColors(QColor(39, 40, 34), QColor(39, 40, 34))
        # sci.setEolMode(QsciScintilla.EolUnix)

       


        sci.setWrapMode(sci.WrapNone)

        # Set selection color defaults
        sci.setSelectionBackgroundColor(QColor(61, 61, 52))
        sci.resetSelectionForegroundColor()

        # Set scrollwidth defaults
        sci.SendScintilla(QsciScintilla.SCI_SETSCROLLWIDTHTRACKING, 1)



        # Set multiselection defaults
        sci.SendScintilla(QsciScintilla.SCI_SETMULTIPLESELECTION, True)
        sci.SendScintilla(QsciScintilla.SCI_SETMULTIPASTE, 1)
        sci.SendScintilla(QsciScintilla.SCI_SETADDITIONALSELECTIONTYPING, True)
  

class CodeEditor(QsciScintilla):
    comment_string = "// "
    line_ending = "\n"
    def __init__(self,parent=None):
        QsciScintilla.__init__(self, parent)

        self.setup()

        self.currentLine=0
        self.currentCursor=0

        features = [
        Theme(self),
        Monokai(self)    ]
        self.setup()
        self.cursorPositionChanged.connect(self.OncursorPositionChanged)

        
    def enterEvent(self, event):
        pass      
    def leaveEvent(self, event):
        pass
    def showEvent(self, event):
        pass
        
    def OncursorPositionChanged(self,line,index):
        #print(line," ",index)
        self.currentLine=line
        self.currentCursor=index


    def keyPressEvent(self, event):
        # Execute the superclasses event
        super().keyPressEvent(event)
        # Check pressed key information
        key = event.key()
        key_modifiers = QApplication.keyboardModifiers()
        if (key == QtCore.Qt.Key_K and 
            key_modifiers == QtCore.Qt.ControlModifier):
                self.toggle_commenting()
    
    def toggle_commenting(self):
        # Check if the selections are valid
        selections = self.get_selections()
        if selections == None:
            return
        # Merge overlapping selections
        while self.merge_test(selections) == True:
            selections = self.merge_selections(selections)
        # Start the undo action that can undo all commenting at once
        self.beginUndoAction()
        # Loop over selections and comment them
        for i, sel in enumerate(selections):
            if self.text(sel[0]).lstrip().startswith(self.comment_string):
                self.set_commenting(sel[0], sel[1], self._uncomment)
            else:
                self.set_commenting(sel[0], sel[1], self._comment)
        # Select back the previously selected regions
        self.SendScintilla(self.SCI_CLEARSELECTIONS)
        for i, sel in enumerate(selections):
            start_index = self.positionFromLineIndex(sel[0], 0)
            # Check if ending line is the last line in the editor
            last_line = sel[1]
            if last_line == self.lines() - 1:
                end_index = self.positionFromLineIndex(sel[1], len(self.text(last_line)))
            else:
                end_index = self.positionFromLineIndex(sel[1], len(self.text(last_line))-1)
            if i == 0:
                self.SendScintilla(self.SCI_SETSELECTION, start_index, end_index)
            else:
                self.SendScintilla(self.SCI_ADDSELECTION, start_index, end_index)
        # Set the end of the undo action
        self.endUndoAction()
    
    def get_selections(self):
        # Get the selection and store them in a list
        selections = []
        for i in range(self.SendScintilla(self.SCI_GETSELECTIONS)):
            selection = (
                self.SendScintilla(self.SCI_GETSELECTIONNSTART, i),
                self.SendScintilla(self.SCI_GETSELECTIONNEND, i)
            )
            # Add selection to list
            from_line, from_index = self.lineIndexFromPosition(selection[0])
            to_line, to_index = self.lineIndexFromPosition(selection[1])
            selections.append((from_line, to_line))
        selections.sort()
        # Return selection list
        return selections
    
    def merge_test(self, selections):
        for i in range(1, len(selections)):
            # Get the line numbers
            previous_start_line = selections[i-1][0]
            previous_end_line = selections[i-1][1]
            current_start_line = selections[i][0]
            current_end_line = selections[i][1]
            if previous_end_line == current_start_line:
                return True
        # Merging is not needed
        return False
    
    def merge_selections(self, selections):
        if len(selections) < 2:
            return selections
        merged_selections = []
        skip_flag = False
        for i in range(1, len(selections)):
            # Get the line numbers
            previous_start_line = selections[i-1][0]
            previous_end_line = selections[i-1][1]
            current_start_line = selections[i][0]
            current_end_line = selections[i][1]
            # Test for merge
            if previous_end_line == current_start_line and skip_flag == False:
                merged_selections.append(
                    (previous_start_line, current_end_line)
                )
                skip_flag = True
            else:
                if skip_flag == False:
                    merged_selections.append(
                        (previous_start_line, previous_end_line)
                    )
                skip_flag = False
                # Add the last selection only if it was not merged
                if i == (len(selections) - 1):
                    merged_selections.append(
                        (current_start_line, current_end_line)
                    )
        # Return the merged selections
        return merged_selections
    
    def set_commenting(self, arg_from_line, arg_to_line, func):
        # Get the cursor information
        from_line = arg_from_line
        to_line = arg_to_line
        # Check if ending line is the last line in the editor
        last_line = to_line
        if last_line == self.lines() - 1:
            to_index = len(self.text(to_line))
        else:
            to_index = len(self.text(to_line))-1
        # Set the selection from the beginning of the cursor line
        # to the end of the last selection line
        self.setSelection(
            from_line, 0, to_line, to_index
        )
        # Get the selected text and split it into lines
        selected_text = self.selectedText()
        selected_list = selected_text.split("\n")
        # Find the smallest indent level
        indent_levels = []
        for line in selected_list:
            indent_levels.append(len(line) - len(line.lstrip()))
        min_indent_level = min(indent_levels)
        # Add the commenting character to every line
        for i, line in enumerate(selected_list):
            selected_list[i] = func(line, min_indent_level)
        # Replace the whole selected text with the merged lines
        # containing the commenting characters
        replace_text = self.line_ending.join(selected_list)
        self.replaceSelectedText(replace_text)
    
    def _comment(self, line, indent_level):
        if line.strip() != "":
            return line[:indent_level] + self.comment_string + line[indent_level:]
        else:
            return line
    
    def _uncomment(self, line, indent_level):
        if line.strip().startswith(self.comment_string):
            return line.replace(self.comment_string, "", 1)
        else:
            return line
        
    def setup(self):
        # Set the autocompletion to be case IN-sensitive
        self.setAutoCompletionCaseSensitivity(False)
        # Set the threshold at which the autocompletion window appears
        self.setAutoCompletionThreshold(1)
        # Set the source from which the autocompletions will be pulled from
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        # Sets whether the characters to the right of the autocompletion
        # will be overwritten when an autocompletion is selected.
        self.setAutoCompletionReplaceWord(True)
        # Select the behaviour of autocompletions when there is only a single
        # entry in the autocompletion list. The selection below sets that
        # when the autocompletion window will always be displayed.
        self.setAutoCompletionUseSingle(QsciScintilla.AcusNever)

        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setBackspaceUnindents(True)
        self.setIndentationGuides(True)

        # Remove the duplicate line numbers margin
        self.setMarginWidth(1, 50)
        self.setMarginType(1, self.SymbolMargin)
        self.setMarginSensitivity(1, True)

        # code with
        self.setEdgeColumn(100)
        self.setEdgeColor(QColor(100,100,100,25))
        self.setEdgeMode(QsciScintilla.EdgeLine)

        self.setFoldMarginColors(QColor(30, 30, 30), QColor(30, 30, 30))
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        # Set folding defaults (http://www.scintilla.org/ScintillaDoc.html#Folding)
        #sci.setFolding(QsciScintilla.BoxedFoldStyle)
        #PlainFoldStyle
        #CircledFoldStyle
        #BoxedFoldStyle
        #CircledTreeFoldStyle
        #BoxedTreeFoldStyle

        self.setSelectionBackgroundColor(QColor(61, 61, 52))
        self.resetSelectionForegroundColor()
        self.SendScintilla(QsciScintilla.SCI_SETSCROLLWIDTHTRACKING, 1)
        
        
        self.setCaretWidth(2)        
        self.setCaretLineVisible(True)
        self.setCaretLineFrameWidth(2)
        self.setCaretLineBackgroundColor(QColor(0,0,0,55))
        self.setCaretForegroundColor(QColor(255, 255, 255,100))  # Altera a cor do cursor
        
        self.SendScintilla(QsciScintilla.SCI_SETMULTIPLESELECTION, True)
        self.SendScintilla(QsciScintilla.SCI_SETADDITIONALSELECTIONTYPING, True)
        self.setMarginsBackgroundColor(QColor(39, 40, 34))
        self.setMarginsForegroundColor(QColor(128, 128, 128))
        scroll_bar_style = """
          QMainWindow {
            background-color: #282a36;
        }
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

if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.show()
    app.exec()
