# put your python code here
spis=[]
maxx=0
minn=0
y=[]
for i in range(0, int(input())):
    a,b=(str(input())).split(" ")
    a,b=int(a),int(b)
    if maxx<max(a,b):
        maxx=max(a,b)
    if minn>min(a,b):
        minn=min(a,b)
    #print(a, b,type(b))
    x=[i for i in range(a,b+1)]
    spis.append(x)
    y=y+x
print(spis)
print(y)
for i in y:
    if y.count(i)==len(spis):
        print()

