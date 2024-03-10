'''
    Day 60
    Create a class representing a simple bank account with deposit and withdraw methods

    Output:

    Current account balance is 100 EUR

    You have succesfuly withdrew 20 EUR from bank account
    Current account balance is 80 EUR

    Succesfuly deposited 50 EUR to bank account
    Current account balance is 130 EUR

    It is not possible to withdraw 500 EUR
    Current available balance is 130 EUR
'''

class Bank_account():
    ''' Simple bank account '''
    def __init__(self, account_balance, currency="EUR"):
        self.account_balance = account_balance
        self.currency = currency

    def get_current_balance(self):
        return self.account_balance, self.currency

    def withdraw(self, amount_of_money):
        if (self.account_balance - amount_of_money >= 0):
            self.account_balance -= amount_of_money
            print(f"\nYou have succesfuly withdrew {amount_of_money} {self.currency} from bank account")
            print(f"Current account balance is {self.account_balance} {self.currency}")
        else:
            print(f"\nIt is not possible to withdraw {amount_of_money} {self.currency}\n"
                  f"Current available balance is {self.account_balance} {self.currency}")

    def deposit(self, amount_of_money):
        ''' Deposit amount of money '''
        if amount_of_money > 0:
            self.account_balance += amount_of_money
            print(f"\nSuccesfuly deposited {amount_of_money} {self.currency} to bank account")
            print(f"Current account balance is {self.account_balance} {self.currency}")

if __name__ == "__main__":
    my_account = Bank_account(100)
    my_deposit, my_currency = my_account.get_current_balance()
    print(f"\nCurrent account balance is {my_deposit} {my_currency}")
    my_account.withdraw(20)
    my_account.deposit(50)
    my_account.withdraw(500)
