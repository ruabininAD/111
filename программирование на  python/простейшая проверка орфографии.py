i=int(input())
words=[]
err=[]
for i in range(0, i):
    words.append(str(input()).lower())
i=int(input())
for i in range(0, i):
    text=str(input())
    text=text.lower()
    text=text.split(" ")
    for t in text:
        if t not in words and t not in err:
            err.append(t)
for i in range(-1, -1*len(err)-1,-1):
    print(err[i])