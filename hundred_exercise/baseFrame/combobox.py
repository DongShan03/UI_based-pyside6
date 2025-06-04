from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QComboBox, QCheckBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        cb = QComboBox()
        cb.addItems(["what", "when", "where"])
        cb.currentIndexChanged.connect(lambda: print(cb.currentText()))

        cb2 = QCheckBox()
        cb2.setText("test")
        cb2.stateChanged.connect(lambda: print(cb2.isChecked()))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(cb)
        mainLayout.addWidget(cb2)
        self.setLayout(mainLayout)



if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
