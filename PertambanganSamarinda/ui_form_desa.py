# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_desa.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(836, 586)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 71, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 60, 81, 20))
        self.txtProvinsi = QLineEdit(Form)
        self.txtProvinsi.setObjectName(u"txtProvinsi")
        self.txtProvinsi.setGeometry(QRect(160, 50, 113, 28))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(100, 470, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(220, 470, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(350, 470, 90, 29))
        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(490, 470, 90, 29))
        self.tableDesa = QTableWidget(Form)
        if (self.tableDesa.columnCount() < 5):
            self.tableDesa.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableDesa.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableDesa.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableDesa.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableDesa.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableDesa.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableDesa.setObjectName(u"tableDesa")
        self.tableDesa.setGeometry(QRect(30, 260, 631, 192))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 100, 111, 20))
        self.txtKabkot = QLineEdit(Form)
        self.txtKabkot.setObjectName(u"txtKabkot")
        self.txtKabkot.setGeometry(QRect(160, 100, 113, 28))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 150, 81, 20))
        self.txtKecamatan = QLineEdit(Form)
        self.txtKecamatan.setObjectName(u"txtKecamatan")
        self.txtKecamatan.setGeometry(QRect(160, 150, 113, 28))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 210, 63, 20))
        self.txtDesa = QLineEdit(Form)
        self.txtDesa.setObjectName(u"txtDesa")
        self.txtDesa.setGeometry(QRect(160, 210, 113, 28))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Data Desa", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Provinsi", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"Bersih", None))
        ___qtablewidgetitem = self.tableDesa.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Desa", None));
        ___qtablewidgetitem1 = self.tableDesa.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Desa", None));
        ___qtablewidgetitem2 = self.tableDesa.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Kab/Kota", None));
        ___qtablewidgetitem3 = self.tableDesa.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem4 = self.tableDesa.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Desa", None));
        self.label_3.setText(QCoreApplication.translate("Form", u"Kabupaten Kota", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Kecamatan", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Desa", None))
    # retranslateUi

