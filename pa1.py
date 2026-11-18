
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    def pop(self):
        if not self.stack:
            print("Stack is Empty")
        else:
            print("Popped element:", self.stack.pop())

    def display(self):
        if not self.stack:
            print("Stack is Empty")
        else:
            print("Stack elements:", self.stack[::-1])

    def reverse_string(self, string):
        s = []
        for char in string:
            s.append(char)

        result = ""
        while s:
            result += s.pop()

        print("Reversed String:", result)

    def reverse_stack(self):
        temp = []
        while self.stack:
            temp.append(self.stack.pop())

        self.stack = temp
        print("Stack reversed successfully")

s = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String")
    print("5. Reverse Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element: ")
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        string = input("Enter a string: ")
        s.reverse_string(string)

    elif choice == 5:
        s.reverse_stack()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
