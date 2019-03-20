n=input()
b=[]
for i in n:
    b.append(int(i))
c=sum(b)
e=str(c)
f=[]
for i in e:
    f.append(i)
d=f[::-1]
if f==d:
    print("YES")
else:
    print("NO")

