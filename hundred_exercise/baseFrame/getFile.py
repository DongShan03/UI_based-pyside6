from PySide6.QtWidgets import QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout()
        btn = QPushButton("选择文件")
        btn.clicked.connect(lambda: print(
            QFileDialog.getOpenFileNames(self, "选择文件", ".", "All Files (*);;Python Files (*.py; *.pyd);;Text Files (*.txt)")
        ))
        btn2 = QPushButton("选择文件夹")
        btn2.clicked.connect(lambda: print(
            QFileDialog.getExistingDirectory(self, "选择文件夹", ".")
        ))
        self.mainLayout.addWidget(btn)
        self.mainLayout.addWidget(btn2)
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
