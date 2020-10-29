class bankaccount():

    def __init__(self,owner,balance = 0):

        self.owner = owner
        self.balance = balance

    def __repr__(self):

            return f"owner: {self.owner} balance: {self.balance}"

    def withdraw(self,money):
        self.money = money
        self.balance = self.balance - self.money
        if self.balance < 0:
            print ("Insufficient balance. Please enter another amount")
        else:
            print ("Transaction Successful")
            print(f"Available balance: {self.balance}")

    def deposit(self,money):

        self.balance = self.balance + money
        print("Successfully deposited")
        print(f"Available balance: {self.balance}")

acct1 = bankaccount('Nikhilesh',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)




acct1.withdraw(500)
