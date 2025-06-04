# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radix converter.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_RadixConverter(object):
    def setupUi(self, RadixConverter):
        if not RadixConverter.objectName():
            RadixConverter.setObjectName(u"RadixConverter")
        RadixConverter.resize(420, 245)
        RadixConverter.setMinimumSize(QSize(418, 245))
        RadixConverter.setMaximumSize(QSize(420, 245))
        self.verticalLayout = QVBoxLayout(RadixConverter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelTop = QLabel(RadixConverter)
        self.labelTop.setObjectName(u"labelTop")
        self.labelTop.setMinimumSize(QSize(300, 30))
        self.labelTop.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.labelTop.setFont(font)
        self.labelTop.setStyleSheet(u"color: rgb(154, 153, 150);\n"
"")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.labelTop)

        self.labelUp = QLabel(RadixConverter)
        self.labelUp.setObjectName(u"labelUp")
        self.labelUp.setMinimumSize(QSize(400, 50))
        self.labelUp.setMaximumSize(QSize(400, 50))
        font1 = QFont()
        font1.setPointSize(35)
        font1.setBold(True)
        self.labelUp.setFont(font1)
        self.labelUp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.labelUp)

        self.lineEditUp = QLineEdit(RadixConverter)
        self.lineEditUp.setObjectName(u"lineEditUp")
        self.lineEditUp.setMinimumSize(QSize(150, 30))
        self.lineEditUp.setMaximumSize(QSize(150, 30))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEditUp)

        self.comboBoxUp = QComboBox(RadixConverter)
        self.comboBoxUp.setObjectName(u"comboBoxUp")
        self.comboBoxUp.setMinimumSize(QSize(240, 30))
        self.comboBoxUp.setMaximumSize(QSize(246, 30))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBoxUp)

        self.lineEditDown = QLineEdit(RadixConverter)
        self.lineEditDown.setObjectName(u"lineEditDown")
        self.lineEditDown.setMinimumSize(QSize(150, 30))
        self.lineEditDown.setMaximumSize(QSize(150, 30))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lineEditDown)

        self.comboBoxDown = QComboBox(RadixConverter)
        self.comboBoxDown.setObjectName(u"comboBoxDown")
        self.comboBoxDown.setMinimumSize(QSize(240, 30))
        self.comboBoxDown.setMaximumSize(QSize(250, 30))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBoxDown)

        self.labelBottom = QLabel(RadixConverter)
        self.labelBottom.setObjectName(u"labelBottom")
        self.labelBottom.setMinimumSize(QSize(400, 30))
        self.labelBottom.setMaximumSize(QSize(400, 30))
        self.labelBottom.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.labelBottom)

        self.comboBoxTop = QComboBox(RadixConverter)
        self.comboBoxTop.setObjectName(u"comboBoxTop")
        self.comboBoxTop.setMinimumSize(QSize(400, 30))
        self.comboBoxTop.setMaximumSize(QSize(400, 30))

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.comboBoxTop)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(RadixConverter)

        QMetaObject.connectSlotsByName(RadixConverter)
    # setupUi

    def retranslateUi(self, RadixConverter):
        RadixConverter.setWindowTitle(QCoreApplication.translate("RadixConverter", u"Radix Converter", None))
        self.labelTop.setText(QCoreApplication.translate("RadixConverter", u"TextLabel=", None))
        self.labelUp.setText(QCoreApplication.translate("RadixConverter", u"TextLabel", None))
        self.labelBottom.setText(QCoreApplication.translate("RadixConverter", u"you should notice something!", None))
    # retranslateUi

