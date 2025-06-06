from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from qfluentwidgets import TextEdit
import time
class WorkThread(QThread):
    singal1 = Signal(str)
    def __init__(self):
        super().__init__()
        print("run")

    def run(self):
        for i in range(10):
            self.singal1.emit(str(i))
            time.sleep(1)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = QLabel("当前值为:0")

        self.workThread = WorkThread()
        self.workThread.singal1.connect(lambda x : self.lb.setText(f"当前值为:{x}"))
        self.workThread.start()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
