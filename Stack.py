#Write a Python program to create a class representing a stack data structure.
# Include methods for pushing and popping elements.


class Stack:
    def __init__(self):
        self.items =[]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self,data):
        self.items.append(data)
        print("Value Pushed on stack:",data)
        return 0

    def pop(self):
        x = self.items.pop()
        print("Value popped from stack:",x)
        return 0

    def display(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            for i in self.items:
                print(i)

        return 0

s = Stack()

while True:
    print("############## STACK #####################")
    print("1. PUSH")
    print("2. POP")
    print("3. Display")
    print("4. Exit")
    print("##############################################")

    choice = int(input("Select Operation:"))

    if choice == 1:
        data = int(input("Enter value to Push:"))
        s.push(data)

    elif choice == 2:
        if s.is_empty() == True:
            print("Stack is already empty")
        else:
            s.pop()

    elif choice == 3:
        s.display()

    else:
        print("########## THANK YOU ############")
        break

