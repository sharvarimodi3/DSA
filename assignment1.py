class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def create_list(self, elements):
        for element in elements:
            self.append(element)
    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List is empty")
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if not current:
            print("Position out of bounds")
            return
        new_node.next = current.next
        current.next = new_node
    def find_middle(self):
        if not self.head:
            print("List is empty")
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"Middle node value: {slow.data}")
        return slow.data
    def delete_node(self, position):
        if not self.head:
            print("List is empty")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if not current or not current.next:
            print("Position out of bounds")
            return
        current.next = current.next.next
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    def sum_consecutive(self):
        if not self.head or not self.head.next:
            print("Not enough nodes to calculate consecutive sums")
            return []
        sums = []
        current = self.head
        while current and current.next:
            pair_sum = current.data + current.next.data
            sums.append(pair_sum)
            current = current.next 
        print(f"Consecutive sums: {sums}")
        return sums
def solution():
    ll = SinglyLinkedList()
    print("--- Creating Linked List ---")
    ll.create_list([10, 20, 30, 40, 50])
    ll.traverse() 
    print("\n--- Inserting 25 at position 2 ---")
    ll.insert_at_position(25, 2)
    ll.traverse()
    print("\n--- Finding Middle Node ---")
    ll.find_middle()
    print("\n--- Deleting node at position 3 ---")
    ll.delete_node(3)
    ll.traverse()
    print("\n--- Calculating Consecutive Sums ---")
    ll.sum_consecutive()
    print("\n--- Reversing List ---")
    ll.reverse()
    ll.traverse()
if __name__ == "__main__":
    solution()