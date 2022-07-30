class bank:
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show your account opening status")
    def deposit(self):
        print("This show your deposited amount")
    def test(self):
        print("this is a test method from bank class")

class HDFC_Bank:
    def hdfc_to_icici(self):
        print("this will show all the transaction happened to icici through hdfc")
    def test(self):
        print("This is a method from hdfc bank")

class ineuron_bank:
    def account_status_icici(self):
        print("an account stats in icici ")

class icici(HDFC_Bank,bank,ineuron_bank): #multiple inheritence
    pass

i = icici()
i.hdfc_to_icici()
i.deposit()
i.transaction()
i.account_opening()
i.test()
i.account_status_icici()
