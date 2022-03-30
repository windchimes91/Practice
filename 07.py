s = input("輸入月租費型式及通話時間為：")
list1 = list(s.split(","))
if list1[0] == "186":
    money = int(list1[1]) * 0.09
elif list1[0] == "386":
    money = int(list1[1]) * 0.08
elif list1[0] == "586":
    money = int(list1[1]) * 0.07
elif list1[0] == "986":
    money = int(list1[1]) * 0.06
if money > int(list1[0]):
    if list1[0] == "186":
        money *= 0.8
    elif list1[0] == "386":
        money *= 0.7
    elif list1[0] == "586":
        money *= 0.6
    elif list1[0] == "986":
        money *= 0.5
else:
    if list1[0] == "186":
        money *= 0.9
    elif list1[0] == "386":
        money *= 0.8
    elif list1[0] == "586":
        money *= 0.7
    elif list1[0] == "986":
        money *= 0.6
print("通話費為：%.0f"%money)