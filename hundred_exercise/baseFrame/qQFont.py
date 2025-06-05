from PySide6.QtWidgets import QApplication, QWidget, QFontDialog, QTextEdit, QLabel, QComboBox, QPushButton, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("选择字体")
        self.label = QTextEdit("改变字体")
        mainLayout = QVBoxLayout()

        self.btn.clicked.connect(self.changeFont)
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.btn)

        self.setLayout(mainLayout)

    def changeFont(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)
        else:
            return


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
