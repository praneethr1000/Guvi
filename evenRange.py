N,Q=map(int,input().split())
x=[]
for i in range(N+1,Q):
    if i%2==0:
        x.append(i)
for i in range(len(x)):
    if i!=len(x)-1:
        print(x[i],end=' ')
    else:
        print(x[i],end='')
