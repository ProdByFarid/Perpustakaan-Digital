# Panduan Proyek: Sistem Perpustakaan Digital Berbasis OOP

Proyek kelompok (6 orang), deadline akhir Oktober 2026.
Penerapan 4 pilar OOP: **Abstraction, Inheritance, Encapsulation, Polymorphism**.

## Tahapan proyek

| Tahap | Isi | Waktu |
|-------|-----|-------|
| 1 | Program inti CLI (tanpa framework, data JSON) | 21 - 28 Sep |
| 2 | Rapikan, tes, pilih database, belajar Django | 29 Sep - 4 Okt |
| 3 | Backend Django + database | 5 - 18 Okt |
| 4 | Frontend HTML, CSS, JS + Tailwind | 19 - 25 Okt |
| 5 | Finalisasi, uji menyeluruh, presentasi | 26 - 31 Okt |

Target selesai 29 Okt, sisakan 2 hari cadangan (Keknya bakal ngaret deh, Tapi semoga ngga).

---

## 1. Struktur folder

```
perpustakaan/
├── main.py                  # pintu masuk program, login lalu arahkan ke menu
├── menu_member.py           # tampilan menu Anggota
├── menu_admin.py            # tampilan menu Admin
├── models/
│   ├── user.py              # User (abstract), Member, Admin
│   ├── book.py              # LibraryItem (abstract), Book, DigitalBook
│   └── loan.py              # Loan (peminjaman)
├── services/
│   ├── storage.py           # satu-satunya file yang baca/tulis JSON
│   ├── user_service.py      # login, daftar, kelola anggota
│   ├── book_service.py      # tambah/ubah/hapus/cari buku
│   └── loan_service.py      # pinjam, kembali, denda, riwayat, laporan
└── data/
    ├── users.json           # admin dan anggota
    ├── books.json           # buku fisik dan digital (dibedakan field "type")
    └── loans.json           # catatan peminjaman
```

### Fungsi tiap bagian

**Root**
- `main.py`: dijalankan dengan `python main.py`. Isinya login, lalu memilih menu sesuai role (admin atau anggota).
- `menu_member.py`: menu Anggota: Dashboard, Katalog Buku, Detail Buku, Peminjaman, Buku Digital, Riwayat Peminjaman, Profil.
- `menu_admin.py`: menu Admin: Dashboard, Kelola Buku, Kelola Anggota, Peminjaman & Pengembalian, Buku Digital, Laporan.

**`models/`** (cetakan objek, tempat OOP paling terlihat)
- `user.py`: `User` (induk, abstract), `Member` dan `Admin` (anak).
- `book.py`: `LibraryItem` (induk, abstract), `Book` (fisik) dan `DigitalBook`.
- `loan.py`: `Loan`, mencatat siapa meminjam apa, jatuh tempo, status, dan denda.

**`services/`** (aturan dan logika program)
- `storage.py`: membaca dan menulis file JSON. Tidak ada file lain yang boleh membuka JSON langsung.
- `user_service.py`, `book_service.py`, `loan_service.py`: logika bisnis per bidang.

**`data/`** (data dummy, bebas diedit)
- Tiga file JSON. Format contoh ada di bagian 5.

### Alur satu fitur (contoh: anggota meminjam buku)
```
menu_member.py  ->  loan_service.borrow()  ->  book_service (cek stok)
                ->  Loan (objek baru)      ->  storage (simpan ke JSON)
```
Alurnya selalu: **menu -> service -> model -> storage**.

---

## 2. Penerapan 4 pilar OOP

| Pilar | Di mana | Contoh |
|-------|---------|--------|
| Abstraction | `User`, `LibraryItem` | Abstract class, tidak boleh dibuat langsung; anak class wajib mengisi method abstract |
| Inheritance | `Member`, `Admin` dari `User`; `Book`, `DigitalBook` dari `LibraryItem` | Atribut umum (nama, judul) ditulis sekali di induk |
| Encapsulation | Password di `User`, stok di `Book`, status di `Loan` | Atribut private, hanya berubah lewat method seperti `verify_password()`, `borrow()`, `mark_returned()` |
| Polymorphism | `get_loan_days()`, `calculate_fine()`, `get_role()` | Buku fisik: 7 hari dan denda per hari. Buku digital: 3 hari dan tanpa denda |

---

## 3. Kontrak method (supaya bisa dikerjakan paralel)

Nama class dan method di bawah **jangan diubah tanpa diskusi**. Menu bisa langsung memanggilnya walau isinya belum selesai.

**models/user.py**
- `User(ABC)`: `verify_password(plain)`, `get_role()` (abstract)
- `Member(User)`: tambahan `max_loans`, `join_date`
- `Admin(User)`

**models/book.py**
- `LibraryItem(ABC)`: `is_available()`, `get_loan_days()`, `calculate_fine(days_late)`, `to_dict()` (semua abstract), `get_info()`
- `Book`: `borrow()`, `return_one()`
- `DigitalBook`: selalu tersedia, tanpa denda

**models/loan.py**
- `Loan`: `days_late()`, `mark_returned(item)`, `to_dict()`

**services/storage.py**
- `load(filename)` mengembalikan list of dict
- `save(filename, data)`

**services/user_service.py**
- `login(username, password)`, `register_member(...)`, `get_all_members()`, `get_member(id)`, `update_profile(id, ...)`, `delete_member(id)`

**services/book_service.py**
- `get_all()`, `get_digital()`, `search(keyword, category)`, `get_by_id(id)`, `add(item)`, `update(item)`, `delete(id)`

**services/loan_service.py**
- `borrow(member, item_id)`, `return_item(loan_id)`, `get_active_by_member(id)`, `get_history_by_member(id)`, `get_all()`
- Laporan: `summary()`, `overdue()`, `popular(top)`

**Aturan bisnis**
- Anggota maksimal 3 pinjaman aktif
- Buku fisik hanya bisa dipinjam jika stok tersedia
- Buku digital selalu bisa dipinjam
- Denda buku fisik dihitung per hari keterlambatan

---

## 4. Pembagian tugas 6 orang

| No | Nama | File yang dimiliki |
|---|------|--------------------|
| 1 | Farid | `models/user.py`, `services/user_service.py` |
| 2 | Annisa | `models/book.py`, `services/book_service.py` |
| 3 | Arya | `models/loan.py`, `services/loan_service.py` |
| 4 | Yoga | `services/storage.py`, `data/*.json` |
| 5 | Rega | `main.py`, `menu_member.py` |
| 6 | Ghina | `menu_admin.py` |

Aturan: **satu file, satu pemilik**. Mau mengubah file orang lain? Chat pemiliknya atau buat Issue di GitHub.

---

## 5. Contoh format data (JSON)

**data/users.json**
```json
[
  {
    "id": "U001",
    "name": "Pustakawan Utama",
    "username": "admin",
    "password_hash": "<hash sha256 dari admin123>",
    "role": "admin"
  },
  {
    "id": "U002",
    "name": "Budi Santoso",
    "username": "budi",
    "password_hash": "<hash sha256 dari member123>",
    "role": "member",
    "join_date": "2026-08-01",
    "max_loans": 3
  }
]
```
Password disimpan sebagai hash, bukan teks asli. Hash bisa dibuat dengan:
```python
import hashlib
print(hashlib.sha256("member123".encode()).hexdigest())
```

**data/books.json** (fisik dan digital dalam satu file)
```json
[
  {
    "id": "B001", "type": "physical",
    "title": "Laskar Pelangi", "author": "Andrea Hirata",
    "category": "Novel", "year": 2005,
    "stock": 3, "available": 3
  },
  {
    "id": "D001", "type": "digital",
    "title": "Pengantar OOP dengan Python", "author": "Tim Dosen",
    "category": "Teknologi", "year": 2023,
    "format": "pdf", "file_size_mb": 4.2
  }
]
```

**data/loans.json**
```json
[
  {
    "id": "L001", "member_id": "U002", "item_id": "B001",
    "borrow_date": "2026-09-15", "due_date": "2026-09-22",
    "return_date": null, "status": "dipinjam", "fine": 0
  }
]
```

---
## 6. Panduan Git (kerja kolaborasi)

### Sekali saja
**Ketua:**
1. Buat repo kosong di GitHub.
2. Settings > Collaborators > undang 5 anggota lain.
3. Dari folder proyek:
   ```bash
   git init
   git add .
   git commit -m "chore: initial project structure"
   git branch -M main
   git remote add origin <URL-REPO>
   git push -u origin main
   ```
4. Settings > Branches: aktifkan branch protection untuk `main` (wajib Pull Request sebelum merge).

**Anggota lain:**
```bash
git clone <URL-REPO>
cd perpustakaan
```

### Alur harian tiap anggota
```bash
git checkout main
git pull origin main                    # ambil update terbaru
git checkout -b feature/nama-fitur      # contoh: feature/login
# ... coding ...
git add .
git commit -m "feat: tambah fungsi login"
git push origin feature/nama-fitur
```
Lalu di GitHub klik **Compare & pull request**, minta 1 teman me-review, dan merge. Setelah merge, kembali ke `main`, `git pull`, lalu buat branch baru.

### Konvensi
- Branch: `feature/...`, `fix/...`, `docs/...`
- Pesan commit: `feat:` fitur baru, `fix:` perbaikan bug, `docs:` dokumentasi
- Commit kecil dan sering, minimal sekali sehari
- Jangan langsung push ke `main`
- Kalau `main` sudah berubah, jalankan `git pull origin main` di branch kamu sebelum push

### Mengatasi konflik
Buka file yang konflik, cari tanda `<<<<<<<`, `=======`, `>>>>>>>`. Pilih isi yang benar, hapus tanda-tandanya, lalu `git add .` dan `git commit`. Kalau ragu, tanya pemilik file.

---

## 7. Jadwal detail

### Tahap 1: Program inti CLI (21 - 28 Sep)
- **21 - 22 Sep:** buat repo, semua clone, kickoff 30 menit (bagi tugas, sepakati kontrak method)
- **22 - 25 Sep:** tiap orang mengerjakan bagiannya lewat branch dan Pull Request
- **26 - 27 Sep:** integrasi, jalankan `python main.py`, perbaiki bug lintas modul
- **28 Sep:** demo internal, beri tag rilis `v0.1-cli`

### Tahap 2: Persiapan Django (29 Sep - 4 Okt)
- Tes dan rapikan kode
- Tulis dokumentasi 4 pilar beserta contoh potongan kodenya
- Putuskan database (rekomendasi: **SQLite** dulu, bawaan Django dan mudah dipindah ke PostgreSQL)
- Semua belajar dasar Django: Model, View, URL, Template

### Tahap 3: Backend Django (5 - 18 Okt)
- Buat project dan app Django
- Ubah class inti menjadi Django Model
- Bagi per fitur: auth, katalog, peminjaman, admin dan laporan

### Tahap 4: Frontend (19 - 25 Okt)
- Template HTML + Tailwind: dashboard, katalog, detail buku, peminjaman, riwayat, profil, halaman admin

### Tahap 5: Finalisasi (26 - 31 Okt)
- Uji menyeluruh, perbaiki bug, README, siapkan presentasi

---

## 8. Persiapan pindah ke Django

Program inti nanti dipindah ke Django. Yang dipakai ulang adalah rancangan class dan aturan bisnisnya.

| Bagian sekarang | Di Django |
|---|---|
| `models/` | Menjadi Django Model (OOP tetap terlihat: abstract base class, inheritance, override method) |
| `services/` | Sebagian besar dipakai ulang, hanya cara ambil data berubah ke ORM |
| `storage.py` + `data/*.json` | Diganti database lewat Django ORM |
| `main.py`, `menu_*.py` | Diganti `views.py`, `urls.py`, dan template HTML |
| Login buatan sendiri | Diganti sistem auth bawaan Django |

### Aturan dari sekarang supaya migrasi mudah
1. **Jangan** pakai `print()` dan `input()` di `models/` dan `services/`. Fungsi cukup mengembalikan data, yang menampilkan hanya file menu.
2. Semua akses data lewat `services/storage.py`, tidak ada file lain yang membuka JSON.
3. Aturan bisnis (batas pinjaman, denda, cek stok) hanya di `models/` dan `services/`, jangan di menu.
4. Fungsi service mengembalikan objek atau list yang bisa dipakai ulang oleh CLI maupun web.

---

## 9. Checklist sebelum demo tahap 1

- [ ] Login admin dan anggota berhasil
- [ ] Anggota bisa mencari buku (judul, penulis, kategori)
- [ ] Anggota bisa melihat detail, meminjam, dan mengembalikan buku
- [ ] Anggota bisa melihat buku digital, riwayat, dan profil
- [ ] Admin bisa tambah, ubah, hapus buku dan anggota
- [ ] Admin bisa memproses pengembalian dan melihat laporan
- [ ] Denda buku fisik terhitung benar, buku digital tanpa denda
- [ ] Batas 3 pinjaman aktif berjalan
- [ ] 4 pilar OOP bisa ditunjukkan di kode
- [ ] Semua anggota punya commit di repo
