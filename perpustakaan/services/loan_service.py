from models.loan import Loan
from services import storage

class LoanService:
    def __init__(self, book_service):
        self.loans = []
        self.book_service = book_service
        self._load_loans()

    def _load_loans(self):
        data = storage.load("loans.json")
        for l in data:
            self.loans.append(Loan(l["loan_id"], l["user_id"], l["book_id"], l["borrow_date"], l["status"]))

    def _save_loans(self):
        storage.save("loans.json", [l.to_dict() for l in self.loans])

    def pinjam_buku(self, user_id, book_id):
        buku = self.book_service.cari_buku(book_id)
        if not buku: return "Buku tidak ditemukan"
        if not buku.tersedia(): return "Buku tidak tersedia/stok habis"

        if buku.get_jenis() == "Buku Fisik":
            buku.kurangi_stok()
            self.book_service._save_books()

        loan_id = f"L{len(self.loans) + 1:03d}"
        new_loan = Loan(loan_id, user_id, book_id)
        self.loans.append(new_loan)
        self._save_loans()
        
        if buku.get_jenis() == "Buku Digital":
            return buku.download()
        return "Berhasil dipinjam"

    def get_riwayat_user(self, user_id):
        return [l for l in self.loans if l.user_id == user_id]

    def get_semua_pinjaman_aktif(self):
        return [l for l in self.loans if l.status == "dipinjam"]