from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from Ui_radixConverter import Ui_RadixConverter


class MyMainWindow(QWidget, Ui_RadixConverter):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.typeDict = ["长度", "质量"]
        self.lengthDict = {"米":100, "厘米":1, "分米":10, "千米":100*1000, "英尺":30.48, "英寸":2.54}
        self.gramDict = {"克":1, "千克":1000, "斤":500, "磅":453.6}
        self.allDict = { 0: self.lengthDict, 1: self.gramDict}
        self.comboBoxTop.addItems(self.typeDict)
        self.init(0)
        self.bind()

    def bind(self):
        self.comboBoxTop.currentIndexChanged.connect(self.init)
        self.lineEditUp.textChanged.connect(self.upChange)
        self.comboBoxUp.currentIndexChanged.connect(self.upChange)
        self.comboBoxDown.currentIndexChanged.connect(self.upChange)

    def upChange(self):
        currentType = self.comboBoxUp.currentText()
        targetType = self.comboBoxDown.currentText()
        bigType = self.comboBoxTop.currentIndex()
        inputNum = int(self.lineEditUp.text())
        targetNum = round(inputNum * self.allDict[bigType][currentType] / self.allDict[bigType][targetType], 5)
        self.lineEditDown.setText(str(targetNum))
        self.labelTop.setText(f"{inputNum} {currentType} = ")
        self.labelUp.setText(f"{targetNum} {targetType}")

    def init(self, index):
        self.labelTop.clear()
        self.labelUp.clear()
        self.comboBoxUp.clear()
        self.comboBoxDown.clear()
        self.comboBoxTop.setCurrentIndex(index)
        self.comboBoxUp.addItems(self.allDict[index].keys())
        self.comboBoxUp.setCurrentIndex(0)
        self.comboBoxDown.addItems(self.allDict[index].keys())
        self.comboBoxDown.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
