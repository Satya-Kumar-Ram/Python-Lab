n = int(input("Enter your number : "))
nwn =int( str(n)[::-1])

if n==nwn:
    print("Palindrome number")
else:
    print("Not Palindrome number")