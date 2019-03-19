#praneeth
n=int(input())
a=list(map(int,input().split()))
t=0
b=[]
for i in range(n):
    if a[i]==i:
        t+=1
        b.append(i)
if t!=0:
    for j in b:
        if j!=b[-1]:
            print(j,end=' ')
        else:
            print(j)
else:
    print(-1)
