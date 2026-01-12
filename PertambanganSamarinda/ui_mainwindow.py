# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
        self.actionDataIup = QAction(MainWindow)
        self.actionDataIup.setObjectName(u"actionDataIup")
        self.actionDataDesa = QAction(MainWindow)
        self.actionDataDesa.setObjectName(u"actionDataDesa")
        self.actionData_Sungai = QAction(MainWindow)
        self.actionData_Sungai.setObjectName(u"actionData_Sungai")
        self.actionDataPemukiman = QAction(MainWindow)
        self.actionDataPemukiman.setObjectName(u"actionDataPemukiman")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuData_Tambang = QMenu(self.menubar)
        self.menuData_Tambang.setObjectName(u"menuData_Tambang")
        self.menuMasterData = QMenu(self.menubar)
        self.menuMasterData.setObjectName(u"menuMasterData")
        self.menuKeluar = QMenu(self.menubar)
        self.menuKeluar.setObjectName(u"menuKeluar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuData_Tambang.menuAction())
        self.menubar.addAction(self.menuMasterData.menuAction())
        self.menubar.addAction(self.menuKeluar.menuAction())
        self.menuData_Tambang.addAction(self.actionDataIup)
        self.menuMasterData.addAction(self.actionDataDesa)
        self.menuMasterData.addAction(self.actionData_Sungai)
        self.menuMasterData.addAction(self.actionDataPemukiman)
        self.menuKeluar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDataIup.setText(QCoreApplication.translate("MainWindow", u"Data IUP", None))
        self.actionDataDesa.setText(QCoreApplication.translate("MainWindow", u"Data Desa", None))
        self.actionData_Sungai.setText(QCoreApplication.translate("MainWindow", u"Data Sungai", None))
        self.actionDataPemukiman.setText(QCoreApplication.translate("MainWindow", u"Data Pemukiman", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuData_Tambang.setTitle(QCoreApplication.translate("MainWindow", u"Data Tambang", None))
        self.menuMasterData.setTitle(QCoreApplication.translate("MainWindow", u"Master Data", None))
        self.menuKeluar.setTitle(QCoreApplication.translate("MainWindow", u"Keluar", None))
    # retranslateUi

