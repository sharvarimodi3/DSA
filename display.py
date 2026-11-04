
stack = [10, 20, 30, 40]

if len(stack) == 0:
    print("Stack is Empty")
else:
    print("Stack elements:")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
