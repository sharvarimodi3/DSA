class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at a specific position
    def insert(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        new_node = Node(data)

        if self.head is None:
            if position != 0:
                print("Position out of range")
                return
            self.head = new_node
            new_node.next = self.head
            return

        if position == 0:
            current = self.head

            while current.next != self.head:
                current = current.next

            new_node.next = self.head
            current.next = new_node
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 1):
            current = current.next
            if current == self.head:
                print("Position out of range")
                return

        new_node.next = current.next
        current.next = new_node

    # Append at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    # Delete a value
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = None

        while True:
            if current.data == data:
                # Only one node
                if current.next == self.head and current == self.head:
                    self.head = None
                    return

                # Delete the head node
                if current == self.head:
                    last = self.head

                    while last.next != self.head:
                        last = last.next

                    self.head = self.head.next
                    last.next = self.head
                else:
                    previous.next = current.next

                return

            previous = current
            current = current.next

            if current == self.head:
                break

        print("Value not found")

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")

# Main program
cll = CircularLinkedList()

cll.append(10)
cll.append(20)
cll.append(30)

print("Original list:")
cll.display()

cll.insert(15, 1)
print("After inserting 15 at position 1:")
cll.display()

cll.delete(20)
print("After deleting 20:")
cll.display()
