x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
print(f"Before swapping x = {x}, y = {y}")

temp = x
x = y
y = temp

print(f"After swapping x = {x}, y = {y}")