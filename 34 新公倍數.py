n = int(input("輸入一正整數："))
while n < 11 or n > 1000:
    n = int(input("輸入一正整數："))
if n % 2 == 0 and n % 11 == 0:
    if n % 5 != 0 or n % 7 != 0:
        print("%d為新公倍數?：YES"%(n))
    else:
        print("%d為新公倍數?：NO"%(n))
else:
    print("%d為新公倍數?：NO"%(n))
