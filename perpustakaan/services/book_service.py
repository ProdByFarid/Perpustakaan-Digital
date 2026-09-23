"""Book catalog management services."""

from models.book import BukuDigital

class BookService:
    def __init__(self):
        self._katalog = {}

    def tambah_buku_digital(self, judul, penulis, id_buku, tahun_terbit, isbn, format_file, ukuran_file):
        if id_buku in self._katalog:
            print(f"ID '{id_buku}' sudah dipakai.")
            return None
        buku = BukuDigital(judul, penulis, id_buku, tahun_terbit, isbn, format_file, ukuran_file)
        self._katalog[id_buku] = buku
        return buku

    def cari_buku(self, id_buku):
        return self._katalog.get(id_buku)

    def cari_berdasarkan_judul(self, keyword):
        keyword = keyword.lower()
        return [b for b in self._katalog.values() if keyword in b.judul.lower()]

    def daftar_semua_buku(self):
        return list(self._katalog.values())

    def perbarui_buku(self, id_buku, judul, penulis, tahun_terbit, isbn, format_file, ukuran_file):
        buku = self.cari_buku(id_buku)
        if buku is None:
            print(f"Buku dengan ID '{id_buku}' tidak ditemukan.")
            return False
        if judul is not None:
            buku.judul = judul
        if penulis is not None:
            buku.penulis = penulis
        if tahun_terbit is not None:
            buku.tahun_terbit = tahun_terbit
        if isbn is not None:
            buku.isbn = isbn
        if format_file is not None and isinstance(buku, BukuDigital):
            buku.format_file = format_file
        if ukuran_file is not None and isinstance(buku, BukuDigital):
            buku.file_ukuran = ukuran_file
        return True
    
    def hapus_buku(self, id_buku):
        if id_buku in self._katalog:
            del self._katalog[id_buku]
            return True
        return False

    def buku_tersedia(self, id_buku):
        buku = self.cari_buku(id_buku)
        if buku is None:
            return False
        return buku.tersedia()

    def download_buku(self, id_buku):
        buku = self.cari_buku(id_buku)
        if buku is None:
            return False
        return buku.download()

    def to_dict_list(self):
        return [buku.to_dict() for buku in self._katalog.values()]

    def load_from_data(self, data_list):
        self._katalog.clear()
        for data in data_list:
            buku = BukuDigital.from_dict(data)
            self._katalog[buku.id_buku] = buku
        
if __name__ == "__main__":
    service = BookService()
    service.tambah_buku_digital("Hujan", "Tere Liye", "B001", "2016", "978-0132350884", "PDF", 2.5)
    service.tambah_buku_digital("Laskar Pelangi", "Andrea Hirata", "B002", "2005", "978-1593279288", "PDF", 12.5)
    for buku in service.daftar_semua_buku():
        print(f"{buku.tampilkan_info()}")

    service.perbarui_buku("B001", judul="Laut Bercerita", penulis=None, tahun_terbit=None, isbn=None, format_file=None, ukuran_file=3.0)
    print(service.download_buku("B002"))
    print("\nDaftar katalog setelah update:")
    for buku in service.daftar_semua_buku():
        print(f"{buku.tampilkan_info()}")

    print(service.to_dict_list())