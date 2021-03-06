class user: #Created class & attributes
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        # self.savings_account = Bank_account(0,100)
        self.account = [checking, savings]

    # Created methods for the class
    def get_account(self,account_number):
        return self.account[account_number]
        

    def display_user_balance(self, account_number):
        print(f"{self.name}'s account balance is ${self.account[account_number].display_account_info()}")
        return self

    def make_deposit(self, account_number, amount):
        self.account[account_number].make_deposit(amount)
        return self

    def make_withdrawl(self, account_number, amount):
        self.account[account_number].make_withdrawl(amount)
        return self


    def make_transfer(self, name, account_number, amount):
        amount = amount
        recipient = name.name
        self.account[account_number].balance -= amount
        name.account[account_number].balance += amount
        print(f"{self.name} made a transfer of ${amount} to {recipient}")
        return self

class Bank_account:
    def __init__(self, rate=0, amount=0):
        self.balance = amount
        self.interest = rate

    #Methods
    def display_account_info(self):
        # print(self.balance)
        return self.balance

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

savings = Bank_account(0.02,0)
checking = Bank_account(0.01,0)

#created instances
koda = user("koda","koda@husky.com")
lola = user("lola", "lola@husky.com")
bella= user("bella", "bella@muttpup.com")

# koda.checking_account.display_account_info()
# koda.savings_account.make_deposit(500).display_account_info()
# lola.savings_account.make_deposit(200).display_account_info()
koda.make_deposit(0,50).display_user_balance(0)
koda.make_withdrawl(0, 25).display_user_balance(0)
koda.make_withdrawl(0, 50).display_user_balance(0)
koda.make_transfer(bella,0,25)