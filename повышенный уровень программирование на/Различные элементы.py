s = str(input())
s = s.split(" ")
cou=0
while s!=[]:
    cou+=1
    o=s[0]
    while o in s:
        s.remove(s[0])
print(cou)