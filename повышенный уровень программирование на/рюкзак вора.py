#https://stepik.org/lesson/13238/step/10?unit=3424
a = str(input()).split()
n, vmestimost= int(a[0]), int(a[1])
produkt=[]
kof=[]
cou=0
for i in range(0, n):
    a = str(input()).split()
    produkt.append([int(a[0]), int(a[1])])
    kof.append(int(a[0])/int(a[1]))
while vmestimost != 0 and  produkt!=[]:
    i = kof.index(max(kof))
    if produkt[i][1]<=vmestimost:   
        vmestimost -= produkt[i][1]
        cou += produkt[i][0]
        produkt.pop(i)
        kof.pop(i)
    elif produkt[i][1]>vmestimost:
        cou += vmestimost * kof[i]
        break
print("%.3f" % cou)