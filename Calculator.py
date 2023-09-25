#Write a Python program to create a calculator class.
# Include methods for basic arithmetic operations.

class calci:
    def add(self,num1,num2):
        sum = num1 + num2
        print("Sum is:",sum)
        print("#####################")
        return 0

    def sub(self,num1,num2):
        sub = abs(num1 - num2)
        print("Difference is:",sub)
        print("#####################")
        return 0

    def multi(self,num1,num2):
        prod = num1 * num2
        print("Product is:",prod)
        print("#####################")
        return 0

    def div(self,num1,num2):
        rem = num1 / num2
        quot = num1 % num2
        print("Remainder is:",rem)
        print("Quotient is:",quot)
        print("#####################")
        return 0

x = calci()
while True:

    print("############## CALCULATOR #####################")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVISION")
    print("5. EXIT")
    print("##############################################")

    choice = int(input("Select Operation:"))
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))

    if choice == 1:
        ans = x.add(num1,num2)

    elif choice == 2:
        ans = x.sub(num1,num2)

    elif choice == 3:
        ans = x.sub(num1,num2)

    elif choice == 4:
        ans = x.div(num1,num2)

    else:
        print("########## THANK YOU ###########")
        break



