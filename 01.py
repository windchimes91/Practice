# number = int(input("請輸入一數字："))
# count = 0
# for i in range(number):
#     if number % (i+1) == 0:
#         count += 1
# if count == 2:
    # print(number)
s ="15693"
count = 0
s1=0 
list1 = []
for i in range(len(s)):
    for j in range(i+1):
        s1 = s[:j+1]
        if int(s1) % 2 == 0:
            break
        for k in range(int(s1)):
           if int(s1) % (k+1) == 0:
               count +=1
        if count == 2:
            print(s1)
        # else:
        #     print(s1)
        #     print(count)
        #     print()
        count = 0

        
