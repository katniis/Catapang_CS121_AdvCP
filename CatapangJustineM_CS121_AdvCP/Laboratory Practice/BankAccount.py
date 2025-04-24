from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__ (self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance
        
    @abstractmethod
    def deposit(self, amount):
        pass
        
    @abstractmethod
    def withdraw (self, amount):
        pass
        
    @abstractmethod
    def display_account_type(self):
        pass

class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = -5000

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= self.OVERDRAFT_LIMIT:
            self._balance -= amount

    def display_account_type(self):
        return "Current Account"

class SavingsAccount(BankAccount):

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print ("Insufficient Fund")

    def display_account_type(self):
        return "Savings Account"
    


def print_account_details(user: BankAccount):
    print(f"Account Number: {user.account_number}")
    print(f"Balance: {user.balance}")
    print(f"Account Type: {user.display_account_type()}")



if __name__ == "__main__":
    #Savings 
    savings1 = SavingsAccount("SA123", 1300)
    savings1.deposit(200)
    savings1.withdraw(500)

    savings2 = SavingsAccount("SA321", 500)
    savings2.deposit(500)
    savings2.withdraw(100)


    #Current
    current1 = CurrentAccount("CA456", -200)
    current1.deposit(500)
    current1.withdraw(100)

    current2 = CurrentAccount("CA654", 1000)
    current2.deposit(200)
    current2.withdraw(10)



    #Print details
    print_account_details(savings1)
    print("-------------------------------")
    print_account_details(current1)
    print("-------------------------------")
    print_account_details(savings2)
    print("-------------------------------")
    print_account_details(current2)


