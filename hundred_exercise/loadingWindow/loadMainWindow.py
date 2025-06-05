import sys, os
sys.path.append(os.path.dirname(__file__))
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication
from PySide6.QtCore import Qt, Signal
from loadWindow import loadingWindow

class myMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("这是主界面")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = loadingWindow(parent=myMainWindow())
    window.show()
    app.exec()
