from PySide6.QtWidgets import QApplication, QWidget, QFontDialog, QTextEdit, QLabel, QComboBox, QPushButton, QVBoxLayout
from PySide6.QtCore import Signal

class MyMainWindow(QWidget):
    sendValueToSubWindow = Signal(str)
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit()
        self.subWindow = SubWindow(parent=self)
        self.btn = QPushButton("发送到子窗口")
        self.btn2 = QPushButton("打开子窗口")
        self.bind()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.textEdit)
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.btn2)
        self.setLayout(self.mainLayout)

    def bind(self):
        self.sendValueToSubWindow.connect(self.subWindow.textEdit.setText)
        self.btn.clicked.connect(self.sendValue)
        self.btn2.clicked.connect(self.subWindow.show)

    def sendValue(self):
        text = self.textEdit.toPlainText()
        self.sendValueToSubWindow.emit(text)

class SubWindow(QWidget):
    sendValueToMainWindow = Signal(str)
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.textEdit = QTextEdit()

        self.subLayout = QVBoxLayout()
        self.subLayout.addWidget(self.textEdit)
        self.bind()
        self.setLayout(self.subLayout)

    def bind(self):
        self.sendValueToMainWindow.connect(self.parent.textEdit.setText)
        self.textEdit.textChanged.connect(self.sendValue)

    def sendValue(self):
        text = self.textEdit.toPlainText()
        self.sendValueToMainWindow.emit(text)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
