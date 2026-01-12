import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # HUBUNGKAN MENU
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionDataDesa.triggered.connect(self.open_data_desa)
        self.ui.actionDataSungai.triggered.connect(self.open_data_sungai)
        self.ui.actionDataPemukiman.triggered.connect(self.open_data_pemukiman)
        self.ui.actionDataIUP.triggered.connect(self.open_data_iup)

    # ===== FUNGSI MENU =====
    def open_data_desa(self):
        QMessageBox.information(self, "Menu", "Nanti buka Form Data Desa")

    def open_data_sungai(self):
        QMessageBox.information(self, "Menu", "Nanti buka Form Data Sungai")

    def open_data_pemukiman(self):
        QMessageBox.information(self, "Menu", "Nanti buka Form Data Pemukiman")

    def open_data_iup(self):
        QMessageBox.information(self, "Menu", "Nanti buka Form Data IUP")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
