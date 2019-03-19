n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if i%2==0:
        if a[i]%2!=0:
            b.append(a[i])
    else:
        if a[i]%2==0:
            b.append(a[i])
for j in b:
    if j!=b[-1]:
        print(j,end=' ')
    else:
        print(j)
