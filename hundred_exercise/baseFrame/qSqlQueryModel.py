from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from qfluentwidgets import PushButton as QPushButton
from qfluentwidgets import LineEdit as QLineEdit


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSqlQueryModel")
        self.resize(800, 600)

        self.table = QTableView()
        #* 和数据库建立联系
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")

        self.model = QSqlQueryModel()
        self.model.setQuery("select * from fakeuser;", self.db)

        self.table = QTableView()
        self.table.setModel(self.model)

        self.line = QLineEdit()
        self.line.setPlaceholderText("请输入搜索内容")
        self.btn = QPushButton("查询")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.line)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
