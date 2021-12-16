
b=[]
flag=1
while flag==1:
    a=str(input())
    if a=="end":
        flag=0
    else:
        a=a.split(" ")
        b.append(a)
q=[]
q.append(list(b[len(b)-1]))
q=q+b
q.append(list( b[0] ))
#print(q)
for i in range(0, len(q)):
    begin=q[i][0]
    body=list(q[i])
    finish=q[i][len(q[i])-1]
    q[i]=[]
    q[i].append(finish)
    q[i]=q[i]+body
    q[i].append(begin)
#print(q)

for i in range(1,len(q)-1):
    for j in range(1, len(q[0])-1):
       q[i][j]=int(q[i-1][j])+int(q[i+1][j])+int(q[i][j-1])+int(q[i][j+1])
print(q)
