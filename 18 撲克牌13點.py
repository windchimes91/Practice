s = input("輸入五張牌（以空白相隔）：")
sum = 0
list1 = s.split()
for i in range(len(list1)):
    if list1[i] == "A" or list1[i] == "a":
        sum += 1
    elif list1[i] == "J" or list1[i] == "j":
        sum += 11
    elif list1[i] == "Q" or list1[i] == "q":
        sum += 12
    elif list1[i] == "K" or list1[i] == "k":
        sum += 13
    else:
        sum += int(list1[i])
print(sum)
