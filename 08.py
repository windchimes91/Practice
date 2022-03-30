n = int(input("輸入第一行正整數為："))
s = input("第二行中數列中的數字為：")
list1 = s.split(" ")
list2= []
for i in list1:
    a = list1.count(list1[i])
    list2.append(a)
