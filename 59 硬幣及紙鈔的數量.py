money = int(input("輸入金額："))
count = 0
while money >= 100:
    money -= 100
    count += 1
while money >= 50:
    money -= 50
    count += 1
while money >= 10:
    money -= 10
    count += 1
while money >= 5:
    money -= 5
    count += 1
while money >= 1:
    money -= 1
    count += 1
print("所需的最少硬幣及紙鈔的數量：",count)
