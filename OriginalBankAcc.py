
class BankAccount:

    def __init__(self, ownerValuePassedToFunction, balanceValuePassedToFunction):

        self.owner = ownerValuePassedToFunction
        self.balance = balanceValuePassedToFunction
    
    def deposit(self, amount):

        self.balance = self.balance + amount

        return self.balance 
    
    def withdraw(self, amount):

        if self.balance > amount:
            self.balance = self.balance - amount
            return True
        else:
            return False
        
        
        

    def currentBalance(self):

        return self.balance


myAccount = BankAccount("Rishi", 20)

print(myAccount.currentBalance())

result = myAccount.withdraw(10)

if result == True:
    print(f"Your withdrawal was successful. Your new balance is {myAccount.currentBalance()}")
else:
    print(f"Sorry, withdrawal failed. Your current balance is {myAccount.currentBalance()}")

