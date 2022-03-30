list1 = ['red','blue','red','green']
times = 1
s = ""
while times < 10:
    s = ""
    list2 = input("輸入顏色：").split()
    n=0
    for i in list2:
        if i in list1:  #i是否在list1裡
            if list1[n] == list2[n]:
                s += "1"
            else:
                s += "2"
        else:
            s += "3"
        n += 1
    times += 1
    if s == "1111":
        print("正確答案")
        break
    else:
        print(s)
