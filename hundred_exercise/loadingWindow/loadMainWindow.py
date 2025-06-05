import sys, os
sys.path.append(os.path.dirname(__file__))
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication
from PySide6.QtCore import Qt, Signal
from loadWindow import loadingWindow
from qfluentwidgets import PushButton

class myMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("这是主界面")
        self.btn = PushButton("进入加载界面")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = loadingWindow(parent=myMainWindow())

    window.show()
    app.exec()
