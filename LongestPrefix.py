N=int(input())
x=[]
for i in range(N):
    x.append(input())
z=len(x[0])
for i in range(1,N):
    if len(x[i])<z:
        z=len(x[i])
s=''
c=0
for j in range(z):
    if c==0:
        t=x[0][j]
        for k in range(1,N):
            if x[k][j]!=t:
                c=1
                break
        if c==0:
            s=s+t
    else:
        break
print(s)
