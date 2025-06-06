from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHeaderView, QHeaderView
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt, QSortFilterProxyModel, QRegularExpression
from qfluentwidgets import TableView as QTableView
from qfluentwidgets import LineEdit as QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.data = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["10", "11", "12"], ["13", "14", "15"]]
        self.line = QLineEdit()
        self.line.setPlaceholderText("请输入搜索内容")
        self.line.textChanged.connect(self.search)

        self.model = QStandardItemModel()
        for rowIndex, rowItem in enumerate(self.data):
            for colIndex, colItem in enumerate(rowItem):
                self.model.setItem(rowIndex, colIndex, QStandardItem(colItem))

        self.agentModel = QSortFilterProxyModel()
        self.agentModel.setSourceModel(self.model)
        #! 对所有列进行搜索
        self.agentModel.setFilterKeyColumn(-1)

        self.table1 = QTableView()
        self.table1.setModel(self.agentModel)
        self.table1.setBorderVisible(True)
        self.table1.setBorderRadius(8)
        self.table1.setWordWrap(False)
        self.table1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table1.setSortingEnabled(True)
        self.table1.verticalHeader().hide()

        self.table2 = QTableView()
        self.table2.setModel(self.agentModel)
        self.table2.setBorderVisible(True)
        self.table2.setBorderRadius(8)
        self.table2.setWordWrap(False)
        self.table2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table2.setSortingEnabled(True)
        self.table2.verticalHeader().hide()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.line)
        self.mainLayout.addWidget(self.table1)
        self.mainLayout.addWidget(self.table2)
        self.setLayout(self.mainLayout)

    def search(self):
        text = self.line.text()
        self.agentModel.setFilterRegularExpression(QRegularExpression(text))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
