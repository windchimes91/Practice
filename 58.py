list1=[]
for i in range(1,11):
    n = int(input("請輸入第%d個數字："%i))
    list1.append(n)
list1.sort()
list1.reverse()
print("最大的3個數字：%d,%d,%d"%(list1[0],list1[1],list1[2]))
list1.reverse()
print("最小的3個數字：%d,%d,%d"%(list1[0],list1[1],list1[2]))
