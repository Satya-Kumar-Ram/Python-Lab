f = int(input("Enter first subject number : "))
s = int(input("Enter second subject number : "))
th = int(input("Enter third subject number : "))
fo = int(input("Enter fourth subject number : "))
fi = int(input("Enter fifth subject number : "))

total = f+s+th+fo+fi
percent = (total/500)*100
print("Total percent obtained = ",percent)
if(percent>90):
    print("Grade : A")
elif(percent>80 and percent<90):
    print("Grade : B")
elif(percent>50 and percent<80):
    print("Grade : C")
else:
    print("Grade : Fail")


