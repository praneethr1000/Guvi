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
x=len(b)
for j in range(x):
    if j!=x-1:
        print(b[j],end=' ')
    else:
        print(b[j])
