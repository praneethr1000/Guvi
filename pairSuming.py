N,K=map(int,input().split())
a=list(map(int,input().split()))
t=0
for i in range(N):
    s=a[i]
    if t==0:
        for j in range(i+1,N):
            if s+a[j]==K:
                print("yes")
                t=1
                break
    else:
        break
if t==0:
    print("no")
