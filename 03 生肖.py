year = int(input("請輸入西元年："))
list1 = ["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
n = (year -1911) % 12
if n == 0:
    print(list1[11])
else:
    print(list1[n-1])
