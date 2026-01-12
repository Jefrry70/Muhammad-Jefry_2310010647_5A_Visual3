from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud_pertambangan import CrudPertambangan


class FormDesa(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        file = QFile("form_desa.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file, self)
        file.close()

        self.setLayout(self.ui.layout())
        self.setWindowTitle("Form Data Desa")
        self.resize(700, 500)

        # CRUD
        self.crud = CrudPertambangan()

        self.id_terpilih = None

        # Hubungkan tombol
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

        self.ui.tableDesa.cellClicked.connect(self.pilih_data)

        # Load data awal
        self.load_data()

    # ================= LOAD =================
    def load_data(self):
        data = self.crud.ambil_semua_desa()

        self.ui.tableDesa.setRowCount(0)

        for row, item in enumerate(data):
            self.ui.tableDesa.insertRow(row)
            self.ui.tableDesa.setItem(row, 0, QTableWidgetItem(str(item["id_desa"])))
            self.ui.tableDesa.setItem(row, 1, QTableWidgetItem(item["provinsi"]))
            self.ui.tableDesa.setItem(row, 2, QTableWidgetItem(item["kabkot"]))
            self.ui.tableDesa.setItem(row, 3, QTableWidgetItem(item["kecamatan"]))
            self.ui.tableDesa.setItem(row, 4, QTableWidgetItem(item["desa"]))

    # ================= PILIH =================
    def pilih_data(self, row, column):
        self.id_terpilih = self.ui.tableDesa.item(row, 0).text()
        self.ui.txtProvinsi.setText(self.ui.tableDesa.item(row, 1).text())
        self.ui.txtKabkot.setText(self.ui.tableDesa.item(row, 2).text())
        self.ui.txtKecamatan.setText(self.ui.tableDesa.item(row, 3).text())
        self.ui.txtDesa.setText(self.ui.tableDesa.item(row, 4).text())

    # ================= SIMPAN =================
    def simpan(self):
        provinsi = self.ui.txtProvinsi.text()
        kabkot = self.ui.txtKabkot.text()
        kecamatan = self.ui.txtKecamatan.text()
        desa = self.ui.txtDesa.text()

        self.crud.simpan_desa(provinsi, kabkot, kecamatan, desa)
        QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
        self.load_data()
        self.bersih()

    # ================= UBAH =================
    def ubah(self):
        if not self.id_terpilih:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu!")
            return

        self.crud.ubah_desa(
            self.id_terpilih,
            self.ui.txtProvinsi.text(),
            self.ui.txtKabkot.text(),
            self.ui.txtKecamatan.text(),
            self.ui.txtDesa.text()
        )

        QMessageBox.information(self, "Sukses", "Data berhasil diubah")
        self.load_data()
        self.bersih()

    # ================= HAPUS =================
    def hapus(self):
        if not self.id_terpilih:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu!")
            return

        jawab = QMessageBox.question(self, "Hapus", "Yakin hapus data?")
        if jawab == QMessageBox.Yes:
            self.crud.hapus_desa(self.id_terpilih)
            self.load_data()
            self.bersih()

    # ================= BERSIH =================
    def bersih(self):
        self.id_terpilih = None
        self.ui.txtProvinsi.clear()
        self.ui.txtKabkot.clear()
        self.ui.txtKecamatan.clear()
        self.ui.txtDesa.clear()
