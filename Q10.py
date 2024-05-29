name = input("Enter your string : ")
Symbol = {'#','*','@','!','%','$'}
newName = ''

for char in name:
    if char not in Symbol:
        newName += char
    else:
        newName += "."
print(newName)

