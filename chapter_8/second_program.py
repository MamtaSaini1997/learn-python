# create Account class with 2 attribute - balance & account no.
# create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, debit):
        self.debit = debit
        self.balance = self.balance - self.debit
        print("debit amount:", self.debit)
        print(f"Remaining Balance is - {self.balance}")

    def credit(self, credit):
        self.credit = credit
        print("credit amount:", self.credit)
        self.balance = self.balance + self.credit
        print(f"Remaining Balance is - {self.balance}")
           
    def get_balance(self):
        print(f"Remaining Balance is - {self.balance}")

Manjeet = Account(100, 123)
Manjeet.debit(10)
Manjeet.get_balance()
Manjeet.credit(100)