
stack = []

string = input("Enter a string: ")

for ch in string:
    stack.append(ch)

reverse = ""

while stack:
    reverse += stack.pop()

print("Original String:", string)
print("Reversed String:", reverse)
