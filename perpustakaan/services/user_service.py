from models.user import Admin, Member
from services import storage

class UserService:
    def __init__(self):
        self.users = []
        self._load_users()

    def _load_users(self):
        data = storage.load("users.json")
        for u in data:
            if u["role"] == "admin":
                self.users.append(Admin(u["user_id"], u["username"], u["password"]))
            else:
                self.users.append(Member(u["user_id"], u["username"], u["password"], u.get("max_loans", 3)))
        
        # Buat default admin jika kosong
        if not any(isinstance(u, Admin) for u in self.users):
            self.users.append(Admin("U001", "admin", "admin123"))
            self._save_users()

    def _save_users(self):
        storage.save("users.json", [u.to_dict() for u in self.users])

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def register(self, username, password):
        if self.get_user_by_username(username):
            return False
        
        new_id = f"U{len(self.users) + 1:03d}"
        new_member = Member(new_id, username, password)
        self.users.append(new_member)
        self._save_users()
        return True

    def get_all_members(self):
        return [u for u in self.users if isinstance(u, Member)]

    def delete_member(self, user_id):
        self.users = [u for u in self.users if u.user_id != user_id or isinstance(u, Admin)]
        self._save_users()