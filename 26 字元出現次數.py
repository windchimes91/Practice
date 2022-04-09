test = input("檢測的字串(end結束)：")
if test == "end":
    print("檢測結束")
    exit()
else:
    s = input("檢測的單一字元：")
count = test.count(s)
print("字元%s出現次數為："%(s),count)
