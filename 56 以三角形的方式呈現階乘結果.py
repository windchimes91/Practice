n = int(input("請輸入一個正整數(<10)："))
s = ""
for i in range(n + 1):
    s = ""
    for j in range(i):
        s += str(i * (j + 1)) + " "
    print(s)
