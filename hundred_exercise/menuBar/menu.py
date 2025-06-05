from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QMenuBar, QFileDialog
from PySide6.QtGui import QAction
import os
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menuBar = self.menuBar()
        self.openFile = QAction("打开文件", self)
        self.openFile.setShortcut("Ctrl+O")
        self.openFile.triggered.connect(self.openFileEvent)
        self.closeFile = QAction("关闭文件", self)
        self.closeFile.setShortcut("Ctrl+E")

        self.fileMenu = QMenu("文件", self)
        self.fileMenu.addAction(self.openFile)
        self.fileMenu.addAction(self.closeFile)
        self.menuBar.addMenu(self.fileMenu)

        self.moreMenu = QMenu("更多", self)
        self.moreMenu.addAction(QAction("设置", self))
        self.moreMenu.addAction(QAction("关于", self))
        self.menuBar.addMenu(self.moreMenu)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

    def openFileEvent(self):
        filename, _ = QFileDialog.getOpenFileName(self, "选择文件", ".", "All Files (*);;Python Files (*.py; *.pyd);;Text Files (*.txt)")
        if os.path.exists(filename):
            print(filename)
        else:
            print("取消选择文件")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
