a = int(input(""))
b = int(input(""))
c = int(input(""))
test = b**2 - 4 * a * c
x1 = (-b + (b**2 - 4 * a * c) ** (1/2)) / 2 * a
x2 = (-b - (b**2 - 4 * a * c) ** (1/2)) / 2 * a
if test > 0:
    print(int(x1))
    print(int(x2))
elif test < 0:
    print(0)
else:
    print(int(x1))



