from abc import ABCMeta, abstractmethod
from random import randint
class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0
    @abstractmethod
    def deposit(self):
        return 0
    @abstractmethod
    def withdraw(self):
        return 0
    @abstractmethod
    def authenticate(self):
        return 0
    @abstractmethod
    def displayBalance(self):
        return 0

class Savings(Account):
    def __init__(self):
        self.accountSavings = {}
    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.accountSavings[self.accountNumber] = [name, initialDeposit]
        print("Your account creation successfull.\
Note this account number for future logins: ", self.accountNumber)

    def deposit(self, depositAmount):
        self.accountSavings[self.accountNumber[1]] += depositAmount
        print("Deposit successfull ")
        self.displayBalance()

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.accountSavings(self.accountNumber[1]):
            print("Insufficient Funds..Can not withdraw")
        else:
            self.accountSavings[self.accountNumber[1]] -= withdrawAmount
            print("withdrawl was successfull ")
            self.displayBalance()

    def authenticate(self, name, accountNumber):
        if accountNumber in self.accountSavings.keys():
            if self.accountSavings([self.accountNumber[0]]) == name:
                print("Authentication is successfull")
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def displayBalance(self):
        print("Available balance in your account is: ", self.accountSavings(self.accountNumber[1]))

savingsAccount = Savings()
while True:
    print("Enter 1 to create a new account: ")
    print("Enter 2 to choose an existing account: ")
    print("Enter 3 to exit: ")
    userChoice = int(input())
    if userChoice == 1:
        print("Enter a name for this account: ")
        name = input()
        print("Enter a initial depositAmount: ")
        depositAmount = int(input())
        savingsAccount.createAccount(name, depositAmount)
    elif userChoice == 2:
        print("Enter Name of your existing account: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw Amount: ")
                print("Enter 2 to deposit an Amount: ")
                print("Enter 3 to display avilable balance: ")
                print("Enter 4 to go back to main menu..")
                choice = int(input())
                if choice == 1:
                    print("Enter an amount to withdraw: ")
                    withdrawAmount = int(input())
                    savingsAccount.withdraw(withdrawAmount)
                elif choice == 2:
                    print("Enter an amount to depsoit in your account: ")
                    amount = int(inuput())
                    savingsAccount.deposit(amount)
                elif choice == 3:
                    savingsAccount.displayBalance()
                elif choice == 4:
                    break
        else:
            print("Authentication Failed...")
    elif userChoice == 3:
        quit()
