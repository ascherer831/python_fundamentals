class user: #Created class & attributes
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.savings_account = Bank_account(0,100)
        self.checking_account = Bank_account(0.2, 500)
    # Created methods for the class
    # def display_user_balance(self):
    #     print(f"{self.name}'s account balance is ${self.balance}")
    #     return self

    # def make_deposit(self, amount):
    #     self.balance += amount
    #     return self

    # def make_withdrawl(self, amount):
    #     self.balance -= amount
    #     return self

    # def make_transfer(self, name, amount):
    #     amount = amount
    #     recipient = name.name
    #     self.balance -= amount
    #     name.balance += amount
    #     print(f"{self.name} made a transfer of ${amount} to {recipient}")
    #     return self

class Bank_account:
    def __init__(self, rate=0, amount=0):
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


#created instances
koda = user("koda","koda@husky.com")
lola = user("lola", "lola@husky.com")
bella= user("bella", "bella@muttpup.com")

koda.checking_account.display_account_info()
koda.savings_account.make_deposit(500).display_account_info()
lola.savings_account.make_deposit(200).display_account_info()
