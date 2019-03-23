n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n+1):
    if i*n in a:
        c+=1
print(c)
