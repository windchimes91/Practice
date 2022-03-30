n = int(input("輸入整數n："))
s = ""
for i in range(1,n,2):
    print(end="    ")
    print(i)
for i in range(1,(n+1),2):
    s += str(i) # s = s + str(i)
for i in range((n-2),0,-2):
    s += str(i)
print(s)
for i in range((n-2),0,-2):
    print(end="    ")
    print(i)
