ch = int(input("國文："))
en = int(input("英文："))
math = int(input("微積分："))
pe = int(input("體育："))
py = int(input("程式設計："))
avg = (ch + en + math + pe + py) / 5
max = max(ch, en,math,pe,py)
min = min(ch, en,math,pe,py)
print("平均分數：%.2f"%(avg))
if max == ch:
    print("最高分科目：國文",max,"分")
elif max == en:
    print("最高分科目：英文",max,"分")
elif max == math:
    print("最高分科目：微積分",max,"分")
elif max == pe:
    print("最高分科目：體育",max,"分")
elif max == py:
    print("最高分科目：程式設計",max,"分")

if min == ch:
    print("最低分科目：國文",min,"分")
elif min == en:
    print("最低分科目：英文",min,"分")
elif min == math:
    print("最低分科目：微積分",min,"分")
elif min == pe:
    print("最低分科目：體育",min,"分")
elif min == py:
    print("最低分科目：程式設計",min,"分")
