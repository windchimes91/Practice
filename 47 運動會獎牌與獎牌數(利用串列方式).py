n = int(input("輸入筆數n："))
one = int(input("金 "))
two = int(input("銀 "))
three = int(input("銅 "))
four = int(input("優 "))
list1 = [["金",one],["銀",two],["銅",three],["優",four]]
for i in range(n):
    print("%s牌得到%d面"%(list1[i][0],list1[i][1]))
