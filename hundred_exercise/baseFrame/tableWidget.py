from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHeaderView, QTableWidgetItem
from qfluentwidgets import TableWidget as QTableWidget


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.data = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.table = QTableWidget()

        self.table.setColumnCount(3)
        self.table.setRowCount(5)
        self.table.setBorderVisible(True)
        self.table.setBorderRadius(8)
        self.table.setWordWrap(False)
        self.table.setHorizontalHeaderLabels(["a", "b", "c"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSortingEnabled(True)
        self.table.verticalHeader().hide()

        for rowIndex, rowItem in enumerate(self.data):
            for colIndex, colItem in enumerate(rowItem):
                self.table.setItem(rowIndex, colIndex, QTableWidgetItem(colItem))

        self.table.setSpan(0, 0, 2, 1)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.table)
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
