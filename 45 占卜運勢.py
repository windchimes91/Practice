m = int(input("月："))
d = int(input("日："))
s = (m * 2 + d) % 3
list1 = ["普通","吉","大吉"]
print(list1[s])
