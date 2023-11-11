batas = int(input(""))

if batas % 2 != 0:
    batas -= 1

for i in range(1, batas + 1, 2):
    print(i, end=" ")

print()  

for i in range(batas, 1, -2):
    print(i, end=" ")
