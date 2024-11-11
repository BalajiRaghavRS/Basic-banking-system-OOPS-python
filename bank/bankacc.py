class Balanceerror(Exception):
    pass
class Bankacc:
    def __init__(self,initialamount,acctname):
        self.balance=initialamount
        self.name=acctname
        print(f"\nAccount '{self.name}' created.\n\nBalance = ${self.balance:.2f}")
    
    def getbalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self,amount):
        self.balance=self.balance +amount
        print(f"\nDeposit Done for '{self.name}'.")
        self.getbalance()

    def viatrans(self,amount):
        if self.balance >=amount:
            return
        else:
            raise Balanceerror(
                f"\nSorry, Account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    def withdraw(self,amount):
        try:
            self.viatrans(amount)
            self.balance=self.balance-amount
            print("\nWithdraw Complete")
            self.getbalance()
        except Balanceerror as error:
            print(f'\nWithdraw error : {error}')
    def transfer(self,amount,account):
        try:
            print('\n========================\n\nBeginning Transfer..🚀🚀🚀')
            self.viatrans(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!!☑️☑️☑️\n\n========================')
        except Balanceerror as error:
            print(f'\nTransfer interrupted. ❌{error}')
class Interestacc(Bankacc):
    def deposit(self, amount):
        interest=amount*1.05
        self.balance=self.balance+interest
        print("\nDeposit Complete.")
        self.getbalance()

class Savingacc(Interestacc):
    def __init__(self,initalamount,acctname):
        super().__init__(initalamount,acctname)
        self.fee=5
    def withdraw(self, amount):
        try:
            self.viatrans(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\nWithdraw Completed.")
            self.getbalance()
        except Balanceerror as error:
            print(f'\nWithdraw interrupted: {error}')
class Rd(Bankacc):
    def __init__(self,amount,years):
        self.amount=amount
        self.years=years
        self.rate=5
        self.interest=self.amount*(self.rate/100)
        self.month=self.years*12
        self.monthrd_rate=self.interest*self.month
        self.rdamount=self.amount*self.month + self.monthrd_rate
        print(f'\nRD amount is {self.amount} and Duration is {self.years} years, Then the rate of interest for the amount is {self.rate:.2f}% the total months {self.month} the interest is {self.monthrd_rate} and total rd amount is {self.rdamount}')

    # def joinrd(self,name):
    #     self.name=name
    #     self.balance=self.balance+self.rdamount
    #     self.getbalance()
class joinrd(Rd):
    def __init__(self, initialamount,years, acctname):
        self.initialamount=initialamount
        self.years=years
        self.acctname=acctname
        Rd(self.initialamount,self.years)
def main():
    print("Enter the Name for Bank Account : ")
    a=input()
    print("\nPlease Enter the initial amount :")
    b=int(input())
    c=Bankacc(b,a)
    print(c)

main()