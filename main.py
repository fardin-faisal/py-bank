class Bank_system:
    def __init__(Faisal, balance):
        Faisal.balance = balance
        Faisal.min_withdraw = 1000
        Faisal.max_withdraw = 100000

    def get_balance(Faisal):
        return Faisal.balance

    def withdraw (Faisal , amount):
        if amount < Faisal.min_withdraw:
            return "Bangti nai!!!"
        elif amount > Faisal.max_withdraw:
            return "Boshte dile suite cas!!!"
        elif amount > Faisal.balance:
            return "Tui gorib re vai!!!"
        else:
            Faisal.balance = Faisal.balance - amount
            return f"Tui succesfully {amount} tk withdraw korsos!"

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