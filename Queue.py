#Write a Python program to create a class representing a queue data structure.
#Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.queue = list()

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self,data):
        self.queue.insert(0,data)
        print("Value Inserted in queue:",data)
        return 0

    def dequeue(self):
        x = self.queue.pop()
        print("Value removed from queue:",x)
        return 0

    def display(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            for  i in self.queue:
                print(i)
        return 0

q = Queue()

while True:
    print("############## QUEUE #####################")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. Display")
    print("4. Exit")
    print("##############################################")

    choice = int(input("Select Operation:"))

    if choice == 1:
        data = int(input("Enter value to insert:"))
        q.enqueue(data)

    elif choice == 2:
        if q.is_empty() == True:
            print("Queue is already empty")
        else:
            q.dequeue()

    elif choice == 3:
        q.display()

    else:
        print("########## THANK YOU ############")
        break
