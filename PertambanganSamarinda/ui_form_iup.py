# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_iup.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1005, 680)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 90, 121, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 140, 63, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 200, 63, 20))
        self.txtNamaUsaha = QLineEdit(Form)
        self.txtNamaUsaha.setObjectName(u"txtNamaUsaha")
        self.txtNamaUsaha.setGeometry(QRect(230, 90, 113, 28))
        self.txtKomoditas = QLineEdit(Form)
        self.txtKomoditas.setObjectName(u"txtKomoditas")
        self.txtKomoditas.setGeometry(QRect(230, 140, 113, 28))
        self.txtLuasSk = QLineEdit(Form)
        self.txtLuasSk.setObjectName(u"txtLuasSk")
        self.txtLuasSk.setGeometry(QRect(230, 200, 113, 28))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(100, 270, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(250, 270, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(400, 270, 90, 29))
        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(550, 270, 90, 29))
        self.tableIup = QTableWidget(Form)
        if (self.tableIup.columnCount() < 6):
            self.tableIup.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableIup.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableIup.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableIup.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableIup.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableIup.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableIup.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableIup.setObjectName(u"tableIup")
        self.tableIup.setGeometry(QRect(100, 340, 751, 192))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 120, 63, 20))
        self.cmbDesa = QComboBox(Form)
        self.cmbDesa.setObjectName(u"cmbDesa")
        self.cmbDesa.setGeometry(QRect(540, 120, 141, 28))
        self.cmbSungaiBesar = QComboBox(Form)
        self.cmbSungaiBesar.setObjectName(u"cmbSungaiBesar")
        self.cmbSungaiBesar.setGeometry(QRect(540, 180, 141, 28))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 180, 63, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nama Usaha", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Komoditas", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"LuasSK", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"Bersih", None))
        ___qtablewidgetitem = self.tableIup.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_iup", None));
        ___qtablewidgetitem1 = self.tableIup.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nama usaha", None));
        ___qtablewidgetitem2 = self.tableIup.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"komoditas", None));
        ___qtablewidgetitem3 = self.tableIup.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Luas sk", None));
        ___qtablewidgetitem4 = self.tableIup.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"desa", None));
        ___qtablewidgetitem5 = self.tableIup.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"sungai besar", None));
        self.label_4.setText(QCoreApplication.translate("Form", u"Desa", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Sungai Besar", None))
    # retranslateUi

