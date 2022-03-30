a = 0
list1 = []
b = 0 
s=""
while a != 6:
    n = input("請輸入傳送密碼（6位數）：")
    a = len(n)
    if a == 6:
        break
    print("請重新輸入")
for i in range(len(n)):
    list1.append(n[i])
# print(list1)
for i in n:
    for j in range(10):
        if j * 4 % 7 == int(i):
            s += str(j)
            break
print("解密後的密碼：",s)
