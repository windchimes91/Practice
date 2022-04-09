n = int(input("測試的資料量："))
i=0
while i < n:
    list1 = input("請輸入血型（父 母 子）：").split()
    father = list1[0]
    mother = list1[1]
    kids = list1[2]
    if father == "O" and mother == "O":
        if kids == "O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif father == "O" or mother == "O":
        if father == "A" or mother == "A":
            if kids == "B" or kids =="AB":
                print("IMPOSSIBLE")
            else:
                print("YES")
    elif father == "O" or mother == "O":
        if father == "B" or mother == "B":
            if kids == "A" or kids =="AB":
                print("IMPOSSIBLE")
            else:
                print("YES")
    elif father == "O" or mother == "O":
        if father == "AB" or mother == "AB":
            if kids == "O" or kids =="AB":
                print("IMPOSSIBLE")
            else:
                print("YES")
    elif father == "A" and mother == "A":
        if kids == "B" or kids =="AB":
            print("IMPOSSIBLE")
        else:
            print("YES")
    elif father == "A" or mother == "A":
        if father == "B" or mother == "B":
            print("YES")
    elif father == "A" or mother == "A":
        if father == "AB" or mother == "AB":
            if kids == "O":
                print("IMPOSSIBLE")
            else:
                print("YES")
    elif father == "B" and mother == "B":
        if kids == "A" or kids =="AB":
            print("IMPOSSIBLE")
        else:
            print("YES")
    elif father == "B" or mother == "B":
        if father == "AB" or mother == "AB":
            if kids == "O":
                print("IMPOSSIBLE")
            else:
                print("YES")
    elif father == "AB" or mother == "AB":
        if father == "AB" or mother == "AB":
            if kids == "O":
                print("IMPOSSIBLE")
            else:
                print("YES")
    i+=1
