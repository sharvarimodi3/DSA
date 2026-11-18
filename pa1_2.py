
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "inserted into queue")

    def dequeue(self):
        if not self.queue:
            print("Queue is Empty")
        else:
            print("Deleted element:", self.queue.pop(0))

    def display(self):
        if not self.queue:
            print("Queue is Empty")
        else:
            print("Queue elements:", self.queue)

    def reverse_queue(self):
        stack = []

        while self.queue:
            stack.append(self.queue.pop(0))

        while stack:
            self.queue.append(stack.pop())

        print("Queue reversed successfully")

q = Queue()

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element: ")
        q.enqueue(item)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        q.reverse_queue()

    elif choice == 5:
        q2 = Queue()
        n = int(input("Enter number of elements in second queue: "))

        for i in range(n):
            item = input("Enter element: ")
            q2.enqueue(item)

        q.queue.extend(q2.queue)
        print("Merged Queue:", q.queue)

    elif choice == 6:
        q2 = Queue()
        n = int(input("Enter number of elements in second queue: "))

        for i in range(n):
            item = input("Enter element: ")
            q2.enqueue(item)

        if q.queue == q2.queue:
            print("Both queues are Identical")
        else:
            print("Queues are Not Identical")

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
