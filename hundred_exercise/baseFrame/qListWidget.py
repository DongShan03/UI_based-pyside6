from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.listWidget = QListWidget()
        self.listWidget.addItems(["da", "da", "da"])

        self.listWidget.insertItem(1, "test")
        self.listWidget.takeItem(2)

        self.listWidget.item(2).setText("test2")
        self.listWidget.item(2).setCheckState(Qt.CheckState.Unchecked)

        self.listWidget.findItems("da", Qt.MatchFlag.MatchExactly)
        self.listWidget.findItems("da", Qt.MatchFlag.MatchContains)
        self.listWidget.findItems("da", Qt.MatchFlag.MatchEndsWith)

        self.listWidget.sortItems(Qt.SortOrder.DescendingOrder)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.listWidget)
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
