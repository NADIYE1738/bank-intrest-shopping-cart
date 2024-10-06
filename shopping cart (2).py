class BankAccount:
    interest_rate = 0.05  # class variable for the interest rate 

    def __init__(self, account_holder):
        self.account_holder = account_holder 
        self.balance = 0  

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
# calculation of the amount with the intrest inclusive

    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")


# Creating two accounts
account1 = BankAccount("Alice white")
account2 = BankAccount("peter")

# Performing operations on the accounts
account1.deposit(55000)
account2.deposit(100000)

account1.withdraw(10000)
account2.withdraw(200000)

account1.apply_interest()
account2.apply_interest()

# Displaying account information
account1.display_account_info()
account2.display_account_info()
