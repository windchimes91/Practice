s = input("輸入自傳(至少10字)：")
s1 = s.replace("，","")
s = s1.replace("。","")
list1 = []
for i in range(len(s)):
    list1.append(s[i])
list1.sort()
list2 = list1
n = len(s) / 2
for i in range(int(n)):
    if list2[i] == list2[i+1]:
        list1.pop(i)
for i in range(int(n-2)):
    if list2[i] == list2[i+1]:
        list1.pop(i)
print(list1)
