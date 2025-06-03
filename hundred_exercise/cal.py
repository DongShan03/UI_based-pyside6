# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cal.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(343, 243)
        Form.setMinimumSize(QSize(200, 120))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textOutput = QPlainTextEdit(Form)
        self.textOutput.setObjectName(u"textOutput")

        self.verticalLayout_2.addWidget(self.textOutput)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buttonClear = QPushButton(Form)
        self.buttonClear.setObjectName(u"buttonClear")

        self.horizontalLayout_5.addWidget(self.buttonClear)

        self.buttonDel = QPushButton(Form)
        self.buttonDel.setObjectName(u"buttonDel")

        self.horizontalLayout_5.addWidget(self.buttonDel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button1 = QPushButton(Form)
        self.button1.setObjectName(u"button1")

        self.horizontalLayout.addWidget(self.button1)

        self.button2 = QPushButton(Form)
        self.button2.setObjectName(u"button2")

        self.horizontalLayout.addWidget(self.button2)

        self.button3 = QPushButton(Form)
        self.button3.setObjectName(u"button3")

        self.horizontalLayout.addWidget(self.button3)

        self.buttonAdd = QPushButton(Form)
        self.buttonAdd.setObjectName(u"buttonAdd")

        self.horizontalLayout.addWidget(self.buttonAdd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button4 = QPushButton(Form)
        self.button4.setObjectName(u"button4")

        self.horizontalLayout_2.addWidget(self.button4)

        self.button5 = QPushButton(Form)
        self.button5.setObjectName(u"button5")

        self.horizontalLayout_2.addWidget(self.button5)

        self.button6 = QPushButton(Form)
        self.button6.setObjectName(u"button6")

        self.horizontalLayout_2.addWidget(self.button6)

        self.buttonMinus = QPushButton(Form)
        self.buttonMinus.setObjectName(u"buttonMinus")

        self.horizontalLayout_2.addWidget(self.buttonMinus)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button7 = QPushButton(Form)
        self.button7.setObjectName(u"button7")

        self.horizontalLayout_3.addWidget(self.button7)

        self.button8 = QPushButton(Form)
        self.button8.setObjectName(u"button8")

        self.horizontalLayout_3.addWidget(self.button8)

        self.button9 = QPushButton(Form)
        self.button9.setObjectName(u"button9")

        self.horizontalLayout_3.addWidget(self.button9)

        self.buttonMul = QPushButton(Form)
        self.buttonMul.setObjectName(u"buttonMul")

        self.horizontalLayout_3.addWidget(self.buttonMul)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button0 = QPushButton(Form)
        self.button0.setObjectName(u"button0")

        self.horizontalLayout_4.addWidget(self.button0)

        self.buttonPoint = QPushButton(Form)
        self.buttonPoint.setObjectName(u"buttonPoint")

        self.horizontalLayout_4.addWidget(self.buttonPoint)

        self.buttonEqual = QPushButton(Form)
        self.buttonEqual.setObjectName(u"buttonEqual")

        self.horizontalLayout_4.addWidget(self.buttonEqual)

        self.buttonDiv = QPushButton(Form)
        self.buttonDiv.setObjectName(u"buttonDiv")

        self.horizontalLayout_4.addWidget(self.buttonDiv)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.buttonClear.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.buttonDel.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.button1.setText(QCoreApplication.translate("Form", u"1", None))
        self.button2.setText(QCoreApplication.translate("Form", u"2", None))
        self.button3.setText(QCoreApplication.translate("Form", u"3", None))
        self.buttonAdd.setText(QCoreApplication.translate("Form", u"+", None))
        self.button4.setText(QCoreApplication.translate("Form", u"4", None))
        self.button5.setText(QCoreApplication.translate("Form", u"5", None))
        self.button6.setText(QCoreApplication.translate("Form", u"6", None))
        self.buttonMinus.setText(QCoreApplication.translate("Form", u"-", None))
        self.button7.setText(QCoreApplication.translate("Form", u"7", None))
        self.button8.setText(QCoreApplication.translate("Form", u"8", None))
        self.button9.setText(QCoreApplication.translate("Form", u"9", None))
        self.buttonMul.setText(QCoreApplication.translate("Form", u"x", None))
        self.button0.setText(QCoreApplication.translate("Form", u"0", None))
        self.buttonPoint.setText(QCoreApplication.translate("Form", u".", None))
        self.buttonEqual.setText(QCoreApplication.translate("Form", u"=", None))
        self.buttonDiv.setText(QCoreApplication.translate("Form", u"/", None))
    # retranslateUi

