from models.book import BukuFisik, BukuDigital

def jalankan_menu_admin(user, user_service, book_service, loan_service):
    while True:
        print(f"\n=== MENU ADMIN ({user.username}) ===")
        print("1. Dashboard")
        print("2. Kelola Buku")
        print("3. Kelola Anggota")
        print("4. Lihat Peminjaman Aktif")
        print("0. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4/0): ")
        
        if pilihan == "1":
            print(f"Total Buku: {len(book_service.daftar_semua_buku())}")
            print(f"Total Anggota: {len(user_service.get_all_members())}")
            
        elif pilihan == "2":
            print("\n-- KELOLA BUKU --")
            print("1. Tambah Buku  2. Lihat Buku  3. Hapus Buku")
            sub = input("Pilih: ")
            if sub == "1":
                tipe = input("Tipe (1. Fisik, 2. Digital): ")
                id_b = input("ID Buku: ")
                jud = input("Judul: ")
                pen = input("Penulis: ")
                if tipe == "1":
                    stok = int(input("Stok: "))
                    buku = BukuFisik(jud, pen, id_b, "2024", "123", stok)
                else:
                    buku = BukuDigital(jud, pen, id_b, "2024", "123", "PDF", 5)
                if book_service.tambah_buku(buku):
                    print("Buku berhasil ditambahkan.")
                else:
                    print("ID sudah ada.")
            elif sub == "2":
                for b in book_service.daftar_semua_buku(): print(b.tampilkan_info())
            elif sub == "3":
                id_b = input("ID Buku yang dihapus: ")
                if book_service.hapus_buku(id_b): print("Dihapus.")
                else: print("Tidak ditemukan.")
                
        elif pilihan == "3":
            print("\n-- KELOLA ANGGOTA --")
            print("1. Lihat Anggota  2. Hapus Anggota")
            sub = input("Pilih: ")
            if sub == "1":
                for m in user_service.get_all_members():
                    print(f"[{m.user_id}] {m.username}")
            elif sub == "2":
                u_id = input("ID User yang dihapus: ")
                user_service.delete_member(u_id)
                print("Anggota dihapus (jika ada).")
                
        elif pilihan == "4":
            print("\n-- BUKU SEDANG DIPINJAM --")
            aktif = loan_service.get_semua_pinjaman_aktif()
            for a in aktif:
                print(f"[{a.loan_id}] User: {a.user_id}, Buku: {a.book_id} ({a.borrow_date})")
                
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")