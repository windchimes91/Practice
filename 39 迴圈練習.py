n = int(input(""))
for i in range(n):
    for j in range(n-i):
        if j % 2 == 0:
           print(" ",end="")
    for j in range(i+1):
        if i % 2 != 0:
            print(" ",end="")
        else:
            print("*",end="")
    print()
for i in range(n):
    if i == 0:
        continue
    for j in range(i+1):
        if j % 2 == 0:
            print(" ",end="")
    for j in range(n-i):
        if i % 2 != 0:
            print(" ",end="")
        else:
            print("*",end="")
    print()
