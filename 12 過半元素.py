s = input("請輸入一整數序列為：")
n = 0
m = 1
s1=""
list1 = s.split()
for i in range(len(list1)):
    n = list1.count(list1[i])
    if n > m:
        m = n
        s1 = list1[i]
if s1=="":
    print("過半元素為：NO")
else:
    print("過半元素為：",s1)
