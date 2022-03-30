n = int(input("輸入一度數（正整數）："))
if n <= 120:
    summer = n * 2.1
    notsummer = n * 2.1
elif n <= 330:
    summer = 120 * 2.1 + (n-120) * 3.02
    notsummer = 120 * 2.1 + (n-120) * 2.68
elif n <= 500:
    summer = 120 * 2.1 + 210 * 3.02 + (n-330) * 4.39
    notsummer = 120 * 2.1 + 210 * 2.68 + (n-330) * 3.61
elif n <= 700:
    summer = 120 * 2.1 + 210 * 3.02 + 170 * 4.39 + (n-500) * 4.97
    notsummer = 120 * 2.1 + 210 * 2.68 + 170 * 3.61 + (n-500) * 4.01
else:
    summer = 120 * 2.1 + 210 * 3.02 + 170 * 4.39 + 200 * 4.97 + (n-700) * 5.63
    notsummer = 120 * 2.1 + 210 * 2.68 + 170 * 3.61 + 200 * 4.01 +(n-700) * 4.5
print("Summer months: %.2f"%(summer))
print("Non-Summer months: %.2f"%(notsummer))

