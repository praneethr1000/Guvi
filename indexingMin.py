N,Q=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(Q):
    U,V=map(int,input().split())
    x.append(min(a[U-1:V]))
for d in range(len(x)):
    if d!=len(x)-1:
        print(x[d],end='\n')
    else:
        print(x[d],end='')
