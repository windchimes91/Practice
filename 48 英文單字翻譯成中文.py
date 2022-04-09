n = int(input("輸入筆數："))
list1 = []
for i in range(n):
    s = input("")
    list1.append(s.split())
    dict1 = dict(list1)
find = input("輸入欲查詢單字：")
ch = dict1[find]
print("%s 中文意思為%s"%(find,ch))
