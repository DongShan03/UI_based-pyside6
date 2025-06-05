from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMainWindow
from cal import Ui_Form
import qtmodern.styles
import qtmodern.windows
import qdarktheme

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("简易计算器")
        self.textOutput.setReadOnly(True)
        self.textOutput.ensureCursorVisible()
        self.button1.clicked.connect(lambda: self.textOutput.insertPlainText("1"))
        self.button2.clicked.connect(lambda: self.textOutput.insertPlainText("2"))
        self.button3.clicked.connect(lambda: self.textOutput.insertPlainText("3"))
        self.button4.clicked.connect(lambda: self.textOutput.insertPlainText("4"))
        self.button5.clicked.connect(lambda: self.textOutput.insertPlainText("5"))
        self.button6.clicked.connect(lambda: self.textOutput.insertPlainText("6"))
        self.button7.clicked.connect(lambda: self.textOutput.insertPlainText("7"))
        self.button8.clicked.connect(lambda: self.textOutput.insertPlainText("8"))
        self.button9.clicked.connect(lambda: self.textOutput.insertPlainText("9"))
        self.button0.clicked.connect(lambda: self.textOutput.insertPlainText("0"))
        self.buttonPoint.clicked.connect(lambda: self.textOutput.insertPlainText("."))
        self.buttonAdd.clicked.connect(lambda: self.textOutput.insertPlainText("+"))
        self.buttonMinus.clicked.connect(lambda: self.textOutput.insertPlainText("-"))
        self.buttonDiv.clicked.connect(lambda: self.textOutput.insertPlainText("/"))
        self.buttonMul.clicked.connect(lambda: self.textOutput.insertPlainText("*"))
        self.buttonEqual.clicked.connect(self.getAnswer)
        self.buttonClear.clicked.connect(lambda: self.textOutput.clear())
        self.buttonDel.clicked.connect(self.back)

    def back(self):
        text = self.textOutput.toPlainText()[:-1]
        self.textOutput.setPlainText(text)
        self.textOutput.moveCursor(self.textOutput.textCursor().MoveOperation.End)

    def getAnswer(self):
        text = self.textOutput.toPlainText()
        self.textOutput.setPlainText(str(eval(text)))
        self.textOutput.moveCursor(self.textOutput.textCursor().MoveOperation.End)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    qdarktheme.setup_theme()
    window.show()
    app.exec()
