num = int(input("Enter your num : "))
d=0
for i in range(2,((num//2)+1)):
    if i%2 == 0:
        d+=1
    
if d>1:
    print("Your number is not prime")
else:
    print("Your number is prime")