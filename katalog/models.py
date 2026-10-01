from django.db import models

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    stok = models.IntegerField(default=1)

    def __str__(self):
        return self.judul

class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    nama_peminjam = models.CharField(max_length=100)
    tanggal_pinjam = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama_peminjam} - {self.buku.judul}"
    
class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    nama_peminjam = models.CharField(max_length=100)
    tanggal_pinjam = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama_peminjam