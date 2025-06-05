from PySide6.QtWidgets import QApplication, QWidget, QToolBox, QStyle, QVBoxLayout, QLabel, QPushButton
import qdarktheme
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.toolBox = QToolBox()
        self.toolBox.setObjectName("toolBox")
        self.getIcon()
        self.getWidgets()
        self.toolBoxAddItem()
        self.toolBox.currentChanged.connect(self.widgetChange)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.toolBox)
        self.setLayout(self.mainLayout)

    def getIcon(self):
        self.arrowRight = self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight)
        self.arrowDown = self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown)

    def getWidgets(self):
        self.widgets = []
        for i in range(1, 4):
            widget = QWidget()
            widgetLayout = QVBoxLayout()
            widgetLayout.addWidget(QLabel(f"Widget {i}"))
            widgetLayout.addWidget(QPushButton(f"按钮{i}"))
            widget.setLayout(widgetLayout)
            self.widgets.append(widget)

    def widgetChange(self, index):
        for i in range(self.toolBox.count()):
            if i == index:
                self.toolBox.setItemIcon(i, self.arrowDown)
            else:
                self.toolBox.setItemIcon(i, self.arrowRight)

    def toolBoxAddItem(self):
        for i, widget in enumerate(self.widgets):
            self.toolBox.addItem(widget, self.arrowRight, f"Widget {i+1}")



if __name__ == "__main__":
    import sys
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("light")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
