from datetime import datetime, timedelta

class Loan:
    def __init__(self, loan_id, user_id, book_id, borrow_date=None, status="dipinjam"):
        self.loan_id = loan_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date or datetime.now().strftime("%Y-%m-%d")
        self.status = status

    def to_dict(self):
        return {
            "loan_id": self.loan_id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "borrow_date": self.borrow_date,
            "status": self.status
        }