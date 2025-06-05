from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("进入")
        self.btn.clicked.connect(self.btnClick)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)


    def btnClick(self):

        replay = QMessageBox.information(self,
                    "提示", "是否进入", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if replay == QMessageBox.Yes:
            print("进入")
        else:
            print("不进入")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
