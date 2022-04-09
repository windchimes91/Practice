s = input("輸入查詢學號為：")
student = [["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
ans = ""
if s == "123":
    ans =" ".join(student[0])
elif s == "456":
    ans =" ".join(student[1])
elif s == "789":
    ans =" ".join(student[2])
elif s == "321":
    ans =" ".join(student[3])
elif s == "654":
    ans =" ".join(student[4])
print("學生資料為：",ans)

