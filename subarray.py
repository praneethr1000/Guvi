M,N=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
t=0
for i in b:
    if i not in a:
        print("NO")
        t+=1
        break
if t==0:
    print("YES")
