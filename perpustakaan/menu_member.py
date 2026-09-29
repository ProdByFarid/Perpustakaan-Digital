def jalankan_menu_member(user, book_service, loan_service):
    while True:
        print(f"\n=== MENU MEMBER ({user.username}) ===")
        print("1. Dashboard")
        print("2. Katalog Buku")
        print("3. Pinjam Buku")
        print("4. Riwayat Peminjaman")
        print("0. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4/0): ")
        
        if pilihan == "1":
            print("Selamat datang di Perpustakaan!")
            
        elif pilihan == "2":
            print("\n-- KATALOG BUKU --")
            buku_list = book_service.daftar_semua_buku()
            for b in buku_list:
                print(b.tampilkan_info())
                
        elif pilihan == "3":
            id_buku = input("Masukkan ID Buku yang ingin dipinjam: ")
            hasil = loan_service.pinjam_buku(user.user_id, id_buku)
            print("Status:", hasil)
            
        elif pilihan == "4":
            print("\n-- RIWAYAT PEMINJAMAN --")
            riwayat = loan_service.get_riwayat_user(user.user_id)
            if not riwayat: print("Belum ada riwayat.")
            for r in riwayat:
                buku = book_service.cari_buku(r.book_id)
                judul = buku.judul if buku else "Buku Terhapus"
                print(f"- {judul} (Dipinjam: {r.borrow_date}) - {r.status}")
                
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")