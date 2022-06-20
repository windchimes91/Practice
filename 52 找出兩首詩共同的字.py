s1 = "紅豆生南國，春來發幾枝？願君多采擷，此物最相思。"
s2 = "春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。"
s1 = s1.replace("，","")
s1 = s1.replace("。","")
s1 = s1.replace("？","")
s2 = s2.replace("，","")
s2 = s2.replace("。","")
list1 = []
list2 = []
for i in range(len(s1)):
    list1.append(s1[i])
    list2.append(s2[i])
ans = []
for i in list1:
    for j in range(len(list2)):
        if i == list2[j]:
            ans.append(i)    
print(ans)