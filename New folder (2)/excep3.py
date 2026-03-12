"""3.Banking System with Transactions 
Simulate real-time transactions between bank accounts. 
Handle errors like overdraft, transaction timeout, incorrect account numbers. """
import time

class BankingError(Exception):
    pass

class OverdraftError(BankingError):
    pass

class InvalidAccountError(BankingError):
    pass

class TransactionTimeoutError(BankingError):
    pass


class BankAccount:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise OverdraftError("Insufficient balance!")
        self.balance -= amount
        print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_no] = account

    def get_account(self, acc_no):
        if acc_no not in self.accounts:
            raise InvalidAccountError("Account number not found!")
        return self.accounts[acc_no]

    def transfer(self, from_acc, to_acc, amount, timeout=5):
        try:
            start_time = time.time()

            sender = self.get_account(from_acc)
            receiver = self.get_account(to_acc)

            if time.time() - start_time > timeout:
                raise TransactionTimeoutError("Transaction timeout!")

            sender.withdraw(amount)
            receiver.deposit(amount)

            print("Transaction Successful!")

        except BankingError as e:
            print("Transaction Failed:", e)




bank = Bank()

acc1 = BankAccount(101, "Alice", 5000)
acc2 = BankAccount(102, "Bob", 3000)

bank.add_account(acc1)
bank.add_account(acc2)


bank.transfer(101, 102, 1000)

print()


bank.transfer(101, 102, 10000)

print()

bank.transfer(101, 999, 500)