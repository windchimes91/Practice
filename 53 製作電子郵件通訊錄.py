n = int(input("輸入n值："))
list1 = []
for i in range(n):
    name = input("請輸入姓名：")
    email = input("請輸入電子郵件：")
    list1.append([name,email])
dict1 = dict(list1)

key1 = input("請輸入查詢電子郵件的姓名：")    
print(key1,"電子郵件帳號為",dict1[key1])
