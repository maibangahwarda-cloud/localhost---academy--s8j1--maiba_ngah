class BankAccount :
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
show_balance = BankAccount ("alice", 1000)
print(f"solde de {show_balance.owner} : {show_balance.balance} FCFA")

def deposit ( self,amount):
    if amount > 0:
        self.balance += amount
    else :
        print("montant invalide")

    account = BankAccount (" Alice ", 1000)

    account . show_balance ()
    account . deposit (500)
    account . show_balance ()
    account . deposit ( -100)
    account . show_balance ()

    print(f"solde de {show_balance} : {account} FCFA")
