s = input("輸入值為：")
s1 = ""; s2 = ""
list1 = list(s.split(","))
list1.sort()
for i in list1:
    s1 += i
list1.reverse()
for i in list1:
    s2 += i
print("最大值數列與最小數列差值為：",int(s2)-int(s1))
