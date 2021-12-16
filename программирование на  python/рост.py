import csv
tsv_file = open("rost.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
a=[[],[],[],[],[],[],[],[],[],[],[]]
for row in read_tsv:
  clas = int(row[0])-1
  h = row[2]
  (a[clas]).append(h)
#print(len(a))

for i in range(0,11):
  a[i] = [int(item) for item in a[i]]
  summ = sum(a[i])
 # print(i, " ", a[i],summ)
  if len(a[i])==0:
    print(i+1, "-")
  else:
    sred=summ/(len(a[i]))
    print(i+1, sred)