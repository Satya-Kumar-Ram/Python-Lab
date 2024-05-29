n = int(input("Enter the range of fibonacci series : "))
sum = 0
n1 = 0
n2 = 1

print("Fibonacci series : ",end="")
for i in range(n):
    print(sum,end=" ")
    n1 = n2
    n2 = sum
    sum = n1+n2