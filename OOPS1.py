class bank:
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show your account opening status")
    def deposit(self):
        print("This show your deposited amount")

class HDFC_Bank(bank):
    def hdfc_to_icici(self):
        print("this will show all the transaction happened to icici through hdfc")

class icici(HDFC_Bank): #multi level inheritence
    pass

i=icici()
i.hdfc_to_icici()
i.deposit()
i.transaction()
i.account_opening()
