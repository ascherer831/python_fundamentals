class user: #Created class & attributes
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.balance = 0
    # Created methods for the class
    def display_user_balance(self):
        print(f"{self.name}'s account balance is ${self.balance}")
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

    def make_transfer(self, name, amount):
        amount = amount
        recipient = name.name
        self.balance -= amount
        name.balance += amount
        print(f"{self.name} made a transfer of ${amount} to {recipient}")
        return self

#created instances
koda = user("koda","koda@husky.com")
lola = user("lola", "lola@husky.com")
bella= user("bella", "bella@muttpup.com")

koda.make_deposit(100).make_deposit(50).make_deposit(100).make_withdrawl(75).display_user_balance()

lola.make_deposit(150).make_deposit(100).make_withdrawl(50).display_user_balance()

bella.make_deposit(400).make_withdrawl(100).make_withdrawl(25).make_withdrawl(25).display_user_balance()

koda.make_transfer(bella, 100).display_user_balance()
bella.display_user_balance()