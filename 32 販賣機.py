have = int(input("小明身上有幾元："))
choice = int(input("販賣機有幾種飲料："))
count = 0
drink = []
for i in range(choice):
    price = int(input(""))
    drink.append(price)
for i in range(choice):
    if have >= drink[i]:
        count += 1
print(count)
