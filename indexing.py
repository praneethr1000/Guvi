N,Q=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(Q):
    U,V=map(int,input().split())
    s=0
    for z in range(U-1,V):
        s=s+a[z]
    x.append(s)
for d in range(len(x)):
    if d!=len(x)-1:
        print(x[d],end='\n')
    else:
        print(x[d],end='')
