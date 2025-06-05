from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMenuBar, QFileDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.openFile = QAction("打开文件", self)
        self.closeFile = QAction("关闭文件", self)
        self.addActions([self.openFile, self.closeFile])

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
