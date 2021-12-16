result=[]
count=0
array= str("a a a a d b b b").split(" ") #str(input()).split(" ")

k=[]
for i in range(1, len(array)):
    if  array[i-1]==array[i]:
        k.append(array[i-1])
    else:
        
        result.append(k)
        k=[]
        
print(result)
        
        
        
