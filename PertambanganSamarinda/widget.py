import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud_pertambangan import CrudPertambangan

from form_desa import FormDesa
from form_iup import FormIup


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Load form.ui
        file = QFile("mainwindow.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file, self)
        file.close()

        # Set window
        self.setLayout(self.ui.layout())
        self.resize(900, 600)
        self.setWindowTitle("Sistem Informasi Pertambangan Samarinda")

        # CRUD
        self.crud = CrudPertambangan()

        # HUBUNGKAN MENU
        self.ui.actionDataDesa.triggered.connect(self.buka_desa)
        self.ui.actionExit.triggered.connect(self.keluar_aplikasi)

        self.ui.actionDataIup.triggered.connect(self.buka_iup)   # ← perhatikan huruf kapital IUP

    def buka_desa(self):
        self.form_desa = FormDesa()
        self.form_desa.show()

    def buka_iup(self):
        self.form_iup = FormIup()
        self.form_iup.show()             # Tampilkan sebagai window terpisah



    # ================= EXIT =================
    def keluar_aplikasi(self):
        jawab = QMessageBox.question(
            self,
            "Keluar Aplikasi",
            "Yakin ingin keluar dari aplikasi?",
            QMessageBox.Yes | QMessageBox.No
        )
        if jawab == QMessageBox.Yes:
            QApplication.quit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
