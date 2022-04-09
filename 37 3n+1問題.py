n = int(input("整數 n："))
ans = ""
while n != 1:
    if n % 2 == 0:
        ans += str(int(n)) + " "
        n = n / 2
    else:
        ans += str(int(n)) + " "
        n = 3 * n + 1
print("數列：",ans + "1")
