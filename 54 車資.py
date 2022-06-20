km = float(input("請輸入路程公里(km)："))
km *= 1000  #km -> m
price = 75
if km > 1500:
    km -= 1500
    while km >= 250:
        km -= 250
        price += 5
    if km != 0:
        price += 5

print("所需車資為：",price)
