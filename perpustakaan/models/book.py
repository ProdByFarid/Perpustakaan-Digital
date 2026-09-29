from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):
    def __init__(self, judul, penulis, id_buku, tahun_terbit, isbn):
        self._judul = judul
        self._penulis = penulis
        self._id_buku = id_buku
        self._tahun_terbit = tahun_terbit
        self._isbn = isbn

    @property
    def judul(self): return self._judul
    @judul.setter
    def judul(self, val): self._judul = val

    @property
    def penulis(self): return self._penulis
    @penulis.setter
    def penulis(self, val): self._penulis = val

    @property
    def id_buku(self): return self._id_buku

    @property
    def tahun_terbit(self): return self._tahun_terbit
    
    @property
    def isbn(self): return self._isbn

    @abstractmethod
    def get_jenis(self): pass

    @abstractmethod
    def tersedia(self): pass

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
        return f"[{self.id_buku}] {self.judul} - {self.penulis} ({self.get_jenis()})"

class BukuFisik(ItemPerpustakaan):
    def __init__(self, judul, penulis, id_buku, tahun_terbit, isbn, stok):
        super().__init__(judul, penulis, id_buku, tahun_terbit, isbn)
        self.stok = stok

    def get_jenis(self): return "Buku Fisik"
    
    def tersedia(self): return self.stok > 0
    
    def kurangi_stok(self):
        if self.stok > 0: self.stok -= 1
            
    def tambah_stok(self):
        self.stok += 1

    def to_dict(self):
        data = super().to_dict()
        data["stok"] = self.stok
        return data

class BukuDigital(ItemPerpustakaan):
    def __init__(self, judul, penulis, id_buku, tahun_terbit, isbn, format_file, ukuran_file):
        super().__init__(judul, penulis, id_buku, tahun_terbit, isbn)
        self.format_file = format_file
        self.ukuran_file = ukuran_file

    def get_jenis(self): return "Buku Digital"
    
    def tersedia(self): return True

    def download(self):
        return f"Mengunduh '{self.judul}' ({self.format_file}, {self.ukuran_file}MB)"

    def to_dict(self):
        data = super().to_dict()
        data["format_file"] = self.format_file
        data["ukuran_file"] = self.ukuran_file
        return data