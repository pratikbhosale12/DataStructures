#Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.customers = {}

    def create_acc(self,acc_no,ini_bal = 0):
        if acc_no in self.customers:
            print("Account already exists")
        else:
            self.customers[acc_no] = ini_bal
            print("Account",acc_no," created successfully")

    def deposit(self,acc_no,amt):
        if acc_no in self.customers:
            self.customers[acc_no] += amt
            print("Deposit of Rs.",amt,"Successfull in",acc_no)
        else:
            print("Invalid Account")

    def withdraw(self,acc_no,amt):
        if acc_no in self.customers:
            if self.customers[acc_no] >= amt:
                self.customers[acc_no] -= amt
                print("Rs.",amt,"Sucessfully withdrawn from",acc_no)
            else:
                print("Insufficient Balance in",acc_no)
        else:
            print("Invalid Account")

    def check_balance(self,acc_no):
        if acc_no in self.customers:
            bal = self.customers[acc_no]
            print("Account Balance for",acc_no,"is Rs:",bal)
        else:
            print("Invalid Account")

cust = Bank()

while True:
    print("############## BANK #####################")
    print("1. Create Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. View Balance")
    print("5. Exit")
    print("##############################################")

    choice = int(input("Select Operation:"))

    if choice == 1:
        acc_no = (input("Enter Account Number:"))
        cust.create_acc(acc_no)

    elif choice == 2:
        acc_no = (input("Enter Account Number:"))
        amt = int(input("Enter Amount to Deposit"))
        cust.deposit(acc_no,amt)

    elif choice == 3:
        acc_no = (input("Enter Account Number:"))
        amt = int(input("Enter Amount to Withdraw"))
        cust.withdraw(acc_no,amt)

    elif choice == 4:
        acc_no = (input("Enter Account Number:"))
        cust.check_balance(acc_no)
    else:
        print("########## THANK YOU ############")
        break
