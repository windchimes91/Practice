main = input("請選擇主餐及升級套餐：")
upcup = input("是否升級成大杯飲料：")
upfr = input("是否轉成大薯：")
dict1 = {"1":72,"2":62,"3":82,"4":44,"5":60}
dict2 = {"A":55,"B":68}
price = dict1.get(main[0],0) + dict2.get(main[1],0)
if upcup == "是":
    price += 7
if upfr == "是":
    price += 13
print("總共為",price,"元")
