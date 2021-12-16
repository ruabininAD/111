i =list(map(int, input().split()))
cou=0
x=i[0]
for i in i[1:]:
    if x<i:
        cou+=1
    x=i
print(cou)