from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PIL import Image, ImageQt
from PySide6.QtCore import Qt, Signal, QTimer
import time

class loadingWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent
        self.label = QLabel()
        self.loadWindow = QVBoxLayout()
        self.loadWindow.addWidget(self.label)
        self.show_img()
        self.bind()
        self.setLayout(self.loadWindow)

    def show_img(self):
        fileName = "C:\\Users\\admin\\Pictures\\screen\\1.png"
        self.img = Image.open(fileName)
        self.label.setPixmap(ImageQt.toqpixmap(self.img))

    def bind(self):
        QTimer.singleShot(1000, self.openMainWindow)

    def openMainWindow(self):
        self.close()
        self.parent.show()
