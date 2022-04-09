classes = int(input(""))
tmp = 0
for i in range(classes):
    people = int(input(""))
    if people > tmp :
        tmp = people
print(tmp)
