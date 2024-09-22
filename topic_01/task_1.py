line1 = input("write your line: ")
length = len(line1)
line2 = ""
for i in range (length):
    line2 += line1[-i-1]
print(line2)