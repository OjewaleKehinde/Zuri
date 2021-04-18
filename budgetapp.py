
class Budget():
    def __init__(self, **categories):
        self.categories = categories

    def deposit(self, amount, category):
        self.categories[category] += amount
        print('The sum of {0} naira has just been deposited into your funds for {1}. Your new {1} balance is {2}'.format(amount,category,self.categories[category]))

    def withdraw(self,amount,category):
        if amount > self.categories[category]:
            print('Your transaction could not be completed due to insufficient funds in your {} balance'.format(category))
        else:
            self.categories[category] -= amount
            print('You have just withdrawn {} naira from your {} balance'.format(amount,category))

    def transfer(self,amount,sender,recipient):
        if amount > self.categories[sender]:
            print('Your transaction could not be completed due to insufficient funds in your {} balance'.format(sender))
        else:
            self.categories[sender] -= amount
            self.categories[recipient] += amount
            print('You have successfully transferred {2} naira from your funds for {0} to your funds for {1}. Your new {0} balance is {3} naira while your new {1} balance is {4} naira'.format(sender,recipient,amount,self.categories[sender],self.categories[recipient]))

    def balance(self, *balanceCategories):
        self.balanceCategories = balanceCategories
        if self.balanceCategories is ():
            print('Your budget balance for each category are as follows:')
            for category, balance in self.categories.items():
                print('Your budget balance for {} is {} naira'.format(category,balance))
            
        else:
            for category in self.balanceCategories:
                print('Your budget balance for {} is {} naira'.format(category,self.categories[category]))

class Budget():
    def __init__(self, **categories):
        self.categories = categories

    def deposit(self, amount, category):
        self.categories[category] += amount
        print('The sum of {0} naira has just been deposited into your funds for {1}. Your new {1} balance is {2}'.format(amount,category,self.categories[category]))

    def withdraw(self,amount,category):
        if amount > self.categories[category]:
            print('Your transaction could not be completed due to insufficient funds in your {} balance'.format(category))
        else:
            self.categories[category] -= amount
            print('You have just withdrawn {} naira from your {} balance'.format(amount,category))

    def transfer(self,amount,sender,recipient):
        if amount > self.categories[sender]:
            print('Your transaction could not be completed due to insufficient funds in your {} balance'.format(sender))
        else:
            self.categories[sender] -= amount
            self.categories[recipient] += amount
            print('You have successfully transferred {2} naira from your funds for {0} to your funds for {1}. Your new {0} balance is {3} naira while your new {1} balance is {4} naira'.format(sender,recipient,amount,self.categories[sender],self.categories[recipient]))

    def balance(self, *balanceCategories):
        self.balanceCategories = balanceCategories
        if self.balanceCategories is ():
            print('Your budget balance for each category are as follows:')
            for category, balance in self.categories.items():
                print('Your budget balance for {} is {} naira'.format(category,balance))
            
        else:
            for category in self.balanceCategories:
                print('Your budget balance for {} is {} naira'.format(category,self.categories[category]))


budget1=Budget(electricity=600,food=800,game=900,housing=1000,gym=350)

budget1.withdraw(100,'food')
budget1.deposit(100,'game')
budget1.transfer(100,'food','housing')
budget1.balance('game')
budget1.balance()

