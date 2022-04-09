n = int(input("輸入查詢組數N為："))
times = 0
while times < n:
    s = input("")
    list1 = s.split()
    if list1[0] == "123":
        if list1[1] == "456":
            print(9000)
        else:
            print("error")
    elif list1[0] == "456":
        if list1[1] == "789":
            print(5000)
        else:
            print("error")
    elif list1[0] == "789":
        if list1[1] == "888":
            print(6000)
        else:
            print("error")
    elif list1[0] == "336":
        if list1[1] == "558":
            print(10000)
        else:
            print("error")
    elif list1[0] == "775":
        if list1[1] == "666":
            print(12000)
        else:
            print("error")
    elif list1[0] == "566":
        if list1[1] == "221":
            print(7000)
        else:
            print("error")
    else:
        print("error")
    times += 1
