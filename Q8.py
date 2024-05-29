n = input("Enter your string : ")
freq = {}
for i in n:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Count of characters in frequencies are :\n",str(freq))

