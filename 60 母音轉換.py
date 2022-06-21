list1 = ["a","e","i","o","u"]
en = input("請輸入一串小寫英文：")
for i in range(len(list1)):
    en = en.replace(list1[i],".")
print(en)
