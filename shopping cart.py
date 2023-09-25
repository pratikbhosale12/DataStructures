#Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.


class Cart:

    def __init__(self):
        self.items =[]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def add_item(self,item_name,price):
        data = (item_name,price)
        self.items.append(data)
        print("Item put in cart:",data)
        return 0

    def remove_item(self,item_name):
        for item in self.items:
            if item[0] == item_name:
                x = self.items.remove(item)
                print("Item removed from cart:",item_name)
            else:
                print("Item not in cart")
        return 0

    def display(self):
        if len(self.items) == 0:
            print("Cart is empty")
        else:
            for item in self.items:
                print(item[0],"-",item[1])
        return 0

    def total(self):
        tot = 0
        for item in self.items:
            tot += item[1]
        print("Total price:",tot)
        return 0

c = Cart()

while True:
    print("############## STACK #####################")
    print("1. Insert in Cart")
    print("2. Remove from Cart")
    print("3. Display Cart")
    print("4. Total Price")
    print("5. Exit")
    print("##############################################")

    choice = int(input("Select Operation:"))

    if choice == 1:
        item_name = (input("Enter Item to add:"))
        price = int(input("Enter Price:"))
        c.add_item(item_name,price)

    elif choice == 2:
        if c.is_empty() == True:
            print("Cart is already empty")
        else:
            data = input("Enter item to remove:")
            c.remove_item(data)

    elif choice == 3:
        c.display()

    elif choice == 4:
        c.total()


    else:
        print("########## THANK YOU ############")
        break
