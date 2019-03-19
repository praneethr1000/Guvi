#praneeth
n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for x in a:
    if x not in b:
        b.append(x)
    else:
        c.append(x)
d=set(c)
e=list(d)
e.sort()
for i in e:
    print(i,end=' ')
