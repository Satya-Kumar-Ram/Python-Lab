name = input("Enter your name : ")
list = []
sname = ""
list = name.split()

for i in range(len(list)-1):
    s = list[i]
    sname = sname + s[0].upper()+"."

sname = sname+list[-1].title()
print(sname)