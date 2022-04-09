ans = input("") 
s = input("")
while s != "0000":
    a = 0 
    b = 0
    for i in range(len(s)):
        for j in range(len(ans)):
            if s[i] == ans[j]:
                if i == j:
                    a += 1
                else:
                    b += 1
    print("%dA%dB"%(a,b))
    s = input("")
