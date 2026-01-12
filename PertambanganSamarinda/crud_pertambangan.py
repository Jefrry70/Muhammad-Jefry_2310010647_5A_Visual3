# crud_pertambangan.py
import mysql.connector
from PySide6.QtWidgets import QMessageBox


class CrudPertambangan:
    def __init__(self):
        try:
            self.koneksi = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pertambangan_samarinda"
            )

            if self.koneksi.is_connected():
                print("Koneksi ke pertambangan_samarinda berhasil!")

        except mysql.connector.Error as err:
            QMessageBox.critical(
                None,
                "Error Koneksi",
                f"Gagal koneksi database:\n{err}"
            )
            self.koneksi = None

    # ==================== DESA ====================
    def simpan_desa(self, provinsi, kabkot, kecamatan, desa):
        cursor = self.koneksi.cursor()
        sql = "INSERT INTO desa (provinsi, kabkot, kecamatan, desa) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (provinsi, kabkot, kecamatan, desa))
        self.koneksi.commit()
        cursor.close()

    def ubah_desa(self, id_desa, provinsi, kabkot, kecamatan, desa):
        cursor = self.koneksi.cursor()
        sql = "UPDATE desa SET provinsi=%s, kabkot=%s, kecamatan=%s, desa=%s WHERE id_desa=%s"
        cursor.execute(sql, (provinsi, kabkot, kecamatan, desa, id_desa))
        self.koneksi.commit()
        cursor.close()

    def hapus_desa(self, id_desa):
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM desa WHERE id_desa=%s"
        cursor.execute(sql, (id_desa,))
        self.koneksi.commit()
        cursor.close()

    def ambil_semua_desa(self):
        cursor = self.koneksi.cursor(dictionary=True)
        cursor.execute("SELECT * FROM desa ORDER BY id_desa DESC")
        data = cursor.fetchall()
        cursor.close()
        return data

    # ==================== IUP SAMARINDA ====================
    def simpan_iup(self, nama_usaha, komoditas, luas_sk, id_desa, id_sungai_besar):
        if self.koneksi is None: return
        cursor = self.koneksi.cursor()
        sql = """
        INSERT INTO iup_samarinda
        (nama_usaha, komoditas, luas_sk, id_desa, id_sungai_besar)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nama_usaha, komoditas, luas_sk, id_desa, id_sungai_besar))
        self.koneksi.commit()
        cursor.close()

    def ubah_iup(self, id_iup, nama_usaha, komoditas, luas_sk, id_desa, id_sungai_besar):
        if self.koneksi is None: return
        cursor = self.koneksi.cursor()
        sql = """
        UPDATE iup_samarinda SET
        nama_usaha = %s,
        komoditas = %s,
        luas_sk = %s,
        id_desa = %s,
        id_sungai_besar = %s
        WHERE id_iup = %s
        """
        cursor.execute(sql, (nama_usaha, komoditas, luas_sk, id_desa, id_sungai_besar, id_iup))
        self.koneksi.commit()
        cursor.close()

    def hapus_iup(self, id_iup):
        if self.koneksi is None: return
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM iup_samarinda WHERE id_iup = %s"
        cursor.execute(sql, (id_iup,))
        self.koneksi.commit()
        cursor.close()

    def ambil_semua_iup(self):
        if self.koneksi is None: return []
        cursor = self.koneksi.cursor(dictionary=True)
        sql = """
        SELECT
        i.id_iup, i.nama_usaha, i.komoditas, i.luas_sk,
        d.desa AS nama_desa,
        s.nama_sungai AS nama_sungai
        FROM iup_samarinda i
        LEFT JOIN desa d ON i.id_desa = d.id_desa
        LEFT JOIN sungai_besar s ON i.id_sungai_besar = s.id_sungai_besar
        ORDER BY i.id_iup DESC
        """
        cursor.execute(sql)
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    def ambil_semua_sungai_besar(self):
        if self.koneksi is None: return []
        cursor = self.koneksi.cursor(dictionary=True)
        cursor.execute("SELECT id_sungai_besar, nama_sungai FROM sungai_besar ORDER BY nama_sungai")
        hasil = cursor.fetchall()
        cursor.close()
        return hasil
