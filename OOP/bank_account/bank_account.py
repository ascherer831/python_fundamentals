class Bank_account:
    def __init__(self, account_name, rate, amount=0):
        self.account_name = account_name
        self.balance = amount
        self.interest = rate

    #Methods
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        if amount > self.balance:
            print("Insuficient funds: Charging a $5 fee.")
            self.balance -= amount + 5
        else:
            self.balance -= amount
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest
            return self
        else:
            return self

a = Bank_account('a', 0.02)
b = Bank_account('b', 0.04, 100)

a.make_deposit(5000).make_deposit(100).make_deposit(200).make_withdrawl(6000).display_account_info().yield_interest().display_account_info()

b.make_deposit(500).make_deposit(500).make_withdrawl(100).make_withdrawl(40).make_withdrawl(10).make_withdrawl(50).yield_interest().display_account_info()
