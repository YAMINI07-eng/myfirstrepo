class Bank:
    def __init__(self):
        self.__balance=0; #private varable
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance or amount<0:
            print("insufficient balance")
        else:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance
b=Bank()
b.deposit(1000)
b.deposit(1200)
b.withdraw(5000)
print(b.get_balance())