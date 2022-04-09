s = input("請輸入英文句子：")
list1 = s.split()
list2 = []
n = len(list1)
for i in range(n):
    list2.append(list1[n-i-1])
print("輸出結果：",list2)
