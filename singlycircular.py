class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a value at a specific position
    def insert(self, data, position):
        new_node = Node(data)

        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next

        if current is None:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node

    # Append a value at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Delete a value
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("Value not found")

    # Display the linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

# Main program
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

print("Original list:")
ll.display()

ll.insert(15, 1)
print("After inserting 15:")
ll.display()

ll.delete(20)
print("After deleting 20:")
ll.display()
