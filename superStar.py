n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(1,n-1):
    c=a[i+1:]
    d=max(c)
    if a[i]>d:
        b.append(a[i])
b.append(a[-1])
t=len(b)
for k in range(t):
    if k!=t-1:
        print(b[k],end=' ')
    else:
        print(b[k],end='\n')
print(max(a))
