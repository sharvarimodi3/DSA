
stack = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    stack.append(x)
    print(x, "pushed into stack")

print("Stack:", stack)
