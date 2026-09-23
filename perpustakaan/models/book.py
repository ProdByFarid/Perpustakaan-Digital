"""Physical and digital library item models."""

from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):
    def __init__(self, judul, penulis, id_buku, tahun_terbit, isbn):
        self._judul = judul
        self._penulis = penulis
        self._id_buku = id_buku
        self._tahun_terbit = tahun_terbit
        self._isbn = isbn

    @property
    def judul(self):
        return self._judul

    @judul.setter
    def judul(self, judul_baru):
        self._judul = judul_baru

    @property
    def penulis(self):
        return self._penulis

    @penulis.setter
    def penulis(self, penulis_baru):    
        self._penulis = penulis_baru

    @property
    def id_buku(self):
        return self._id_buku

    @property
    def tahun_terbit(self):
        return self._tahun_terbit

    @tahun_terbit.setter
    def tahun_terbit(self, tahun_baru):
        self._tahun_terbit = tahun_baru

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn_baru):
        self._isbn = isbn_baru

    @abstractmethod
    def get_jenis(self):
        pass

    @abstractmethod
    def tersedia(self):
        pass

    def to_dict(self):
        return {
            "id_buku": self.id_buku,
            "judul": self.judul,
            "penulis": self.penulis,
            "tahun_terbit": self.tahun_terbit,
            "isbn": self.isbn,
            "jenis": self.get_jenis(),
        }

    def tampilkan_info(self):
        return f"{self.id_buku} | {self.judul} - {self.penulis} | {self.get_jenis()} | Tahun: {self.tahun_terbit} | ISBN: {self.isbn}"

class BukuDigital(ItemPerpustakaan):
    def __init__(self, judul, penulis, id_buku, tahun_terbit, isbn, format_file, ukuran_file):
        super().__init__(judul, penulis, id_buku, tahun_terbit, isbn)
        self._format_file = format_file
        self._ukuran_file = ukuran_file

    @property
    def format_file(self):
        return self._format_file

    @format_file.setter
    def format_file(self, format_baru):
        self._format_file = format_baru

    @property
    def file_ukuran(self):
        return self._ukuran_file

    @file_ukuran.setter
    def file_ukuran(self, ukuran_baru):
        self._ukuran_file = ukuran_baru

    def get_jenis(self):
        return "Buku Digital"

    def tersedia(self):
        return True

    def download(self):
        return f"Mengunduh '{self.judul}' ({self._format_file}, {self._ukuran_file}MB)"

    def to_dict(self):
        data = super().to_dict()
        data["format_file"] = self._format_file
        data["file_ukuran"] = self._ukuran_file
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["judul"], data["penulis"], data["id_buku"], data["tahun_terbit"], data["isbn"], data["format_file"], data["file_ukuran"])

    def tampilkan_info(self):
        return f"{super().tampilkan_info()} | Format: {self._format_file} | Ukuran: {self._ukuran_file}MB"