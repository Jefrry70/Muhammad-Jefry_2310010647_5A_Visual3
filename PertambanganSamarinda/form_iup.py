# form_iup.py
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud_pertambangan import CrudPertambangan

class FormIup(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        file = QFile("form_iup.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file, self)
        file.close()

        self.setLayout(self.ui.layout())
        self.setWindowTitle("Data IUP Pertambangan Samarinda")
        self.resize(900, 600)

        # CRUD object
        self.crud = CrudPertambangan()
        self.id_terpilih = None

        # Hubungkan tombol
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih_form)

        # Load combo
        self.load_combo_desa()
        self.load_combo_sungai()

        # Hubungkan klik tabel
        self.ui.tableIup.cellClicked.connect(self.pilih_baris)

        # Muat data awal
        self.muatan_data()

    def load_combo_desa(self):
        data = self.crud.ambil_semua_desa()
        self.ui.cmbDesa.clear()
        self.ui.cmbDesa.addItem("-- Pilih Desa --", 0)
        for row in data:
            self.ui.cmbDesa.addItem(row['desa'], row['id_desa'])

    def load_combo_sungai(self):
        data = self.crud.ambil_semua_sungai_besar()
        self.ui.cmbSungaiBesar.clear()
        self.ui.cmbSungaiBesar.addItem("-- Pilih Sungai Besar --", 0)
        for row in data:
            self.ui.cmbSungaiBesar.addItem(row['nama_sungai'], row['id_sungai_besar'])

    def muatan_data(self):
        data = self.crud.ambil_semua_iup()
        self.ui.tableIup.setRowCount(0)
        for baris, record in enumerate(data):
            self.ui.tableIup.insertRow(baris)
            self.ui.tableIup.setItem(baris, 0, QTableWidgetItem(str(record['id_iup'])))
            self.ui.tableIup.setItem(baris, 1, QTableWidgetItem(record['nama_usaha']))
            self.ui.tableIup.setItem(baris, 2, QTableWidgetItem(record['komoditas']))
            self.ui.tableIup.setItem(baris, 3, QTableWidgetItem(str(record['luas_sk'])))
            self.ui.tableIup.setItem(baris, 4, QTableWidgetItem(record['nama_desa'] or '-'))
            self.ui.tableIup.setItem(baris, 5, QTableWidgetItem(record['nama_sungai'] or '-'))

    def pilih_baris(self, row, column):
        self.id_terpilih = self.ui.tableIup.item(row, 0).text()

        self.ui.txtNamaUsaha.setText(self.ui.tableIup.item(row, 1).text())
        self.ui.txtKomoditas.setText(self.ui.tableIup.item(row, 2).text())
        self.ui.txtLuasSk.setText(self.ui.tableIup.item(row, 3).text())

        # Set combo desa
        nama_desa = self.ui.tableIup.item(row, 4).text()
        index = self.ui.cmbDesa.findText(nama_desa)
        if index >= 0:
            self.ui.cmbDesa.setCurrentIndex(index)

        # Set combo sungai
        nama_sungai = self.ui.tableIup.item(row, 5).text()
        index = self.ui.cmbSungaiBesar.findText(nama_sungai)
        if index >= 0:
            self.ui.cmbSungaiBesar.setCurrentIndex(index)

    def simpan(self):
        nama = self.ui.txtNamaUsaha.text().strip()
        komoditas = self.ui.txtKomoditas.text().strip()
        luas_str = self.ui.txtLuasSk.text().strip()

        if not nama or not komoditas or not luas_str:
            QMessageBox.warning(self, "Perhatian", "Lengkapi semua field!")
            return

        try:
            luas = float(luas_str)
        except ValueError:
            QMessageBox.warning(self, "Perhatian", "Luas SK harus berupa angka!")
            return

        id_desa = self.ui.cmbDesa.currentData()
        id_sungai = self.ui.cmbSungaiBesar.currentData()

        if id_desa == 0 or id_sungai == 0:
            QMessageBox.warning(self, "Perhatian", "Pilih Desa dan Sungai Besar!")
            return

        self.crud.simpan_iup(nama, komoditas, luas, id_desa, id_sungai)
        QMessageBox.information(self, "Sukses", "Data berhasil disimpan!")
        self.muatan_data()
        self.bersih_form()

    def ubah(self):
        if not self.id_terpilih:
            QMessageBox.warning(self, "Perhatian", "Pilih data dulu di tabel!")
            return

        nama = self.ui.txtNamaUsaha.text().strip()
        komoditas = self.ui.txtKomoditas.text().strip()
        luas_str = self.ui.txtLuasSk.text().strip()

        if not nama or not komoditas or not luas_str:
            QMessageBox.warning(self, "Perhatian", "Lengkapi semua field!")
            return

        try:
            luas = float(luas_str)
        except ValueError:
            QMessageBox.warning(self, "Perhatian", "Luas SK harus berupa angka!")
            return

        id_desa = self.ui.cmbDesa.currentData()
        id_sungai = self.ui.cmbSungaiBesar.currentData()

        if id_desa == 0 or id_sungai == 0:
            QMessageBox.warning(self, "Perhatian", "Pilih Desa dan Sungai Besar!")
            return

        self.crud.ubah_iup(self.id_terpilih, nama, komoditas, luas, id_desa, id_sungai)
        QMessageBox.information(self, "Sukses", "Data berhasil diubah!")
        self.muatan_data()
        self.bersih_form()

    def hapus(self):
        if not self.id_terpilih:
            QMessageBox.warning(self, "Perhatian", "Pilih data dulu!")
            return

        jawab = QMessageBox.question(self, "Hapus", "Yakin hapus data ini?",
                                   QMessageBox.Yes | QMessageBox.No)
        if jawab == QMessageBox.Yes:
            self.crud.hapus_iup(self.id_terpilih)
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")
            self.muatan_data()
            self.bersih_form()

    def bersih_form(self):
        self.id_terpilih = None
        self.ui.txtNamaUsaha.clear()
        self.ui.txtKomoditas.clear()
        self.ui.txtLuasSk.clear()
        self.ui.cmbDesa.setCurrentIndex(0)
        self.ui.cmbSungaiBesar.setCurrentIndex(0)
