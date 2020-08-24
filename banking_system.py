from abc import ABCMeta, abstractmethod
from random import randint
class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0
    @abstractmethod
    def authenticate(self):
        return 0
    @abstractmethod
    def withdraw(self):
        return 0
    @abstractmethod
    def deposit(self):
        return 0
    @abstractmethod
    def displayBalance(self):
        return 0

class SavingsAccount(Account):
    def __init__(self):
        #[key][0]-->name
        self.savingsAccount  = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
        print("Account creation successfull..")
        print("Your account number is: ", self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication is successfull..")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication failed")
            return False

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingsAccount(self.accountNumber[1]):
            print("Insufficient funds..")
        else:
            self.savingsAccount[self.accountNumber[1]] -= withdrawAmount
            print("withdrawl was successfull, Available balance: ", self.savingsAccount(self.accountNumber[1]))


    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber[1]] += depositAmount
        print("Deposit successfull, available balance: ", self.savingsAccount(self.accountNumber[1]))


    def displayBalance(self):
        print("Available balnce in your account is: ",self.savingsAccount(self.accountNumber[1]))

s1 = SavingsAccount()
#s1.createAccount("Vijay", 20000)
s1.authenticate("Vijay", 65843)
