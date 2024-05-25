# Define BankAccount class
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

# Create an instance of BankAccount
bank_acc = BankAccount("123456", "Bana")

# Perform deposit and withdrawal
bank_acc.deposit(1000)
print("Balance after deposit: $", bank_acc.get_balance())
bank_acc.withdraw(500)
print("Balance after withdrawal: $", bank_acc.get_balance())

# Define SavingsAccount subclass
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.deposit(interest_amount)

    def print_info(self):
        print("Current balance: $", self.get_balance())
        print("Interest rate: ", self.interest_rate)

# Create an instance of SavingsAccount
savings_acc = SavingsAccount("789012", "Sam", 5)
savings_acc.deposit(2000)
savings_acc.apply_interest()
savings_acc.print_info()
