N,Q=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(Q):
    U,V=map(int,input().split())
    b=a[U-1:V]
    f=b[1:]
    c=b[0]
    for z in f:
        c=c^z
    x.append(c)
for d in range(len(x)):
    if d!=len(x)-1:
        print(x[d],end='\n')
    else:
        print(x[d],end='')
