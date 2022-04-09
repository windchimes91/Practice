n = int(input(""))
list1 = []
for i in range(n):
    s = int(input(""))
    list1.append(s)
for i in range(n):
    if int(list1[i]) % 9 == 0 or int(list1[i]) % 11 == 0:
        print("第 %d 個點 %d"%(i+1,list1[i]))

