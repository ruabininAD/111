i = int(input())
y, x=0, 0
ax={"север":0, "запад": -1, 'юг':0, "восток":1}
ay={"север":1, "запад": 0, 'юг':-1, "восток":0}
for i in range(0,i):
    command=str(input()).split(" ")
    x = x + int(command[1]) * ax[command[0]]
    y = y + int(command[1]) * ay[command[0]]
print(x,y)