gametime = input("請輸入遊戲時間：").split(":")
time = int(gametime[0]) * 60 + int(gametime[1])
time -= 75
count = 6
soldier = 1
while time >= 30:
    time -= 30
    count += 6
    soldier += 1
    if soldier % 2 == 0:
        count -= 1
    if soldier % 3 == 0:
        count += 1

print(count,"隻兵")

