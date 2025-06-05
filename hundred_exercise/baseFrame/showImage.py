from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QSlider, QFileDialog, QLabel, QPushButton, QVBoxLayout
from PIL import Image, ImageQt, ImageFilter

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("选择图像")
        self.btn.clicked.connect(self.btnClick)

        self.lbnShowImg = QLabel()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 20)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(4)
        self.slider.valueChanged.connect(self.sliderChange)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.lbnShowImg)
        self.mainLayout.addWidget(self.slider)
        self.setLayout(self.mainLayout)

    def btnClick(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "选择图像", ".", "Picture Files (*.png; *.jpg; *.jpeg; *.tif);;")
        self.img = Image.open(fileName)
        self.lbnShowImg.setPixmap(ImageQt.toqpixmap(self.img))


    def sliderChange(self, value):
        self.blurPic = self.img.filter(ImageFilter.GaussianBlur(radius=value))
        self.lbnShowImg.setPixmap(ImageQt.toqpixmap(self.blurPic))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
