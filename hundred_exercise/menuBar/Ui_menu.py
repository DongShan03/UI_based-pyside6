# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionsave_as = QAction(MainWindow)
        self.actionsave_as.setObjectName(u"actionsave_as")
        self.actionedit = QAction(MainWindow)
        self.actionedit.setObjectName(u"actionedit")
        self.actionexport = QAction(MainWindow)
        self.actionexport.setObjectName(u"actionexport")
        self.actionexport_as = QAction(MainWindow)
        self.actionexport_as.setObjectName(u"actionexport_as")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionsave_as)
        self.menu.addSeparator()
        self.menu.addAction(self.actionedit)
        self.menu_2.addAction(self.actionexport)
        self.menu_2.addAction(self.actionexport_as)
        self.menu_2.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionsave_as.setText(QCoreApplication.translate("MainWindow", u"save as", None))
        self.actionedit.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.actionexport.setText(QCoreApplication.translate("MainWindow", u"export", None))
        self.actionexport_as.setText(QCoreApplication.translate("MainWindow", u"export as ", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
    # retranslateUi

