# to create the bank account class
class bank:
    def __init__(self):
        self.bal = 0 # initialize balance to 0
        print("Welcome to the Reserved bank of india")
        
    def deposit(self):
        amt = float(input("Enter amount to be Deposited: "))
        self.bal += amt
        print("\nAmount Deposited:", amt)
    def withdraw(self):
        amt = float(input("Enter amount to be Withdrawn: "))
        if self.bal >= amt:
            self.bal -= amt
            print("\nYou Withdrew:", amt)
        else:
            print("\nInsufficient bal")
    def display(self):
        print("\nNet Available Balance =", self.bal)
        
# driver code
    s = Bank()  # Create an object of Bank
    s.deposit()        # Deposit money
    s.withdraw()       # Withdraw money
    s.display()        # Display balance
