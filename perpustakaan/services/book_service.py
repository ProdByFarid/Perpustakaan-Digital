from models.book import BukuFisik, BukuDigital
from services import storage

class BookService:
    def __init__(self):
        self._katalog = {}
        self._load_books()

    def _load_books(self):
        data = storage.load("books.json")
        for b in data:
            if b["jenis"] == "Buku Fisik":
                self._katalog[b["id_buku"]] = BukuFisik(b["judul"], b["penulis"], b["id_buku"], b["tahun_terbit"], b["isbn"], b["stok"])
            else:
                self._katalog[b["id_buku"]] = BukuDigital(b["judul"], b["penulis"], b["id_buku"], b["tahun_terbit"], b["isbn"], b["format_file"], b["ukuran_file"])

    def _save_books(self):
        storage.save("books.json", [b.to_dict() for b in self._katalog.values()])

    def tambah_buku(self, buku):
        if buku.id_buku in self._katalog:
            return False
        self._katalog[buku.id_buku] = buku
        self._save_books()
        return True

    def daftar_semua_buku(self):
        return list(self._katalog.values())

    def cari_buku(self, id_buku):
        return self._katalog.get(id_buku)

    def hapus_buku(self, id_buku):
        if id_buku in self._katalog:
            del self._katalog[id_buku]
            self._save_books()
            return True
        return False