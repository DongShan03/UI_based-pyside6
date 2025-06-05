from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLabel, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        self.gridLayout = QGridLayout()
        line1 = QLineEdit()
        line1.setPlaceholderText("请输入用户名")
        line2 = QLineEdit()
        line2.setPlaceholderText("请输入密码")
        self.gridLayout.addWidget(QLabel("用户名:"), 0, 0)
        self.gridLayout.addWidget(line1, 0, 1)
        self.gridLayout.addWidget(QLabel("密码:"), 1, 0)
        self.gridLayout.addWidget(line2, 1, 1)
        btn = QPushButton("退出")
        btn.clicked.connect(self.close)
        self.gridLayout.addWidget(btn, 2, 0, 1, 2)

        self.mainLayout.addLayout(self.gridLayout)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
