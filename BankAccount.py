
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

myAccount = BankAccount("Rishi", 0)

print(chr(27) + "[H" + chr(27) + "[J")

while True:
    print("Press 1 for Deposit")
    print("Press 2 for Withdrawal")
    print("Press 3 for Check balance")
    print("Press 4 to quit")

    userChoice = input("What would you like to do today? ")
    

    if userChoice == "4":
        
        break
    
    elif userChoice == "3":
        
        print(f"Your current balance is {myAccount.currentBalance()}")
    
    elif userChoice == '1':

        amount_deposited = input("How much would you like to deposit? ")

        if type(amount_deposited) != int:

            print("Not a valid amount. Please try again")
            continue
 

        myAccount.deposit(int(amount_deposited))

        print(f"Your current balance is {myAccount.currentBalance()}")
    
    elif userChoice == '2':

        amount_withdrawn = input("How much would you like to withdraw? ")

        if type(amount_withdrawn) != int:

            print("Not a valid amount. Please try again")
            continue

        myAccount.withdraw(int(amount_withdrawn))

        print(f"Your current balance is {myAccount.currentBalance()}")
    
    else:

        print("Invalid choice. Please choose again.")

    

