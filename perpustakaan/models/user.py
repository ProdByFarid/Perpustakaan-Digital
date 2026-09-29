from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def verify_password(self, plain):
        return self.password == plain

    @abstractmethod
    def get_role(self):
        pass

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "role": self.get_role()
        }

class Admin(User):
    def get_role(self):
        return "admin"

class Member(User):
    def __init__(self, user_id, username, password, max_loans=3):
        super().__init__(user_id, username, password)
        self.max_loans = max_loans

    def get_role(self):
        return "member"
        
    def to_dict(self):
        data = super().to_dict()
        data["max_loans"] = self.max_loans
        return data