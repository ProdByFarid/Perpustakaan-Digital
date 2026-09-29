from services.user_service import UserService
from services.book_service import BookService
from services.loan_service import LoanService
from menu_admin import jalankan_menu_admin
from menu_member import jalankan_menu_member

def login_flow(user_service):
    while True:
        username = input("\nMasukkan Username: ")
        user = user_service.get_user_by_username(username)
        
        if not user:
            print("Username tidak valid/tidak ditemukan.")
            continue # Kembali input username sesuai flowchart
            
        batas_percobaan = 3
        while batas_percobaan > 0:
            password = input("Masukkan Password: ")
            if user.verify_password(password):
                print("Login Berhasil!")
                return user
            
            batas_percobaan -= 1
            if batas_percobaan > 0:
                print(f"Password salah! Sisa percobaan: {batas_percobaan}")
            else:
                print("Login Gagal! Anda telah mencoba 3 kali.")
                return None

def registrasi_flow(user_service):
    print("\n--- REGISTRASI MEMBER ---")
    while True:
        username = input("Masukkan Username baru: ")
        if user_service.get_user_by_username(username):
            print("Username sudah dipakai, coba yang lain.")
            continue
        
        password = input("Masukkan Password: ")
        if len(password) < 3:
            print("Password tidak valid (terlalu pendek).")
            continue
            
        if user_service.register(username, password):
            print("Registrasi Berhasil! Silakan Login.")
            break

def main():
    user_service = UserService()
    book_service = BookService()
    loan_service = LoanService(book_service)
    
    while True:
        print("\n=== MENU UTAMA PERPUSTAKAAN ===")
        print("1. Login")
        print("2. Registrasi")
        print("0. Logout/Keluar")
        
        pilihan = input("Pilih opsi (1/2/0): ")
        
        if pilihan == "1":
            user = login_flow(user_service)
            if user:
                if user.get_role() == "admin":
                    jalankan_menu_admin(user, user_service, book_service, loan_service)
                else:
                    jalankan_menu_member(user, book_service, loan_service)
                    
        elif pilihan == "2":
            registrasi_flow(user_service)
            
        elif pilihan == "0":
            print("Terima kasih sudah berkunjung.")
            break
            
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()