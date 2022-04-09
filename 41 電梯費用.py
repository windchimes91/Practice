times = int(input("搭了幾次電梯："))
now = 1
price = 0
for i in range(times):
    stage = int(input(""))
    if stage > now:
        price += (stage - now) * 20
    else:
        price += (now - stage) * 10
    now = stage
print(price,"元")
