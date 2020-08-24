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

    def deposit(self, depositAmount):
        self.accountSavings[self.accountNumber[1]] += depositAmount
        print("Deposit successfull, Available balance is: ", self.accountSavings[self.accountNumber[1]])

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.accountSavings[self.accountNumber[1]]:
            print("Insufficient Funds..Can not withdraw")
        else:
            self.accountSavings[self.accountNumber[1]] -= withdrawAmount
            print("withdrawl was successfull, Available balance: ", self.savingsAccount(self.accountNumber[1]))

    def authenticate(self, name, accountNumber):
        if accountNumber in self.accountSavings.keys():
            if self.accountSavings[self.accountNumber[0]] == name:
                print("Authentication is successfull")
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def displayBalance(self):
        print("Available balance in your account is: ", self.accountSavings[self.accountNumber[1]])
s1 = Savings()
