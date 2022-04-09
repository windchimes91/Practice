n = int(input("組數為："))
times = 0
while times < n:
    times += 1
    list1 = input("第%d組："%(times)).split()
    sum = 0
    total = int(list1[0])
    helf = int(list1[1])
    sum = total * 250 + helf * 175
    print("第%d組應繳費用：%d"%(times,sum))
