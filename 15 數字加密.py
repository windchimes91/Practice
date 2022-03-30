number = input("輸入一組四位數字為：")
list1 = []
tmp = 0
s1 = ""
for i in range(len(number)):
    list1.append(str((int(number[i])+7) % 10))
for i in range(2):
    a = list1[i]
    b = list1[i+2]
    tmp = a
    a = b
    b = tmp
    list1[i] = a
    list1[i+2] = b 
for i in range(len(list1)):
    s1 += list1[i]
print("輸出後加密的數字為：",s1)
