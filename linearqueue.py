
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(value, "inserted into queue")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow!")
            return

        temp = self.front
        print("Deleted element:", temp.value)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty!")
            return

        temp = self.front
        print("Queue:", end=" ")

        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next

        print("None")


q = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
