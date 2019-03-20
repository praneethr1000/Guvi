n,k=map(int,input().split())
a=list(map(int,input().split()))
t=0
for i in range(n):
    if t==0:
        for j in range(i+1,n):
            if a[i]+a[j]==k:
                t+=1
                print("YES")
                break
    else:
        break
if t==0:
    print("NO")
