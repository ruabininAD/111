i =int(input())
x =int(input())
y =int(input())
xp=[]
yp=[]
while x>1:
  xp.append(x//2)
  x=x//2
while y>1:
  yp.append(y//2)
  y=y//2
maxx=0
for i in xp:
    for j in yp:
        if i == j and i>maxx:
            maxx=i
print(maxx)
