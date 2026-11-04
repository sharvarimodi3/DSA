
stack = [10, 20, 30, 40]
temp = []

print("Original Stack:", stack)

while stack:
    temp.append(stack.pop())

stack = temp

print("Reversed Stack:", stack)
