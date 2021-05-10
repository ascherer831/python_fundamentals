class user: #Created class & attributes
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.balance = 0
    # Created methods for the class
    def display_user_balance(self):
        print(f"{self.name}'s account balance is ${self.balance}")

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount

    def make_transfer(self, name, amount):
        self.balance -= amount
        name.balance += amount

#created instances
koda = user("koda","koda@husky.com")
lola = user("lola", "lola@husky.com")
bella= user("bella", "bella@muttpup.com")

koda.make_deposit(100)
koda.make_deposit(50)
koda.make_deposit(100)
koda.make_withdrawl(75)
koda.display_user_balance()

lola.make_deposit(150)
lola.make_deposit(100)
lola.make_withdrawl(50)
lola.display_user_balance()

bella.make_deposit(400)
bella.make_withdrawl(100)
bella.make_withdrawl(25)
bella.make_withdrawl(25)
bella.display_user_balance()

koda.make_transfer(bella, 100)
koda.display_user_balance()
bella.display_user_balance()