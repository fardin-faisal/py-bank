class Bank_system:
    def __init__(Faisal, balance):
        Faisal.balance = balance
        Faisal.min_withdraw = 1000
        Faisal.max_withdraw = 100000

    def get_balance(Faisal):
        return Faisal.balance

    def withdraw (Faisal , amount):
        if amount < Faisal.min_withdraw:
            return f"no money for you. Minimum need to take {Faisal.min_withdraw} taka"
        elif amount > Faisal.max_withdraw:
            return f"crosses max limit : {Faisal.max_withdraw}"
        elif amount > Faisal.balance:
            return "No money sorry"
        else:
            Faisal.balance = Faisal.balance - amount
            return f"Here is yuor money : {amount}"

    def deposit(Faisal, amount):
        Faisal.balance = Faisal.balance + amount

bal = int(input('Enter Balance: '))
my_bank = Bank_system(bal)

wit = int(input('Enter the withdraw ammount: '))
f"Withdrawed ammount : {my_bank.withdraw(wit)} tk"
print(my_bank.get_balance())


dep = int(input('Enter Deposit_Balance: '))
my_bank.deposit(dep)
print(my_bank.get_balance())