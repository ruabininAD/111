st_orig=str(input())
fn_orig=str(input())
a=[]
b=[]
for i in range(0, len(st_orig)):
    a.append(st_orig[i])
    b.append(fn_orig[i])
tex=str(input())
tex_1=""
for i in tex:
    tex_1=tex_1+b[a.index(i)]
tex=str(input())
tex_2=""
for i in tex:
    tex_2=tex_2+a[b.index(i)]
print(tex_1)
print(tex_2)

