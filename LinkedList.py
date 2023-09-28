class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeg(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertEnd(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        curr_node = self.head
        while(curr_node.next != None):
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = None

    def insert_Before(self,data,value):
        new_node = Node(data)
        curr_node = self.head

        if self.head.data == value:
            self.insertBeg(data)
            return

        while(curr_node.next.data != value):
            curr_node = curr_node.next

        new_node.next = curr_node.next
        curr_node.next = new_node

    def insert_After(self,data,value):
        new_node = Node(data)
        curr_node = self.head

        while curr_node.data != value:
            curr_node = curr_node.next

        if curr_node.next == None:
            self.insertEnd(data)
            return

        else:
            new_node.next = curr_node.next
            curr_node.next = new_node

    def insertIndex(self,data,index):
        new_node = Node(data)
        curr_node = self.head
        position = 0
        if position == index:
            self.insertBeg(data)
            return

        else:
            while(curr_node != None and position+1 != index):
                curr_node = curr_node.next
                position += 1
            if curr_node != None:
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print("Index is Out of range")

    def update_node_at_index(self,value,index):
        curr_node = self.head
        position = 0

        while(curr_node != None and position != index):
            curr_node = curr_node.next
            position += 1

        if curr_node != None:
            curr_node.data = value
        else:
            print("Index out of range")

    def delete_Beg(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        else:
            self.head = self.head.next

    def delete_End(self):
        curr_node = self.head

        if self.head == None:
            print("Linked List is Empty")
            return
        else:
            while(curr_node.next.next != None):
                curr_node = curr_node.next
            curr_node.next = None

    def delete_After(self,value):
        curr_node = self.head

        while(curr_node.data != value):
            curr_node = curr_node.next

        if curr_node.next == None:
            print("No node exists after:",value)
        else:
            curr_node.next = curr_node.next.next

    def delete_Before(self,value):
        curr_node = self.head

        if self.head == value:
            print("No node before:",value)
            return

        elif self.head.next.data == value:
            self.delete_Beg()
            return

        else:
            while(curr_node.next.next.data != value):
                curr_node = curr_node.next

            curr_node.next = curr_node.next.next

    def delete_index(self,index):
        curr_node = self.head
        position = 0
        if position == index:
            self.delete_Beg()
            return
        else:
            while(curr_node.next !=None and position+1 != index):
                curr_node = curr_node.next
                position += 1

            curr_node.next = curr_node.next.next

    def delete_value(self,value):
        if self.head == value:
            self.delete_Beg()
            return

        curr_node = self.head

        while(curr_node.next.data != value):
            curr_node = curr_node.next

        curr_node.next = curr_node.next.next

    def size_ll(self):
        if self.head == None:
            print("Empty LL")
            return

        curr_node = self.head
        size = 1
        while(curr_node.next != None):
            size += 1
            curr_node = curr_node.next
        print("Size of LL:",size)

    def display(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        curr_node = self.head
        while(curr_node != None):
            print(curr_node.data)
            curr_node = curr_node.next


ll = LinkedList()

while True:

    print("################## Linked List ##########################")
    print("1. Insert Node at the Beginning")
    print("2. Insert Node at the End")
    print("3. Insert Node Before a Given Node")
    print("4. Insert Node After a Given Node")
    print("5. Insert Node at an Index")
    print("6. Update Node at an Index")
    print("7. Delete Node at the Beginning")
    print("8. Delete Node at the End")
    print("9. Delete Node Before a Given Node")
    print("10. Delete Node After a Given Node")
    print("11. Delete Node at an Index")
    print("12. Delete Node with particular value")
    print("13. Check Size of Linked List")
    print("14. Display Linked List")
    print("#######################################################")

    print("Hello Programmer!!!")

    choice = int(input("What Do you Desire:"))

    if choice == 1:
        data = input("Enter Value:")
        ll.insertBeg(data)
        print("Value:",data,"inserted at beginning")
        print("##############################################")

    elif choice == 2:
        data = input("Enter Value:")
        ll.insertEnd(data)
        print("Value:",data,"inserted at beginning")
        print("##############################################")

    elif choice == 3:
        data = input("Enter Value to Insert:")
        value = input("Enter Value to Insert Before:")
        ll.insert_Before(data,value)
        print("Value:",data,"inserted Before value:",value)
        print("##############################################")

    elif choice == 4:
        data = input("Enter Value to Insert:")
        value = input("Enter Value to Insert After:")
        ll.insert_After(data,value)
        print("Value:",data,"inserted After value:",value)
        print("##############################################")

    elif choice == 5:
        data = input("Enter Value to Insert:")
        index = input("Enter Index to Insert value at:")
        ll.insertIndex(data,index)
        print("Value:",data,"inserted at Index:",index)
        print("##############################################")

    elif choice == 6:
        data = input("Enter New value to update:")
        index = input("Enter Index to update value at:")
        ll.update_node_at_index(data,index)
        print("Value:",data,"updated at index :",index)
        print("##############################################")

    elif choice == 7:
        ll.delete_Beg()
        print("First Node Deleted")
        print("##############################################")

    elif choice == 8:
        ll.delete_End()
        print("Last Node Deleted")
        print("##############################################")

    elif choice == 9:
        value = input("Enter value to Delete Before:")
        ll.delete_Beg(value)
        print("Node Before",value,"successfully deleted")
        print("##############################################")

    elif choice == 10:
        value = input("Enter value to Delete After:")
        ll.delete_After(value)
        print("Node After",value,"successfully deleted")
        print("##############################################")

    elif choice == 11:
        index = input("Enter index to Delete node:")
        ll.delete_index(index)
        print("Node at Index",index,"successfully deleted")
        print("##############################################")

    elif choice == 12:
        value = input("Enter value to Delete:")
        ll.delete_value(value)
        print("Node having value ",value,"successfully deleted")
        print("##############################################")

    elif choice == 13:
        ll.size_ll()
        print("##############################################")

    elif choice == 14:
        ll.display()
        print("##############################################")

    elif choice == 15:
        print("Thank You!!! See You Soon")
        print("##############################################")

    else:
        print("OOPS!!! Looks like you selected the wrong option")
        print("##############################################")















'''ll.insertBeg(1)
ll.insertEnd(2)
ll.insertBeg(3)
ll.display()
ll.insertIndex(4,2)
ll.display()
'''
