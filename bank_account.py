class Accont:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print(f'{self.name}账户存入{amount}钱，余额是{self.balance}')

    def withdraw(self,amount):
        if self.balance<amount:
            print('你的钱不够了，取不出这么多')
        else:
            self.balance-=amount
            print(f'{self.name}账户取出{amount}钱,余额是{self.balance}')

acc=Accont('lili',0)
acc.deposit(1000)
acc.withdraw(500)
acc.withdraw(600)
