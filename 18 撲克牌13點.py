s = input("輸入五張牌：")
sum = 0
list1 = s.split()
for i in range(len(list1)):
    if list1[i] == "A":
        sum += 1
    elif list1[i] == "J":
        sum += 11
    elif list1[i] == "Q":
        sum += 12
    elif list1[i] == "K":
        sum += 13
    else:
        sum += int(list1[i])
print(sum)
