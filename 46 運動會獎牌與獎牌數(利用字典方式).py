n = input("處理方式(1)字典(2)串列：")
one = input("金 ")
two = input("銀 ")
three = input("銅 ")
four = input("優 ")
dict1 = {"金牌":one,"銀牌":two,"銅牌":three,"優牌":four}
if n == "1":
    key1 = dict1.keys()
    value1 = dict1.values()
    key3 = list(key1)
    value3 = list(value1)
    for i in range(4):
        print("%s得到%s面"%(key3[i],value3[i]))
else:
    items1 = list(dict1.items())
    for key2,value2 in items1:
        print("%s得到%s面"%(key2,value2))
    
